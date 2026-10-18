---
name: technical-debt-remediation
description: "Plan and implement a bounded technical-debt fix using repository evidence, approval, focused tests, and documentation. Use when a debt item or risky maintenance issue needs incremental remediation rather than analysis alone."
argument-hint: "[issue, module, or debt description]"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  Continue broader config review.
  Approved skill changes: all of them.
started: "2026-10-17T20:39:34.0421109-07:00"
ended: "2026-10-17T20:45:14.3269450-07:00"
task_durations:
  - task: "Skill authoring and integration"
    duration: "00:05:40"
total_duration: "00:05:40"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "AIASD/AI-Assisted-Software-Development-Course/.github/skills/technical-debt-remediation/SKILL.md"
---

# Technical Debt Remediation

Use for a bounded maintenance fix when the user wants implementation, not only a debt assessment. For analysis-only requests, use [Refactoring Opportunities Analysis](../refactor-analysis/SKILL.md).

## Procedure

1. Identify the debt item, affected component, user or operational impact, requested scope, and non-goals. Ask for missing evidence instead of guessing.
2. Inspect the relevant code, tests, architecture guidance, repository instructions, and documentation. Separate verified facts, assumptions, risks, and decisions still needed.
3. Propose an incremental plan with expected behavior, acceptance criteria, focused tests, and documentation changes. Wait for user approval before editing.
4. Implement only the approved scope. Preserve unrelated changes and follow local conventions.
5. Add or update focused tests and directly related documentation. Do not widen the work into general cleanup or redesign.
6. Run the narrowest relevant checks, review the diff, and compare the result with every acceptance criterion. Repair in-scope failures and rerun the relevant checks.
7. Summarize changed files, verification results, remaining risks, and follow-up debt.

## Boundaries

- Do not commit, push, create or assign issues, or merge without explicit authorization.
- Do not treat this Skill as permission to access external systems or execute a cloud-agent workflow.
- Escalate when safe incremental remediation depends on a product, architecture, or compatibility decision.
