---
name: create-agent-instructions-file
description: "Generate comprehensive authoring guidelines for custom GitHub Copilot agents"

ai_generated: true
model: "OpenAI/GPT-6@Luna"
operator: "johnmillerATcodemag-com"
chat_id: "convert-prompt-files-to-skills-20261016"
prompt: |
  help me convert the prompt files in the prompts folder into skills.
started: "2026-10-16T21:25:07.811Z"
ended: "2026-10-16T21:43:11.234Z"
task_durations:
  - task: "Converting repository prompt files to skills"
    duration: "00:18:03"
total_duration: "00:18:03"
ai_log: "ai-logs/2026/10/16/convert-prompt-files-to-skills-20261016/conversation.md"
source: ".github/prompts/create-agent-instructions-file.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Replaced unsupported legacy agent headers with current schema verification, scoped design, examples, and behavior review."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Generate Custom Agent Instructions

Create or revise guidance for authoring focused custom agents. Follow the repository's [agent-file instructions](../../instructions/agent-file.instructions.md), the selected host's current schema, and the AI provenance policy.

## Workflow

1. Confirm whether the requested deliverable is an authoring guide or a specific `.agent.md` file, and identify the intended host and scope.
2. Review existing agents and instructions to avoid duplicate roles and conflicting behavior.
3. Verify the supported file location, frontmatter properties, tool configuration, and activation behavior from current host documentation.
4. Define a focused mission, intended users/triggers, expertise, bounded workflow, expected output, and out-of-scope requests.
5. Specify only supported frontmatter. Do not require legacy `Focus`, `Temperature`, or `Style` headers, or invent `@command` activation syntax.
6. Select the minimum host-supported tools needed. Explain that natural-language instructions do not enforce authorization or isolation.
7. Include realistic examples, templates, or behavior checks only when they improve predictable use. For persona agents, test evidence-based decisions, clarification behavior, and prioritization boundaries.
8. Validate YAML, links, scope, and representative in-scope/out-of-scope interactions. Ask before overwriting canonical guidance.

## Expected Content

An agent authoring guide should cover purpose and when to use an agent, naming/location, supported YAML fields, role and workflow design, tool scope, response expectations, examples, validation, maintenance, and common anti-patterns. Keep recommendations distinct from host requirements.

## Guardrails

- Do not assume frontmatter fields or activation syntax across hosts.
- Avoid broad personas, excessive tools, redundant sections, private organizational details, and fabricated metrics.
- Preserve provenance and existing user changes; do not overwrite a canonical guide without approval.



