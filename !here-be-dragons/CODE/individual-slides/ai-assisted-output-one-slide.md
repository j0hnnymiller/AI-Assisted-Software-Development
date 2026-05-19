---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "ai-assisted-output-policy-2025-10-15"
prompt: |
  Create a single Marp slide summarizing the AI provenance and logging policy
  in `.github/instructions/ai-assisted-output.instructions.md`.
started: "2025-10-15T13:00:00Z"
ended: "2025-10-15T13:02:00Z"
task_durations:
  - task: "draft"
    duration: "00:02:00"
total_duration: "00:02:00"
ai_log: "ai-logs/2025/10/15/ai-assisted-output-policy-2025-10-15/conversation.md"
source: ".github/instructions/ai-assisted-output.instructions.md"
---

<!-- _class: lead, center -->

# AI-Assisted Output Policy — At a Glance

- Purpose: enforce provenance for all AI-assisted artifacts
- Requires: embedded YAML front matter (ai_generated, model, operator, chat_id, ai_log, timestamps)
- Workflow: new chat → `ai-logs/yyyy/mm/dd/<chat-id>/conversation.md` + `summary.md`
- Enforcement: CI/PR checks should fail files with `ai_generated: true` missing `chat_id` or `ai_log`

---
