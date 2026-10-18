---
name: academia-logging-monitoring
description: "Add or improve Academia application logs, metrics, traces, dashboards, and alerts without exposing sensitive data."
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

# Academia Logging and Monitoring

## When to Use

Use when instrumenting application behavior, diagnosing operational gaps, or adding actionable monitoring.

## Workflow

1. Inspect existing logging, metrics, tracing, dashboards, alerting, and deployment conventions.
2. Identify the operational question each signal should answer and use established telemetry libraries and naming.
3. Add structured, appropriately leveled events and useful service/operation measurements. Keep high-cardinality dimensions bounded.
4. Redact credentials, tokens, student records, and other sensitive data; apply data-retention and access policies already in force.
5. Test emitted telemetry and redaction where practical, and document any new dashboard or alert.

## Acceptance Checks

- Signals support a concrete diagnosis or service objective; do not invent alert thresholds.
- Correlation context is preserved without recording secrets or unnecessary personal data.
- Instrumentation failures do not break core application behavior.
- Validation and monitoring limitations are stated.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
