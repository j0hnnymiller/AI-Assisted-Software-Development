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

## Lab: Getting Started with GitHub Copilot

Objectives

- Install and configure GitHub Copilot
- Verify authentication with your GitHub account
- Explore core Copilot UI components in VS Code

Activities

1. Install the GitHub Copilot extension from the VS Code marketplace.
2. Sign in with your GitHub account and verify Copilot access.
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

---

## Lab: Understanding Context Management

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

---

## Lab: Chat Management and Workflow

Objectives

- Organize chat sessions effectively
- Use chat history as a working reference
- Develop efficient workflow patterns with main and quick chat

Activities

1. Chat organization:
   - Review current chat history
   - Identify conversations that should have been separate
   - Practice starting new chats at natural topic boundaries
2. Context preservation:
   - Run one focused feature chat
   - Add only relevant context files
   - Complete work without context overflow
3. Quick chat practice:
   - Keep main chat for primary task flow
   - Use quick chat for side questions
   - Return to main chat with context preserved
4. Chat history review:
   - Locate previous high-quality solutions
   - Identify prompts that worked well
   - Capture repeatable prompt patterns

Success Criteria

- Chat history is organized and meaningful
- You can quickly find and reuse previous solutions
- You can use multiple chat windows without losing primary context

Context Window Management

- Context is a limited resource
- Start a new chat when focus changes
- Keep conversations targeted and specific
- If Copilot forgets early details, reset with a fresh chat

::: notes
Duration ~00:20

Introduce this lab as productivity hygiene that prevents context fatigue and low-quality responses later in the day. Coach participants to separate work streams by topic, and use quick chat for interruptions so their main conversation remains coherent and reusable. During the history review, have each learner identify one prompt that worked well and explain why it worked, which helps them build a personal prompting playbook. Finish with the context window management bullets as operational rules they can apply in every future session.
:::

---

## Lab: Exploring Copilot Modes

Objectives

- Understand differences between Ask, Edit, and Agent modes
- Know when to use each mode
- Understand premium token usage implications

Activities

1. Ask mode:
   - Ask Copilot to explain a selected code snippet
   - Request multiple implementation approaches
   - Try different models and compare response style
   - Note that Ask mode is best for exploration
2. Edit mode:
   - Select existing code and request a refactor
   - Review inline proposed changes
   - Accept or reject updates intentionally
3. Agent mode:
   - Create a new file and add starter content
   - Request coordinated changes across multiple files
   - Ask Copilot to run terminal commands
   - Recheck premium token usage after actions

Success Criteria

- You can choose the right mode for the task
- You can explain relative token usage tradeoffs
- You can complete a multi-file action using Agent mode

::: notes
Duration ~00:20

Position this lab as decision-making practice so participants learn to match the mode to the work, not just default to one interface. In Ask mode, emphasize low-risk exploration and comparative learning with different models before making any code changes. In Edit mode, slow down and review diffs so learners build trust through verification rather than blind acceptance. In Agent mode, demonstrate value on a task that justifies automation, then connect the result to token usage so participants can balance cost and productivity in real workflows.
:::
