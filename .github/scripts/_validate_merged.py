from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a merged Marp deck against a manifest")
    parser.add_argument("merged_path", help="Path to the merged markdown deck")
    parser.add_argument(
        "manifest_path",
        nargs="?",
        help="Optional manifest path used to validate module slides and traceability",
    )
    return parser.parse_args()


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def resolve_repo_path(path_str: str) -> Path:
    path = Path(path_str)
    return path if path.is_absolute() else (repo_root() / path).resolve()


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def split_front_matter(text: str) -> tuple[str | None, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not match:
        return None, text
    return match.group(1), text[match.end() :]


def is_yaml_front_matter_block(block: str) -> bool:
    if not block.startswith("---"):
        return False
    lines = block.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---" or lines[-1].strip() != "---":
        return False
    body = "\n".join(lines[1:-1])
    try:
        parsed = yaml.safe_load(body)
    except Exception:
        return False
    return isinstance(parsed, dict)


def split_slides(text: str) -> list[str]:
    slides: list[str] = []
    buffer: list[str] = []
    in_backtick = False
    in_tilde = False
    for line in re.split(r"\r?\n", text):
        if re.match(r"^```", line):
            in_backtick = not in_backtick
            buffer.append(line)
            continue
        if re.match(r"^~~~", line):
            in_tilde = not in_tilde
            buffer.append(line)
            continue
        if not in_backtick and not in_tilde and re.match(r"^---\s*$", line):
            slides.append("\n".join(buffer).strip())
            buffer = []
            continue
        buffer.append(line)
    slides.append("\n".join(buffer).strip())
    return slides


def count_separators_outside_fences(text: str) -> int:
    count = 0
    in_backtick = False
    in_tilde = False
    for line in re.split(r"\r?\n", text):
        if re.match(r"^```", line):
            in_backtick = not in_backtick
            continue
        if re.match(r"^~~~", line):
            in_tilde = not in_tilde
            continue
        if not in_backtick and not in_tilde and re.match(r"^---\s*$", line):
            count += 1
    return count


def remove_front_matter(text: str) -> str:
    return re.sub(r"\A---\r?\n.*?\r?\n---\r?\n?", "", text, count=1, flags=re.S)


def strip_initial_h1_and_provenance(text: str) -> str:
    lines = re.split(r"\r?\n", text)
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines) and re.match(r"^#\s+", lines[index]):
        del lines[index]
        while index < len(lines) and not lines[index].strip():
            index += 1
        if index < len(lines) and re.match(r"^_Merged from: .*_$", lines[index]):
            del lines[index]
    return "\r\n".join(lines).strip("\r\n")


def trim_edge_separators(text: str) -> str:
    text = re.sub(r"\A(?:\s*\r?\n)*---(?:\r?\n\s*)*", "", text, count=1)
    text = re.sub(r"(?:\r?\n\s*)*---\s*\Z", "", text, count=1)
    return text.strip("\r\n")


def rewrite_image_paths(text: str) -> str:
    return re.sub(r"(?<!\.\./)(?<![A-Za-z]:\\)images/", "marp/images/", text)


def rebuild_expected_output(manifest: dict) -> str:
    section_names = [section["name"] for section in manifest["sections"]]
    front_matter: str | None = None
    blocks: list[str] = []

    for section_index, section in enumerate(manifest["sections"]):
        if section_index > 0:
            bullets = [
                f"- **▶ {name}**" if name == section["name"] else f"- {name}"
                for name in section_names
            ]
            blocks.append("\r\n".join(["<!-- _class: lead -->", "", "## Course Modules", "", *bullets]))

        for deck in section.get("decks") or []:
            deck_path = resolve_repo_path(deck.replace("\\", "/"))
            raw = deck_path.read_text(encoding="utf-8-sig")
            fm_text, _ = split_front_matter(raw)
            if front_matter is None:
                if fm_text is None:
                    raise ValueError(f"Missing front matter in first source deck: {deck}")
                front_matter = fm_text
            body = remove_front_matter(raw)
            body = strip_initial_h1_and_provenance(body)
            body = rewrite_image_paths(body)
            body = trim_edge_separators(body)
            if body.strip():
                blocks.append(body)

    if front_matter is None:
        raise ValueError("No front matter found in manifest sources")

    return "---\r\n" + front_matter + "\r\n---\r\n\r\n" + "\r\n\r\n---\r\n\r\n".join(blocks) + "\r\n"


