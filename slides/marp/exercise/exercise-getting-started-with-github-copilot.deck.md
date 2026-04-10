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

## Exercise: Getting Started with GitHub Copilot

Objectives

- Install and configure GitHub Copilot
- Verify authentication with your GitHub account
- Explore core Copilot UI components in VS Code

Activities

1. Install the GitHub Copilot extension from the VS Code marketplace.
2. Sign in with your GitHub account and verify Copilot access.

::: column

3. Locate and explore:

- Chat window and chat history
- New chat button
- Quick chat feature and keyboard shortcut
- Settings menu
- Model selection dropdown

4. Check your premium token usage bar.
5. Create a new chat and experiment with the interface.

Success Criteria

- Copilot extension is installed and authenticated
- You can open and close chat windows
- You can explain main chat versus quick chat
- You can find and use chat history

::: notes
Duration ~00:30

Use this lab as the onboarding checkpoint for all remaining Copilot exercises. Start by confirming everyone has VS Code open and can reach the extension marketplace, then walk the room while participants sign in and complete authentication. Pause after each interface element so learners can find it before moving forward, especially quick chat and model selection since these are easy to miss for first-time users. Close by asking each participant to start one test chat so you can confirm readiness before transitioning to context management.
:::