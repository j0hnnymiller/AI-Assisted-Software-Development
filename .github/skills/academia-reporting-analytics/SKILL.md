---
name: academia-reporting-analytics
description: "Implement Academia reports and analytics with verified metric definitions, privacy controls, and scalable queries."
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

# Academia Reporting and Analytics

## When to Use

Use for operational reports, dashboards, aggregate metrics, or analytics features.

## Workflow

1. Identify source-of-truth data, existing query/reporting patterns, authorized audiences, and documented metric definitions.
2. Clarify filters, time ranges, aggregation rules, freshness requirements, and export needs.
3. Implement queries and presentation through existing layers. Prefer bounded, read-only access for analytics and avoid unnecessary data duplication.
4. Apply privacy, authorization, retention, and de-identification requirements; do not expose identifiable student or faculty data by default.
5. Test metric calculations, empty and boundary cases, access restrictions, and query behavior on representative fixtures.

## Acceptance Checks

- Each metric has a documented definition and traceable source.
- Reports respect the caller's data scope and avoid unintended disclosure.
- Performance claims or thresholds are based on measured requirements.
- Results are reproducible for the same source data and parameters.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
