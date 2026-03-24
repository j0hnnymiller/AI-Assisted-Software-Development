"""
generate_pptx.py -- Build a PPTX from a YAML manifest using python-pptx.
Requires: pip install python-pptx pyyaml

Usage:
    python generate_pptx.py <yaml_path> <output_pptx_path>

🔒 CRITICAL INVARIANTS (DO NOT BREAK):

1. FIRST SECTION EXCEPTION:
   The first section (idx=0) in the YAML manifest MUST NOT receive injected slides.
   Only sections with idx > 0 get the three injected slides (module list, header, agenda).

   Rationale: First section typically contains welcome/title slides. Adding navigation
   slides before it creates an awkward opening that frontloads course structure.

   Implementation: The section loop MUST use enumerate() and check: if idx > 0

2. SPEAKER NOTES ON ALL SLIDES:
   Every slide (injected and content) MUST have speaker notes:
   - Injected slides: Notes explaining auto-generation and purpose
   - Content slides: Notes showing source file path (e.g., "Source: Slides\\...")

   Rationale: Provides context in PowerPoint for instructors and maintainers.

   Implementation: All add_*_slide() functions MUST accept 'note' parameter and call
   set_slide_notes(slide, note) when note is provided.

3. MARKDOWN LINK RENDERING:
   Markdown links [text](url) are processed according to these rules:
   - If link text == link target: render as just "text"
   - If link text != link target: render as "text: url"

   Rationale: Reduces redundancy for self-describing URLs while preserving
   clarity when link text differs from target.

   Implementation: process_markdown_links() function in parse_slide()

4. MARKDOWN BOLD FORMATTING:
   Markdown bold syntax **text** is parsed and rendered as actual bold formatting in PPTX.

   Rationale: Ensures emphasis and visual hierarchy from source markdown is preserved
   in the PowerPoint output without manual reformatting.

   Implementation: apply_markdown_formatting() function parses **bold** syntax and
   creates text runs with font.bold = True. Used by add_title_content_slide() when
   adding body content to slides.

   Example: "**Principal Engineer**" renders as bold text, not literal asterisks.

5. MARKDOWN BLOCKQUOTE RENDERING:
   Blockquote lines (starting with '> ') are rendered as italic text in PPTX.

   Rationale: PPTX has no native blockquote element. Italic is the closest visual
   equivalent and distinguishes quoted material from normal body text.

   Implementation: apply_markdown_formatting() detects lines starting with '> ',
   strips the prefix, and wraps the content in italic runs.

   Example: "> 'Programming hasn't changed'" renders as italic text without the '> '.

See .github/instructions/slide-pipeline.instructions.md for full specification.
Use the verification checklist in that file before committing changes.
"""
import argparse
import hashlib
import re
from pathlib import Path

import yaml
from lxml import etree
from pptx import Presentation
from pptx.enum.text import MSO_AUTO_SIZE
from pptx.util import Inches

LAYOUT_TITLE_SLIDE = 0  # Title Slide layout
LAYOUT_TITLE_CONTENT = 1  # adjust index if template differs
LAYOUT_SECTION_HEADER = 2  # adjust index if template differs
LAYOUT_TWO_COLUMN = 3  # adjust index if template differs
LAYOUT_TITLE_ONLY = 5  # adjust index if template differs

ALLOWED_SLIDE_EXTENSIONS = {".md", ".markdown"}


def ensure_markdown_slide_entry(slide_path: str | Path) -> None:
    """Fail fast when a manifest slide entry is not a markdown source file."""
    path = Path(slide_path)
    ext = path.suffix.lower()
    if ext and ext not in ALLOWED_SLIDE_EXTENSIONS:
        allowed = ", ".join(sorted(ALLOWED_SLIDE_EXTENSIONS))
        raise ValueError(
            f"Non-markdown slide entry detected: {slide_path} "
            f"(extension: {ext}). Expected one of: {allowed}. "
            "Use a markdown slide source in sections[].slides, or configure a .pptx under the top-level template field."
        )


def extract_slide_title(file_path: Path) -> str:
    """Return the first ## H2 heading text, or the file stem as fallback."""
    ensure_markdown_slide_entry(file_path)
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


def resolve_repo_path(repo_root: Path, candidate: str | Path) -> Path:
    """Resolve a manifest path relative to the repository root."""
    path = Path(candidate)
    if path.is_absolute():
        return path
    return repo_root / path


