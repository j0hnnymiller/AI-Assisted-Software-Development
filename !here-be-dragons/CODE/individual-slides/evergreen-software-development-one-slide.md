---
marp: true
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "<github-username>"
chat_id: "<chat-id>"
prompt: |
  Generate a single Marp slide summarizing the evergreen software development instructions.
started: "<ISO8601-started>"
ended: "<ISO8601-ended>"
task_durations:
  - task: "draft-slide"
    duration: "00:00:00"
total_duration: "00:00:00"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"
source: ".github/instructions/evergreen-software-development.instructions.md"
---

<!-- _class: lead -->

# Evergreen Software Development

- Keep `main` buildable, secure, releasable
- Automate dependency updates & CI (Dependabot, SCA)
- Merge small, frequent changes; pin and monitor deps
- PR checklist: CI green, security review, changelog
- Enforcement: GitHub Action "Evergreen check" (deps + tests)

---

*See `.github/instructions/evergreen-software-development.instructions.md` for details*
