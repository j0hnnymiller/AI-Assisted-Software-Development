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

## Exercise: Code Coverage

Objectives

- Set up code coverage reporting
- Interpret coverage data
- Improve coverage based on identified gaps

Activities

1. Enable Coverage Collection:
   - Prompt: "Add code coverage reporting to my test project"
   - Review dependencies added
   - Resolve NuGet/dependency issues with Copilot

2. Generate Coverage Report:
   - Run tests with coverage
   - Review percentage
   - Identify uncovered paths

::: column

3. Improve Coverage:
   - Add tests for uncovered methods
   - Re-run coverage and verify improvement
   - Discuss if 100% coverage is necessary

Success Criteria

- Coverage reporting configured successfully
- Coverage reports can be generated and interpreted
- Reasonable coverage achieved (>80% line coverage)
- Learner understands what coverage metrics mean

::: notes
Duration ~00:40

## Code Coverage Exercise Instructions

**Prerequisites:** Stable test suite

### Objectives

- Use coverage as a guide for targeted testing.

### Activities

- Treat uncovered code as investigation points, not automatic defects.

### Success Criteria

- Coverage setup works and leads to actionable improvements.
  :::