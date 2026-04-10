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

## Exercise: Calculator Project - Testing

Objectives

- Generate unit tests with AI assistance
- Identify quality issues in generated tests
- Understand why generated tests require review

Activities

1. Generate Initial Tests:
   - Prompt: "Create unit tests for the calculator operations"
   - Review generated test structure
   - Verify tests call calculator code

2. Fix Test Issues:
   - If tests are trivial (for example 1 + 1 only), identify issue
   - Prompt: "Update tests to call Calculator class methods"
   - Verify improved test quality

::: column

3. Run Tests:
   - Execute test suite
   - Review output
   - Debug failing tests with Copilot

4. Add Edge Cases:
   - Prompt: "Add tests for edge cases like division by zero"
   - Verify exception handling tests

Success Criteria

- Minimum 8 test cases
- Tests call actual calculator methods
- Edge cases and error conditions included
- All tests pass

::: notes
Duration ~01:00

## Testing Exercise Instructions

**Prerequisites:** Calculator logic implemented

### Objectives

- Improve test quality, not just test count.

### Activities

- Review generated tests critically before accepting.

### Success Criteria

- Test suite is meaningful, comprehensive, and green.
  :::