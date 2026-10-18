---
name: academia-identity-and-permissions
description: "Implement Academia authentication, authorization, user management, and permission changes with least privilege."
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

# Academia Identity and Permissions

## When to Use

Use for sign-in, identity lifecycle, user administration, roles, permissions, or authorization policy changes.

## Workflow

1. Trace the existing identity provider, session/token handling, user model, authorization middleware, and role/permission checks.
2. Confirm required user types and access rules from approved requirements; avoid inventing roles or weakening existing controls.
3. Implement authentication and authorization through established server-side patterns. Apply least privilege and deny access by default where the system's policy permits.
4. Protect credential and personal data; never log secrets or tokens. Record sensitive administrative changes using existing audit mechanisms.
5. Add tests for unauthenticated access, each affected role/permission boundary, invalid credentials or claims, and authorized flows.

## Acceptance Checks

- Access decisions are enforced at trusted server boundaries, not only in the UI.
- User-management operations cannot grant broader access than the approved policy.
- Existing users and sessions remain compatible or have a documented migration path.
- Tests demonstrate both allowed and denied cases.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
