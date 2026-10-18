---
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
source: "user request"
---

# Legacy Prompt Archive (Deprecated)

> Do not create new prompt files. Reusable workflows belong in `.github/skills/<name>/SKILL.md`; one-off work belongs in chat. This directory is retained only for prompt migration records.

## Retained Migration Sources

| Legacy source | Canonical replacement |
| --- | --- |
| [`update-application-c4-diagrams.md`](update-application-c4-diagrams.md) | [`update-application-c4-diagrams`](../skills/update-application-c4-diagrams/SKILL.md) |
| [`generate-implementation-prompts-prompt.md`](generate-implementation-prompts-prompt.md) | 14 Academia component skills listed below |

### Academia Component Skills

**Core infrastructure**

- [`academia-database-migrations`](../skills/academia-database-migrations/SKILL.md)
- [`academia-identity-and-permissions`](../skills/academia-identity-and-permissions/SKILL.md) - combines authentication, authorization, user management, and permissions
- [`academia-api-gateway-routing`](../skills/academia-api-gateway-routing/SKILL.md)
- [`academia-logging-monitoring`](../skills/academia-logging-monitoring/SKILL.md)

**Academic management**

- [`academia-student-enrollment`](../skills/academia-student-enrollment/SKILL.md)
- [`academia-course-scheduling`](../skills/academia-course-scheduling/SKILL.md)
- [`academia-grades-transcripts`](../skills/academia-grades-transcripts/SKILL.md)
- [`academia-faculty-management`](../skills/academia-faculty-management/SKILL.md)

**Administration**

- [`academia-reporting-analytics`](../skills/academia-reporting-analytics/SKILL.md)
- [`academia-system-configuration`](../skills/academia-system-configuration/SKILL.md)
- [`academia-data-import-export`](../skills/academia-data-import-export/SKILL.md)

**Interfaces and delivery**

- [`academia-web-portals`](../skills/academia-web-portals/SKILL.md) - combines student, faculty, and administrative web interfaces
- [`academia-mobile-apps`](../skills/academia-mobile-apps/SKILL.md)
- [`academia-integration-deployment`](../skills/academia-integration-deployment/SKILL.md) - combines system integration and deployment automation

Only these two prompt source files currently exist in this directory. The previous category listings described files that are no longer present and are intentionally removed.

## Migration and Sync Policy

- Compare prompts by purpose, workflow, inputs, outputs, and constraints, not by filename.
- Update a matching canonical skill or propose a new focused skill when no equivalent exists; obtain approval before creating it.
- Keep each source prompt marked as deprecated with links to its replacement until maintainers decide otherwise.
- Prompt files remain visible to cross-repository inventory but have `distribute: "none"` in the sync manifest. Do not import, propagate, or delete them through the sync workflow.
- Keep this index accurate and validate all replacement links.
