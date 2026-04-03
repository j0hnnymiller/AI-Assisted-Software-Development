"""Temporary Phase 1 build script for aia-compliance merged deck."""
import pathlib
import re

ROOT = pathlib.Path(r'c:\git\AIASD\AI-Assisted-Software-Development-Course')


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def strip_front_matter(text):
    """Remove leading YAML front matter block. Returns (fm_text, body_text)."""
    if not text.startswith('---'):
        return '', text
    end = text.index('\n---', 3)
    fm = text[:end + 4]
    body = text[end + 4:].lstrip('\n')
    return fm, body


def strip_first_h1(body):
    """Strip the first # H1 heading line and immediately following blank lines."""
    lines = body.split('\n')
    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i < len(lines) and re.match(r'^# ', lines[i]):
        lines.pop(i)
        while i < len(lines) and lines[i].strip() == '':
            lines.pop(i)
    return '\n'.join(lines)


def strip_leading_separator(body):
    """Strip one leading bare --- and surrounding blank lines."""
    body = body.lstrip('\n')
    if body.startswith('---\n') or body == '---':
        body = body[4:].lstrip('\n') if body.startswith('---\n') else ''
    return body


def strip_trailing_separator(body):
    """Strip one trailing bare --- and surrounding blank lines."""
    body = body.rstrip('\n')
    if body.endswith('\n---'):
        body = body[:-4].rstrip('\n')
    elif body == '---':
        body = ''
    return body


def rewrite_image_paths(body):
    return body.replace('images/', 'marp/images/')


def module_list_slide(sections, current_idx):
    bullets = []
    for i, s in enumerate(sections):
        name = s['name']
        if i == current_idx:
            bullets.append(f'- **\u25b6 {name}**')
        else:
            bullets.append(f'- {name}')
    return '<!-- _class: lead -->\n\n## Course Modules\n\n' + '\n'.join(bullets)


SEP = '\n\n---\n\n'

sections = [
    {'name': 'AI-Assisted Compliance Webinar',
     'decks': ['slides/marp/aia/aia-compliance-welcome.md']},
    {'name': 'Compliance Challenges',
     'decks': ['slides/marp/aia/aia-compliance-challenges.slides.md']},
    {'name': 'Compliance Assessments',
     'decks': ['slides/marp/aia/aia-compliance-IEC62304-assessment-process.slides.md']},
    {'name': 'Conclusions',
     'decks': ['slides/marp/aia/aia-compliance-conclusion.slides.md']},
]

parts = []
first_fm = ''
front_matter_captured = False

for sec_idx, section in enumerate(sections):
    section_parts = []
    for deck_path in section.get('decks', []):
        raw = read(deck_path)
        fm, body = strip_front_matter(raw)
        if not front_matter_captured:
            first_fm = fm
            front_matter_captured = True
        body = strip_first_h1(body)
        body = strip_leading_separator(body)
        body = strip_trailing_separator(body)
        body = rewrite_image_paths(body)
        section_parts.append(body.strip())

    if sec_idx == 0:
        parts.extend(section_parts)
    else:
        ml = module_list_slide(sections, sec_idx)
        parts.append(ml)
        parts.extend(section_parts)

merged_body = SEP.join(parts)
merged = first_fm + '\n' + merged_body + '\n'

out_path = ROOT / 'slides/merged/aia-compliance-draft.md'
out_path.write_text(merged, encoding='utf-8')
print(f'Written: {out_path}')

# Count slides (bare --- outside fenced code blocks)
in_fence = False
sep_count = 0
for line in merged_body.split('\n'):
    stripped = line.strip()
    if stripped.startswith('```') or stripped.startswith('~~~'):
        in_fence = not in_fence
    if not in_fence and stripped == '---':
        sep_count += 1
slide_count = 1 + sep_count
print(f'Merged deck: {slide_count} slide(s) across {len(sections)} section(s).')
