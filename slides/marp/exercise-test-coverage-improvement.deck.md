---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "lab2-test-coverage-improvement-exercise-20260317"
prompt: |
  create an exercise slide, using the #file:exercise-template.md, for Lab 2: Test Coverage Improvement.
started: "2026-03-17T03:19:00Z"
ended: "2026-03-17T03:23:00Z"
task_durations:
  - task: "template alignment"
    duration: "00:01:00"
  - task: "exercise authoring"
    duration: "00:03:00"
total_duration: "00:04:00"
ai_log: "ai-logs/2026/03/17/lab2-test-coverage-improvement-exercise-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

## Exercise: Test Coverage Improvement

Objectives

- Analyze code coverage reports
- Use Copilot to intelligently add tests
- Achieve target coverage percentage
- Balance quantity vs. quality of tests

Activities

1. Review Current Coverage:

- Run tests with coverage reporting
- Identify uncovered code paths
- Analyze coverage percentage by file/class

2. Targeted Test Generation:

- Prompt: "Add tests to increase code coverage to [X]%"
- Observe how Copilot identifies gaps
- Review generated tests for quality

3. Strategic Coverage Improvement:

- Prompt: "Add tests for edge cases in division operation"
- Prompt: "Add tests for corner cases like divide by zero"
- Prompt: "Add integration tests for evaluate arithmetic method"

4. Verify Test Quality:

- Confirm tests call real implementation code
- Confirm tests verify expected behavior, not just execution
- Confirm edge cases are properly handled

5. Re-run Coverage:

- Execute test suite with coverage
- Compare before/after percentages
- Identify remaining gaps

Success Criteria

- Code coverage increased by at least 20 percentage points
- All new tests are meaningful and test actual implementation
- Tests include edge cases and error conditions
- Coverage report shows improved metrics
- Understanding of test quality vs. quantity trade-offs

::: notes
Duration ~00:45

## Test Coverage Improvement Exercise Instructions

**Prerequisites:** Lab 1 completed, existing test suite

### Objectives

- Analyze code coverage reports
- Use Copilot to intelligently add tests
- Achieve target coverage percentage
- Balance quantity vs. quality of tests

### Activities

1. Review current coverage metrics and identify weak areas by file/class.
2. Use Copilot prompts to generate targeted tests for uncovered code paths.
3. Improve strategically with edge-case and integration-focused prompts.
4. Validate test quality to ensure behavior is truly verified.
5. Re-run coverage and compare before/after outcomes.

### Success Criteria

- Coverage increases by at least 20 percentage points.
- New tests are meaningful and exercise actual implementation logic.
- Edge cases and error conditions are covered.
- Coverage reporting clearly shows improvement.
- Participants can explain quality vs. quantity trade-offs.

### Key Learning Point

As discovered in the session, asking Copilot to "increase coverage to 50%" can work because it can intelligently identify which code paths need testing. This can be more efficient than manually finding every gap, but quality checks are still required.
:::
