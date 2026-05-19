---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "phase12-bold-regression-deck-20260409"
prompt: |
  create a dedicated regression deck for markdown bold rendering in pptx titles,
  subtitles, and content placeholders.
started: "2026-04-09T00:00:00Z"
ended: "2026-04-09T00:00:00Z"
task_durations:
  - task: "bold regression deck authoring"
    duration: "00:00:00"
total_duration: "00:00:00"
ai_log: "ai-logs/2026/04/09/phase12-bold-regression-deck-20260409/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# **Bold Regression Coverage** || **Subtitle Placeholder Bold Coverage**

::: notes
This H1-only slide is the dedicated centered-two-titles bold regression case.
Confirm that both the title and subtitle placeholders render without literal asterisks and preserve bold formatting.

**Expected PPTX Rendering:**

- Layout: Centered Two Titles
- Title Placeholder: "Bold Regression Coverage" rendered in bold
- Subtitle Placeholder: "Subtitle Placeholder Bold Coverage" rendered in bold
- Content Placeholder: (empty)
:::

---

<!-- layout: Title Slide -->

## **Dedicated Bold Title Slide**

This subtitle placeholder contains **bold subtitle text** for regression coverage.

::: notes
This slide isolates explicit Title Slide layout behavior for markdown bold rendering.
Confirm the title placeholder is bold and that only the marked subtitle fragment is bold in the subtitle placeholder.

**Expected PPTX Rendering:**

- Layout: Title Slide
- Title Placeholder: "Dedicated Bold Title Slide" rendered in bold
- Subtitle Placeholder: sentence with only "bold subtitle text" rendered in bold
- Content Placeholder: (empty)
:::

---

## **Dedicated Bold Placeholder Slide**

This placeholder contains **bold placeholder text** in the body paragraph.

- This bullet includes **bold bullet text** for placeholder coverage

::: notes
This slide isolates markdown bold rendering inside a normal content placeholder.
Confirm the title placeholder is bold, the body paragraph preserves inline bold, and the bullet preserves inline bold.

**Expected PPTX Rendering:**

- Layout: Title and Content
- Title Placeholder: "Dedicated Bold Placeholder Slide" rendered in bold
- Content Placeholder: body paragraph with only "bold placeholder text" in bold
- Bullet Placeholder Text: bullet with only "bold bullet text" in bold
:::
