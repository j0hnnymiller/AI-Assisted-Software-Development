---
name: academia-mobile-apps
description: "Implement or revise Academia mobile application features using the repository's existing platform and service contracts."
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

# Academia Mobile Apps

## When to Use

Use for mobile-specific application features, platform integration, or mobile release workflows.

## Workflow

1. Verify the mobile platforms and application framework actually present in the repository.
2. Trace API contracts, authentication, secure storage, navigation, offline behavior, and release configuration relevant to the requested feature.
3. Implement using established platform conventions and shared service contracts; do not introduce a new framework or offline mode without approval.
4. Consider device permissions, accessibility, network failures, and secure handling of locally stored academic data.
5. Add tests using current mobile test tooling, including platform-specific cases when applicable.

## Acceptance Checks

- The feature works on supported platforms and does not regress shared service behavior.
- Secrets and sensitive records are not exposed in logs, insecure storage, or error messages.
- Offline and synchronization semantics are explicit if affected.
- Unsupported devices, platforms, and performance limits are not assumed.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
