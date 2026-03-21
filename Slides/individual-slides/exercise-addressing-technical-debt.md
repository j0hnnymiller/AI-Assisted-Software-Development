---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-addressing-technical-debt-20260320"
prompt: |
  create an exercise marp slide using the Slides\individual-slides\exercise-template.pptx template for the following:


  # **Exercise: Prompt Copilot to Address Technical Debt**

  ### Duration

  10 minutes

  ### Objectives

  - Practice writing high-signal prompts
  - Apply architectural constraints
  - Produce safe, incremental remediation requests

  ### Activities

  1. Select a small piece of technical debt.
  2. Write a prompt that includes:
     - Description of the debt
     - Constraints and rules
     - Expected behavior
     - Required tests and documentation
  3. Ask Copilot to propose a remediation.
  4. Review the output for correctness.

  ### Success Criteria

  - Prompt is clear, scoped, and actionable
  - Copilot produces a safe, incremental change
  - Output aligns with architectural rules
  - Provenance metadata is included

  ::: notes
  Encourage participants to choose a real example from their brownfield system. The goal is clarity and safety, not complexity.
  :::

  ---

  # **Exercise: Assigning an Issue to Copilot**

  ### Duration

  10 minutes

  ### Objectives

  - Convert technical debt into a structured issue
  - Provide Copilot with actionable context
  - Practice writing acceptance criteria

  ### Activities

  1. Select a technical debt item.
  2. Create a GitHub-style issue with:
     - Title
     - Description
     - Impact and risk
     - Acceptance criteria
     - Provenance metadata
  3. Assign the issue to Copilot.
  4. Review Copilot's proposed remediation.

  ### Success Criteria

  - Issue is clear and well-structured
  - Acceptance criteria are testable
  - Copilot produces a relevant draft
  - Provenance metadata is present

  ::: notes
  This exercise reinforces the workflow of treating Copilot as a junior developer who receives tasks and produces drafts.
  :::

  ---

  # **Exercise: Delegating Work to Copilot**

  ### Duration

  15 minutes

  ### Objectives

  - Practice delegating multi-step tasks
  - Ensure Copilot follows architectural rules
  - Validate AI-generated remediation plans

  ### Activities

  1. Select a multi-step technical debt item.
  2. Ask Copilot to:
     - Analyze the problem
     - Propose a remediation plan
     - Generate code changes
     - Update tests
     - Update documentation
  3. Review Copilot's output.
  4. Identify missing context or risks.

  ### Success Criteria

  - Delegation prompt is complete and structured
  - Copilot produces a multi-step plan
  - Output is safe, incremental, and reversible
  - Human review identifies any gaps

  ::: notes
  This exercise builds confidence in delegating larger tasks while maintaining safety and architectural alignment. Emphasize that humans remain the final reviewers.
  :::
started: "2026-03-20T17:18:30.8705200-07:00"
ended: "2026-03-20T17:24:30.8705200-07:00"
task_durations:
  - task: "template mapping"
    duration: "00:02:00"
  - task: "exercise authoring"
    duration: "00:03:00"
  - task: "provenance and catalog updates"
    duration: "00:01:00"
total_duration: "00:06:00"
ai_log: "ai-logs/2026/03/20/exercise-addressing-technical-debt-20260320/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

## Exercise: Prompt Copilot to Address Technical Debt

Duration: 10 minutes

Objectives

- Practice writing high-signal prompts
- Apply architectural constraints
- Produce safe, incremental remediation requests

Activities

1. Select a small piece of technical debt.
2. Write a prompt that includes:
   - Description of the debt
   - Constraints and rules
   - Expected behavior
   - Required tests and documentation
3. Ask Copilot to propose a remediation.
4. Review the output for correctness.

Success Criteria

- Prompt is clear, scoped, and actionable
- Copilot produces a safe, incremental change
- Output aligns with architectural rules
- Provenance metadata is included

::: notes

## Prompt Copilot to Address Technical Debt Exercise Instructions

**Duration:** 10 minutes
**Prerequisites:** Access to a real or representative brownfield codebase with at least one small, well-understood debt item

Use this exercise to teach precision, not volume. Ask participants to choose one narrow debt item such as a brittle conditional, duplicated validation logic, or missing test coverage, then force the prompt to be explicit about constraints, expected behavior, and required non-code updates. Remind them that a strong remediation prompt should limit blast radius and make review easier by asking for incremental, reversible changes. Close by asking what context was still missing from the prompt and how that gap could have changed Copilot's output.
:::

---

## Exercise: Assigning an Issue to Copilot

Duration: 10 minutes

Objectives

- Convert technical debt into a structured issue
- Provide Copilot with actionable context
- Practice writing acceptance criteria

Activities

1. Select a technical debt item.
2. Create a GitHub-style issue with:
   - Title
   - Description
   - Impact and risk
   - Acceptance criteria
   - Provenance metadata
3. Assign the issue to Copilot.
4. Review Copilot's proposed remediation.

Success Criteria

- Issue is clear and well-structured
- Acceptance criteria are testable
- Copilot produces a relevant draft
- Provenance metadata is present

::: notes

## Assigning an Issue to Copilot Exercise Instructions

**Duration:** 10 minutes
**Prerequisites:** Familiarity with GitHub issues or an equivalent work-item format

Frame this exercise as a handoff discipline exercise: the issue should be detailed enough that a junior developer or agent can start safely without guesswork. Encourage participants to write acceptance criteria that can be verified in code review or by running tests, rather than vague goals like "clean this up." Highlight that impact, risk, and provenance metadata are part of the issue quality bar because they help reviewers understand why the debt matters and what must be traceable. Transition by comparing the resulting issue with the earlier prompt and asking which format gave Copilot stronger execution context.
:::

---

## Exercise: Delegating Work to Copilot

Duration: 15 minutes

Objectives

- Practice delegating multi-step tasks
- Ensure Copilot follows architectural rules
- Validate AI-generated remediation plans

Activities

1. Select a multi-step technical debt item.
2. Ask Copilot to:
   - Analyze the problem
   - Propose a remediation plan
   - Generate code changes
   - Update tests
   - Update documentation
3. Review Copilot's output.
4. Identify missing context or risks.

Success Criteria

- Delegation prompt is complete and structured
- Copilot produces a multi-step plan
- Output is safe, incremental, and reversible
- Human review identifies any gaps

::: notes

## Delegating Work to Copilot Exercise Instructions

**Duration:** 15 minutes
**Prerequisites:** A technical debt item large enough to require sequencing across code, tests, and documentation

This exercise is about orchestration and review discipline. Encourage participants to pick something with multiple steps, then ask Copilot for analysis, a plan, and implementation support in a way that still preserves human checkpoints before merging. Stress that the best answer is not the most ambitious one; it is the one that breaks the work into safe stages, respects architecture boundaries, and makes rollback straightforward. End by asking the group to identify where human review added value, especially around hidden dependencies, missing tests, or documentation obligations.
:::