def main() -> int:
    args = parse_args()
    merged_path = resolve_repo_path(args.merged_path)
    manifest = None
    if args.manifest_path:
        manifest = yaml.safe_load(resolve_repo_path(args.manifest_path).read_text(encoding="utf-8"))

    text = merged_path.read_text(encoding="utf-8")
    normalized_text = normalize_newlines(text)
    errors: list[str] = []

    front_matter, body = split_front_matter(text)

    if front_matter is None:
        errors.append("FAIL 1: missing front matter block at top")
    else:
        print("1. Single front matter block at top: OK")

    if front_matter is None:
        errors.append("FAIL 2: cannot locate front matter end")
    else:
        try:
            yaml.safe_load(front_matter)
            print("2. Front matter YAML parse: OK")
        except Exception as exc:
            errors.append(f"FAIL 2: {exc}")

    slides = split_slides(body)
    yaml_like_slides = [slide for slide in slides if is_yaml_front_matter_block(slide)]
    if yaml_like_slides:
        errors.append(f"FAIL 1: found {len(yaml_like_slides)} additional front matter-like block(s) in body")

    if re.match(r"\A\s*---\s*(\r?\n|\Z)", body):
        errors.append("FAIL 3: leading separator immediately after front matter")
    if re.search(r"(?s)---\s*\Z", text):
        errors.append("FAIL 3: trailing separator at end of file")
    consecutive = 0
    prev_sep = False
    in_backtick = False
    in_tilde = False
    for line in re.split(r"\r?\n", body):
        stripped = line.strip()
        if re.match(r"^```", line):
            in_backtick = not in_backtick
        elif re.match(r"^~~~", line):
            in_tilde = not in_tilde
        is_sep = not in_backtick and not in_tilde and stripped == "---"
        if is_sep and prev_sep:
            consecutive += 1
        prev_sep = is_sep
        if stripped and not is_sep:
            prev_sep = False
    if consecutive:
        errors.append(f"FAIL 3: {consecutive} consecutive separator pair(s)")
    else:
        print("3. Separator integrity: OK")

    in_backtick = False
    in_tilde = False
    for line in re.split(r"\r?\n", body):
        if re.match(r"^```", line):
            in_backtick = not in_backtick
        elif re.match(r"^~~~", line):
            in_tilde = not in_tilde
    if in_backtick or in_tilde:
        errors.append("FAIL 4: fence imbalance")
    else:
        print("4. Fence balance: OK")

    notes_open = 0
    notes_close = 0
    in_notes = False
    for line in re.split(r"\r?\n", body):
        if re.match(r"^\s*::: notes\s*$", line):
            notes_open += 1
            in_notes = True
            continue
        if in_notes and re.match(r"^\s*:::\s*$", line):
            notes_close += 1
            in_notes = False
            continue
        if in_notes and re.match(r"^---\s*$", line):
            errors.append("FAIL 5: notes block crosses a slide boundary")
            break
    if notes_open != notes_close:
        errors.append(f"FAIL 5: ::: notes={notes_open} opens vs {notes_close} closes")
    else:
        print(f"5. Notes blocks balanced ({notes_open}): OK")

    empty_slides = [index + 1 for index, slide in enumerate(slides) if not slide.strip()]
    if empty_slides:
        errors.append(f"FAIL 6: empty slide block(s) at positions {empty_slides[:5]}")
    else:
        print(f"6. Slide block non-emptiness: OK ({len(slides)} slides)")

    if manifest is not None:
        expected_modules = max(len(manifest["sections"]) - 1, 0)
        module_slides = [slide for slide in slides if re.search(r"(?m)^## Course Modules\s*$", slide)]
        if len(module_slides) != expected_modules:
            errors.append(f"FAIL 7: module list slides={len(module_slides)} expect {expected_modules}")
        else:
            section_names = [section["name"] for section in manifest["sections"]]
            module_errors = []
            for section in manifest["sections"][1:]:
                expected_marker = f"**▶ {section['name']}**"
                matches = [slide for slide in module_slides if expected_marker in slide]
                if len(matches) != 1:
                    module_errors.append(section["name"])
                    continue
                bullets = [re.sub(r"^-\s*", "", line.strip()) for line in matches[0].splitlines() if line.strip().startswith("-")]
                expected_bullets = [f"**▶ {name}**" if name == section["name"] else name for name in section_names]
                if bullets != expected_bullets:
                    module_errors.append(section["name"])
            if module_errors:
                errors.append(f"FAIL 7: module slide mismatch for section(s): {module_errors}")
            else:
                print(f"7. Module list slides injected: {len(module_slides)} (expect {expected_modules})")
    else:
        print("7. Module slide validation: skipped (no manifest provided)")

    if manifest is not None:
        traceability_missing = []
        for section in manifest["sections"]:
            for deck in section.get("decks") or []:
                raw = resolve_repo_path(deck.replace("\\", "/")).read_text(encoding="utf-8-sig")
                body_text = trim_edge_separators(rewrite_image_paths(strip_initial_h1_and_provenance(remove_front_matter(raw))))
                if body_text and normalize_newlines(body_text) not in normalized_text:
                    traceability_missing.append(deck)
        if traceability_missing:
            errors.append(f"FAIL 8: traceability missing for deck(s): {traceability_missing}")
        else:
            print("8. Manifest-to-output traceability: OK")
    else:
        print("8. Manifest-to-output traceability: skipped (no manifest provided)")

    missing_images = []
    for match in sorted(set(re.findall(r"marp/images/[^)\s\"']+", text))):
        image_path = repo_root() / "slides" / Path(match)
        if not image_path.exists():
            missing_images.append(match)
    if missing_images:
        errors.append(f"FAIL 9: missing rewritten image path(s): {missing_images[:5]}")
    else:
        print("9. Post-rewrite image path resolution: OK")

    h1_lines = [line for line in re.split(r"\r?\n", body) if re.match(r"^# ", line)]
    provenance_lines = [line for line in re.split(r"\r?\n", body) if re.match(r"^_Merged from: .*_$", line)]
    if h1_lines or provenance_lines:
        errors.append(f"FAIL 10: remaining H1={len(h1_lines)} provenance={len(provenance_lines)}")
    else:
        print("10. No H1 headings or merged provenance lines in body: OK")

    seen_hashes: set[str] = set()
    duplicate_found = False
    for slide in slides:
        normalized = re.sub(r"\s+", " ", slide).strip()
        if not normalized:
            continue
        digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        if digest in seen_hashes:
            duplicate_found = True
            break
        seen_hashes.add(digest)
    if duplicate_found:
        errors.append("FAIL 11: duplicate slide block detected")
    else:
        print("11. Duplicate slide block detection: OK")

    if manifest is not None:
        expected_text = rebuild_expected_output(manifest)
        if hashlib.sha256(normalize_newlines(expected_text).encode("utf-8")).hexdigest() != hashlib.sha256(normalized_text.encode("utf-8")).hexdigest():
            errors.append("FAIL 12: deterministic output mismatch vs manifest rebuild")
        else:
            print("12. Deterministic output check: OK")
    else:
        print("12. Deterministic output check: skipped (no manifest provided)")

    separators = count_separators_outside_fences(body)
    print(f"V7. Slide count: 1 + {separators} = {1 + separators}")

    if errors:
        print("\nVALIDATION ERRORS:")
        for error in errors:
            print(" ", error)
        return 1

    print("\nPhase 1.5: all checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
