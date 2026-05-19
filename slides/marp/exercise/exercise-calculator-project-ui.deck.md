---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "calculator-project-exercise-deck-20260317"
prompt: |
  create an exercise slide deck, using the #file:exercise-template.md, for the provided calculator project exercise content.
started: "2026-03-17T03:28:00Z"
ended: "2026-03-17T03:36:00Z"
task_durations:
  - task: "content normalization"
    duration: "00:03:00"
  - task: "deck authoring"
    duration: "00:05:00"
total_duration: "00:08:00"
ai_log: "ai-logs/2026/03/17/calculator-project-exercise-deck-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
<!-- layout: Two Content -->

## Exercise: Calculator Project - UI

Objectives

- Use AI to scaffold UI event handlers
- Connect UI controls to logic functions
- Validate end-to-end workflow

Activities

1. Ask AI to generate event-binding code for numeric/operator controls
2. Integrate logic functions from prior exercises
3. Test full workflow:
   - Enter decimal
   - Toggle sign
   - Apply percentage
   - Store result in memory

::: column

Success Criteria

- UI triggers all calculator functions correctly
- End-to-end workflow completes without errors
- Learner can explain UI-to-logic mapping

::: notes
Duration ~00:15

## UI Exercise Instructions

**Prerequisites:** Core logic stable and testable

### Objectives

- Wire UI interactions cleanly to existing logic.

### Activities

- Prioritize event mapping clarity over visual polish.

### Success Criteria

- Workflow passes from input to output with no breaks.
  :::