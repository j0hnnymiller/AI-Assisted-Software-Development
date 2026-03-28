#!/usr/bin/env python3
"""
Phase 0 + Phase 1 agent merge script.
Created by merge-marp-decks.prompt.md agent run.
Validates and merges Marp slide decks per the prompt spec.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "pyyaml", "--quiet"], check=True)
    import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
YAML_FILE  = REPO_ROOT / "Slides" / "manifests" / "aiasd-311-monday.yaml"
OUTPUT_FILE = REPO_ROOT / "Slides" / "merged" / "aiasd-311-monday-draft.md"
SEP = "\n\n---\n\n"
MERGE_CHAR_REPLACEMENTS = {
    "`": "'",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_front_matter(text: str):
    """Return (front_matter, body).
    front_matter ends with '---\\n'; body has the first blank line removed."""
    if not text.startswith("---"):
        return "", text
    lines = text.split("\n")
    closing = None
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            closing = i
            break
    if closing is None:
        return "", text
    fm = "\n".join(lines[: closing + 1]) + "\n"
    body_lines = lines[closing + 1 :]
    if body_lines and body_lines[0] == "":
        body_lines = body_lines[1:]
    return fm, "\n".join(body_lines)


def get_first_h2(body: str):
    for line in body.splitlines():
        m = re.match(r"^## (.+)", line)
        if m:
            return m.group(1).strip()
    return None


def strip_h1(text: str) -> str:
    """Strip all bare # H1 headings and any immediately-following _Merged from:_ lines."""
    lines = text.splitlines(keepends=True)
    result, i = [], 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^# (?!#)", line):
            i += 1
            while i < len(lines) and re.match(r"^_Merged from:", lines[i].strip()):
                i += 1
            continue
        result.append(line)
        i += 1
    return "".join(result)


def rewrite_images(text: str) -> str:
    text = text.replace("](images/", "](marp/images/")
    text = text.replace('src="images/', 'src="marp/images/')
    text = text.replace("src='images/", "src='marp/images/")
    text = text.replace("url('images/", "url('marp/images/")
    text = text.replace('url("images/', 'url("marp/images/')
    text = text.replace("url(images/", "url(marp/images/")
    return text


def normalize_merge_characters(text: str) -> str:
    """Replace characters that routinely merge poorly in generated decks."""
    for source, target in MERGE_CHAR_REPLACEMENTS.items():
        text = text.replace(source, target)
    return text


def process_body(content: str) -> str:
    """Strip front matter, strip H1 headings, rewrite image paths, trim whitespace."""
    _, body = strip_front_matter(content)
    body = strip_h1(body)
    body = rewrite_images(body)
    body = normalize_merge_characters(body)
    return body.strip()


def count_slides(text: str) -> int:
    """1 + number of bare '---' lines outside fenced code blocks, skipping front matter."""
    # Skip the YAML front matter block
    if text.startswith("---"):
        end = text.find("\n---\n", 3)
        if end != -1:
            text = text[end + 5:]
    count = 1
    in_fence = False
    fence_marker = None
    for line in text.splitlines():
        s = line.strip()
        if not in_fence:
            m = re.match(r"^(`{3,}|~{3,})", s)
            if m:
                in_fence = True
                fence_marker = m.group(1)
            elif s == "---":
                count += 1
        else:
            tail = s[len(fence_marker) :] if s.startswith(fence_marker) else None
            if tail is not None and not tail.strip():
                in_fence = False
    return count


def iter_lines_outside_fences(text: str):
    """Yield lines outside fenced code blocks so validation ignores examples."""
    in_fence = False
    fence_marker = None

    for line in text.splitlines():
        s = line.strip()
        if not in_fence:
            m = re.match(r"^(`{3,}|~{3,})", s)
            if m:
                in_fence = True
                fence_marker = m.group(1)
                continue
            yield line
            continue

        tail = s[len(fence_marker) :] if s.startswith(fence_marker) else None
        if tail is not None and not tail.strip():
            in_fence = False
            fence_marker = None


# ---------------------------------------------------------------------------
# Validation  (Phase 0)
# ---------------------------------------------------------------------------

