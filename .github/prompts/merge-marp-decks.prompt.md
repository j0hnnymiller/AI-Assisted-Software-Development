---
mode: agent
model: "anthropic/claude-sonnet-4-5@2025-02-19"
tools: ["read", "create", "edit", "search", "run_command"]
description: Merges Marp slide decks listed in a YAML file into a single Marp deck and generates a PPTX with named sections using python-pptx.
prompt_metadata:
  id: merge-marp-decks
  title: Merge Marp Slide Decks and Generate PPTX
  owner: johnmillerATcodemag-com
  version: 2.1.0
  created: 2026-03-12
  updated: 2026-03-13
  output_path: Slides/aiasd-311-monday-draft.md
  output_format: markdown
  category: slides
  tags: [marp, slides, merge, presentation, markdown, pptx, python-pptx]
---

# Merge Marp Slide Decks and Generate PPTX

Merge the Marp slide decks defined in `$YAML_FILE` into a single Marp slide deck saved as
`$OUTPUT_FILE`, then generate a PPTX with named sections using `python-pptx`.

## Default Values

- `$YAML_FILE` = `Slides/aiasd-311-monday.yaml`
- `$OUTPUT_FILE` = derived from `$YAML_FILE`: strip `.yaml` and append `-draft.md`
  (e.g. `Slides/aiasd-311-monday.yaml` → `Slides/aiasd-311-monday-draft.md`)
- `$PPTX_SCRIPT` = `Slides/output/generate_pptx.py`
- `$PPTX_OUTPUT` = `Slides/output/aiasd-draft.monday.pptx`

> **Agent verification (Issue 3)**: After computing `$OUTPUT_FILE`, confirm its filename
> matches the pattern `<course>-<format>-<day>-draft.md` derived from the `$YAML_FILE` stem.

## YAML Structure

`$YAML_FILE` uses a sectioned structure:

```yaml
sections:
  - name: <Section Name>
    slides:
      - Slides\individual-slides\<file>.md
      - Slides\individual-slides\<file>.md
  - name: <Empty Section>
    slides:
      # no slide files listed — still creates an empty PPTX section
```

Each section has a `name` and an optional `slides` list. Sections with no slide files
(null, empty, or comment-only) are still present in the final PPTX as **empty sections**.

---

## Phase 0 — Validate Source Files

For every source file path referenced in `$YAML_FILE`, read the file and check:

| # | Rule | Check |
|---|------|-------|
| 1 | **Front matter** | File begins with a valid Marp YAML front-matter block (`---` … `---`) |
| 2 | **No H1 in body** | No `# H1` headings appear after the front-matter block |
| 3 | **H2 present** | At least one `## H2` heading exists in the body |
| 4 | **Image paths** | No `../images/` references (must use `images/` prefix) |
| 5 | **No trailing separator** | File does not end with a bare `---` line |
| 6 | **Encoding** | No vertical-tab (`\x0b`) characters |

Log a warning for each violation and continue — do not abort. Print a validation summary
before writing `$OUTPUT_FILE`:

```
Validation complete: N file(s) checked, M warning(s) found.
```

> **Agent verification (Issue 1)**: After running Phase 0, confirm the validation summary
> is printed. For a file known to violate a rule (e.g. ends with `---`), verify the warning
> appears and the merge still completes successfully.

---

## Phase 1 — Merge Markdown

### Steps

1. Read `$YAML_FILE`; collect all sections (names + slide file lists) in manifest order
2. Collect all section names into a list — used to build every module list slide
3. For each section, build the section block following the rules below
4. Concatenate all section blocks (each injected slide and each merged source block
   separated by exactly one `\n\n---\n\n`)
5. Write the result to `$OUTPUT_FILE`

### Injected slides

Insert three auto-generated slides at the start of **every** section, before any source
content slides. They are produced entirely from manifest data and source file titles.

#### 1. Module list slide (always, first in every section)

```markdown
<!-- _class: lead -->

## Course Modules

- Section A
- **▶ Current Section**
- Section C
```

Rules:

- One bullet per section in manifest order, using the exact `name` from YAML
- The section being introduced: `**▶ Section Name**` (bold, arrow prefix)
- All other sections: plain `Section Name`

#### 2. Section header slide (always, second)

```markdown
<!-- _class: lead -->

# Section Name
```

`Section Name` is the exact `name` value from the manifest.

#### 3. Section agenda slide (third, only when section has source files)

