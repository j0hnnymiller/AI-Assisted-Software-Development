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

# Leading and Trailing Separator Coverage

_Merged from: slides/marp/regression-phase12/source-b.deck.md_

::: notes
Explain that this file intentionally stresses separator normalization logic.
The leading separator after the deck heading should not create duplicate joins in merged output.
The provenance line should be stripped in Phase 1 when merged.

**Expected PPTX Rendering:**

- Layout: Title Slide (deck-level H1, not first in manifest)
- Title Placeholder: "Leading and Trailing Separator Coverage"
- Subtitle Placeholder: (empty)
- Notes: This notes block content
- Phase 1 Behavior: H1 and provenance line stripped during merge
- Separator Handling: Leading separator after H1 normalized (not doubled)
  :::

---

## Starts After Leading Separator

This deck intentionally starts content after a leading separator.
Phase 1 should normalize file joins to avoid doubled separators.

::: notes
Verify merged markdown has exactly one separator boundary before this slide block.
Confirm no extra blank slide appears at the file boundary.
Use this as the reference for leading separator normalization.

**Expected PPTX Rendering:**

- Layout: Title and Content
- Title Placeholder: "Starts After Leading Separator"
- Content Placeholder: Body paragraph text (2 lines)
- Notes: This notes block content
- Phase 1 Behavior: Leading --- after H1 stripped, single separator boundary maintained
  :::

---

## Ends With Trailing Separator Candidate

This deck intentionally ends with a bare separator so validation can flag it.
Phase 1 should strip one trailing separator during merge.

::: notes
This slide is paired with an intentional trailing --- at end of file.
Phase 0 should warn about trailing separator and Phase 1 should strip one trailing boundary.
Confirm merged output does not end with duplicate separators from this source file.

**Expected PPTX Rendering:**

- Layout: Title and Content
- Title Placeholder: "Ends With Trailing Separator Candidate"
- Content Placeholder: Body paragraph text (2 lines)
- Notes: This notes block content
- Phase 0 Behavior: Validation warning about trailing --- in source file
- Phase 1 Behavior: Trailing --- stripped, no duplicate separator at end of merged deck
  :::

---
