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
- Result: Specific implementation that matches existing code patterns\*
  ::: notes
  **Timing:** 3-4 minutes

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

::: notes
**Timing:** 15-20 minutes hands-on lab with instructor guidance

**Lab Introduction:**
"This is your first real hands-on practice with context management. Open VS Code and follow along—we'll work through this together."

**Activity 1: Basic Context Addition (5-7 minutes)**
Walk through each @ symbol type:

- **@workspace**: "Try typing @workspace and searching for a class or function name. Copilot will search your entire codebase."
- **@file**: "Type @file and start typing a filename. This gives Copilot the full content of that file—like handing someone a document before asking a question about it."
- **@terminal**: "If you've just run a command that failed, use @terminal to include the error output. Copilot can see the actual error messages and stack traces."
- **@vscode**: "Ask questions like '@vscode how do I change the theme?' or '@vscode what's the keyboard shortcut for...?' This tells Copilot you're asking about VS Code itself, not your code."

**Activity 2: Prompt Practice (5-7 minutes)**

- Have participants write a vague prompt first (like "optimize this function" without context)
- Show the generic result
- Then rewrite: "@file:myfile.js optimize the calculateTotal function for large datasets (1000+ items)"
- Compare the quality difference side-by-side
- Emphasize: "Same question, dramatically different results—just by adding context."

**Activity 3: Context Window Experiment (5 minutes)**

- "Start a chat and keep asking follow-up questions. After 10-15 exchanges, ask Copilot to reference something you said at the beginning."
- "Notice how Copilot might struggle or forget? That's context window limitations—the AI can only 'remember' a limited amount of conversation."
- **Key Teaching Moment:** "When you notice this happening, start a fresh chat. Don't try to fight a shrinking context window—just open a new session for the new topic."

**Common Pitfalls to Mention:**

- Forgetting to use @ symbols and then being disappointed with vague results
- Overloading one chat with too many unrelated questions
- Not realizing the context window is full (Copilot gets "forgetful")

**Success Check:**
Walk around (if in person) or ask participants to confirm:

- "Can everyone use @file to reference a specific file?" (Show of hands or chat confirmation)
- "Can everyone see the difference between a vague prompt and one with context?"

**Transition:** "Great work! Now that you understand context, let's talk about organizing your chat sessions for maximum efficiency..."
:::

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

::: notes
**Timing:** 15-20 minutes hands-on lab

**Lab Introduction:**
"Chat management might sound boring, but it's the difference between constantly fighting Copilot and having smooth, productive conversations. Let's build good habits now."

**Activity 1: Chat Organization (5 minutes)**

- **Review Chat History:** "Open your chat history panel. Look at the chats you've created so far today."
- **Identify Mistakes:** "Find a chat where you started asking about one thing (e.g., error handling) and then pivoted to something completely unrelated (e.g., database queries). That's a sign you should have started a new chat."
- **Practice New Chats:** "Rule of thumb: If you're changing topics, start a new chat. If it's a follow-up or refinement of the current topic, continue the same chat."
- **Example:** "Bad: One chat for 'implement login, fix CSS, add tests, refactor database layer.' Good: Four separate chats—each focused on one task."

**Activity 2: Context Preservation (5 minutes)**

- **Start Focused Chat:** "Pick ONE small feature to implement—something specific like 'add validation to the email field.'"
- **Add Context Systematically:** "Start with @file references for the relevant files. Don't dump the entire codebase—just the files you know are involved."
- **Track Progress:** "As you work through the task, keep the chat focused. If you finish and want to start something else, open a new chat."
- **Success Indicator:** "You'll know you're doing this right when you complete a task without Copilot forgetting earlier parts of the conversation."

**Activity 3: Quick Chat Practice (3-5 minutes)**

