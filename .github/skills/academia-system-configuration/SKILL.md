---
name: academia-system-configuration
description: "Implement Academia application and tenant configuration with validation, safe secret handling, and compatibility."
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

# Academia System Configuration

## When to Use

Use for application, environment, feature, or tenant configuration changes.

## Workflow

1. Trace how configuration is loaded, validated, overridden, and deployed in each affected environment.
2. Confirm which values are safe configuration and which are secrets; keep secrets in the repository's approved secret store.
3. Add typed validation and safe failure behavior using current project conventions. Avoid silent defaults that change security or business behavior.
4. Preserve compatibility for existing deployments or provide an explicit migration and rollout plan.
5. Add tests for missing, malformed, boundary, and environment-specific values without embedding real secrets.

## Acceptance Checks

- Configuration ownership, scope, and precedence are explicit.
- Invalid or missing required values fail clearly and safely.
- Secret material is not committed, logged, or exposed to clients.
- No cloud provider or deployment platform is assumed without repository evidence.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
