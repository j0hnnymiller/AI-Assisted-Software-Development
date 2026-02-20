#!/usr/bin/env python3
"""
Extract PPTX to Marp Markdown format with speaker notes.
Requires: pip install python-pptx
"""

import os
import sys
from pathlib import Path

try:
    from pptx import Presentation
except ImportError:
    print("Error: python-pptx not installed. Install with: pip install python-pptx")
    sys.exit(1)


def extract_text_from_shape(shape):
    """Extract text from a shape, handling text frames and tables."""
    text_parts = []

    try:
        # Try text frame first
        if hasattr(shape, "text_frame") and shape.has_text_frame:
            for paragraph in shape.text_frame.paragraphs:
                text = paragraph.text.strip()
                if text:
                    # Determine if it's a bullet point based on paragraph level
                    level = paragraph.level
                    if level > 0:
                        indent = "  " * (level - 1)
                        text_parts.append(f"{indent}- {text}")
                    else:
                        text_parts.append(text)

        # Try table
        elif shape.shape_type == 19:  # 19 = MSO_SHAPE_TYPE.TABLE
            try:
                table = shape.table
                for row in table.rows:
                    row_text = []
                    for cell in row.cells:
                        row_text.append(cell.text.strip())
                    if any(row_text):
                        text_parts.append(" | ".join(row_text))
            except:
                pass
    except Exception:
        # Silently skip shapes that cause errors
        pass

    return text_parts


def convert_pptx_to_marp(pptx_path, output_path):
    """Convert PPTX to Marp Markdown with speaker notes."""

    print(f"Loading presentation: {pptx_path}")
    prs = Presentation(pptx_path)

    # Get presentation title
    title = Path(pptx_path).stem.replace('-', ' ').replace('_', ' ')

    # Start building markdown
    markdown_lines = []

    # Add Marp header
    markdown_lines.extend([
        "---",
        "marp: true",
        "theme: default",
        "paginate: true",
        "header: ''",
        "footer: ''",
        "---",
        "",
        f"# {title}",
        "",
        "---",
        ""
    ])

    # Process each slide
    for slide_num, slide in enumerate(prs.slides, 1):
        print(f"Processing slide {slide_num}...")

        slide_content = []

        # Extract text from all shapes
        for shape in slide.shapes:
            text_parts = extract_text_from_shape(shape)
            if text_parts:  # Only extend if we got results
                slide_content.extend(text_parts)

        # Add slide content
        if slide_content:
            # First line is typically the title
            if slide_content:
                first_line = slide_content[0]
                # Check if it looks like a title (short and not a bullet)
                if len(first_line) < 100 and not first_line.startswith('-'):
                    markdown_lines.append(f"# {first_line}")
                    remaining = slide_content[1:]
                else:
                    remaining = slide_content

                # Add remaining content
                if remaining:
                    markdown_lines.append("")
                    markdown_lines.extend(remaining)

        # Extract speaker notes
        if slide.has_notes_slide:
            notes_slide = slide.notes_slide
            notes_text_frame = notes_slide.notes_text_frame
            notes_text = notes_text_frame.text.strip()

            if notes_text:
                markdown_lines.append("")
                markdown_lines.append("<!--")
                markdown_lines.append("Speaker Notes:")
                markdown_lines.append("")
                # Add notes with proper formatting
                for line in notes_text.split('\n'):
                    line = line.strip()
                    if line:
                        markdown_lines.append(line)
                markdown_lines.append("-->")

        # Add slide separator
        markdown_lines.append("")
        markdown_lines.append("---")
        markdown_lines.append("")

    # Write output file
    print(f"Writing output to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_lines))

    print(f"Successfully converted {len(prs.slides)} slides")
    print(f"Output file: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pptx_to_marp.py <input.pptx> [output.md]")
        sys.exit(1)

    input_path = sys.argv[1]

    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        # Default output path
        output_path = Path(input_path).with_suffix('.marp.md')

    if not os.path.exists(input_path):
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    convert_pptx_to_marp(input_path, output_path)
