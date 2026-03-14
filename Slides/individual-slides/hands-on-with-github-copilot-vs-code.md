---
marp: true
theme: default
paginate: true
---

## Hands-On with GitHub Copilot

Installation and configuration
- Installing the extension
- Setting up authentication
- Configuring settings
Sharing configuration across an organization
- Shared configuration templates (e.g., .copilot/settings.json) can be distributed across projects to standardize behavior.
https://www.codemag.com/Blog/AI/AIASD-install-guide

::: notes
Walk through installation, auth, and a quick coding session; encourage participants to follow along.
:::

---

## Lab: Getting Started with GitHub Copilot

Duration: Follow along
Objectives
Install and configure GitHub Copilot
Verify authentication with GitHub account
Explore the Copilot UI components
Activities
Install GitHub Copilot extension from VS Code marketplace
Sign in with your GitHub account (verify Copilot subscription)
Locate and explore:
- Chat window and chat history
- New chat button
- Quick chat feature (keyboard shortcut)
- Settings menu
- Model selection dropdown
Check your premium token usage bar
Create a new chat and experiment with the interface
Success Criteria
- Copilot extension installed and authenticated
- Can open/close chat windows
- Understand difference between main chat and quick chat
- Know where to find chat history

::: notes
## **Lab 1: Getting Started with GitHub Copilot**


**Duration:** 20-30 minutes
**Prerequisites:** VS Code installed


### Objectives


- Install and configure GitHub Copilot
- Verify authentication with GitHub account
- Explore the Copilot UI components


### Activities


1. Install GitHub Copilot extension from VS Code marketplace
2. Sign in with your GitHub account (verify Copilot subscription)
3. Locate and explore:
- Chat window and chat history
- New chat button
- Quick chat feature (keyboard shortcut)
- Settings menu
- Model selection dropdown
4. Check your premium token usage bar
5. Create a new chat and experiment with the interface


### Success Criteria


- Copilot extension installed and authenticated
- Can open/close chat windows
- Understand difference between main chat and quick chat
- Know where to find chat history
:::

---

## Prompt Specificity

Add error handling to my code
- Result: Generic response asking what type of errors, what language, what code?
Add error handling to my JavaScript function that calls an external API. I want to handle network timeouts, 404 errors, and JSON parsing failures. Return user-friendly error messages.
- Result: Better, but still generic without seeing actual code structure
@file:api-client.js Add comprehensive error handling to the fetchUserData function. Handle network timeouts (>5s), HTTP errors (404, 500, etc.), and JSON parsing failures.   Return user-friendly error messages that match our existing error format in @file:error-types.js
- Result: Specific implementation that matches existing code patterns*

---

## Lab: Understanding Context Management

Duration: Follow along
Objectives
Learn to add context using @ symbols
Understand context window limitations
Practice writing effective prompts
Activities
1. Basic Context Addition:
Use `@workspace` to search across your codebase
Use `@file` to reference specific files
Use `@terminal` to include terminal output in chat
Use `@vscode` to ask VS Code-specific questions
2. Prompt Practice:
Write a vague prompt, observe results
Rewrite with specific context, compare results
Add file references to improve accuracy
3. Context Window Experiment:
Start a long conversation in one chat
Notice when Copilot starts "forgetting" earlier context
Practice starting new chats for new topics
Success Criteria
Can use all @ context types
Understand when to start fresh chat sessions
Notice quality difference between vague and specific prompts

---

## Lab: Chat Management & Workflow

Duration: Follow along
Objectives
- Organize chat sessions effectively
- Use chat history for reference
- Develop efficient workflow patterns
Activities
1. Chat Organization:
- Review your chat history
- Identify chats that should have been separate sessions
- Practice starting new chats at appropriate times
2. Context Preservation:
- Start a focused chat for one feature
- Add relevant context systematically
- Complete task without context overflow
3. Quick Chat Practice:
- Use main chat for primary task
- Use quick chat for side questions
- Return to main chat without losing context
4. Chat History Review:
- Find and reference previous solutions
- Learn from past prompts that worked well
- Identify patterns in effective conversations
Success Criteria
- Chat history is organized and meaningful
- Can find and reference previous solutions
- Efficient workflow developed for using multiple chat windows
Context Window Management
- Remember from the session:
  - Context is a **limited resource**
  - Start new chat when changing focus areas
  - Keep conversations targeted and specific
  - When Copilot "forgets" earlier context, it's time for a new session

---

## Using Copilot in different modes

Ask Mode
- Simple prompt completion and inline suggestions
Edit Mode
- Automatic file edits
Agent Mode
- Perform actions on your behalf
Custom Modes
- Execute specific workflows

::: notes
Explain Ask vs Edit modes and when each is most useful. Speak to Agent Mode and Custom Chat Modes briefly. We’ll work with those later.
:::

---

## Lab: Exploring Copilot Modes

Duration: Follow along
Objectives
Understand differences between Ask, Edit, and Agent modes
Know when to use each mode
Understand premium token implications
Activities
1. Ask Mode:
Ask Copilot to explain a code snippet (no changes made)
Request multiple implementation approaches
Try different models and observe response quality
Note: This doesn't consume premium tokens for advanced models
2. Edit Mode:
Select code in a file
Ask Copilot to refactor it
Observe inline suggestions and changes
Accept or reject proposed changes
3. Agent Mode:
Ask Copilot to create a new file and add content
Request changes across multiple files
Have Copilot run terminal commands
Check premium token usage after agent actions
Success Criteria
Can distinguish when to use each mode
Understand token consumption differences
Successfully use agent mode for multi-file operations

---

## IDE Support for AI Assistance

IDE / Editor | Built-In AI Features | Supported AI Assistants | Strengths | Limitations
--- | --- | --- | --- | ---
VS Code | Deep AI integration through extensions; increasingly AI-first workflows | GitHub Copilot, Cline, ChatGPT-based extensions, Gemini integrations | Extremely flexible; huge ecosystem; top-tier AI support; widely adopted | Requires extension management; quality varies by plugin
Visual Studio (Windows) | Native GitHub Copilot integration; AI-powered IntelliCode | GitHub Copilot, IntelliCode | Strong enterprise + .NET support; excellent refactoring and debugging | Less flexible than VS Code for non-Microsoft stacks
JetBrains IDEs | JetBrains AI Assistant; code completion, refactoring, doc generation | JetBrains AI Assistant, GitHub Copilot | Deep static analysis + AI; strong multi-language support | JetBrains AI Assistant is subscription-based; Copilot integration not as seamless
Cursor IDE | AI-first editor; conversational coding; multi-file reasoning | Built-in AI models (GPT-based, Claude-based), Copilot alternatives | Designed for AI pair-programming; strong repo-wide reasoning | Not a traditional IDE; still maturing for large enterprise workflows
Replit | AI-powered Ghostwriter for code generation, debugging, and explanations | Ghostwriter | Great for beginners and rapid prototyping; browser-based | Less powerful for large, multi-module projects
Builder.io / Builder Code Editor | AI-enhanced coding environment with integrated assistants | Multiple AI integrations depending on setup | Strong web-dev focus; modern AI-native UX | Not a general-purpose IDE
Code-B Editors | Predictive code generation, debugging, and review | Multiple AI models depending on configuration | Strong AI-centric workflows; optimized for speed | Less mainstream; smaller ecosystem
Claude Code | Terminal-first AI coding assistant; autonomous repo-wide reasoning | Latest models from Anthropic and other via configuration | Exceptional multi-file context handling; ideal for agentic workflows and automated patching | Not a GUI IDE; best suited for terminal-centric development and large codebases
