import os

import yaml

manifest_path = r"c:\git\AIASD\AI-Assisted-Software-Development-Course\slides\manifests\aiasd-311-monday.ge.manifest.md"
base_dir = r"c:\git\AIASD\AI-Assisted-Software-Development-Course"

with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = yaml.safe_load(f)

# Phase 0: Validate
warnings = []
results = {}

for section in manifest.get('sections', []):
    for deck in section.get('decks', []):
        deck_path = os.path.join(base_dir, deck.replace('\\', '/'))
        if not os.path.exists(deck_path):
            warnings.append(f"Missing file: {deck}")
            continue
        with open(deck_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Validation checks
        if not content.startswith('---'):
            warnings.append(f"{deck}: Missing front matter")
        if '## ' not in content:
            warnings.append(f"{deck}: Missing H2 heading")
        if '../images/' in content:
            warnings.append(f"{deck}: Contains ../images/ reference")
        if content.strip().endswith('---'):
            warnings.append(f"{deck}: Trailing separator")
        if '\x0b' in content:
            warnings.append(f"{deck}: Contains vertical tab")

        results[deck] = content

print(f"Validation complete: {len(results)} file(s) checked, {len(warnings)} warning(s) found.")
for w in warnings:
    print(f"WARN: {w}")

# Phase 1: Merge Markdown
merged_content = []
section_names = [s.get('name') for s in manifest.get('sections', [])]

first_file = True
slide_count = 0

for i, section in enumerate(manifest.get('sections', [])):
    # Module list slide (skip for first section)
    if i > 0:
        module_slide = ["<!-- _class: lead -->\n\n## Course Modules\n"]
        for name in section_names:
            if name == section.get('name'):
                module_slide.append(f"- **▶ {name}**")
            else:
                module_slide.append(f"- {name}")

        merged_content.append('\n'.join(module_slide))
        slide_count += 1

    for deck in section.get('decks', []):
        if deck not in results:
            continue
        content = results[deck]

        # Process content
        lines = content.split('\n')

        # Extract front matter
        fm_end = 0
        if content.startswith('---'):
            for j in range(1, len(lines)):
                if lines[j].strip() == '---':
                    fm_end = j
                    break

        if first_file:
            # Keep front matter
            merged_content.append('\n'.join(lines[0:fm_end+1]))
            first_file = False

        body_lines = lines[fm_end+1:] if fm_end > 0 else lines

        # Strip H1 and immediately following metadata/blank lines
        in_h1_removal = False
        cleaned_body = []
        skip_next_blank = False

        for k, line in enumerate(body_lines):
            if in_h1_removal:
                if line.strip().startswith('_Merged from:') or line.strip() == '':
                    continue
                else:
                    in_h1_removal = False
                    cleaned_body.append(line)
            elif line.startswith('# '):
                in_h1_removal = True
            else:
                cleaned_body.append(line)

        body_text = '\n'.join(cleaned_body).strip()

        # Strip leading ---
        if body_text.startswith('---'):
            body_text = body_text[3:].lstrip()

        # Strip trailing ---
        if body_text.endswith('---'):
            body_text = body_text[:-3].rstrip()

        # Rewrite image paths
        body_text = body_text.replace('images/', 'marp/images/')

        # Count slides in this deck:
        # We need to count non-fenced `---`
        in_fence = False
        deck_slides = 1
        for line in body_text.split('\n'):
            if line.strip().startswith('```') or line.strip().startswith('~~~'):
                in_fence = not in_fence
            elif line.strip() == '---' and not in_fence:
                deck_slides += 1
        slide_count += deck_slides

        merged_content.append(body_text)

merged_text = '\n\n---\n\n'.join(merged_content)

out_path = r"c:\git\AIASD\AI-Assisted-Software-Development-Course\slides\merged\aiasd-311-monday.ge-draft.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(merged_text)

print(f"Merged deck: {slide_count} slide(s) across {len(section_names)} section(s).")
