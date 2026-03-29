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
---

# Table Mermaid and Background Branches

::: notes
Introduce this deck as the content-feature branch coverage set.
Explain that table, mermaid, background images, and legacy inline image markers are all represented.
Mention that expected warnings are acceptable for unavailable Mermaid tooling.

**Expected PPTX Rendering:**

- Layout: Title Slide (deck-level H1, not first in manifest)
- Title Placeholder: "Table Mermaid and Background Branches"
- Subtitle Placeholder: (empty)
- Notes: This notes block content
- Phase 1 Behavior: H1 stripped during merge
  :::

---

## Background Image Title Only

![bg fit](images/cqrs-command-query-flow.jpg)

::: notes
This slide should route to title-only output with a resolved background image path.
Verify background image placement and ensure no placeholder body text appears.
If the image is missing, record warning output and fix path references.

**Expected PPTX Rendering:**

- Layout: Title Only (H2 + background image only, no body text)
- Title Placeholder: "Background Image Title Only"
- Content Placeholder: (empty - background image slide)
- Background: Image from marp/images/cqrs-command-query-flow.jpg
- Notes: This notes block content
- Image Handling: ![bg fit] syntax triggers background placement
  :::

---

## Markdown Table Branch

| Branch       | Trigger               | Expected          |
| ------------ | --------------------- | ----------------- |
| Table parser | markdown table syntax | table slide path  |
| Note merge   | ::: notes block       | notes plus source |

::: notes
This table should route through the table-specific slide creation path.
The speaker notes should be combined with source metadata in PPTX.

**Expected PPTX Rendering:**

- Layout: Title and Content (table routing)
- Title Placeholder: "Markdown Table Branch"
- Content Placeholder: PowerPoint table (3 columns × 3 rows including header)
- Table Content: Headers "Branch", "Trigger", "Expected" + 2 data rows
- Notes: This notes block content + source file reference
- Table Handling: Markdown table converted to native PPTX table object
  :::

---

## Mermaid Rendering Branch

```mermaid
flowchart LR
  A[Source Deck] --> B[Phase 1 Merge]
  B --> C[Phase 2 PPTX]
```

If Mermaid CLI exists, this should render an image.
If Mermaid CLI is unavailable, the script should print a warning and keep text content.

::: notes
This slide exercises Mermaid extraction and optional rendering behavior.
When Mermaid CLI is present, verify PNG insertion as inline image content.
When absent, verify warning output and retained markdown text path.

**Expected PPTX Rendering (Mermaid CLI Available):**

- Layout: Title and Content
- Title Placeholder: "Mermaid Rendering Branch"
- Content Placeholder: Rendered PNG image from Mermaid diagram + body text
- Image: Flowchart with 3 nodes and 2 arrows
- Notes: This notes block content

**Expected PPTX Rendering (Mermaid CLI Unavailable):**

- Layout: Title and Content
- Title Placeholder: "Mermaid Rendering Branch"
- Content Placeholder: Code block text + body text (diagram not rendered)
- Warning Expected: Mermaid CLI unavailable message
- Notes: This notes block content
  :::

---

## Legacy Inline Image Marker

!Slide 1 image: images/feature-flag-retirement.jpg

Legacy marker parsing should collect this image as inline content.

::: notes
This slide uses the legacy image marker format to test backward-compatible parsing.
Confirm add_inline_images receives the resolved path and image placement succeeds.
If image lookup fails, capture warning output for path diagnostics.

**Expected PPTX Rendering:**

- Layout: Title and Content
- Title Placeholder: "Legacy Inline Image Marker"
- Content Placeholder: Inline image (if found) + body paragraph text
- Image: From marp/images/feature-flag-retirement.jpg
- Notes: This notes block content
- Image Handling: "!Slide N image:" legacy syntax parsed and inserted
  :::

---

## Heading Only Title Only Branch

::: notes
This heading-only slide verifies the title-only branch for H2 with no body content.
Confirm the output uses title-only layout behavior and no content frame text.
Use this to validate the V5 check in the merge prompt verification list.

**Expected PPTX Rendering:**

- Layout: Title Only (H2 with no body content triggers this layout)
- Title Placeholder: "Heading Only Title Only Branch"
- Content Placeholder: (empty - no body content)
- Notes: This notes block content
- Routing: Heading-only detection uses LAYOUT_TITLE_ONLY index
- Validation: Agent verification check V5 target
  :::