def get_slide_layout(prs: Presentation, preferred_names: list[str], fallback_index: int):
    """Return the first layout whose name matches, else fall back to an index."""
    normalized_names = {name.strip().casefold() for name in preferred_names if name.strip()}

    for layout in prs.slide_layouts:
        layout_name = getattr(layout, "name", "").strip().casefold()
        if layout_name in normalized_names:
            return layout

    try:
        return prs.slide_layouts[fallback_index]
    except IndexError:
        return prs.slide_layouts[0]


def build_section_id(section_name: str, slide_start_idx: int) -> str:
    """Return a deterministic section id for the PPTX XML."""
    digest = hashlib.sha1(f"{section_name}:{slide_start_idx}".encode("utf-8")).hexdigest()
    return str(int(digest[:8], 16))


def split_marp_slides(md_content: str) -> list[str]:
    """Split a Marp markdown file into individual slide blocks.

    Strips the YAML front matter, then splits the remaining content on bare
    `---` lines that are NOT inside fenced code blocks.
    Returns a list of slide content strings (one per slide).
    """
    lines = md_content.splitlines()

    # Strip YAML front matter. We can't just take the first closing `---`
    # because AI provenance `prompt: |` blocks may legitimately contain `---`
    # lines as plain scalar content.
    if lines and lines[0].strip() == "---":
        for end in range(1, len(lines)):
            if lines[end] != "---":
                continue
            front_matter = "\n".join(lines[1:end])
            try:
                parsed = yaml.safe_load(front_matter)
            except yaml.YAMLError:
                continue
            if isinstance(parsed, dict):
                lines = lines[end + 1:]
                break

    # Split on bare --- separators outside fenced code blocks
    slides: list[list[str]] = []
    current: list[str] = []
    in_fence = False
    fence_pat = re.compile(r"^(`{3,}|~{3,})")

    for line in lines:
        if fence_pat.match(line):
            in_fence = not in_fence
        if line == "---" and not in_fence:
            slides.append(current)
            current = []
        else:
            current.append(line)
    slides.append(current)

    # Filter out empty or whitespace-only blocks
    return ["\n".join(block).strip() for block in slides if any(l.strip() for l in block)]


def process_markdown_links(text: str) -> str:
    """
    Process markdown links according to rendering rules:
    - If link text == link target: render just the link text
    - If link text != link target: render as "link text: link target"
    """
    def replace_link(match):
        link_text = match.group(1)
        link_target = match.group(2)

        if link_text == link_target:
            return link_text
        else:
            return f"{link_text}: {link_target}"

    # Match markdown links: [text](url)
    # Use non-greedy matching to handle multiple links on one line
    pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    return re.sub(pattern, replace_link, text)


def apply_markdown_formatting(text_frame, line_text: str) -> None:
    """
    Parse markdown bold and blockquote syntax and add formatted runs to the text frame paragraph.
    Supports **bold text** syntax and > blockquote syntax.

    Blockquote lines (starting with '> ') are rendered as italic text — PPTX has no
    native blockquote element so italic is the closest visual equivalent.

    Example: "This is **bold text** and normal"
    -> Run 1: "This is " (normal)
    -> Run 2: "bold text" (bold)
    -> Run 3: " and normal" (normal)

    Example: "> 'Programming hasn't changed'"
    -> Run 1: "'Programming hasn't changed'" (italic)
    """
    # Handle blockquote lines: render as italic, strip the '> ' prefix
    is_blockquote = line_text.startswith("> ")
    if is_blockquote:
        line_text = line_text[2:]

    # Pattern to match **bold text**
    # Using non-greedy matching to handle multiple bold sections on one line
    pattern = r'\*\*([^\*]+)\*\*'

    # Find all bold sections
    bold_sections = []
    for match in re.finditer(pattern, line_text):
        bold_sections.append((match.start(), match.end(), match.group(1)))

    # If no bold sections, just add the text as-is (with italic if blockquote)
    if not bold_sections:
        p = text_frame.add_paragraph()
        if line_text.startswith("- "):
            p.text = line_text[2:]
            p.level = 0
        else:
            p.text = line_text
        if is_blockquote:
            for run in p.runs:
                run.font.italic = True
            # If text was set directly (no runs), we need to use a run
            if not p.runs:
                p.clear()
                run = p.add_run()
                run.text = line_text
                run.font.italic = True
        return

    # Build the line with formatting
    p = text_frame.add_paragraph()
    if line_text.startswith("- "):
        # Remove bullet prefix, it will be added by paragraph level
        line_text = line_text[2:]
        p.level = 0
        # Adjust positions for removed "- "
        bold_sections = [(start - 2, end - 2, text) for start, end, text in bold_sections]

    # Add runs with proper formatting
    last_pos = 0
    for start, end, bold_text in bold_sections:
        # Add normal text before this bold section
        if start > last_pos:
            run = p.add_run()
            run.text = line_text[last_pos:start]
            if is_blockquote:
                run.font.italic = True

        # Add bold text
        run = p.add_run()
        run.text = bold_text
        run.font.bold = True
        if is_blockquote:
            run.font.italic = True

        last_pos = end

    # Add any remaining normal text after the last bold section
    if last_pos < len(line_text):
        run = p.add_run()
        run.text = line_text[last_pos:]
        if is_blockquote:
            run.font.italic = True


