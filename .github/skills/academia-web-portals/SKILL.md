---
name: academia-web-portals
description: "Implement consistent student, faculty, and administrative web portal workflows in an existing Academia application."
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

# Academia Web Portals

## When to Use

Use for student portal, faculty dashboard, administrative interface, or shared web navigation changes.

## Workflow

1. Inspect the existing frontend stack, route structure, design system, accessibility conventions, and user journeys.
2. Identify role-specific tasks and permissions from approved requirements; keep student, faculty, and administrator views distinct where policy requires.
3. Implement within the existing UI architecture. Enforce sensitive access in server/API layers as well as hiding unauthorized interface actions.
4. Provide responsive and accessible interaction states, including loading, empty, validation, and error states.
5. Add component or end-to-end tests using existing tools for key journeys, keyboard/accessibility behavior, and role boundaries.

## Acceptance Checks

- Portal content and actions match the authenticated user's authorized role.
- UI behavior remains usable across supported viewports and assistive technology patterns.
- Existing routes and design conventions remain intact or are migrated explicitly.
- Do not assume a frontend framework or invent role-specific policy.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
