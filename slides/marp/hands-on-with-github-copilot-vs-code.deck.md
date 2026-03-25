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

## Prompt Specificity

Add error handling to my code

- Result: Generic response asking what type of errors, what language, what code?
  Add error handling to my JavaScript function that calls an external API. I want to handle network timeouts, 404 errors, and JSON parsing failures. Return user-friendly error messages.
- Result: Better, but still generic without seeing actual code structure
  @file:api-client.js Add comprehensive error handling to the fetchUserData function. Handle network timeouts (>5s), HTTP errors (404, 500, etc.), and JSON parsing failures.   Return user-friendly error messages that match our existing error format in @file:error-types.js
- Result: Specific implementation that matches existing code patterns\*

::: notes
Duration ~00:04

**Delivery Instructions:**
This slide demonstrates the progression from terrible to excellent prompts—walk through each example deliberately.

**Example 1 (Bad):** "Add error handling to my code" - Read this with a slightly exasperated tone. Point out: What code? What language? What kind of errors? Copilot literally has no context to work with. This is like asking a contractor to "fix your house" with no other information.

**Example 2 (Better):** Read the second prompt and note improvements: specifies JavaScript, specifies function purpose (external API call), lists specific error types (network timeouts, 404, JSON parsing). But emphasize the problem: "still generic without seeing actual code structure." Copilot doesn't know your coding patterns, your existing error handling approach, or your project structure.

**Example 3 (Best):** Read the third prompt slowly, highlighting key improvements:

- Uses `@file:api-client.js` to reference specific file (Copilot can see the actual code)
- Names the exact function (`fetchUserData`)
- Provides precise timeout threshold (>5s, not just "timeouts")
- Lists specific HTTP codes (404, 500, etc.)
- References another file `@file:error-types.js` for consistency with existing patterns

**Key Teaching Point:** "The difference between prompt 1 and prompt 3 is the difference between Copilot asking YOU 10 clarifying questions versus Copilot just doing exactly what you need. Specificity saves time."

**Audience Interaction:** Ask: "How many of you have written prompts like example 1? Don't worry—we all start there. By the end of today, you'll be writing prompts like example 3 automatically."

**Transition:** "Now let's practice this in a hands-on lab where you'll learn to add context using @ symbols..."
:::

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
Explain Ask vs Edit modes and when each is most useful. Speak to Agent Mode and Custom Chat Modes briefly. We'll work with those later.
:::

---

<!-- layout: Two Content -->

## IDE Support for AI Assistance

**Established IDEs**

- **VS Code**
  Deep extension ecosystem with strong Copilot, Cline, ChatGPT, and Gemini support.
- **Visual Studio**
  Strong .NET refactoring, debugging, and native Copilot integration.
- **JetBrains IDEs**
  Excellent static analysis and multi-language depth; AI features are strong but more subscription-driven.
- **Cursor**
  AI-first editing experience with strong multi-file reasoning, but less mature for some enterprise workflows.

::: column

**Lightweight and Specialized Options**

- **Replit**
  Browser-based and beginner-friendly for rapid prototyping.
- **Builder.io / Builder Code Editor**
  Web-focused environment with modern AI-native workflows.
- **Code-B editors**
  Fast AI-centric editing, but with a smaller ecosystem.
- **Claude Code**
  Terminal-first, repo-wide reasoning and patching; powerful, but not a GUI IDE.

**Selection lens**

- GUI IDEs favor structured refactoring and debugging.
- AI-first tools favor conversational, agentic workflows.
- Team choice depends on stack, governance, and workflow fit.