def contains_markdown_table(body: str) -> bool:
    """Check if the body contains a markdown table."""
    lines = body.strip().splitlines()
    for i, line in enumerate(lines):
        # A markdown table has a separator line with |---|---| pattern
        if re.match(r'^\s*\|?\s*[-:]+\s*\|', line):
            return True
    return False


def parse_markdown_table(body: str) -> list[list[str]]:
    """Parse a markdown table and return rows of cells.

    Returns a list of rows, where each row is a list of cell values.
    Example:
        | Header 1 | Header 2 |
        |----------|----------|
        | Cell 1   | Cell 2   |

    Returns: [['Header 1', 'Header 2'], ['Cell 1', 'Cell 2']]
    """
    lines = body.strip().splitlines()
    rows = []

    for line in lines:
        line = line.strip()
        # Skip separator lines (|---|---|)
        if re.match(r'^\|?\s*[-:]+\s*\|', line):
            continue
        # Parse table rows
        if '|' in line:
            # Remove leading/trailing pipes if present
            if line.startswith('|'):
                line = line[1:]
            if line.endswith('|'):
                line = line[:-1]
            # Split by pipe and strip whitespace
            cells = [cell.strip() for cell in line.split('|')]
            rows.append(cells)

    return rows


def parse_slide(md_content: str) -> tuple[str, str, str | None, str]:
    """Return (title, body, background_image_path, speaker_notes) parsed from a single markdown slide block."""
    lines = md_content.strip().splitlines()

    title = ""
    body_lines = []
    bg_image = None
    speaker_notes = ""

    # Pattern to match Marp background images: ![bg ...](path)
    bg_pattern = re.compile(r'!\[bg[^\]]*\]\(([^)]+)\)')

    for line in lines:
        if not title and line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            if not title:
                title = line[3:].strip()
        else:
            # Extract background image path if present
            stripped = line.strip()
            if stripped.startswith("![bg"):
                match = bg_pattern.match(stripped)
                if match:
                    bg_image = match.group(1)
            # Skip Marp directives (background images and HTML comments)
            elif not stripped.startswith("<!--"):
                body_lines.append(line)

    # Extract speaker notes (::: notes ... :::) from body
    body = "\n".join(body_lines).strip()
    notes_pattern = re.compile(r":::[ \t]*notes(.*?):::", re.DOTALL | re.IGNORECASE)
    notes_match = notes_pattern.search(body)
    if notes_match:
        speaker_notes = notes_match.group(1).strip()
        body = notes_pattern.sub("", body).strip()

    # Process markdown links according to rendering rules
    body = process_markdown_links(body)

    return title, body, bg_image, speaker_notes


def set_slide_notes(slide, note_text: str) -> None:
    """Set the speaker notes on a slide."""
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = note_text


def populate_text_placeholder(shape, body: str) -> None:
    """Populate a text placeholder using the existing markdown formatting rules."""
    tf = shape.text_frame
    tf.clear()
    for line in body.splitlines():
        apply_markdown_formatting(tf, line)
    tf.margin_top = Inches(0.05)
    tf.margin_bottom = Inches(0.05)
    tf.margin_left = Inches(0.1)
    tf.margin_right = Inches(0.1)
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE


