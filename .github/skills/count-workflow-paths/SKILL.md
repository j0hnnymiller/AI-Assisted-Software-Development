---
name: count-workflow-paths
description: "Enumerate and count simple paths through a supplied workflow or state machine, with explicit loop, terminal-state, and path-explosion rules."
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  Merge useful gaps and create proposed new skills
started: "2026-10-17T19:33:05.9169653-07:00"
ended: "2026-10-17T19:52:32.094572-07:00"
task_durations:
  - task: "Approved cross-repository prompt-to-skill migration"
    duration: "00:19:26"
total_duration: "00:19:26"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "ai-practitioner-resources/.github/prompts/count-workflow-paths.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Separated generic path analysis from repository-specific issue/project automation."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Workflow Path Counting

Use this skill to count unique paths through a directed workflow graph and, when requested, produce path-based test cases.

## Procedure

1. Obtain the graph or extract states, transitions, entry points, terminal states, guards, and retry/loop semantics from supplied documentation.
2. Normalize state and transition identifiers; preserve distinct guarded transitions when they represent different behavior.
3. Define the counting rules with the user: path length, whether paths must end at a terminal state, how cycles are treated, and whether retry loops are excluded or bounded.
4. Enumerate simple paths using a visited-state set, or use an explicit loop bound for cyclic workflows. Record excluded/bounded edges and assumptions.
5. Detect unreachable states, dead ends, duplicate transitions, invalid targets, and paths that cannot reach a terminal state.
6. Report the count with a compact path listing or an approved artifact when tractable. For large graphs, report algorithm, bounds, and representative paths rather than implying exhaustive output.
7. Keep generic path analysis separate from repository-specific issue/project automation. If asked to create test issues or add them to a project, verify the active repository's generated artifact flow, permissions, labels, project identifiers, and commands; draft the actions first and obtain explicit authorization before any external write.

## Output

Include graph scope, path-counting rules, total count, enumerated paths (or artifact location), unreachable/dead-end findings, and complexity limitations.

## Guardrails

- Never silently treat retries, cycles, or conditional branches as ordinary paths.
- Do not claim exhaustive enumeration when a bound, truncation, or graph uncertainty exists.
- Do not create external work items without approval.
- Do not copy repository-specific issue templates, project IDs, labels, scripts, or `gh` commands from a legacy prompt into a generic workflow; verify them in the target repository and prefer its maintained generation/validation pipeline.

---

## Revision History

- 2026-10-18 — Clarified the boundary between reusable path analysis and repository-specific issue/project automation. See the [chat log](../../../ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md).
