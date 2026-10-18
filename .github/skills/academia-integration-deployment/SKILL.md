---
name: academia-integration-deployment
description: "Implement Academia system integrations and deployment automation using verified contracts and existing CI/CD workflows."
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

# Academia Integration and Deployment

## When to Use

Use for external/internal service integrations, environment promotion, release automation, or deployment pipeline changes.

## Workflow

1. Map current service contracts, dependency ownership, CI/CD workflows, environments, secret sources, and release/rollback processes.
2. Confirm authentication, data ownership, reliability expectations, compatibility, and failure semantics for each integration.
3. Implement the smallest contract or pipeline change using repository-supported tooling. Keep credentials out of source and build logs.
4. Add contract/integration tests and pipeline validation. Document rollout order, health checks, and rollback or forward-recovery steps.
5. Avoid changing production resources or publishing artifacts unless explicitly requested and approved.

## Acceptance Checks

- Integration and deployment behavior is reproducible and observable.
- Environment-specific configuration and secrets remain separated from code.
- Failure, retry, timeout, and rollback behavior are explicit and tested where practical.
- No cloud provider, deployment target, or availability objective is assumed without evidence.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
