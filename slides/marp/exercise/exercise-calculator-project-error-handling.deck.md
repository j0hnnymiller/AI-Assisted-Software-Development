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

## Exercise: Calculator Project - Error Handling

Objectives

- Use AI to identify common error conditions
- Implement error messages and recovery logic
- Ensure graceful reset after errors

Activities

1. Ask AI to list calculator errors (for example divide by zero)
2. Generate error detection and display logic
3. Implement reset path after an error
4. Test error scenarios with AI-generated tests

::: column

Success Criteria

- Errors are detected and displayed correctly
- Calculator recovers cleanly
- Learner can explain error-handling flow

::: notes
Duration ~00:10

## Error Handling Exercise Instructions

**Prerequisites:** Core operations implemented

### Objectives

- Build robust error paths without breaking user flow.

### Activities

- Validate both error detection and post-error recovery.

### Success Criteria

- Error handling is visible, predictable, and recoverable.
  :::