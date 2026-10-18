---
name: create-instruction-prompt
description: "Redirect instruction-generation prompt requests to the canonical skill-based workflow; does not create prompts."

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
source: ".github/prompts/create-instruction-prompt.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Deprecated prompt generation and redirected to the canonical instruction-authoring skill."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Retired Instruction Prompt Generator

Do not create `*.instructions.prompt.md` files. Use [`create-instruction-files-instructions`](../create-instruction-files-instructions/SKILL.md) to create or update instruction files directly.

When migrating an existing instruction-generating prompt, compare its reusable requirements with that skill, preserve unique guidance there, and mark the prompt deprecated with a replacement link.
