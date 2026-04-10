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
## Exercise: Calculator Project - Sign Toggle (+/-)

Objectives

- Use AI to generate sign-toggle logic
- Understand effect on active input and stored value

Activities

1. Ask AI to generate toggle-sign function for active value
2. Integrate into input workflow
3. Test before and after digit entry

Success Criteria

- Sign toggle works for integers and decimals
- Learner can explain stored vs active value impact

::: notes
Duration ~00:08

## Sign Toggle Exercise Instructions

**Prerequisites:** Numeric input flow functioning

### Objectives

- Add predictable sign toggling.

### Activities

- Keep implementation minimal and test transitions.

### Success Criteria

- Toggle is stable across value states.
  :::