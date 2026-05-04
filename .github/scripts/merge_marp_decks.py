"""
Phase 1 Merge Script - Generate complete merged markdown from manifest
Reads slides/manifests/aiasd-311-monday.ge.manifest.md and merges all source files according to spec.
"""
import re
from pathlib import Path

import yaml


def strip_h1_and_provenance(content):
    """Remove H1 headers and YAML front matter provenance from source content."""
    # Remove BOM if present
    content = content.lstrip('\ufeff')

    # Remove YAML front matter (handle both \n and \r\n line endings)
    content = re.sub(r'^---\s*[\r\n]+.*?[\r\n]+---\s*[\r\n]+', '', content, flags=re.DOTALL)

    # Remove H1 headers but preserve centered two-title format (contains ||)
    lines = content.split('\n')
    filtered_lines = []
    for line in lines:
        # Keep the line unless it's an H1 that doesn't contain ||
        if line.startswith('# ') and '||' not in line:
            continue  # Skip this H1
        filtered_lines.append(line)

    content = '\n'.join(filtered_lines)
    return content.strip()

def strip_outer_separators(content):
    """Remove leading and trailing --- separators, keep internal ones."""
    lines = content.split('\n')
    # Remove leading ---
    while lines and lines[0].strip() == '---':
        lines.pop(0)
    # Remove trailing ---
    while lines and lines[-1].strip() == '---':
        lines.pop()
    return '\n'.join(lines)

def rewrite_image_paths(content):
    """Rewrite images/ to marp/images/."""
    return content.replace('images/', 'marp/images/')

def get_module_list_slide(sections, current_section):
    """Generate module list slide with current section highlighted."""
    lines = ["<!-- layout: Section Header -->", "", "## Course Modules", ""]
    for section in sections:
        section_name = section['name']
        if section_name == current_section:
            lines.append(f"- **▶ {section_name}**")
        else:
            lines.append(f"- {section_name}")
    return '\n'.join(lines)

def merge_section(section_data, base_path, sections, is_first_section):
    """Merge all files in a section."""
    result = []

    # Add module list slide for sections 2-6 (not first/Intro section)
    if not is_first_section:
        module_list = get_module_list_slide(sections, section_data['name'])
        result.append(module_list)

    # Process each file in the section
    for i, deck_path in enumerate(section_data['decks']):
        # Normalize path separators for cross-platform compatibility
        deck_path = deck_path.replace('\\', '/')
        file_path = Path(deck_path)
        print(f"  Processing: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Do NOT strip anything from the first file (welcome-to-aiasd.deck.md) as it provides front matter
        if is_first_section and i == 0:
            # Keep complete content including front matter for first file
            processed = content.strip()
        else:
            # Apply standard processing to all other files
            processed = strip_h1_and_provenance(content)
            processed = strip_outer_separators(processed)

        processed = rewrite_image_paths(processed)
        result.append(processed)

    return result

def main():
    # Load manifest
    manifest_path = Path("slides/manifests/aiasd-311-monday.ge.manifest.md")
    output_path = Path("slides/merged/aiasd-311-monday.ge-draft.md")
    base_path = Path("slides")

    print(f"Loading manifest: {manifest_path}")
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = yaml.safe_load(f)

    title = manifest['title']
    sections = manifest['sections']

    print(f"\nMerging deck: {title}")
    print(f"Sections: {len(sections)}")

    all_content = []

    # Process each section
    for i, section in enumerate(sections):
        section_name = section['name']
        is_first = (i == 0)

        print(f"\nSection {i+1}: {section_name} ({len(section['decks'])} files)")
        section_content = merge_section(section, base_path, sections, is_first)
        all_content.extend(section_content)

    # Join all content with proper separators
    merged_content = '\n\n---\n\n'.join(all_content)

    # Write output
    print(f"\nWriting merged deck to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(merged_content)

    # Count slides (count --- separators outside code blocks + 1)
    slide_count = merged_content.count('\n---\n') + 1

    print("\n✓ Phase 1 complete!")
    print(f"  Merged deck: {slide_count} slides across {len(sections)} sections")
    print(f"  Output: {output_path}")

if __name__ == "__main__":
    main()
