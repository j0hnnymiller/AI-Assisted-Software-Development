---
name: academia-api-gateway-routing
description: "Implement Academia API gateway, routing, versioning, and cross-cutting request policies using the existing architecture."
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

# Academia API Gateway and Routing

## When to Use

Use for API gateway, endpoint routing, API versioning, or shared request-policy changes.

## Workflow

1. Map the existing gateway, service boundaries, endpoint conventions, authentication flow, and API contracts.
2. Confirm routes, consumers, and compatibility requirements before changing public behavior.
3. Implement routing and shared middleware with established patterns. Do not introduce a gateway product or service boundary without architectural approval.
4. Define consistent handling for validation failures, authorization failures, throttling, and upstream errors where these are in scope.
5. Add contract and integration tests for route selection, version behavior, error responses, and access policies.

## Acceptance Checks

- Existing supported routes and contracts continue to work or have an approved migration plan.
- Sensitive routes retain server-side authentication and authorization.
- Errors do not expose secrets, internal stack traces, or unnecessary personal data.
- Routing behavior is observable through existing logging and monitoring conventions.

## Cross-Cutting Validation

Follow the repository's coding and test conventions. Run component unit and integration tests plus relevant cumulative end-to-end/regression flows; verify data integrity, API compatibility, security, performance, and documentation where applicable. Report tests not run and do not invent coverage targets.
