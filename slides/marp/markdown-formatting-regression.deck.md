---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-25"
operator: "johnmillerATcodemag-com"
chat_id: "markdown-regression-slide-20260325"
prompt: |
  Add a dedicated markdown regression slide deck to verify PPTX rendering for
  bold, italic, underline, strikethrough, ordered lists, unordered lists,
  task lists, links, blockquotes, inline code, fenced code blocks, and tables.
started: "2026-03-25T00:00:00Z"
ended: "2026-03-25T00:10:00Z"
task_durations:
  - task: "author regression deck"
    duration: "00:07:00"
  - task: "validate rendering flow"
    duration: "00:03:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2026/03/25/markdown-regression-slide-20260325/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

## Markdown Rendering Regression

This deck contains one slide per markdown feature with richer examples.

- Goal: visual regression checks after formatter changes
- Script under test: `scripts/generate_pptx.py`
- Focus: parser behavior and rendering output in generated PPTX

::: notes
This is the cover and intent slide for the regression suite.
The following slides isolate markdown features so failures are easy to diagnose.
If a specific feature regresses, use the slide title to map directly to parser logic.
:::

---

## Emphasis and Inline Styles

- **Bold sample**: `**critical**` should render bold
- _Italic sample_ (asterisk)
- _Italic sample_ (underscore)
- ~~Strikethrough sample~~
- <u>Underline sample</u>
- Mixed sample: **bold + _italic_ + ~~strike~~ + <u>underline</u>**
- Inline code sample: `SELECT * FROM slides WHERE id = 1`

| Feature     | Source      | Expected       |
| ----------- | ----------- | -------------- |
| Bold        | **text**    | bold           |
| Italic      | _text_      | italic         |
| Strike      | ~~text~~    | strike-through |
| Underline   | <u>text</u> | underline      |
| Inline Code | `code`      | monospace      |

::: notes
Validate each inline token type on this slide.
Pay special attention to strikethrough and underline, which may vary by PPTX client.
Inline code should use a monospace face and preserve literal content.
:::

---

## Lists (Unordered, Ordered, Task)

- Dash bullet item

* Star bullet item

- Plus bullet item

1. Ordered item one
2. Ordered item two
3. Ordered item three

- [ ] Task unchecked
- [x] Task checked
- [ ] Task with **bold** and `code`

::: notes
Confirm dash, star, and plus markers are treated as list entries.
Ordered list items should remain readable and in sequence.
Task list markers should preserve the checked or unchecked indicator text.
:::

---

## Nested Lists (Permutation Coverage)

- Parent dash
  - Child dash under dash
  * Child star under dash
  - Child plus under dash
    - Grandchild dash under plus

* Parent star
  - Child dash under star
  * Child star under star
  - Child plus under star

- Parent plus
  - Child dash under plus
  * Child star under plus
  - Child plus under plus

1. Parent ordered one
   1. Child ordered one-one
   2. Child ordered one-two
   - Child unordered under ordered
2. Parent ordered two
   - Child star under ordered
   * Child plus under ordered

- Parent task wrapper
  - [ ] Nested task unchecked
  - [x] Nested task checked
  - Nested non-task sibling

1. Ordered with nested tasks
   - [ ] Ordered nested task unchecked
   - [x] Ordered nested task checked

::: notes
This slide intentionally mixes nested list marker permutations.
Use it to verify indentation handling and marker preservation at multiple nesting levels.
If nested structure appears flattened, treat that as a known renderer gap unless nesting support is added.
:::

---

## Links and Images

- Bare URL: https://ai-resources.codemag.com
- Markdown link: [AI Resources](https://ai-resources.codemag.com)
- Matching text/target link: [https://example.com](https://example.com)
- Relative image syntax: ![Dependency Diagram](images/dependency-diagram.jpg)
- Absolute image syntax: ![Sample Image](file:///C:/temp/sample.jpg)

| Feature               | Source                                     | Expected                       |
| --------------------- | ------------------------------------------ | ------------------------------ |
| Link (text != target) | [text](https://example.com)                | text: https://example.com      |
| Link (text == target) | [https://example.com](https://example.com) | https://example.com            |
| Image annotation      | ![alt](images/file.jpg)                    | annotation behavior documented |

::: notes
Links should be normalized by the parser according to configured rules.
Image syntax coverage is included to verify current behavior and guard against accidental parsing changes.
This slide does not assume inline image rendering unless the renderer implements it.
:::

---

## Blockquotes

> Single-line quote should render as emphasized text.

> Multi-line quote first line.
> Multi-line quote second line.

Normal paragraph for contrast directly below the quote.

| Feature    | Source        | Expected               |
| ---------- | ------------- | ---------------------- |
| Blockquote | > quoted text | italic/emphasized line |

::: notes
Check quote lines are visually distinct from normal paragraph text.
Verify multi-line quoted blocks preserve line boundaries and readability.
:::

---

## Code Blocks

Inline code examples:

- `print("hello")`
- `SELECT id, title FROM deck`

Fenced code block:

```python
for i in range(3):
  print(i)
```

Fenced code block with shell commands:

```bash
python .\scripts\generate_pptx.py .\slides\aiasd-311-monday.yaml .\slides\output\aiasd-311-monday-draft.pptx
```

::: notes
Inline code should use monospace formatting.
Fenced code is expected to remain as readable plain code lines unless dedicated code-block styling is added.
Verify line breaks are preserved inside fenced blocks.
:::

---

## Table Parsing and Formatting

| Feature          | Sample                      | Expected                  |
| ---------------- | --------------------------- | ------------------------- |
| Bold             | **text**                    | bold                      |
| Italic           | _text_                      | italic                    |
| Strike           | ~~text~~                    | strike                    |
| Underline        | <u>text</u>                 | underline                 |
| Link             | [text](https://example.com) | text: https://example.com |
| Inline Code      | `code`                      | monospace font            |
| Ordered List     | 1. item                     | ordered line retained     |
| Unordered List   | - item / \* item / + item   | bulleted line             |
| Task List        | - [ ] item / - [x] item     | [ ] / [x] line            |
| Blockquote       | > quote                     | italic line               |
| Fenced Code      | `python ... `               | plain code lines          |
| Image Annotation | ![alt](images/file.jpg)     | annotation behavior       |

::: notes
This table is the primary stress test for markdown parsing inside table cells.
All inline formatting tokens should render here, not as literal markdown text.
Use this slide to catch regressions where table cells bypass formatter logic.
:::
