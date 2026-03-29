---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "prompt-file.instructions-2025-10-15"
prompt: |
  Create a single Marp slide summarizing the Copilot-specific instructions in
  `.github/instructions/copilot-instructions.md`.
started: "2025-10-15T16:00:00Z"
ended: "2025-10-15T16:02:00Z"
task_durations:
  - task: "draft"
    duration: "00:02:00"
total_duration: "00:02:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: ".github/instructions/copilot-instructions.md"
---

<!-- _class: lead, center -->

# Copilot Instructions — Key Points

- Always use the underlying AI model in `model` (provider/model@version)
- Capture full provenance in YAML front matter (11 required fields)
- New chat → new `ai-logs/yyyy/mm/dd/<chat-id>/` with `conversation.md` + `summary.md`
- Operator must be the GitHub username (do not use literal "USER")

---
