---
name: technical-debt-remediation
description: "Use when analyzing, planning, or implementing a bounded technical-debt fix. Ground the work in repository evidence, propose an incremental plan, wait for approval, then verify code, tests, and documentation changes."
argument-hint: "[issue, module, or debt description]"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "apply-agent-skills-agent-host-course-migration-20260927"
prompt: |
  For F-001, F-002 - make the recommended changes, but drop any reference to a prompt file. Since promptfiles are deprecated, there is no need to teach them in the course.

  For F-003 - implement the changes proposed in this chat.

  F-004, F-005 - Convert these into skills
started: "2026-09-27T11:22:59-07:00"
ended: "2026-09-27T11:42:07-07:00"
task_durations:
  - task: "technical debt Skill authoring"
    duration: "00:19:08"
total_duration: "00:19:08"
ai_log: "ai-logs/2026/09/27/apply-agent-skills-agent-host-course-migration-20260927/conversation.md"
source: "johnmillerATcodemag-com"
---

# Technical Debt Remediation

Use this procedure in an Agent Host workspace session. Keep GitHub issue assignment or cloud-agent execution separate unless the user explicitly selects that workflow.

## Procedure

1. Identify the debt item, affected component, user/operational impact, and requested scope. Ask for missing evidence rather than guessing.
2. Inspect relevant source, tests, architecture guidance, repository instructions, and documentation. State verified facts, assumptions, risks, and non-goals.
3. Propose a minimal, incremental plan with expected behavior, acceptance criteria, tests, and documentation updates. Wait for approval before changing files.
4. Implement only the approved scope. Preserve existing user changes and follow local conventions.
5. Update or add focused tests and relevant documentation. Do not claim checks passed unless they were executed.
6. Run the focused checks, review the diff, and compare results against each acceptance criterion. Repair in-scope failures and rerun the relevant checks.
7. Summarize changed files, verification results, remaining risks, and any follow-up debt.

## Boundaries

- Do not expand the task into a broad cleanup or redesign.
- Do not commit, push, assign issues, or merge without explicit authorization.
- Do not treat a Skill instruction as a permission or security control.
- Escalate when safe incremental remediation requires product or architecture decisions.
