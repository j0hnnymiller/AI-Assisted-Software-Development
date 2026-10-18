---
name: academia-database-migrations
description: "Implement or revise Academia database schemas and data migrations using the repository's existing data-access patterns."
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

# Academia Database Migrations

## When to Use

Use for database schema, migration, or persistence changes in an Academia application.

## Workflow

1. Inspect the current schema, data-access layer, migration tooling, deployment process, and related tests.
2. Confirm the requested entities, constraints, and relationships from requirements or existing behavior; ask about unresolved business rules.
3. Implement the smallest migration using repository conventions. Preserve existing data and keep deployment compatibility in mind.
4. Add or update tests for a fresh database, upgrade from supported prior versions, constraints, and failure handling.
5. Update schema or operations documentation when the supported workflow changes.

## Acceptance Checks

- Migration order and dependencies are explicit and compatible with the project's tooling.
- Existing data is preserved or transformed according to approved rules.
- Upgrade behavior is tested; rollback or forward-recovery is addressed where the platform supports it.
- No framework, database, schema, or performance target is assumed without evidence.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
