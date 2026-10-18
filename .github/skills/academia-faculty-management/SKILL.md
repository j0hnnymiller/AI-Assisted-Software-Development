---
name: academia-faculty-management
description: "Implement Academia faculty records, assignments, and faculty-facing workflows using existing domain conventions."
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  files in the .github/prompts folder should be campared with the canonical skills. If a skill does not exist for the prompt, create a new skill. Prompt files are being deprecated. update the instructions, skills, and agents, responsible for syncing .github files.
started: "2026-10-17T18:21:06.8108325-07:00"
ended: "2026-10-17T18:37:09.0441419-07:00"
task_durations:
  - task: "Prompt-to-skill migration and sync guidance"
    duration: "00:16:02"
total_duration: "00:16:02"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: ".github/prompts/generate-implementation-prompts-prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added evidence-grounded artifact and dependency mapping for faculty implementation plans."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Academia Faculty Management

## When to Use

Use for faculty profiles, affiliations, teaching assignments, or faculty administration.

## Workflow

1. Inspect faculty entities, employment/affiliation data, course assignment flows, and role checks.
2. Confirm authoritative rules for appointment status, departments, assignment eligibility, and workload before encoding them.
3. Implement the requested change across existing service, API, and UI layers; preserve links to courses and terms.
4. Protect staff and student information according to existing access and data-handling policies.
5. Add tests for lifecycle transitions, assignment validation, permissions, and relevant data integrity constraints.
6. For a requested implementation map, identify the feature's domain rules, affected layers/artifacts, dependencies, test evidence, and acceptance checks. Keep the map aligned with the repository's current structure and label proposed artifacts as such.

## Acceptance Checks

- Faculty records and assignments cannot become inconsistent with course/term state.
- Administrative actions follow existing authorization and audit conventions.
- Unknown employment or workload policy is explicitly surfaced rather than inferred.
- Execution maps identify prerequisites and artifact ownership without duplicating the feature's business rules or asserting unverified files.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
