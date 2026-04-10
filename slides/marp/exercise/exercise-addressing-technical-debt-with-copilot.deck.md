---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-technical-debt-copilot-workflows-20260322"
prompt: |
  create an exercise marp deck covering three copilot workflows for technical debt:
  prompt-first remediation, issue-driven remediation, and delegating a multi-step task.
started: "2026-03-22T12:35:12.0096510-07:00"
ended: "2026-03-22T12:38:26.6899826-07:00"
task_durations:
  - task: "template review"
    duration: "00:01:00"
  - task: "exercise slide authoring"
    duration: "00:01:30"
  - task: "provenance and catalog updates"
    duration: "00:00:44"
total_duration: "00:03:14"
ai_log: "ai-logs/2026/03/22/exercise-technical-debt-copilot-workflows-20260322/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Addressing Technical Debt with Copilot || Ask Copilot to Clean Your Room

---

<!-- Layout: Two Content -->

## Exercise: Prompt Copilot to Address Technical Debt

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

::: column

  3. Ask Copilot to propose a remediation.
  4. Review the output for correctness.

Success Criteria
  - Prompt is clear, scoped, and actionable
  - Copilot produces a safe, incremental change
  - Output aligns with architectural rules
  - Provenance metadata is included

::: notes
Duration ~00:10

Use this first exercise to make participants slow down and specify the work before they ask for code. Encourage them to choose a small but real technical debt item from their own system, because realistic context exposes whether the prompt includes enough architecture, testing, and documentation guidance to keep the change safe. During the review step, ask them to inspect whether Copilot stayed incremental, respected the stated constraints, and requested or updated tests instead of only proposing a code edit. Transition by explaining that a strong prompt is useful, but durable team workflows usually need the same clarity captured in a structured issue.
:::

---

## Exercise: Assigning an Issue to Copilot

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
     ::: column
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
Duration ~00:10

Frame this exercise as the handoff from ad hoc prompting to a repeatable engineering process. Participants should write the issue as if they were briefing a junior developer: the title should be specific, the problem statement should identify impact and risk, and the acceptance criteria should make review straightforward and testable. When they evaluate Copilot's draft, focus on whether the output follows the issue rather than whether it merely looks polished, because a clean-looking response can still drift from the requested scope. Transition by noting that once the issue is strong, teams can delegate larger units of work with more confidence, as long as they keep the plan reviewable and reversible.
:::

---

<!-- Layout: Two Content -->

## Exercise: Delegating Work to Copilot

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

::: column

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
Duration ~00:15

This final exercise is about controlled delegation, not blind trust. Ask participants to evaluate the output in layers: first the analysis, then the proposed sequence of changes, then whether the generated edits remain small enough to review and roll back safely. If Copilot skips tests, documentation, or architecture rules, treat that as a signal that the delegation prompt still needs sharper boundaries or missing context. Close by reinforcing that Copilot can accelerate larger remediation efforts, but humans remain responsible for approving the plan, spotting risk, and deciding whether the generated work is actually ready to merge.
:::
