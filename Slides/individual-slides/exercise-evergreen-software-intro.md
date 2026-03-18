---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "evergreen-exercise-deck-20260316"
prompt: |
  create an exercise slide deck, using the #file:exercise-template.md, for evergreen software development principles and failure modes.
started: "2026-03-17T03:32:00Z"
ended: "2026-03-17T03:39:00Z"
task_durations:
  - task: "template mapping"
    duration: "00:02:00"
  - task: "deck authoring"
    duration: "00:05:00"
total_duration: "00:07:00"
ai_log: "ai-logs/2026/03/16/evergreen-exercise-deck-20260316/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

## Evergreen Software Development - Core Principles Exercise Instructions

**Duration:** 20-25 minutes
**Prerequisites:** Basic familiarity with architecture and automated testing

### Objectives

- Use intent-first design to anchor long-term maintainability.
- Keep interfaces stable while improving internals.
- Add practical AI guardrails and governance checks.

### Activities

- Capture intent and invariants before code changes.
- Separate contracts from implementation details.
- Define mandatory validation gates before regeneration.

### Success Criteria

- Intent and constraints are explicit and testable.
- Contract stability is preserved during internal change.
- Regeneration workflow is governed by tests and review.
- Team can explain how this supports evergreen outcomes.

---
