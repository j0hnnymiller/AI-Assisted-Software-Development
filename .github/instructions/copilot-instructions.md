---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "prompt-file.instructions-2025-10-15"
prompt: |
  Consolidate all Copilot-specific instructions into a single copilot-instructions.md file
  that can be referenced from other meta-prompts, prompts, and instruction files.
started: "2025-10-15T16:00:00Z"
ended: "2025-10-15T16:15:00Z"
task_durations:
  - task: "requirements consolidation"
    duration: "00:10:00"
  - task: "file creation"
    duration: "00:05:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Clarified the file's role as repository-wide constraints and linked the current instruction/skill guidance."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Repository-Specific GitHub Copilot Instructions

This file contains repository-wide constraints for Copilot. Follow the applicable files under `.github/instructions/` and `.github/skills/` for task-specific requirements and workflows.

## Core Principles

### Excluded Context

- Never read, search, quote, summarize, attach, or otherwise include files or content from `!here-be-dragons/` in any request, prompt, tool call, or response. Apply this exclusion to every task. If relevant material is needed, ask the user to provide it outside that folder.

---

## Revision History

- 2026-10-18 — Clarified that this file contains repository-wide constraints rather than duplicating the repository's full instruction and skill guidance. See the [chat log](../../ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md).
