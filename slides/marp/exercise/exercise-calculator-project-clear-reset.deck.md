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

## Exercise: Calculator Project - Clear / Reset

Objectives

- Use AI to scaffold state-management logic
- Implement CE (clear entry) and C (clear all) behaviors
- Understand UI state transitions

Activities

1. Ask AI to outline the difference between CE and C
2. Generate code for clearing current input vs full state
3. Integrate logic into calculator state object
4. Test transitions with sample input sequences

::: column

Success Criteria

- CE clears only the active entry
- C resets the entire calculator state

::: notes
Duration ~00:15

## Clear / Reset Exercise Instructions

**Prerequisites:** Basic calculator state model

### Objectives

- Separate entry-level clear from full reset behavior.
- Verify expected transitions from each action.

### Activities

- Use focused prompts and test state transitions quickly.

### Success Criteria

- CE and C behaviors are consistent and explainable.
  :::