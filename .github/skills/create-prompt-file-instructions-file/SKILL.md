---
name: create-prompt-file-instructions-file
description: "Redirect legacy prompt-authoring requests to the canonical skill-based instruction workflow; does not create prompts."

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
source: ".github/prompts/create-prompt-file-instructions-file.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Deprecated prompt generation and redirected to the canonical instruction-authoring skill."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Retired Prompt-Authoring Workflow

Do not create prompt files or prompt-authoring guides. For current instruction creation and maintenance, use [`create-instruction-files-instructions`](../create-instruction-files-instructions/SKILL.md). Consult [`prompt-file.instructions.md`](../../instructions/prompt-file.instructions.md) only when migrating an existing prompt.

For a new reusable workflow, create or update a skill after approval and update the relevant README index.
