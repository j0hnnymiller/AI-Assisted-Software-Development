"""
Phase 1 merge script for aia-compliance.manifest.md.
Implements rules from .github/prompts/merge-marp-decks.prompt.md.
"""
import re
import sys
from pathlib import Path

import yaml

REPO = Path(".")

def strip_front_matter(text):
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return "", text
    idx = text.find("\n---\n", 3)
    if idx == -1:
        idx = text.find("\n---", 3)
        if idx != -1 and idx + 4 >= len(text):
            return text[: idx + 4], ""
        return "", text
    fm = text[: idx + 4]
    body = text[idx + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    return fm, body

def strip_first_h1(body):
    lines = body.split("\n")
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r"^#\s", stripped) or stripped == "#":
            del lines[i]
            if i < len(lines) and re.match(r"^_Merged from:.*_$", lines[i].strip()):
                del lines[i]
            break
    return "\n".join(lines)

def strip_leading_sep(body):
    body = body.lstrip("\n")
    m = re.match(r"^---[ \t]*\n", body)
    if m:
        body = body[m.end():].lstrip("\n")
    elif body.strip() == "---":
        body = ""
    return body

def strip_trailing_sep(body):
    body = body.rstrip("\n")
    if re.search(r"\n---[ \t]*$", body):
        body = re.sub(r"\n---[ \t]*$", "", body).rstrip("\n")
    elif body.strip() == "---":
        body = ""
    return body

def rewrite_images(body):
    return re.sub(r"(?<!marp/)images/", "marp/images/", body)

def module_slide(section_names, current_idx):
    lines = ["<!-- _class: lead -->", "", "## Course Modules", ""]
    for i, name in enumerate(section_names):
        if i == current_idx:
            lines.append(f"- **\u25b6 {name}**")
        else:
            lines.append(f"- {name}")
    return "\n".join(lines)

def count_slides(content):
    # skip front matter
    if content.startswith("---\n"):
        idx = content.find("\n---\n", 3)
        body = content[idx + 4:] if idx != -1 else ""
    else:
        body = content
    in_fence = False
    fence_char = None
    seps = 0
    for line in body.split("\n"):
        s = line.strip()
        if not in_fence:
            if s.startswith("```") or s.startswith("~~~"):
                in_fence = True
                fence_char = "```" if s.startswith("```") else "~~~"
            elif s == "---":
                seps += 1
        else:
            if fence_char == "```" and s.startswith("```"):
                in_fence = False
            elif fence_char == "~~~" and s.startswith("~~~"):
                in_fence = False
    return 1 + seps

manifest = yaml.safe_load(Path("slides/manifests/aia-compliance.manifest.md").read_text(encoding="utf-8"))
sections = manifest["sections"]
section_names = [s["name"] for s in sections]

first_fm = None
blocks = []
SEP = "\n\n---\n\n"

for sec_idx, section in enumerate(sections):
    decks = section.get("decks") or []
    if sec_idx > 0:
        blocks.append(module_slide(section_names, sec_idx))
    for raw_path in decks:
        fpath = REPO / raw_path.replace("\\\\", "/").replace("\\", "/")
        content = fpath.read_text(encoding="utf-8").replace("\r\n", "\n")
        fm, body = strip_front_matter(content)
        if first_fm is None and fm:
            first_fm = fm
        body = strip_first_h1(body)
        body = strip_leading_sep(body)
        body = strip_trailing_sep(body)
        body = rewrite_images(body)
        body = body.strip("\n")
        if body:
            blocks.append(body)

if not first_fm:
    sys.exit("ERROR: no front matter captured")

merged_content = first_fm + "\n" + SEP.join(blocks) + "\n"
out = Path("slides/merged/aia-compliance-draft.md")
out.write_text(merged_content, encoding="utf-8")
sc = count_slides(merged_content)
print(f"Merged deck: {sc} slide(s) across {len(sections)} section(s).")
print(f"Written: {out}")
