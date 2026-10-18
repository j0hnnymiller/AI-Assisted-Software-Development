---
name: academia-data-import-export
description: "Implement Academia data import and export workflows with validation, integrity, privacy, and recoverable failures."
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

# Academia Data Import and Export

## When to Use

Use for bulk loading, migration between systems, or exporting academic records.

## Workflow

1. Inspect supported formats, source/target schemas, existing job patterns, and data-retention or access requirements.
2. Specify field mapping, validation, duplicate handling, partial-failure behavior, and authorization before implementation.
3. Validate input before persistence; use bounded processing and transactional or staged workflows appropriate to the current system.
4. Make retries safe where possible, produce actionable error summaries, and avoid including sensitive row data in logs.
5. Test valid data, malformed input, duplicate records, partial failures, access control, and large-input behavior within measured limits.

## Acceptance Checks

- Imports preserve referential integrity and do not silently discard invalid records.
- Exports include only approved fields and authorized records.
- File size, encoding, and record-count limits are explicit when required.
- No format, data-retention duration, or throughput target is invented.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
