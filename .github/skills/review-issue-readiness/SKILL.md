---
name: review-issue-readiness
description: "Assess whether a work item is ready for implementation, including clarity, dependencies, parallel independence, sizing, priority, risk, labels, assignees, and possible splitting."
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
source: "ai-practitioner-resources/.github/prompts/pm-review.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# Issue Readiness Review

Use this skill to review backlog items before implementation or sprint planning. Apply the repository's existing issue schema, label taxonomy, and project rules when provided.

## Procedure

1. Inspect the issue text and referenced requirements, code areas, dependencies, and acceptance criteria.
2. Assess clarity, testability, scope, user value, dependencies, security/privacy implications, and missing decisions.
3. Determine whether the item can be implemented independently. Check shared files, APIs, data models, sequencing, and coordination needs; state evidence and confidence.
4. Recommend a priority, size/effort category, risk level, labels, and assignee only when supported by the repository's definitions and evidence.
5. Decide whether to split the issue. If so, propose independently verifiable child items with dependency links.
6. Suggest a concise title/body rewrite that preserves intent and makes acceptance criteria testable.
7. Return the caller's required output format exactly. If a strict JSON schema is supplied, validate field names, types, and allowed values. If the schema is absent or ambiguous, ask for it instead of inventing a contract.

## Output

Provide a readiness decision, evidence-backed gaps/questions, independence rationale, suggested priority/size/risk, labels/assignee recommendations, split plan if needed, and revised issue text in the required format.

## Guardrails

- Do not create, assign, label, reprioritize, or modify issues unless explicitly authorized and the appropriate tool is available.
- Do not infer people, estimates, business priority, or project taxonomy.
- Treat independence as conditional on repository evidence, not as a guarantee of conflict-free parallel work.
