---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-28"
operator: "johnmillerATcodemag-com"
chat_id: "phase12-regression-decks-20260328"
prompt: |
  compare generate_pptx.py to regression manifest and create new regression decks/manifests that exercise phase 1 and phase 2 logic.
started: "2026-03-28T00:00:00Z"
ended: "2026-03-28T00:20:00Z"
task_durations:
  - task: "coverage analysis and deck authoring"
    duration: "00:20:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2026/03/28/phase12-regression-decks-20260328/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
title: Phase 1 and Phase 2 Regression Harness
subtitle: Merge and PPTX branch coverage
---

# Phase 1 and Phase 2 Regression Harness

::: notes
Open the regression suite and explain that this deck is intentionally synthetic.
Mention that the first H1 in the first deck should remain a title-only slide in PPTX.
Transition to the next slide where link and separator handling are tested.

**Expected PPTX Rendering:**

- Layout: Title Slide
- Title Placeholder: "Phase 1 and Phase 2 Regression Harness"
- Subtitle Placeholder: (empty - no subtitle in this slide)
- Notes: This notes block content
- Behavior: First H1 in first deck becomes title slide, not stripped
  :::

---

## Link and Image Rewrite Coverage

- Matching link text and target: [https://example.com](https://example.com)
- Different link text and target: [Docs](https://example.com/docs)
- Local image reference for merge rewrite: ![Safety Workflow](images/aiasd-safety-workflow.jpg)

```yaml
meta:
  keep_this_separator_like_text: "---"
  still_inside_code_fence: true
```

::: notes
This slide verifies markdown link processing and image path handling.
The YAML code fence includes a literal --- line that must not be treated as a slide separator.
The merged markdown should keep that line verbatim.

**Expected PPTX Rendering:**

- Layout: Title and Content
- Title Placeholder: "Link and Image Rewrite Coverage"
- Content Placeholder: Bulleted list (3 bullets) + code block content (monospace)
- Image Handling: 
  - Phase 1: Image path rewritten to marp/images/ in merged deck
  - Phase 2: Image markdown extracted and removed from bullet text
  - Phase 2: Image rendered as picture shape in slide (not as markdown text)
  - Bullet text preserved: "Local image reference for merge rewrite:" (without markdown)
- Code Block Rendering:
  - Fence markers (```) not rendered (invisible in output)
  - Language identifier (yaml) not rendered
  - Code block content rendered in monospace font
  - Literal "---" inside code block preserved, not treated as separator
- Notes: This notes block content
  :::