def split_two_column_body(body: str) -> tuple[str, str]:
    """Split slide body into left/right column text.

    Supported formats:
    - Explicit separator line: `::: column`
    - Two or more `###` subsections, where the first two become left/right columns
    """
    separator_pattern = re.compile(r"^\s*:::\s*column\s*$", re.IGNORECASE | re.MULTILINE)
    if separator_pattern.search(body):
        left, right = separator_pattern.split(body, maxsplit=1)
        return left.strip(), right.strip()

    sections: list[tuple[str | None, list[str]]] = []
    current_heading: str | None = None
    current_lines: list[str] = []

    for line in body.splitlines():
        if line.startswith("### "):
            if current_heading is not None or current_lines:
                sections.append((current_heading, current_lines))
            current_heading = line[4:].strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_heading is not None or current_lines:
        sections.append((current_heading, current_lines))

    if len(sections) >= 2:
        def render_section(section_heading: str | None, section_lines: list[str]) -> str:
            rendered_lines: list[str] = []
            if section_heading:
                rendered_lines.append(f"**{section_heading}**")
            rendered_lines.extend(section_lines)
            return "\n".join(rendered_lines).strip()

        left_heading, left_lines = sections[0]
        right_heading, right_lines = sections[1]
        return render_section(left_heading, left_lines), render_section(right_heading, right_lines)

    return body.strip(), ""


def add_title_content_slide(prs: Presentation, title: str, body: str, note: str = "") -> None:
    """Add a Title and Content layout slide with markdown bold formatting support."""
    layout = get_slide_layout(prs, ["Title and Content"], LAYOUT_TITLE_CONTENT)
    slide = prs.slides.add_slide(layout)
    if slide.shapes.title:
        slide.shapes.title.text = title

    for shape in slide.placeholders:
        if shape.placeholder_format.idx == 1:
            populate_text_placeholder(shape, body)
            break

    if note:
        set_slide_notes(slide, note)


def add_two_column_slide(
    prs: Presentation,
    title: str,
    left_body: str,
    right_body: str,
    note: str = "",
) -> None:
    """Add a two-column slide using the template's two-column layout."""
    layout = get_slide_layout(prs, ["Two Column", "Two Columns", "Two Content"], LAYOUT_TWO_COLUMN)
    slide = prs.slides.add_slide(layout)
    if slide.shapes.title:
        slide.shapes.title.text = title

    for shape in slide.placeholders:
        idx = shape.placeholder_format.idx
        if idx == 1 and left_body:
            populate_text_placeholder(shape, left_body)
        elif idx == 2 and right_body:
            populate_text_placeholder(shape, right_body)

    if note:
        set_slide_notes(slide, note)


def add_table_slide(prs: Presentation, title: str, table_data: list[list[str]], note: str = "") -> None:
    """Add a Title and Content layout slide with a table."""
    layout = prs.slide_layouts[LAYOUT_TITLE_CONTENT]
    slide = prs.slides.add_slide(layout)

    if slide.shapes.title:
        slide.shapes.title.text = title

    # Remove the content placeholder to make room for the table
    for shape in slide.placeholders:
        if shape.placeholder_format.idx == 1:
            sp = shape.element
            sp.getparent().remove(sp)
            break

    # Calculate table dimensions
    rows = len(table_data)
    cols = max(len(row) for row in table_data) if table_data else 0

    if rows > 0 and cols > 0:
        # Position and size the table
        left = Inches(0.5)
        top = Inches(2.0)
        width = Inches(9.0)
        height = Inches(0.5 * rows)  # Dynamic height based on number of rows

        # Add table
        table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
        table = table_shape.table

        # Populate table cells
        for i, row_data in enumerate(table_data):
            for j, cell_value in enumerate(row_data):
                if j < cols:  # Ensure we don't exceed column count
                    cell = table.cell(i, j)
                    cell.text = cell_value
                    # Format header row (first row) differently
                    if i == 0:
                        cell.text_frame.paragraphs[0].font.bold = True
                        cell.text_frame.paragraphs[0].font.size = Inches(0.18)

    if note:
        set_slide_notes(slide, note)


def add_title_only_slide(prs: Presentation, title: str, bg_image: str | None = None, note: str = "") -> None:
    """Add a Title Only layout slide (no body content), optionally with a background image."""
    try:
        layout = get_slide_layout(prs, ["Title Only"], LAYOUT_TITLE_ONLY)
    except IndexError:
        layout = get_slide_layout(prs, ["Title and Content"], LAYOUT_TITLE_CONTENT)

    slide = prs.slides.add_slide(layout)

    # Add background image first (before setting title) so it appears behind content
    if bg_image:
        try:
            # Add image to fill the slide (standard 16:9 is 10x7.5 inches)
            pic = slide.shapes.add_picture(
                bg_image,
                left=0,
                top=0,
                width=Inches(10),
                height=Inches(7.5)
            )
            # Move the picture to the back by manipulating the XML
            slide.shapes._spTree.remove(pic._element)
            slide.shapes._spTree.insert(2, pic._element)
        except Exception as e:
            print(f"  WARNING: Could not add background image {bg_image}: {e}")

    # Set title after adding background image
    if slide.shapes.title:
        slide.shapes.title.text = title

    if note:
        set_slide_notes(slide, note)


