#!/usr/bin/env python3
"""
Convert PPTX to Markdown by extracting text content from slides.
"""

import os
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


def extract_text_from_pptx(pptx_path):
    """Extract text from PPTX file by parsing the XML structure."""
    try:
        slides_text = []

        with zipfile.ZipFile(pptx_path, 'r') as pptx:
            # List all files in the PPTX
            file_list = pptx.namelist()

            # Get slide files and sort them properly
            slide_files = []
            for filename in file_list:
                if filename.startswith('ppt/slides/slide') and filename.endswith('.xml'):
                    # Extract slide number
                    match = re.search(r'slide(\d+)\.xml', filename)
                    if match:
                        slide_num = int(match.group(1))
                        slide_files.append((slide_num, filename))

            # Sort by slide number
            slide_files.sort(key=lambda x: x[0])

            print(f"Found {len(slide_files)} slides")

            for slide_num, slide_file in slide_files:
                try:
                    slide_xml = pptx.read(slide_file)

                    # Parse XML with namespace handling
                    root = ET.fromstring(slide_xml)

                    # Extract text elements
                    text_elements = []

                    # Find all text runs
                    for t_elem in root.iter():
                        if t_elem.tag.endswith('}t') and t_elem.text:
                            text_elements.append(t_elem.text.strip())

                    if text_elements:
                        slide_text = '\n'.join(text_elements)
                        slides_text.append((slide_num, slide_text))
                        print(f"Slide {slide_num}: {len(text_elements)} text elements")
                    else:
                        print(f"Slide {slide_num}: No text found")

                except Exception as e:
                    print(f"Error processing slide {slide_num}: {e}")
                    continue

        return slides_text

    except FileNotFoundError:
        print(f"Error: File not found: {pptx_path}")
        return []
    except zipfile.BadZipFile:
        print(f"Error: Invalid PPTX file: {pptx_path}")
        return []
    except Exception as e:
        print(f"Error reading PPTX: {e}")
        return []


def convert_pptx_to_md(pptx_path, md_path):
    """Convert PPTX file to Markdown."""
    print(f"Converting: {pptx_path}")

    if not os.path.exists(pptx_path):
        print(f"Error: Input file not found: {pptx_path}")
        return False

    # Extract slides
    slides = extract_text_from_pptx(pptx_path)

    if not slides:
        print("No content extracted from PPTX")
        return False

    # Write markdown
    try:
        os.makedirs(os.path.dirname(md_path), exist_ok=True)

        with open(md_path, 'w', encoding='utf-8') as f:
            # Get the base filename for title
            title = Path(pptx_path).stem.replace('-', ' ').title()
            f.write(f"# {title}\n\n")
            f.write(f"Converted from: {os.path.basename(pptx_path)}\n\n")

            for slide_num, slide_text in slides:
                f.write(f"## Slide {slide_num}\n\n")

                # Clean up text formatting
                lines = slide_text.split('\n')
                formatted_lines = []

                for line in lines:
                    line = line.strip()
                    if line:
                        # If line looks like a title (all caps or title case), make it a header
                        if line.isupper() and len(line.split()) <= 6:
                            formatted_lines.append(f"### {line.title()}")
                        else:
                            # Check if it's a bullet point
                            if any(line.startswith(bullet) for bullet in ['•', '○', '▪', '-', '*']):
                                formatted_lines.append(line)
                            else:
                                formatted_lines.append(f"- {line}")

                if formatted_lines:
                    f.write('\n'.join(formatted_lines))
                else:
                    f.write(slide_text)

                f.write('\n\n')

        print(f"Successfully created: {md_path}")
        print(f"Converted {len(slides)} slides")
        return True

    except Exception as e:
        print(f"Error writing Markdown: {e}")
        return False


if __name__ == "__main__":
    # Default paths
    pptx_file = "Slides/individual-slides/Fundementals-Agenda.pptx"
    md_file = "Slides/individual-slides/Fundementals-Agenda.md"

    # Allow command line arguments
    if len(sys.argv) >= 2:
        pptx_file = sys.argv[1]
    if len(sys.argv) >= 3:
        md_file = sys.argv[2]

    success = convert_pptx_to_md(pptx_file, md_file)
    sys.exit(0 if success else 1)
