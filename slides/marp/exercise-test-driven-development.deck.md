---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "lab3-test-driven-development-exercise-20260317"
prompt: |
  create an exercise slide, using the #file:exercise-template.md, for Lab 3: Test-Driven Development (TDD) with Copilot.
started: "2026-03-17T03:21:00Z"
ended: "2026-03-17T03:25:00Z"
task_durations:
  - task: "template mapping"
    duration: "00:01:00"
  - task: "exercise authoring"
    duration: "00:03:00"
total_duration: "00:04:00"
ai_log: "ai-logs/2026/03/17/lab3-test-driven-development-exercise-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Exercise: Test-Driven Development with Copilot || Exercise: Write the Test First. Trust the Process.

## Exercise: Lab 3 - Test-Driven Development (TDD) with Copilot

Objectives

- Practice TDD workflow with AI assistance
- Write failing tests before implementation
- Use tests to drive design decisions
- Understand red-green-refactor cycle

Activities

1. Define New Feature:

- Choose a feature (for example, memory operations for calculator)
- Store current result (ANS/answer functionality)
- Recall previous result
- Handle "ANS + 5" style operations

2. Write Failing Tests First:

- Prompt: "Using TDD, create tests for a memory/answer feature in the calculator. DO NOT implement the feature yet."
- Review generated tests
- Verify tests reference methods that do not exist yet

3. Run Tests (Expect Failures):

- Execute test suite
- Observe compilation errors or test failures
- Document what is missing

4. Implement Feature to Pass Tests:

- Prompt: "Implement the memory/answer feature to make the tests pass"
- Review generated implementation
- Run tests again
- Verify all tests now pass

5. Refactor:

- With tests passing, ask for improvements
- Prompt: "Refactor the answer implementation for better readability"
- Verify tests still pass after refactoring

Success Criteria

- Tests written before implementation
- Initial test run shows failures (red phase)
- Implementation makes all tests pass (green phase)
- Code refactored while maintaining passing tests
- Understanding of TDD benefits and workflow

::: notes
Duration ~00:60

## Lab 3 - Test-Driven Development (TDD) with Copilot Exercise Instructions

**Prerequisites:** Understanding of TDD principles

### Objectives

- Practice TDD workflow with AI assistance
- Write failing tests before implementation
- Use tests to drive design decisions
- Understand red-green-refactor cycle

### Activities

1. Select a small feature and define expected behavior.
2. Ask Copilot for tests only, and confirm the implementation is still missing.
3. Run tests and capture failures to validate the red phase.
4. Implement the minimum code required to satisfy tests.
5. Refactor for readability and maintainability while keeping tests green.

### Success Criteria

- Tests are authored before implementation code.
- The first execution clearly fails (red).
- Feature implementation makes tests pass (green).
- Refactoring preserves passing tests.
- Participants can explain the value of TDD in AI-assisted development.

### TDD Cycle

1. **Red:** Write a failing test.
2. **Green:** Write minimal code to make it pass.
3. **Refactor:** Improve code while keeping tests green.
   :::
