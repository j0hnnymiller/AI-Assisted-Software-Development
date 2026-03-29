import unittest

from scripts.generate_pptx import split_marp_slides


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


if __name__ == "__main__":
    unittest.main()
