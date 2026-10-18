---
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
source: "user request"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# Legacy Prompt-Generator Index (Deprecated)

This folder contains no active prompt generators. Do not add prompt files here; use reusable skills directly.

## Skill Replacements

| Legacy generator workflow | Current skill |
| --- | --- |
| Create or update instruction-authoring guidance | [`create-instruction-file-authoring-instructions`](../../skills/create-instruction-file-authoring-instructions/SKILL.md) |
| Create or update use-case authoring guidance | [`create-use-case-authoring-instructions`](../../skills/create-use-case-authoring-instructions/SKILL.md) |
| Generate general instruction files | [`generate-instructions`](../../skills/generate-instructions/SKILL.md) |
| Add AI provenance policy guidance | [`create-ai-assisted-output-policy`](../../skills/create-ai-assisted-output-policy/SKILL.md) |
| Review and improve existing instructions | [`validate-and-improve-instructions`](../../skills/validate-and-improve-instructions/SKILL.md) |

The legacy prompt-authoring generator skills are migration references only. They must not create `.prompt.md` or `*.instructions.prompt.md` files; route new reusable workflows to skills and one-off requests to chat.
