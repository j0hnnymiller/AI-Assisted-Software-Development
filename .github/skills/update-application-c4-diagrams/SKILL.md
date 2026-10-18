---
name: update-application-c4-diagrams
description: "Document an application's verified current state with Mermaid C4 context and container diagrams."
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
source: ".github/prompts/update-application-c4-diagrams.md"
---

# Update Application C4 Diagrams

## When to Use

Use when asked to document or refresh an application's current architecture with Mermaid C4 diagrams.

## Workflow

1. Inspect the repository's source, configuration, deployment files, tests, and existing documentation before describing the system.
2. Separate verified facts from assumptions. Mark unresolved details as `TODO`; do not infer services, users, vendors, technologies, or data flows.
3. Update the appropriate existing README or overview document. Create a new overview only when no suitable documentation location exists.
4. Add a focused C4 Context (C1) diagram and C4 Container (C2) diagram. Add C3 only for a critical component when it adds useful detail.
5. Include a concise executive summary, verified technology stack, high-level architecture, and build/run instructions only when supported by repository evidence.
6. Link to deeper documentation and keep diagrams small enough to review.

## Acceptance Checks

- C1 and C2 match the observed system boundaries, actors, containers, and relationships.
- Labels and descriptions are traceable to code, configuration, or existing approved documentation.
- Mermaid syntax is validated with the renderer used by the project or target host when available.
- Links resolve and existing documentation remains accurate.
- Report any unverified assumptions and validation limitations.

Do not change application code as part of a documentation-only request.
