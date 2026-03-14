"""
generate_pptx.py -- Build a PPTX from a YAML manifest using python-pptx.
Requires: pip install python-pptx pyyaml

Usage:
    python generate_pptx.py <yaml_path> <output_pptx_path>
"""
import argparse
import re
from pathlib import Path

import yaml
from lxml import etree
from pptx import Presentation

LAYOUT_TITLE_CONTENT = 1  # adjust index if template differs
LAYOUT_SECTION_HEADER = 2  # adjust index if template differs
LAYOUT_TITLE_ONLY = 5  # adjust index if template differs


def extract_slide_title(file_path: Path) -> str:
    """Return the first ## H2 heading text, or the file stem as fallback."""
    try:
        text = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return file_path.stem

    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]

    for line in text.splitlines():
        m = re.match(r"^## (.+)", line)
        if m:
            return m.group(1).strip()
    return file_path.stem


def parse_slide(md_content: str) -> tuple[str, str]:
    """Return (title, body) parsed from a markdown slide block."""
    lines = md_content.strip().splitlines()
    if lines and lines[0].strip() == "---":
        end = next(
            (i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"),
            None,
        )
        if end:
            lines = lines[end + 1 :]

    title = ""
    body_lines = []
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


def add_module_list_slide(prs: Presentation, all_sections: list[str], current: str) -> None:
    """Add a Course Modules navigation slide; current section is bold + arrow."""
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


def add_section_agenda_slide(prs: Presentation, section_name: str, slide_files: list) -> None:
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

    # python-pptx exposes the underlying <p:presentation> element via part._element.
    prs_el = prs.part._element
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

        add_module_list_slide(prs, all_section_names, section_name)
        add_section_header_slide(prs, section_name)
        add_section_agenda_slide(prs, section_name, slides)

        for slide_path in slides:
            slide_file = Path(slide_path)
            if not slide_file.exists():
                print(f"  WARNING: not found -- {slide_file}")
                continue

            md = slide_file.read_text(encoding="utf-8")
            title, body = parse_slide(md)
            if body:
                add_title_content_slide(prs, title or slide_file.stem, body)
            else:
                add_title_only_slide(prs, title or slide_file.stem)

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
            print(
                f"  INFO: Section '{section_name}' is empty -- only injected slides added"
            )

    prs.save(output_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build PPTX from YAML manifest")
    parser.add_argument("yaml_path", help="Path to the YAML manifest file")
    parser.add_argument("output_path", help="Path for the generated PPTX")
    args = parser.parse_args()
    build_presentation(Path(args.yaml_path), Path(args.output_path))
