---
name: deprecate-create-prompt-instructions
description: "Explains legacy prompt formats and routes reusable workflows to skills; does not create prompts."

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
source: ".github/prompts/create-prompt-instructions.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Deprecated new prompt authoring and redirected reusable workflows to skills.; Redirected implementation-prompt requests to requirements-derived chat guidance or reusable skills."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Retired Prompt-Authoring Workflow

Do not create new prompt files or prompt-authoring guides. Use [`create-instruction-file-authoring-instructions`](../create-instruction-file-authoring-instructions/SKILL.md) for instruction documents and [`prompt-file.instructions.md`](../../instructions/prompt-file.instructions.md) only as a legacy-format migration reference.

Reusable task workflows belong in skills; one-off tasks belong in chat. When a request asks for an implementation prompt, convert it into a requirements-derived execution checklist or plan in the conversation, or into a skill if it is a reusable multi-step workflow. Do not create a `.prompt.md` file as a workaround for the deprecated format.

Before deriving steps, identify the authoritative requirements, scope, dependencies, acceptance criteria, test expectations, and safety constraints. Separate known facts from assumptions and ask for unresolved decisions that materially affect implementation. Keep the resulting guidance actionable but do not prescribe unverified files, commands, APIs, or outputs.
