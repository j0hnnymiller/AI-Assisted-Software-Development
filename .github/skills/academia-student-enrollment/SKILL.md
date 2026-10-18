---
name: academia-student-enrollment
description: "Implement Academia student enrollment and profile workflows from verified business rules."
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
---

# Academia Student Enrollment

## When to Use

Use for student records, profile workflows, applications, enrollment, or registration changes.

## Workflow

1. Read the current domain model, enrollment flows, related requirements, and existing integration tests.
2. Identify the authoritative rules for eligibility, prerequisites, capacity, holds, waitlists, and enrollment periods; ask when any rule is unclear.
3. Implement the requested vertical slice across persistence, business logic, API, and UI only where those layers exist and are in scope.
4. Make state changes transactional and safe against duplicate submissions or concurrent enrollment when supported by the persistence model.
5. Add tests for approved rules, invalid transitions, access boundaries, and data integrity; update user-facing documentation as needed.

## Acceptance Checks

- Student personal data is exposed only to authorized users and purposes.
- Enrollment decisions are enforced by trusted application logic, not only presentation code.
- Existing records and related course registrations remain consistent.
- No unapproved enrollment rule or coverage percentage is assumed.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