- **Main Chat = Primary Work:** "Open your main chat. Start working on a feature implementation."
- **Side Question = Quick Chat:** "While working, you might wonder: 'What's the VS Code shortcut for...?' or 'How does Array.prototype.reduce work?' Use Quick Chat (keyboard shortcut: show it on screen) for these side questions."
- **Return to Main:** "After getting your answer, close Quick Chat and continue in your main chat. Your main context is preserved."
- **Why This Matters:** "Quick Chat prevents your main chat from getting derailed by unrelated questions. Keeps your work chat focused and your question answered."

**Activity 4: Chat History Review (3-5 minutes)**

- **Find Previous Solutions:** "Go back to your chat history. Find a chat where Copilot gave you a good solution to a problem."
- **Learn from Past Prompts:** "Look at what YOU asked. What made that prompt work? Was it specific? Did you use @file references? Did you provide examples?"
- **Pattern Recognition:** "Over time, you'll notice: 'When I ask questions this way, I get better results.' That's your effective prompt pattern—document it, reuse it."

**Key Reminders (bottom of slide):**

- Point to "Context Window Management" bullets at the bottom
- **Context is Limited:** "Think of context like RAM—you have a fixed amount. Use it wisely."
- **New Chat = Fresh Start:** "When Copilot forgets earlier conversation, it's not broken—you've just hit the limit. Start fresh."
- **Targeted Conversations:** "One chat, one topic. Multi-tasking doesn't work in AI chats any better than it works for humans."

**Success Check:**
Ask participants:

- "Can everyone find their chat history panel?"
- "Did everyone successfully use Quick Chat without losing main chat context?"
- "Can you think of a time today where you should have started a new chat but didn't?"

**Transition:** "Now that you know how to manage conversations, let's look at the different MODES Copilot offers—Ask, Edit, and Agent modes..."
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

::: notes
**Timing:** 15-20 minutes hands-on lab

**Lab Introduction:**
"This lab is about understanding the differences between Copilot modes and—critically—when each mode consumes your premium tokens. Let's dive in."

**Activity 1: Ask Mode (5-7 minutes)**

- **Explain a Code Snippet:** "Open a file in your project. Select a function. Ask Copilot: 'Explain what this function does.' Copilot will analyze and explain—no code changes."
- **Request Multiple Approaches:** "Ask: 'Show me three different ways to implement this logic.' Copilot will provide alternatives in the chat without touching your files."
- **Model Selection:** "Try asking the same question with different models (e.g., GPT-4o vs Claude). Notice how responses differ in style, depth, and tone."
- **KEY POINT:** "Ask mode is read-only. No code changes = no risk. And here's the bonus: **Ask mode doesn't consume premium tokens** even when using advanced models. You can ask questions all day without worrying about token limits."

**Why Ask Mode is Powerful:**

- Safe exploration (no accidental code changes)
- Great for learning ("Explain this regex pattern")
- Perfect for brainstorming ("What are different ways to handle authentication?")
- Free premium model access for questions

**Activity 2: Edit Mode (5-7 minutes)**

- **Select and Refactor:** "Highlight a block of code. Ask Copilot: 'Refactor this to use async/await' or 'Extract this into a separate function.'"
- **Observe Inline Suggestions:** "Copilot will show proposed changes directly in your editor—highlighted text, additions, deletions."
- **Accept or Reject:** "You can accept the entire change, accept parts of it, or reject and try again. This is interactive editing."
- **Use Case:** "Edit mode is perfect for improving existing code: refactoring, renaming, restructuring, adding error handling, improving readability."

**When to Use Edit Mode:**

- You know exactly where the change needs to happen
- You're refining or improving existing code
- You want to see diffs before accepting changes

**Activity 3: Agent Mode (5-7 minutes)**

