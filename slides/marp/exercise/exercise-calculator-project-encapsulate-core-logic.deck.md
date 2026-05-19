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

## Exercise: Calculator Project - Encapsulate Core Logic

Objectives

- Separate UI concerns from computational logic
- Use AI to scaffold standalone core logic module/class
- Ensure UI communicates through a clean API
- Validate improved testability and maintainability

Activities

1. Ask AI to generate dedicated component (for example CalculatorEngine or CalculatorCore) containing:
   - Arithmetic operations
   - State management
   - Trig/percentage/memory logic where implemented

::: column

2. Review and refine API surface (naming, inputs, outputs)
3. Replace UI-embedded logic with component calls

Success Criteria

- All features route through external logic component
- UI contains only event handling/display updates
- Learner can explain modularity and reuse benefits

::: notes
Duration ~00:15

## Encapsulate Core Logic Exercise Instructions

**Prerequisites:** UI and logic currently coupled

### Objectives

- Improve architecture through separation of concerns.

### Activities

- Create clear, testable boundaries between UI and engine.

### Success Criteria

- Core logic is isolated and reusable.
  :::