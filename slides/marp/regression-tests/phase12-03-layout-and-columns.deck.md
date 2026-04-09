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

# Layout and Column Branches

::: notes
Introduce this deck as the explicit layout-routing test set.
Call out that both successful and failing layout-name scenarios are included.
Explain that each slide is crafted to force a unique branch in the PPTX generator.

**Expected PPTX Rendering:**

- Layout: Title Slide (deck-level H1, not first in manifest)
- Title Placeholder: "Layout and Column Branches"
- Subtitle Placeholder: (empty)
- Notes: This notes block content
- Phase 1 Behavior: H1 stripped during merge
  :::

---

<!-- layout: Title Slide -->

## Explicit Title Slide Layout

This content validates named layout resolution for a known layout.

::: notes
This slide should use add_named_layout_slide with a valid layout name.
Verify that the requested layout is honored without fallback warnings.
Confirm body placement in the expected placeholder.

**Expected PPTX Rendering:**

- Layout: Title Slide (explicit via comment directive)
- Title Placeholder: "Explicit Title Slide Layout"
- Subtitle Placeholder: "This content validates named layout resolution for a known layout."
- Content Placeholder: (empty - title slide layout has no body frame)
- Notes: This notes block content
- Routing: Explicit layout comment takes precedence
  :::

---

<!-- layout: Two Content -->

## Explicit Two Content Layout

### Left Column

- left one
- left two

### Right Column

- right one
- right two

::: notes
This slide exercises explicit Two Content layout with heading-based left/right extraction.
Confirm both columns are populated and title remains in the title placeholder.
Use this as a baseline before testing separator-driven two-column behavior.

**Expected PPTX Rendering:**

- Layout: Two Content (explicit via comment directive)
- Title Placeholder: "Explicit Two Content Layout"
- Left Column Placeholder: "Left Column" heading + 2 bullets ("left one", "left two")
- Right Column Placeholder: "Right Column" heading + 2 bullets ("right one", "right two")
- Notes: This notes block content
- Splitting: H3 headings mark column boundaries
  :::

---

## Separator Based Two Content

Left side keeps these bullets.

- alpha
- beta

::: column

Right side keeps these bullets.

- gamma
- delta

::: notes
This slide exercises automatic two-column detection based on ::: column separator.
Verify split_two_column_body handles separator content without explicit layout directives.
Check that both columns appear and ordering is preserved.

**Expected PPTX Rendering:**

- Layout: Two Content (auto-detected via ::: column separator)
- Title Placeholder: "Separator Based Two Content"
- Left Column Placeholder: "Left side keeps these bullets." + 2 bullets ("alpha", "beta")
- Right Column Placeholder: "Right side keeps these bullets." + 2 bullets ("gamma", "delta")
- Notes: This notes block content
- Splitting: ::: column marker splits content into left/right
  :::

---

## Exercise: Objectives and Activities Auto Split

Objectives:

- Identify the logic
- Verify the split

Activities:

- Run the merge prompt
- Inspect generated output

::: notes
This exercise-titled slide should trigger the Objectives and Activities fallback split logic.
Verify left column starts at Objectives and right column starts at Activities.
Confirm this works even without ::: column.

**Expected PPTX Rendering:**

- Layout: Two Content (auto-detected via "Exercise:" title + "Objectives:" and "Activities:" keywords)
- Title Placeholder: "Exercise: Objectives and Activities Auto Split"
- Left Column Placeholder: "Objectives:" + 2 bullets ("Identify the logic", "Verify the split")
- Right Column Placeholder: "Activities:" + 2 bullets ("Run the merge prompt", "Inspect generated output")
- Notes: This notes block content
- Splitting: Objectives/Activities keyword detection without ::: column
  :::

---

<!-- layout: Definitely Not A Real Layout -->

## Unknown Layout Fallback

The script should warn about the layout name and fall back to standard branch logic.

::: notes
This slide intentionally requests a non-existent layout to trigger warning and fallback.
Confirm a warning is printed and the slide is still generated through normal routing.
Capture this warning as expected behavior in test notes.

**Expected PPTX Rendering:**

- Layout: Title and Content (fallback after unknown layout warning)
- Title Placeholder: "Unknown Layout Fallback"
- Content Placeholder: Body paragraph text
- Notes: This notes block content
- Warning Expected: "layout 'Definitely Not A Real Layout' not found in template"
- Behavior: Generator prints warning, falls back to standard title+content
  :::

---

<!-- _class: hide -->

## Hidden Slide Branch

This slide verifies that Phase 2 marks hide-class slides as hidden in the generated PPTX.

::: notes
This slide is the regression sentinel for hidden-slide behavior.
Keep it in the deck to ensure Phase 2 still honors the hide class marker.

**Expected PPTX Rendering:**

- Layout: Title and Content
- Title Placeholder: "Hidden Slide Branch"
- Content Placeholder: Body paragraph text
- Hidden: true (slide XML attribute show="0")
- Notes: This notes block content
  :::