- **Create New File:** "Ask Copilot: 'Create a new file utils/validation.js and add email validation logic.' Copilot will create the file AND add content."
- **Multi-File Changes:** "Request: 'Update all my test files to use the new mocking library.' Copilot will scan your project, identify test files, and modify them."
- **Run Terminal Commands:** "Ask: 'Install the lodash package and add it to my imports.' Copilot can run `npm install lodash` for you."
- **Check Premium Tokens:** "After these actions, check your token usage bar (top of chat window). **Agent mode DOES consume premium tokens** because Copilot is taking actions on your behalf—creating files, running commands, making decisions."

**Agent Mode Power and Cost:**

- Can handle complex multi-step tasks autonomously
- Saves enormous time (one prompt → entire feature scaffolded)
- But: Uses premium tokens because it's doing real work
- Best for: scaffolding new features, bulk refactors, project setup

**Token Strategy Discussion:**

- "Think of Ask mode for learning and exploring (free premium)."
- "Use Edit mode for targeted changes (moderate token use)."
- "Save Agent mode for high-value complex tasks (premium tokens, totally worth it)."

**Success Check:**

- "Can everyone explain the difference between Ask and Agent mode?" (Ask: read-only, no tokens; Agent: takes action, uses tokens)
- "Did everyone successfully use Agent mode to create a file?"
- "Anyone hit token limits? Let's talk about managing usage."

**Common Question:** "Why does Agent mode use tokens but Ask mode doesn't?"
**Answer:** "Agent mode is actively doing work: analyzing your entire codebase, making decisions, creating files, running commands. That's expensive computation. Ask mode just answers questions based on what you show it—much simpler."

**Transition:** "Now that you understand the modes, let's look at the broader IDE landscape—what other tools offer AI assistance, and how does Copilot compare..."
:::

---

## IDE Support for AI Assistance

| IDE / Editor                     | Built-In AI Features                                                    | Supported AI Assistants                                              | Strengths                                                                                   | Limitations                                                                       |
| -------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| VS Code                          | Deep AI integration through extensions; increasingly AI-first workflows | GitHub Copilot, Cline, ChatGPT-based extensions, Gemini integrations | Extremely flexible; huge ecosystem; top-tier AI support; widely adopted                     | Requires extension management; quality varies by plugin                           |
| Visual Studio (Windows)          | Native GitHub Copilot integration; AI-powered IntelliCode               | GitHub Copilot, IntelliCode                                          | Strong enterprise + .NET support; excellent refactoring and debugging                       | Less flexible than VS Code for non-Microsoft stacks                               |
| JetBrains IDEs                   | JetBrains AI Assistant; code completion, refactoring, doc generation    | JetBrains AI Assistant, GitHub Copilot                               | Deep static analysis + AI; strong multi-language support                                    | JetBrains AI Assistant is subscription-based; Copilot integration not as seamless |
| Cursor IDE                       | AI-first editor; conversational coding; multi-file reasoning            | Built-in AI models (GPT-based, Claude-based), Copilot alternatives   | Designed for AI pair-programming; strong repo-wide reasoning                                | Not a traditional IDE; still maturing for large enterprise workflows              |
| Replit                           | AI-powered Ghostwriter for code generation, debugging, and explanations | Ghostwriter                                                          | Great for beginners and rapid prototyping; browser-based                                    | Less powerful for large, multi-module projects                                    |
| Builder.io / Builder Code Editor | AI-enhanced coding environment with integrated assistants               | Multiple AI integrations depending on setup                          | Strong web-dev focus; modern AI-native UX                                                   | Not a general-purpose IDE                                                         |
| Code-B Editors                   | Predictive code generation, debugging, and review                       | Multiple AI models depending on configuration                        | Strong AI-centric workflows; optimized for speed                                            | Less mainstream; smaller ecosystem                                                |
| Claude Code                      | Terminal-first AI coding assistant; autonomous repo-wide reasoning      | Latest models from Anthropic and other via configuration             | Exceptional multi-file context handling; ideal for agentic workflows and automated patching | Not a GUI IDE; best suited for terminal-centric development and large codebases   |