def add_section_header_slide(prs: Presentation, section_name: str, note: str = "") -> None:
    """Add a section header slide (# Section Name, lead layout)."""
    try:
        layout = get_slide_layout(prs, ["Section Header"], LAYOUT_SECTION_HEADER)
    except IndexError:
        layout = prs.slide_layouts[0]

    slide = prs.slides.add_slide(layout)
    if slide.shapes.title:
        slide.shapes.title.text = section_name

    if note:
        set_slide_notes(slide, note)


def add_title_slide(prs: Presentation, title: str, subtitle: str = "", note: str = "") -> None:
    """Add a Title Slide layout (typically used for presentation opening)."""
    try:
        layout = get_slide_layout(prs, ["Title Slide"], LAYOUT_TITLE_SLIDE)
    except IndexError:
        layout = prs.slide_layouts[0]

    slide = prs.slides.add_slide(layout)

    # Title Slide typically has two placeholders: title (idx 0) and subtitle (idx 1)
    for shape in slide.placeholders:
        idx = shape.placeholder_format.idx
        if idx == 0:
            shape.text = title
        elif idx == 1 and subtitle:
            shape.text = subtitle

    if note:
        set_slide_notes(slide, note)


def add_module_list_slide(prs: Presentation, all_sections: list[str], current: str, note: str = "") -> None:
    """Add a Course Modules navigation slide; current section is bold + arrow."""
    layout = get_slide_layout(prs, ["Title and Content"], LAYOUT_TITLE_CONTENT)
    slide = prs.slides.add_slide(layout)
    if slide.shapes.title:
        slide.shapes.title.text = "Course Modules"

    for shape in slide.placeholders:
        if shape.placeholder_format.idx == 1:
            tf = shape.text_frame
            tf.clear()
            tf.word_wrap = True
            for name in all_sections:
                p = tf.add_paragraph()
                p.level = 0
                run = p.add_run()
                if name == current:
                    run.text = f"▶ {name}"
                    run.font.bold = True
                else:
                    run.text = name
            tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
            break

    if note:
        set_slide_notes(slide, note)


def add_section_agenda_slide(
    prs: Presentation, section_name: str, slide_files: list, repo_root: Path
) -> None:
    """Add an agenda slide listing titles extracted from source files."""
    if not slide_files:
        return

    # Extract file paths (support both string and dict entries)
    paths = []
    for entry in slide_files:
        if isinstance(entry, dict):
            path = entry.get("file") or entry.get("path")
        else:
            path = entry
        if path:
            paths.append(path)

    titles = [extract_slide_title(resolve_repo_path(repo_root, f)) for f in paths]
    add_title_content_slide(
        prs,
        section_name,
        "\n".join(f"- {t}" for t in titles),
        note="Auto-generated section agenda slide listing slide titles from manifest"
    )


