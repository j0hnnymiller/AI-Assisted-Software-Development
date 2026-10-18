---
name: databricks-apps-cicd-advisory
description: "Assess or design CI/CD for Databricks Apps, including source control, validation, deployment promotion, secrets, permissions, rollback, and operational checks."
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  Merge useful gaps and create proposed new skills
started: "2026-10-17T19:33:05.9169653-07:00"
ended: "2026-10-17T19:52:32.094572-07:00"
task_durations:
  - task: "Approved cross-repository prompt-to-skill migration"
    duration: "00:19:26"
total_duration: "00:19:26"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "Messer/.github/prompts/cicd-advisory-databricks-apps.prompt.md"
---

# Databricks Apps CI/CD Advisory

Use this skill to advise on a Databricks Apps delivery pipeline. Verify platform capabilities and commands against the team's current Databricks product version and approved documentation.

## Inputs

- App framework and repository layout, workspaces/environments, deployment identity, existing pipeline, approval model, secrets handling, and release constraints.
- Separate confirmed platform configuration from assumptions.

## Procedure

1. Inventory build inputs, app configuration, dependencies, tests, generated artifacts, and environment-specific settings.
2. Define pull-request checks: formatting, unit/integration tests, dependency and secret scans, and configuration validation.
3. Design a least-privilege CI identity and a secure authentication method supported by the target workspace and runner.
4. Define deployment stages and promotion rules. Keep artifacts immutable where feasible; avoid rebuilding different code for production.
5. Separate secrets and environment configuration from source. Document ownership, rotation, and access without recording secret values.
6. Add deployment validation, health/smoke checks, audit evidence, failure notification, and a tested rollback or forward-fix procedure.
7. Identify product-specific uncertainties and verify commands, APIs, and permissions using current official Databricks documentation.

## Output

Deliver a pipeline overview, stage/check matrix, identity and secret-handling plan, environment promotion flow, failure/rollback steps, and open questions. Provide sample configuration only when the runner and supported interfaces are known.

## Guardrails

- Do not assume a particular CI provider, workspace topology, deployment command, or feature availability.
- Never include credentials, tokens, workspace secrets, or sensitive deployment identifiers in examples.
- Do not deploy or modify a live workspace unless explicitly authorized.
