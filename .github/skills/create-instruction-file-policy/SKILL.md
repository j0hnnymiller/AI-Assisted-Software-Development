---
name: create-instruction-file-policy
description: "Deprecated alias for create-instruction-file-authoring-instructions; use the canonical skill to create or update instruction-file guidance."

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
source: ".github/prompts/create-instruction-file-instructions.prompt.md"
revisions:
- chat_id: "skill-naming-convention-20261018"
  model: "unknown/unknown@unknown"
  date: "2026-10-18"
  change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
  ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
- chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
  model: "unknown/unknown@unknown"
  date: "2026-10-18"
  change: "Retired this duplicate workflow and redirected it to the canonical instruction-file authoring skill."
  ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Deprecated Instruction-File Policy Generator

This skill duplicated the canonical instruction-file authoring workflow and prescribed
the retired `.instruction.md` suffix and a fixed output path. Do not use it to create
instruction guides.

Use [`create-instruction-file-authoring-instructions`](../create-instruction-file-authoring-instructions/SKILL.md)
to create or revise instruction-file guidance. Follow the current
[instruction-file conventions](../../instructions/instruction-files.instructions.md)
and adapt sections, templates, examples, and checklists to the verified repository
requirements rather than copying a fixed legacy template.




