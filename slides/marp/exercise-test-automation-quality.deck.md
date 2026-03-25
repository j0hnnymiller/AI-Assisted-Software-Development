---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "test-automation-quality-exercise-20260319"
prompt: |
  create an exercise marp slide using the slides\exercise-template.pptx template for the following:

  ## Exercise: Strengthening Test Automation & Code Quality

  Duration
  20 minutes
  Objectives
  Identify gaps in test automation
  Use AI to generate missing tests
  Apply intelligent linting and quality gates
  Validate test adequacy and architectural alignment
  Activities
  Select a brownfield module or function.
  Review existing tests for:
    - Coverage gaps
    - Missing edge cases
    - Redundant or brittle tests
  Ask AI to generate missing tests.
  Run linting and architectural checks.
  Propose quality gates to enforce improvements.
  Add provenance metadata to all new artifacts.
  Success Criteria
  Coverage gaps are identified and addressed
  AI-generated tests are validated and correct
  Linting and architectural issues are resolved
  Proposed quality gates are actionable and safe
  Provenance metadata is included

  ::: notes
  Encourage participants to treat this as a real modernization task.

  The goal is not to generate as many tests as possible – it's to improve the safety, clarity, and maintainability of the testing framework in a targeted, evergreen-aligned way.
  :::
started: "2026-03-19T14:30:00Z"
ended: "2026-03-19T14:35:00Z"
task_durations:
  - task: "exercise slide creation"
    duration: "00:05:00"
total_duration: "00:05:00"
ai_log: "ai-logs/2026/03/19/test-automation-quality-exercise-20260319/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

## Exercise: Strengthening Test Automation & Code Quality

Objectives

- Identify gaps in test automation
- Use AI to generate missing tests
- Apply intelligent linting and quality gates
- Validate test adequacy and architectural alignment

Activities

1. Select a brownfield module or function
2. Review existing tests for:
   - Coverage gaps
   - Missing edge cases
   - Redundant or brittle tests

::: column

3. Ask AI to generate missing tests
4. Run linting and architectural checks
5. Propose quality gates to enforce improvements
6. Add provenance metadata to all new artifacts

Success Criteria

- Coverage gaps are identified and addressed
- AI-generated tests are validated and correct
- Linting and architectural issues are resolved
- Proposed quality gates are actionable and safe
- Provenance metadata is included

::: notes
Duration ~00:20

## Strengthening Test Automation & Code Quality Exercise Instructions

**Prerequisites:** Access to a brownfield codebase with existing tests

### Objectives

- Identify gaps in test automation
- Use AI to generate missing tests
- Apply intelligent linting and quality gates
- Validate test adequacy and architectural alignment

### Activities

1. **Select a brownfield module or function** - Choose a component with existing but incomplete test coverage.
2. **Review existing tests** - Analyze for coverage gaps, missing edge cases, and brittle or redundant tests.
3. **Ask AI to generate missing tests** - Use targeted prompts to fill identified gaps.
4. **Run linting and architectural checks** - Execute automated quality tools to identify issues.
5. **Propose quality gates** - Define enforceable quality standards for continuous improvement.
6. **Add provenance metadata** - Document all AI-assisted artifacts with proper metadata.

### Success Criteria

- Coverage gaps are identified and addressed
- AI-generated tests are validated and correct
- Linting and architectural issues are resolved
- Proposed quality gates are actionable and safe
- Provenance metadata is included

### Key Teaching Point

Encourage participants to treat this as a real modernization task.

The goal is not to generate as many tests as possible – it's to improve the safety, clarity, and maintainability of the testing framework in a targeted, evergreen-aligned way.

Focus on quality over quantity, and ensure that any proposed quality gates are achievable and won't block legitimate work.
:::
