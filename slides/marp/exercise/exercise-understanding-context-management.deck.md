---
ai_generated: true
model: "openai/gpt-5.3-codex@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-github-copilot-vscode-workflows-20260322"
prompt: |
  create an exercise marp slide deck using the slides\exercise-template.pptx template for the provided GitHub Copilot labs (getting started, context management, chat workflow, and modes)
started: "2026-03-22T00:00:00Z"
ended: "2026-03-22T00:20:00Z"
task_durations:
  - task: "exercise deck authoring"
    duration: "00:12:00"
  - task: "provenance logging"
    duration: "00:05:00"
  - task: "readme update"
    duration: "00:03:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2026/03/22/exercise-github-copilot-vscode-workflows-20260322/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
<!-- layout: Two Content -->

## Exercise: Understanding Context Management

Objectives

- Learn to add context using @ symbols
- Understand context window limitations
- Practice writing effective prompts

Activities

1. Basic context addition:

- Use `@workspace` to search your codebase
- Use `@file` to reference specific files
- Use `@terminal` to include command output
- Use `@vscode` for VS Code product questions

::: column

2. Prompt practice:

- Write a vague prompt and observe the result
- Rewrite with specific context and compare quality
- Add file references to improve accuracy

3. Context window experiment:

- Run a longer single conversation
- Observe when early context gets dropped
- Start a new chat when topic focus changes

Success Criteria

- You can use all four @ context types
- You can identify when to start a fresh chat
- You can show quality improvements from specific prompts

::: notes
Duration ~00:20

Frame this as the first skill that directly improves Copilot output quality without changing tools or models. During the @ symbol walkthrough, have participants perform each step live and explain what new information Copilot gains from each context type. For the prompt comparison, ask learners to keep the same goal and only change context quality so the difference is obvious and measurable. End by normalizing context window limits as expected behavior, then reinforce the habit that new topic equals new chat.
:::