#!/usr/bin/env python3
"""
Phase 1: Merge Marp Slide Decks
Combines individual Marp slide files into a unified deck with injected navigation slides.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

# Character replacements for merge normalization
# NOTE: Backtick replacement is handled specially to preserve code fences
MERGE_CHAR_REPLACEMENTS = {
    # Backticks are handled by normalize_backticks() to preserve code fences
}

def normalize_backticks(body: str) -> str:
    """
    Replace single backticks with single quotes for inline code,
    but preserve triple backticks and triple tildes for code fences.

    This prevents breaking code fence markers (``` or ~~~) while still
    normalizing problematic characters in inline content.
    """
    lines = body.split('\n')
    result = []

    for line in lines:
        stripped = line.strip()
        # Preserve lines that start with code fence markers
        if stripped.startswith('```') or stripped.startswith('~~~'):
            result.append(line)
        else:
            # Replace single backticks in non-fence lines
            # Only replace standalone backticks, not those in groups of 3+
            modified = line
            # Replace single backticks that aren't part of triple backticks
            # Use negative lookahead/lookbehind to avoid matching ``` sequences
            modified = re.sub(r'(?<!`)`(?!`)', "'", modified)
            result.append(modified)

    return '\n'.join(result)


def load_manifest(manifest_path: str) -> Dict:
    """Load and parse the YAML manifest."""
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract_front_matter_and_body(content: str) -> Tuple[Optional[str], str]:
    """
    Extract YAML front matter and body from a markdown file.
    Returns (front_matter, body) tuple.
    """
    # Match front matter: starts with ---, ends with ---
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if match:
        return match.group(1), match.group(2)
    return None, content

def extract_first_h2(body: str) -> Optional[str]:
    """Extract the first ## H2 heading from the body."""
    # Find first ## heading (not inside code blocks)
    lines = body.split('\n')
    in_code_block = False

    for line in lines:
        # Track code fences
        if line.strip().startswith('```') or line.strip().startswith('~~~'):
            in_code_block = not in_code_block
            continue

        if not in_code_block and line.startswith('## '):
            return line[3:].strip()

    return None

def remove_h1_headings(body: str, preserve_first_h1: bool = False) -> str:
    """Remove any # H1 headings and their provenance lines.

    Exception: Preserve H1s with || separator (Centered Two Titles layout directive),
    but still strip any provenance lines that follow them.

    Args:
        body: The markdown body text
        preserve_first_h1: If True, preserve the very first H1 encountered (for first deck in manifest)
    """
    lines = body.split('\n')
    result = []
    i = 0
    first_h1_seen = False

    while i < len(lines):
        line = lines[i]

        # Check if this is an H1 heading
        if line.startswith('# ') and not line.startswith('## '):
            # Preserve first H1 if requested (first deck in manifest)
            if preserve_first_h1 and not first_h1_seen:
                first_h1_seen = True
                result.append(line)
                i += 1

                # Still skip blank lines and provenance after preserved H1
                while i < len(lines) and lines[i].strip() == '':
                    i += 1

                if i < len(lines) and lines[i].strip().startswith('_Merged from:'):
                    i += 1
                    # Skip blank lines after provenance
                    while i < len(lines) and lines[i].strip() == '':
                        i += 1

                continue

            # Preserve H1s with || separator (layout directive for Centered Two Titles)
            if '||' in line:
                result.append(line)
                i += 1

                # Still skip blank lines and provenance after preserved H1s
                while i < len(lines) and lines[i].strip() == '':
                    i += 1

                if i < len(lines) and lines[i].strip().startswith('_Merged from:'):
                    i += 1
                    # Skip blank lines after provenance
                    while i < len(lines) and lines[i].strip() == '':
                        i += 1

                continue

            # Regular H1 - strip it and its provenance
            i += 1

            # Skip blank lines directly after the stripped H1.
            while i < len(lines) and lines[i].strip() == '':
                i += 1

            # Strip immediately-adjacent provenance lines after H1.
            if i < len(lines) and lines[i].strip().startswith('_Merged from:'):
                i += 1

                # Also skip one blank spacer after the provenance line.
                while i < len(lines) and lines[i].strip() == '':
                    i += 1

            continue

        result.append(line)
        i += 1

    return '\n'.join(result)

def remove_provenance_lines(body: str) -> str:
    """Remove provenance lines (_Merged from: ..._) that appear after H1 headings.

    These lines are metadata added during merge and should not appear in the final output.
    They typically appear on the line following an H1 heading.
    """
    lines = body.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a provenance line
        if line.strip().startswith('_Merged from:') and line.strip().endswith('_'):
            # Skip the provenance line
            i += 1
            # Skip any blank lines after provenance
            while i < len(lines) and lines[i].strip() == '':
                i += 1
            continue

        result.append(line)
        i += 1

    return '\n'.join(result)

def clean_file_body(body: str, preserve_first_h1: bool = False) -> str:
    """
    Clean a file body according to merge rules:
    - Keep H1 headings intact (changed: no longer stripping H1s)
    - Remove provenance lines (_Merged from: ..._)
    - Rewrite source-local images/ references for merged deck output
    - Normalize merge-time character substitutions
    - Strip leading and trailing slide separators

    Args:
        body: The markdown body text
        preserve_first_h1: DEPRECATED parameter (kept for API compatibility, no longer used)
    """
    # NOTE: H1 headings are now preserved in merged markdown
    # Phase 2 (generate_pptx.py) will render them as Section Header slides

    # Remove provenance lines that appear after H1 headings
    body = remove_provenance_lines(body)

    # Source decks keep images under slides/marp/images, but merged decks live in slides/.
    body = body.replace('](images/', '](marp/images/')
    body = body.replace('src="images/', 'src="marp/images/')
    body = body.replace("src='images/", "src='marp/images/")
    body = body.replace("url('images/", "url('marp/images/")
    body = body.replace('url("images/', 'url("marp/images/')
    body = body.replace('url(images/', 'url(marp/images/')

    # Rewrite legacy inline image markers used by older slide exports.
    body = re.sub(
        r'(!Slide\s+\d+\s+image:\s+)images/',
        r'\1marp/images/',
        body,
        flags=re.IGNORECASE,
    )

    # Normalize backticks (preserving code fence markers)
    body = normalize_backticks(body)

    # Normalize other characters that render poorly or inconsistently after merge
    for source, target in MERGE_CHAR_REPLACEMENTS.items():
        body = body.replace(source, target)

    # Strip leading and trailing --- separators (with surrounding whitespace)
    body = body.strip()

    # Remove leading separator
    if body.startswith('---'):
        body = body[3:].lstrip('\n')

    # Remove trailing separator
    if body.endswith('---'):
        body = body[:-3].rstrip('\n')

    return body.strip()

def count_slides_in_block(body: str) -> int:
    """
    Count slides in a body block.
    Each bare --- outside code blocks is a slide separator.
    """
    lines = body.split('\n')
    in_code_block = False
    separator_count = 0

    for line in lines:
        stripped = line.strip()

        # Track code fences
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_code_block = not in_code_block
            continue

        # Count bare --- lines outside code blocks
        if not in_code_block and stripped == '---':
            separator_count += 1

    # slide_count = 1 + number of separators
    return 1 + separator_count

def create_module_list_slide(section_names: List[str], current_idx: int) -> str:
    """Create the module list slide with current section highlighted."""
    bullets = []
    for i, name in enumerate(section_names):
        if i == current_idx:
            bullets.append(f"- **▶ {name}**")
        else:
            bullets.append(f"- {name}")

    return f"""<!-- _class: lead -->

## Course Modules

{chr(10).join(bullets)}"""

def create_section_header_slide(section_name: str) -> str:
    """Create the section header slide."""
    return f"""<!-- _class: lead -->

# {section_name}"""

def create_section_agenda_slide(section_name: str, slide_titles: List[str]) -> str:
    """
    Create the section agenda slide.
    Excludes slides whose titles start with "Exercise" (case-insensitive).
    """
    # Filter out exercise slides
    filtered_titles = [
        title for title in slide_titles
        if not title.lower().startswith('exercise')
    ]

    if not filtered_titles:
        # No agenda if no non-exercise slides
        return ""

    bullets = [f"- {title}" for title in filtered_titles]

    return f"""## {section_name}

{chr(10).join(bullets)}"""

def merge_marp_decks(manifest_path: str, output_path: str):
    """Main merge function."""
    manifest = load_manifest(manifest_path)
    sections = manifest.get('sections', [])

    if not sections:
        print("ERROR: No sections found in manifest")
        sys.exit(1)

    # Collect section names for module list
    section_names = [s['name'] for s in sections]

    # Storage for merged content
    merged_parts = []
    first_front_matter = None
    total_slide_count = 0
    global_file_idx = 0  # Track if we're processing the very first file

    print(f"Processing {len(sections)} sections...")

    for section_idx, section in enumerate(sections):
        section_name = section['name']
        deck_files = section.get('decks', [])

        print(f"\n=== Section {section_idx + 1}: {section_name} ===")

        # Process slide files first to get titles
        file_contents = []
        slide_titles = []

        for slide_entry in deck_files:
            # Handle both formats: string path or dict with 'file' key
            if isinstance(slide_entry, dict):
                file_path = slide_entry.get('file')
            else:
                file_path = slide_entry

            if not file_path:
                continue

            # Read the file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except FileNotFoundError:
                print(f"  WARNING: File not found: {file_path}")
                continue

            # Extract front matter and body
            front_matter, body = extract_front_matter_and_body(content)

            # Save first front matter
            if first_front_matter is None and front_matter:
                first_front_matter = front_matter

            # Extract first H2 for agenda
            first_h2 = extract_first_h2(body)
            if first_h2:
                slide_titles.append(first_h2)
            else:
                # Fallback to filename
                slide_titles.append(Path(file_path).stem)

            # Clean the body (preserve first H1 for very first file only)
            is_first_file = (global_file_idx == 0)
            cleaned_body = clean_file_body(body, preserve_first_h1=is_first_file)
            global_file_idx += 1

            # Count slides in this file
            slide_count = count_slides_in_block(cleaned_body)
            if is_first_file:
                print(f"  {Path(file_path).name}: {slide_count} slides [FIRST FILE - H1 PRESERVED]")
            else:
                print(f"  {Path(file_path).name}: {slide_count} slides")

            file_contents.append(cleaned_body)

        # For first section (idx=0), skip injected slides
        if section_idx == 0:
            print("  [First section: skipping injected slides]")
            # Just add content slides
            for content in file_contents:
                merged_parts.append(content)
                total_slide_count += count_slides_in_block(content)
        else:
            # Add module list slide
            module_list = create_module_list_slide(section_names, section_idx)
            merged_parts.append(module_list)
            total_slide_count += 1
            print("  + Module list slide")

            # Add section header slide
            section_header = create_section_header_slide(section_name)
            merged_parts.append(section_header)
            total_slide_count += 1
            print("  + Section header slide")

            # Add section agenda slide (if non-exercise slides exist)
            section_agenda = create_section_agenda_slide(section_name, slide_titles)
            if section_agenda:
                merged_parts.append(section_agenda)
                total_slide_count += 1
                print(f"  + Section agenda slide ({len([t for t in slide_titles if not t.lower().startswith('exercise')])} topics)")

            # Add content slides
            for content in file_contents:
                merged_parts.append(content)
                total_slide_count += count_slides_in_block(content)

    # Assemble final output
    final_output = []

    # Add front matter
    if first_front_matter:
        final_output.append(f"---\n{first_front_matter}\n---")

    # Join all parts with slide separators
    final_output.append('\n\n---\n\n'.join(merged_parts))

    # Write output
    output_content = '\n\n'.join(final_output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_content)

    print(f"\n{'='*60}")
    print("Phase 1 Complete!")
    print(f"Total slides: {total_slide_count}")
    print(f"Output: {output_path}")
    print(f"{'='*60}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        manifest_path = 'slides/manifests/aiasd-311-monday.manifest.md'
    else:
        manifest_path = sys.argv[1]

    # Derive output filename
    manifest_stem = Path(manifest_path).stem
    output_path = f'slides/{manifest_stem}-draft.md'

    if len(sys.argv) >= 3:
        output_path = sys.argv[2]

    merge_marp_decks(manifest_path, output_path)