def build_presentation(yaml_path: Path, output_path: Path) -> None:
    yaml_path = yaml_path.resolve()
    repo_root = yaml_path.parent.parent

    with open(yaml_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    sections_cfg = config.get("sections", [])
    all_section_names = [s.get("name", "Unnamed Section") for s in sections_cfg]

    template = config.get("template")
    if template:
        template_path = resolve_repo_path(repo_root, template)
        if not template_path.exists():
            template_path = Path(template)
        prs = Presentation(str(template_path))
        print(f"Using template: {template_path}")
    else:
        prs = Presentation()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Populate the template title slide (slide 0) if title/subtitle are provided.
    prs_title = config.get("title", "")
    prs_subtitle = config.get("subtitle", "")
    if prs.slides and (prs_title or prs_subtitle):
        title_slide = prs.slides[0]
        for shape in title_slide.placeholders:
            idx = shape.placeholder_format.idx
            if idx == 0 and prs_title:
                shape.text = prs_title
            elif idx == 1 and prs_subtitle:
                shape.text = prs_subtitle

    # Populate the template Agenda slide (slide 1) with section names.
    if len(prs.slides) > 1:
        agenda_slide = prs.slides[1]
        # Only populate if title is "Agenda" (or placeholder is empty)
        agenda_title = ""
        for shape in agenda_slide.shapes:
            if shape.has_text_frame and "title" in shape.name.lower():
                agenda_title = shape.text_frame.text.strip()
                break
        if agenda_title.lower() == "agenda":
            for shape in agenda_slide.placeholders:
                if shape.placeholder_format.idx == 1:
                    tf = shape.text_frame
                    tf.clear()
                    tf.word_wrap = True
                    for name in all_section_names:
                        p = tf.add_paragraph()
                        p.text = name
                    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
                    break

    # python-pptx exposes the underlying <p:presentation> element via part._element.
    prs_el = prs.part._element
    ns14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
    etree.register_namespace("p14", ns14)
    section_lst_tag = f"{{{ns14}}}sectionLst"
    section_lst = prs_el.find(section_lst_tag)
    if section_lst is not None:
        prs_el.remove(section_lst)
    section_lst = etree.SubElement(prs_el, section_lst_tag)

    for idx, section in enumerate(sections_cfg):
        section_name = section.get("name", "Unnamed Section")
        slides = [s for s in (section.get("slides") or []) if s]

        slide_start_idx = len(prs.slides)

        # Per specification (.github/instructions/slide-pipeline.instructions.md section 4):
        # Skip injected slides for first section to prevent navigation-heavy opening
        # that would precede the welcome slide.
        if idx > 0:
            add_module_list_slide(
                prs,
                all_section_names,
                section_name,
                note="Auto-generated course navigation slide showing all modules with current section highlighted"
            )
            add_section_header_slide(
                prs,
                section_name,
                note="Auto-generated section header slide to announce the section"
            )
            add_section_agenda_slide(prs, section_name, slides, repo_root)

        for slide_entry in slides:
            # Support both simple string paths and dict with layout specification
            if isinstance(slide_entry, dict):
                slide_path = slide_entry.get("file") or slide_entry.get("path")
                layout_type = slide_entry.get("layout", "").strip().lower()
            else:
                slide_path = slide_entry
                layout_type = ""

            ensure_markdown_slide_entry(slide_path)

            slide_file = resolve_repo_path(repo_root, slide_path)
            if not slide_file.exists():
                print(f"  WARNING: not found -- {slide_file}")
                continue

            note = f"Source: {slide_path}"
            md = slide_file.read_text(encoding="utf-8")
            slide_blocks = split_marp_slides(md)
            for block in slide_blocks:
                title, body, bg_image, speaker_notes = parse_slide(block)

                # Combine source path with speaker notes if they exist
                if speaker_notes:
                    combined_note = f"{speaker_notes}\n\n---\n\nSource: {slide_path}"
                else:
                    combined_note = note

                # Resolve background image path relative to Slides folder (yaml_path.parent)
                bg_image_path = None
                if bg_image:
                    # Try resolving relative to yaml_path.parent (Slides folder)
                    bg_image_path = (yaml_path.parent / bg_image).resolve()
                    if not bg_image_path.exists():
                        # Fall back to repo root resolution
                        bg_image_path = resolve_repo_path(repo_root, bg_image)
                    if not bg_image_path.exists():
                        print(f"  WARNING: background image not found -- {bg_image_path}")
                        bg_image_path = None
                    else:
                        bg_image_path = str(bg_image_path)

                # Honor explicit layout specification
                if layout_type == "title" or layout_type == "title slide":
                    # Extract subtitle from body (first line)
                    subtitle = body.split("\n")[0] if body else ""
                    add_title_slide(prs, title or slide_file.stem, subtitle, note=combined_note)
                elif layout_type in {"two column", "two columns", "two content"}:
                    left_body, right_body = split_two_column_body(body)
                    add_two_column_slide(
                        prs,
                        title or slide_file.stem,
                        left_body,
                        right_body,
                        note=combined_note,
                    )
                elif contains_markdown_table(body):
                    # Parse and create table slide
                    table_data = parse_markdown_table(body)
                    add_table_slide(prs, title or slide_file.stem, table_data, note=combined_note)
                elif body:
                    add_title_content_slide(prs, title or slide_file.stem, body, note=combined_note)
                else:
                    add_title_only_slide(prs, title or slide_file.stem, bg_image=bg_image_path, note=combined_note)

        slide_end_idx = len(prs.slides)
        all_sld_ids = list(prs.slides._sldIdLst)
        section_el = etree.SubElement(
            section_lst,
            f"{{{ns14}}}section",
            attrib={
                "name": section_name,
                "id": build_section_id(section_name, slide_start_idx),
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
