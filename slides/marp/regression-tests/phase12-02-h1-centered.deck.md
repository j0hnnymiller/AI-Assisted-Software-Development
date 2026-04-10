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

# **Architecture Truth** || **But Make It Memorable**

_Merged from: slides/marp/regression-phase12/source-a.deck.md_

::: notes
This slide should trigger the centered two titles branch because it is H1-only with matter-of-fact and witty parts.
Confirm the title and subtitle placeholders are both populated in the generated PPTX.
Point out that the provenance line exists to test Phase 1 stripping behavior.

**Expected PPTX Rendering:**

- Layout: Centered Two Titles
- Title Placeholder: "Architecture Truth" rendered in bold
- Subtitle Placeholder: "But Make It Memorable" rendered in bold
- Content Placeholder: (empty - H1-only slide)
- Notes: This notes block content
- Phase 1 Behavior: H1 and provenance line stripped during merge
- Split Logic: Text before "||" → title, text after "||" → subtitle
  :::

---

# Plain Divider Title

::: notes
This H1-only slide should route to the centered title branch after the first deck-level H1 has been seen.
Validate that no body placeholder text appears and only the centered title is used.
Move to the next content slide to verify normal flow resumes.

**Expected PPTX Rendering:**

- Layout: Centered Title
- Title Placeholder: "Plain Divider Title"
- Subtitle Placeholder: (empty)
- Content Placeholder: (empty - H1-only slide)
- Notes: This notes block content
- Phase 1 Behavior: H1 stripped during merge (not first deck H1)
- Routing: No "||" delimiter, so single centered title layout
  :::

---

## Content After H1 Dividers

This slide confirms normal title and content flow after H1-only blocks with **bold placeholder text** preserved.

- Placeholder bullet with **bold emphasis** later in the line

::: notes
This deck intentionally begins with H1-only slides.
After the first deck-level H1 in the manifest, these should route to centered title layouts.
The provenance line after the first H1 is included to exercise merge stripping behavior.

**Expected PPTX Rendering:**

- Layout: Title and Content
- Title Placeholder: "Content After H1 Dividers"
- Content Placeholder: Body paragraph text with inline bold + bullet text with inline bold
- Notes: This notes block content
- Behavior: Normal H2 + body routing after H1-only dividers
  :::