def validate(path: Path, content: str) -> list:
    warnings = []
    fm, body = strip_front_matter(content)
    body_lines = list(iter_lines_outside_fences(body))

    # Rule 1 – valid front matter
    if not content.startswith("---") or not fm:
        warnings.append(f"  WARNING [{path.name}] Rule 1: Missing/invalid front matter")

    # Rule 2 – no H1 in body
    seen_slide_separator = False
    seen_first_slide_content = False
    allowed_title_h1_consumed = False
    for line in body_lines:
        stripped = line.strip()

        if stripped == "---":
            seen_slide_separator = True
            continue

        if not stripped:
            continue

        if not seen_slide_separator and stripped.startswith("<!--") and stripped.endswith("-->"):
            continue

        if re.match(r"^# (?!#)", line):
            if not seen_slide_separator and not seen_first_slide_content and not allowed_title_h1_consumed:
                allowed_title_h1_consumed = True
                seen_first_slide_content = True
                continue

            warnings.append(
                f"  WARNING [{path.name}] Rule 2: H1 heading in body: {line.strip()[:60]}"
            )
            break

        seen_first_slide_content = True

    # Rule 3 – at least one H2
    if not any(re.match(r"^## ", l) for l in body_lines):
        warnings.append(f"  WARNING [{path.name}] Rule 3: No ## H2 heading found")

    # Rule 4 – source decks reference their local images/ folder
    if "../images/" in content:
        warnings.append(f"  WARNING [{path.name}] Rule 4: Contains ../images/ reference")

    # Rule 5 – no trailing ---
    if content.rstrip().endswith("---"):
        warnings.append(f"  WARNING [{path.name}] Rule 5: File ends with bare --- separator")

    # Rule 6 – no vertical-tab
    if "\x0b" in content:
        warnings.append(f"  WARNING [{path.name}] Rule 6: Contains vertical-tab character")

    return warnings


# ---------------------------------------------------------------------------
# Injected slide builders
# ---------------------------------------------------------------------------

def module_list_slide(all_names, current) -> str:
    lines = ["<!-- _class: lead -->", "", "## Course Modules", ""]
    for name in all_names:
        if name == current:
            lines.append(f"- **▶ {name}**")
        else:
            lines.append(f"- {name}")
    return "\n".join(lines)


def section_header_slide(name) -> str:
    return f"<!-- _class: lead -->\n\n# {name}"


def section_agenda_slide(name, titles) -> str:
    lines = [f"## {name}", ""]
    for t in titles:
        lines.append(f"- {t}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"YAML  : {YAML_FILE}")
    print(f"Output: {OUTPUT_FILE}")
    print()

    with open(YAML_FILE, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    sections   = config.get("sections", [])
    all_names  = [s.get("name", "Unnamed") for s in sections]

    # Collect unique source file paths (manifest order)
    all_paths: list[str] = []
    for section in sections:
        for p in (section.get("decks") or []):
            if p and p not in all_paths:
                all_paths.append(p)

    # Load file contents
    contents: dict[str, str] = {}
    load_warnings = []
    for rel in all_paths:
        fp = REPO_ROOT / rel
        try:
            contents[rel] = fp.read_text(encoding="utf-8")
        except FileNotFoundError:
            load_warnings.append(f"  WARNING [{rel}]: File not found")

    # ── Phase 0 ──────────────────────────────────────────────────────────
    print("=== Phase 0: Validation ===")
    all_warnings = list(load_warnings)
    for rel, txt in contents.items():
        all_warnings.extend(validate(REPO_ROOT / rel, txt))
    for w in all_warnings:
        print(w)
    print(
        f"\nValidation complete: {len(all_paths)} file(s) checked, "
        f"{len(all_warnings)} warning(s) found."
    )
    print()

    # ── Phase 1 ──────────────────────────────────────────────────────────
    print("=== Phase 1: Merge ===")

    # Global front matter from the very first source file across all sections
    global_fm = ""
    for section in sections:
        deck_entries = [s for s in (section.get("decks") or []) if s]
        if deck_entries and deck_entries[0] in contents:
            global_fm, _ = strip_front_matter(contents[deck_entries[0]])
            break

    if not global_fm:
        print("ERROR: Could not extract global front matter — aborting.")
        sys.exit(1)

    # Build the ordered list of slide-content strings
    slide_blocks: list[str] = []

    for section in sections:
        section_name = section.get("name", "Unnamed")
        src_decks    = [s for s in (section.get("decks") or []) if s]

        # Collect first H2 from each source file (for agenda slide)
        first_h2s = []
        for p in src_decks:
            txt = contents.get(p, "")
            _, body = strip_front_matter(txt)
            h2 = get_first_h2(body)
            first_h2s.append(h2 if h2 else Path(p).stem)

        # 1. Module list slide (always)
        slide_blocks.append(module_list_slide(all_names, section_name))

        # 2. Section header slide (always)
        slide_blocks.append(section_header_slide(section_name))

        # 3. Section agenda slide + content (only when section has source files)
        if src_decks:
            slide_blocks.append(section_agenda_slide(section_name, first_h2s))

            for p in src_decks:
                txt = contents.get(p, "")
                if not txt:
                    print(f"  WARNING: skipping empty/missing {p}")
                    continue
                body = process_body(txt)
                if body:
                    slide_blocks.append(body)

    # global_fm ends with '---\n'; add one blank line then all slide blocks
    full_output = global_fm + "\n" + SEP.join(slide_blocks)

    # Write output file
    OUTPUT_FILE.write_text(full_output, encoding="utf-8")

    n_slides   = count_slides(full_output)
    n_sections = len(sections)
    print(f"Merged deck: {n_slides} slide(s) across {n_sections} section(s).")
    print(f"Written: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
