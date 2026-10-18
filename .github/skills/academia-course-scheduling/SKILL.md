---
name: academia-course-scheduling
description: "Implement Academia course catalog, term offerings, and scheduling workflows using verified academic rules."
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

# Academia Course Catalog and Scheduling

## When to Use

Use for course catalog, sections, academic terms, schedules, prerequisites, or seat-capacity workflows.

## Workflow

1. Inspect the current catalog model, term/calendar rules, schedule flows, and course-related APIs and tests.
2. Verify course lifecycle, prerequisite, capacity, time-conflict, and add/drop rules from approved requirements.
3. Implement changes using existing domain and persistence patterns, preserving references to enrolled students and faculty.
4. Consider concurrent seat allocation, waitlist transitions, and time-zone handling only when those behaviors are supported or requested.
5. Add unit and integration tests for relevant catalog states, schedule conflicts, and boundary conditions.

## Acceptance Checks

- Course, section, term, and schedule data remain consistent through supported state transitions.
- Prerequisite, seat, and conflict rules are explicit and testable.
- Existing API contracts remain compatible or are versioned through the project's established approach.
- Unspecified academic-calendar rules are raised as questions, not invented.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
