---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "prompt-file.instructions-2025-10-15"
prompt: |
  Create an instruction file that ensures all instruction-generating prompts
  include AI provenance requirements in their deliverable sections.
started: "2025-10-15T15:20:00Z"
ended: "2025-10-15T15:30:00Z"
task_durations:
  - task: "instruction design"
    duration: "00:08:00"
  - task: "template creation"
    duration: "00:02:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: ".github/copilot/Promptfiles/meta/create-instruction-file-instructions.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Deprecated authoring instruction-generating prompts and redirected reusable workflows to skills."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
applyTo: "**/*.instructions.prompt.md"
---

# Legacy Instruction-Prompt Reference (Deprecated)

> **Deprecated:** Do not create new `*.instructions.prompt.md` files or other prompt generators. Use an existing workspace skill or create a skill for reusable instruction-authoring workflows. This file is retained only to support migration of existing prompt files.

## Migration Workflow

1. Compare the existing prompt's purpose, inputs, workflow, and outputs with skills under [`../skills/`](../skills/).
2. If a skill already covers the workflow, update that skill only when the prompt contains useful, verified requirements that are missing.
3. If no skill covers a reusable workflow, create a skill; do not create a replacement prompt.
4. Preserve an existing prompt only as a clearly deprecated migration record when removal is not authorized. Link it to its replacement skill.
5. Verify current requirements against repository policy and host behavior. Do not carry forward stale paths, unsupported fields, example secrets, or unverifiable provenance.
6. Validate front matter, links, and the final skill/prompt index.

## Legacy Requirements (Migration Context Only)

The historical sections below describe expectations the old prompt format attempted to enforce. They are not instructions to create, regenerate, or distribute prompt files.

### Provenance

Instruction files that are created or revised must follow [`ai-assisted-output.instructions.md`](ai-assisted-output.instructions.md), including embedded YAML provenance and a traceable conversation log. Generate or update instruction files through [`create-instruction-files-instructions`](../skills/create-instruction-files-instructions/SKILL.md), not through a prompt generator.

### Historical Prompt Content

Existing prompts may contain provenance templates, output requirements, or validation checklists. Treat these as migration input only. Keep only requirements that remain accurate and useful in the replacement skill or instruction file.

Do not submit, regenerate, or use legacy prompts as active workflows. Route reusable work to skills and one-off work to the active chat.
