---
name: academia-grades-transcripts
description: "Implement Academia grade entry, calculation, history, and transcript workflows with auditable access controls."
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

# Academia Grades and Transcripts

## When to Use

Use for grade entry, grading rules, grade history, academic standing, or transcript generation.

## Workflow

1. Trace grade-related models, workflows, authorization, current calculations, and audit behavior.
2. Confirm grading scales, rounding, retake, correction, transcript, and academic-standing rules from approved requirements.
3. Implement changes with precise numeric handling and preserve the history or audit trail required by the domain.
4. Restrict grade and transcript access to authorized roles, and avoid exposing student records in logs or errors.
5. Add tests for calculations, corrections, permissions, transcript consistency, and applicable edge cases.

## Acceptance Checks

- Calculations follow documented policy; no grading scale or precision rule is guessed.
- Changes remain attributable and auditable using existing system mechanisms.
- Transcript output agrees with persisted authoritative data.
- Tests cover both permitted and denied actions.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
