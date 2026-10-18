---
name: implement-vertical-slice
description: "Implement one bounded vertical slice from an approved specification or plan. Use when a slice has defined acceptance criteria and needs repository-grounded implementation, focused verification, and an evidence-based handoff."
argument-hint: "[slice specification path]"
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
source: "AIASD/AI-Assisted-Software-Development-Course/.github/skills/implement-vertical-slice/SKILL.md"
---

# Implement One Vertical Slice

Use the user-supplied specification as the authority for one slice. Follow the repository's [vertical-slice implementation guidance](../../instructions/vertical-slice.instructions.md) and any domain-specific instructions that apply.

## Procedure

1. Resolve the supplied specification or plan. If it is missing or ambiguous, ask which committed source defines the slice.
2. Read the specification, prerequisites, acceptance criteria, applicable instructions, and relevant implementation and test patterns. Identify conflicts, missing decisions, dependencies, exclusions, and verification commands.
3. Present a bounded implementation plan with scope, acceptance criteria, and verification. Wait for approval before editing.
4. Implement only the approved slice in small, reviewable changes. Preserve unrelated user work and follow existing patterns.
5. Run the specified focused tests and other required checks. If a check fails, report the evidence and repair only within the approved scope before rerunning it.
6. Compare the implementation against each acceptance criterion and inspect the diff. Prepare user-facing showcase steps only when requested or required by the specification.
7. Summarize changed files, verification commands and results, acceptance coverage, unresolved risks, and the next dependency in the plan.

## Boundaries

- Do not silently expand scope or begin a dependent slice.
- Do not commit, push, merge, or discard user work without explicit authorization.
- Do not claim checks passed unless they were run and their results were observed.
- Treat a worktree as Git-change isolation, not as a security boundary.
