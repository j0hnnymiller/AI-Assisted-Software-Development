---
name: chatmode-authoring
description: "Create or revise a focused VS Code chat mode with a clear role, supported configuration, bounded workflow, tool scope, examples, and validation."
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
source: "AI-SW-Dev/.github/prompts/create_chatmode_guidance.md"
---

# Chat Mode Authoring

Use this skill to author or review a chat mode for a defined persona or recurring conversational workflow. Verify the selected host's current format and capabilities before generating configuration.

## Inputs

- Intended users, role, recurring tasks, domain boundaries, expected response style, tools needed, and target host.
- Existing instructions, agents, skills, and chat modes that may overlap.

## Procedure

1. Confirm that a chat mode is the right primitive: use a skill for on-demand workflows, instructions for always-on/file-scoped rules, or an agent when separate tool/context boundaries are required.
2. Define a focused mission, supported use cases, out-of-scope requests, and escalation or clarification behavior.
3. Verify supported file location, extension, YAML schema, activation behavior, and tool configuration from current host documentation and repository conventions.
4. Specify a concise workflow and response contract. Include examples only when they materially clarify expected behavior.
5. Grant only the tools needed for the workflow; distinguish instruction text from enforced platform permissions.
6. Check for duplication, conflicting guidance, unsupported front matter, secrets, and repository-specific assumptions.
7. Validate YAML and links, then test representative in-scope and out-of-scope requests in the intended host.

## Output

Create or revise the chat mode only at the approved path. Summarize its role, triggers, tool scope, boundaries, schema evidence, and validation results.

## Guardrails

- Do not use unsupported header fields or claim that prose enforces authorization or isolation.
- Avoid broad personas, redundant instructions, unnecessary tools, and hard-coded personal or environment details.
- Ask before overwriting an existing mode or replacing a canonical workflow.
