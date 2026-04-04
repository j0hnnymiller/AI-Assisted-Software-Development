import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from pptx import Presentation

from scripts.generate_pptx import (
    build_presentation,
    mark_slide_hidden,
    parse_slide,
    split_marp_slides,
)


class SplitMarpSlidesTests(unittest.TestCase):
    def test_tab_indented_front_matter_is_stripped(self):
        md_content = """---
ai_generated: true
model: \"openai/gpt-5.3-codex@2026-03-28\"
prompt: |
\tcompare generate_pptx.py to regression manifest
\tand create new regression decks
marp: true
theme: default
paginate: true
---

# Architecture Truth || But Make It Memorable

::: notes
**Expected PPTX Rendering:**
- Layout: Centered Two Titles
:::

---

## Content After H1 Dividers

Body text.
"""

        slides = split_marp_slides(md_content)

        self.assertEqual(2, len(slides))
        self.assertTrue(slides[0].startswith("# Architecture Truth || But Make It Memorable"))
        self.assertNotIn("ai_generated:", slides[0])
        self.assertIn("**Expected PPTX Rendering:**", slides[0])

    def test_parse_slide_detects_hide_class_comment(self):
        slide_block = """<!-- _class: hide -->

## Placeholder for Instructor Bio

Body text
"""

        (
            title,
            body,
            _bg_image,
            _speaker_notes,
            _layout_name,
            _inline_images,
            _title_is_h1,
            _matter_of_fact_title,
            should_hide_slide,
        ) = parse_slide(slide_block)

        self.assertEqual("Placeholder for Instructor Bio", title)
        self.assertEqual("Body text", body)
        self.assertTrue(should_hide_slide)

    def test_mark_slide_hidden_sets_show_zero(self):
        prs = Presentation()
        slide = prs.slides.add_slide(prs.slide_layouts[0])

        mark_slide_hidden(slide)

        self.assertEqual("0", slide._element.get("show"))

    def test_regression_manifest_marks_hidden_slide_in_output(self):
        repo_root = Path(__file__).resolve().parent
        manifest_path = repo_root / "slides" / "manifests" / "regression-test-01.manifest.md"

        with TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "regression-test-01-draft.pptx"
            build_presentation(manifest_path, output_path)

            prs = Presentation(output_path)
            hidden_titles = [
                (slide.shapes.title.text.strip() if slide.shapes.title and slide.shapes.title.text else "")
                for slide in prs.slides
                if slide._element.get("show") == "0"
            ]

        self.assertIn("Hidden Slide Branch", hidden_titles)


if __name__ == "__main__":
    unittest.main()