Lists the first `## H2` heading from each source file as a bullet.

```markdown
## Section Name

- Slide Title From File 1
- Slide Title From File 2
```

Slide title extraction:

1. Strip the YAML front-matter block (`---` … `---`) from the file content
2. Find the **first `## H2` heading** in the remaining text
3. Use its text (without `## `) as the title
4. Fallback: file stem (filename without extension) if no `## H2` is found

#### Full slide order per section

```
1. Module list slide              (always)
2. Section header slide           (always)
3. Section agenda slide           (only when section has source files)
4. Content slides from file 1     (only when section has source files)
5. Content slides from file 2 …
```

### Merge rules for source content files

#### Front matter

- Use the YAML front matter from the **first source file across all sections**
- Place it at the very top of `$OUTPUT_FILE`, before the first section block
- Strip front matter from all subsequent source files
- The first file's front matter provides `title:` and `subtitle:` — do not remove them

#### Level-1 headings (`# H1`)

- Strip **all** `# H1` headings from every source file (replaced by injected section
  header slides)
- Also strip any immediately-following provenance lines like `_Merged from: ..._`

#### Slide separators (`---`)

- Preserve all `---` separators that appear within each source file's content
- `---` lines that appear inside fenced code blocks (` ``` ` or `~~~`) are **never** treated
  as slide separators — preserve them verbatim
- Between injected slides and between source file blocks use exactly one `\n\n---\n\n`
- Do not double-up separators

> **Agent verification (Issue 2)**: Open a source file containing a YAML code block with
> internal `---` lines. After merging, confirm those `---` lines are present verbatim in
> `$OUTPUT_FILE` and do not create unexpected extra slides (slide count must match
> expectation).

#### All other content

- Include verbatim: `## H2` headings, body text, bullet lists, images, speaker notes
  (`::: notes` blocks), inline styles

#### Image paths

- Source files use `../images/` for their own Marp preview; the merged deck lives in
  `Slides/`, so rewrite `../images/` → `images/` in all image references
- All other content is preserved verbatim

### Output format

- Single YAML front matter block at top (from first source file, with `title:` and
  `subtitle:` fields)
- No `# H1` headings in the body
- `<!-- _class: lead -->` directives present on module list and section header slides
- `## H2` headings on all content slides and section agenda slides

### Slide counting

After writing `$OUTPUT_FILE`, count and report the total number of slides produced:

```
slide_count = 1 + (number of bare --- lines outside fenced code blocks)
```

Each injected slide (module list, section header, section agenda) counts as 1 slide.
Report the count in the form: `Merged deck: N slide(s) across M section(s).`

> **Agent verification (Issue 7)**: Compare the reported slide count against a manual count
> of `---` separators in `$OUTPUT_FILE` (excluding those inside code fences). The counts
> must match.

---

## Phase 2 — Generate PPTX with Sections

Create `$PPTX_SCRIPT` using the template below, then execute it.

### Script Requirements

The script must:

1. Parse `$YAML_FILE` to get sections and their slide file lists
2. Collect all section names — used to build every module list slide
3. For **every** section (including empty ones) emit four slide groups in order:
   a. Module list slide (all section names; current section highlighted)
   b. Section header slide
   c. Section agenda slide (only when section has source files)
   d. One content slide per source file
4. Group every slide in the section under a named `<p14:section>` XML element
5. Save to `$PPTX_OUTPUT`

### Script Template

```python
"""
generate_pptx.py — Build a PPTX from a YAML manifest using python-pptx.
Requires: pip install python-pptx pyyaml

Usage:
    python generate_pptx.py <yaml_path> <output_pptx_path>
"""
import argparse
import re
import yaml
from pathlib import Path
from pptx import Presentation
from lxml import etree

LAYOUT_TITLE_CONTENT  = 1  # adjust index if template differs
LAYOUT_SECTION_HEADER = 2  # adjust index if template differs
LAYOUT_TITLE_ONLY     = 5  # adjust index if template differs


def extract_slide_title(file_path: Path) -> str:
    """Return the first ## H2 heading text, or the file stem as fallback."""
    try:
        text = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return file_path.stem
    # Strip YAML front matter
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    for line in text.splitlines():
        m = re.match(r"^## (.+)", line)
        if m:
            return m.group(1).strip()
    return file_path.stem


def parse_slide(md_content: str) -> tuple[str, str]:
    """Return (title, body) parsed from a markdown slide block."""
    lines = md_content.strip().splitlines()
    if lines and lines[0].strip() == "---":
        end = next((i for i, l in enumerate(lines[1:], 1) if l.strip() == "---"), None)
        if end:
            lines = lines[end + 1:]
    title, body_lines = "", []
    for line in lines:
        if not title and line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            if not title:
                title = line[3:].strip()
        else:
            body_lines.append(line)
    return title, "\n".join(body_lines).strip()


def add_title_content_slide(prs: Presentation, title: str, body: str) -> None:
    """Add a Title and Content layout slide."""
    layout = prs.slide_layouts[LAYOUT_TITLE_CONTENT]
    slide = prs.slides.add_slide(layout)
    if slide.shapes.title:
        slide.shapes.title.text = title
    for shape in slide.placeholders:
        if shape.placeholder_format.idx == 1:
            tf = shape.text_frame
            tf.clear()
            for line in body.splitlines():
                p = tf.add_paragraph()
                if line.startswith("- "):
                    p.text = line[2:]
                    p.level = 0
                else:
                    p.text = line
            break


def add_title_only_slide(prs: Presentation, title: str) -> None:
    """Add a Title Only layout slide (no body content)."""
    try:
        layout = prs.slide_layouts[LAYOUT_TITLE_ONLY]
    except IndexError:
        layout = prs.slide_layouts[LAYOUT_TITLE_CONTENT]
    slide = prs.slides.add_slide(layout)
    if slide.shapes.title:
        slide.shapes.title.text = title


def add_section_header_slide(prs: Presentation, section_name: str) -> None:
    """Add a section header slide (# Section Name, lead layout)."""
    try:
        layout = prs.slide_layouts[LAYOUT_SECTION_HEADER]
    except IndexError:
        layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(layout)
    if slide.shapes.title:
        slide.shapes.title.text = section_name


def add_module_list_slide(
    prs: Presentation, all_sections: list[str], current: str
) -> None:
    """Add a 'Course Modules' navigation slide; current section is bold + arrow."""
    layout = prs.slide_layouts[LAYOUT_TITLE_CONTENT]
    slide = prs.slides.add_slide(layout)
    if slide.shapes.title:
        slide.shapes.title.text = "Course Modules"
    for shape in slide.placeholders:
        if shape.placeholder_format.idx == 1:
            tf = shape.text_frame
            tf.clear()
            for name in all_sections:
                p = tf.add_paragraph()
                p.level = 0
                run = p.add_run()
                if name == current:
                    run.text = f"▶ {name}"
                    run.font.bold = True
                else:
                    run.text = name
            break


def add_section_agenda_slide(
    prs: Presentation, section_name: str, slide_files: list
) -> None:
    """Add an agenda slide listing titles extracted from source files."""
    if not slide_files:
        return
    titles = [extract_slide_title(Path(f)) for f in slide_files]
    add_title_content_slide(prs, section_name, "\n".join(f"- {t}" for t in titles))


def build_presentation(yaml_path: Path, output_path: Path) -> None:
    with open(yaml_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    sections_cfg = config.get("sections", [])
    all_section_names = [s.get("name", "Unnamed Section") for s in sections_cfg]

    prs = Presentation()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    prs_el = prs.presentation
    ns14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
    etree.register_namespace("p14", ns14)
    section_lst_tag = f"{{{ns14}}}sectionLst"
    section_lst = prs_el.find(section_lst_tag)
    if section_lst is None:
        section_lst = etree.SubElement(prs_el, section_lst_tag)

    for section in sections_cfg:
        section_name = section.get("name", "Unnamed Section")
        slides = [s for s in (section.get("slides") or []) if s]

        slide_start_idx = len(prs.slides)

        # 1. Module list slide
        add_module_list_slide(prs, all_section_names, section_name)

        # 2. Section header slide
        add_section_header_slide(prs, section_name)

        # 3. Section agenda slide (only when source files exist)
        add_section_agenda_slide(prs, section_name, slides)

        # 4. Content slides
        for slide_path in slides:
            slide_file = Path(slide_path)
            if not slide_file.exists():
                print(f"  WARNING: not found — {slide_file}")
                continue
            md = slide_file.read_text(encoding="utf-8")
            title, body = parse_slide(md)
            if body:
                add_title_content_slide(prs, title or slide_file.stem, body)
            else:
                add_title_only_slide(prs, title or slide_file.stem)

        # Register named section in XML
        slide_end_idx = len(prs.slides)
        all_sld_ids = list(prs.slides._sldIdLst)
        section_el = etree.SubElement(
            section_lst,
            f"{{{ns14}}}section",
            attrib={
                "name": section_name,
                "id": str(abs(hash(section_name + str(slide_start_idx))) % (10**8)),
            },
        )
        sld_id_lst_section = etree.SubElement(section_el, f"{{{ns14}}}sldIdLst")
        for sld_el in all_sld_ids[slide_start_idx:slide_end_idx]:
            etree.SubElement(
                sld_id_lst_section,
                f"{{{ns14}}}sldId",
                attrib={"id": sld_el.get("id")},
            )
        if not slides:
            print(f"  INFO: Section '{section_name}' is empty — only injected slides added")

    prs.save(output_path)
    print(f"✅ Saved: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build PPTX from YAML manifest")
    parser.add_argument("yaml_path", help="Path to the YAML manifest file")
    parser.add_argument("output_path", help="Path for the generated PPTX")
    args = parser.parse_args()
    build_presentation(Path(args.yaml_path), Path(args.output_path))
```

### Execution

After creating `$PPTX_SCRIPT`, run:

```bash
pip install python-pptx pyyaml --quiet
python $PPTX_SCRIPT $YAML_FILE $PPTX_OUTPUT
```

Report any warnings (missing slide files) and confirm the output path on success.

> **Agent verification (Issue 4)**: Inspect the written `$PPTX_SCRIPT` — confirm no
> hard-coded `YAML_PATH` or `OUTPUT_PATH` variables exist and the script accepts `yaml_path`
> and `output_path` as positional arguments. Run `python $PPTX_SCRIPT $YAML_FILE $PPTX_OUTPUT`
> and verify the PPTX is created at `$PPTX_OUTPUT`.
>
> **Agent verification (Issue 5)**: Open the generated PPTX. For any source slide whose
> `## heading` had no body content, confirm that slide uses the `Title Only` layout
> (index `LAYOUT_TITLE_ONLY`), not `Title and Content`.

---

## Deliverables

1. `$OUTPUT_FILE` — merged Marp markdown deck (with injected module list, section header,
   and agenda slides)
2. `$PPTX_SCRIPT` (`Slides/output/generate_pptx.py`) — PPTX generation script
3. `$PPTX_OUTPUT` — generated PPTX with named sections

## Section Handling Rules

- **Every** section in the YAML becomes a named section in the PPTX, regardless of whether
  it contains source slide files
- Every section gets a module list slide and a section header slide
- Sections with source files additionally get a section agenda slide followed by content slides
- Sections with no source files produce only the module list slide and section header slide,
  and an empty PPTX section group
- Section names in the PPTX match the `name` field in the YAML exactly
- Slide file paths are resolved relative to the repository root

> **Agent verification (Issue 6)**: Add a section to `$YAML_FILE` with no `slides:` entries.
> Run the PPTX phase and confirm `INFO: Section '...' is empty — only injected slides added`
> is printed, and the resulting PPTX contains a named section group with only the module
> list and section header slides.

---

## Agent Verification Checklist

Run all checks below after the pipeline completes to confirm spec conformance.

| # | Issue | Check | Pass condition |
|---|-------|-------|----------------|
| V1 | Source validation | Phase 0 summary printed before `$OUTPUT_FILE` is written | `Validation complete: N file(s) checked, M warning(s) found.` appears in output |
| V2 | Code-fence `---` preserved | Merge a source file that contains `---` inside a fenced code block | No unexpected extra slides; the embedded `---` appears verbatim in `$OUTPUT_FILE` |
| V3 | Output file named correctly | Inspect `$OUTPUT_FILE` path | Filename matches `<course>-<format>-<day>-draft.md` derived from `$YAML_FILE` stem |
| V4 | Script accepts CLI arguments | Inspect written `$PPTX_SCRIPT` | No hard-coded `YAML_PATH`/`OUTPUT_PATH`; `argparse` with `yaml_path` and `output_path` positional args present |
| V5 | `Title Only` layout used | Source file with `## heading` and no body content | PPTX slide uses `Title Only` layout (`LAYOUT_TITLE_ONLY` index), not `Title and Content` |
| V6 | Empty section logged | YAML section with no `slides:` entries | `INFO: Section '...' is empty — only injected slides added` printed during PPTX phase |
| V7 | Slide count reported | Any successful merge run | Output includes `Merged deck: N slide(s) across M section(s).` |
