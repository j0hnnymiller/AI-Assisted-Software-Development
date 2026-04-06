---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "github-copilot-skills-practical-introduction-20260321"
prompt: |
  create a marp deck explaining the following content:

  Below is a complete **Marp slide deck** (Markdown) with **Pandoc-style speaker notes** that synthesizes the *latest GitHub Copilot Skills documentation* based on the search results you requested.
  Citations appear where required.

started: "2026-03-21T21:05:53Z"
ended: "2026-03-21T21:20:53Z"
task_durations:
  - task: "slide outline"
    duration: "00:03:00"
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and catalog updates"
    duration: "00:03:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/github-copilot-skills-practical-introduction-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

﻿---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "welcome-back-slide-20260314"
prompt: |
  create a marp deck containing a slide welcoming attendees back. include a point for questions
started: "2026-03-14T15:46:54Z"
ended: "2026-03-14T15:47:00Z"
task_durations:
  - task: "draft"
    duration: "00:00:06"
total_duration: "00:00:06"
ai_log: "ai-logs/2026/03/14/welcome-back-slide-20260314/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Welcome Back || The Return of the Prompter

## Welcome Back to AI-Assisted Software Development

- Ready to continue where we left off
- Today's session builds on what we've covered
- We're all in this together — participation welcome
- **Questions are always welcome — ask anytime!**

::: notes
Duration ~00:02

Welcome everyone back to the session. Take a moment to let people settle in before diving into content. Acknowledge that it's great to see everyone back and express enthusiasm for the session ahead.

Key talking points:

- Remind attendees of the previous session's topics briefly
- Emphasize that questions are encouraged at any point — not just at the end
- Set a positive, inclusive tone for the session
- If this is after a break, give people 30 seconds to get re-focused

Transition: "Let's pick up right where we left off..."
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- **▶ Instructions vs Prompts vs Custom Agents**
- Managing Context
- Custom Agents
- Skills
- MCP

---

<!-- _class: lead -->

# Instructions vs Prompts vs Custom Agents

---

## Instructions vs Prompts vs Custom Agents

- What Are Custom Agents?

---

﻿---
marp: true
theme: default
paginate: true
---

# Comparing AI Development Approaches || Know Thy Copilot: Context, Artifacts, and Agent Files

---

## What Are Custom Agents?

Definition
  - Preconfigured AI personalities for specific domains
  - Combine behavioral rules with specialized knowledge
  - Provide contextual expertise for particular scenarios

Key Characteristics
  - Scope: Domain or role-specific interactions
  - Context: Rich background knowledge and constraints
  - Purpose: Act as specialized “AI expert” for conversations

---

## DevOps Engineer Custom Agent

Role: "Senior DevOps Engineer"

Expertise:
  - CI/CD pipelines
  - Infrastructure as Code
  - Container orchestration
  - Monitoring and observability

Behavior:
  - Focus on scalability and reliability
  - Recommend industry best practices
  - Consider security implications
  - Suggest automation opportunities

---

## Custom Agents: Use Cases

Perfect For:
  - Domain Expertise → Get specialized knowledge
  - Role-Playing → AI acts as specific professional
  - Context Switching → Different perspectives on same problem
  - Learning → Educational conversations with expert personas

Examples:
  - Security Architect Mode → Focus on security concerns
  - Database Expert Mode → Optimize data architecture
  - UX Designer Mode → Human-centered design guidance

---

## Comparison Matrix

| Aspect      | Instruction Files      | Prompt Files           | Custom Agents             |
| ----------- | ---------------------- | ---------------------- | ----------------------------- |
| Purpose     | Define AI behavior     | Execute specific tasks | Provide specialized expertise |
| Scope       | Repository-wide        | Single task/workflow   | Conversational context        |
| Persistence | Always active          | On-demand execution    | Session-based                 |
| Reusability | High (across projects) | High (task templates)  | Medium (role-specific)        |
| Complexity  | Simple rules           | Detailed procedures    | Rich contextual knowledge     |

---

## Layered Integration Approach

```mermaid
graph TD
    A["Instruction Files<br/>(Security Standards, Coding Rules)"] -->|Base Behavior| B["Prompt Files<br/>(Security Audit Template)"]
    B -->|Task Execution| C["Custom Agents<br/>(Security Architect Persona)"]
    C -->|Conversational Context| D["Result: Specialized Security Expert<br/>using standardized processes with<br/>consistent quality standards"]
```

---

## Real-World Integration Example

Scenario: Implementing User Authentication

Instruction Files provide:
  - Security coding standards
  - Testing requirements
  - Documentation standards

Prompt File executes:
  - “Implement OAuth2 Authentication System”
  - Step-by-step implementation guide

Custom Agents offers:
  - Security Architect expertise
  - Best practice recommendations
  - Threat modeling insights

---

## The Integration Advantage

When Used Together:

- Higher Quality: Consistent standards + structured execution + expert knowledge
- Greater Efficiency: Automated workflows with specialized guidance
- Better Outcomes: Comprehensive approach covers all development aspects
- Reduced Risk: Multiple layers of validation and expertise

Result: > AI becomes a true development partner, not just a code generator

---

<!-- _class: lead -->

## Course Modules

- Intro
- Instructions vs Prompts vs Custom Agents
- **▶ Managing Context**
- Custom Agents
- Skills
- MCP

---

<!-- _class: lead -->

# Managing Context

---

## Managing Context

- Managing GitHub Copilot Effectively

---

﻿---
marp: true
theme: default
paginate: true
---
# Managing GitHub Copilot Effectively || Fast, Eager, and Sometimes Confidently Wrong

## Managing GitHub Copilot Effectively

- Copilot is powerful, but not entirely autonomous
- Effective use requires structure, guardrails, and clear intent
- Treat Copilot as a developer whose output improves with guidance
- Your process determines the quality of its contributions

::: notes
This slide frames Copilot as a tool that amplifies engineering discipline rather than replacing it.

The message is: Copilot is not magic.

It's a reasoning engine that responds to structure, clarity, and context.

When managed well, it becomes a force multiplier.

When unmanaged, it becomes unpredictable.
:::

---

## A Managed Junior Developer

- Copilot is fast, eager, and sometimes confidently wrong
- Provide clear instructions, constraints, and examples
- Review everything - trust its speed, not its judgment
- Use iterative loops:
    instruct → generate → review → refine
- Give Copilot ownership of tasks, not architecture

::: notes
This analogy resonates with engineering teams.

Copilot behaves like a junior developer: capable, but lacking context and judgment.

It thrives when you give it structure and feedback.

It struggles when you ask it to “just figure it out.”

The more intentional your guidance, the more reliable its output becomes.
:::

---

## Prompt Engineering Best Practices

- Be explicit about goals, constraints, and success criteria
- Provide examples of the desired pattern or style
- Break large tasks into smaller, testable steps
- Use instruction files for stable rules and architectural boundaries
- Ask Copilot to explain its reasoning when correctness matters

::: notes
Prompting is not about clever phrasing – it's about clarity.

Copilot performs best when you define intent, boundaries, and examples.

Instruction files are especially powerful because they give Copilot a persistent “north star” for your codebase.

Think of prompts as design briefs, not commands.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Instructions vs Prompts vs Custom Agents
- Managing Context
- **▶ Custom Agents**
- Skills
- MCP

---

<!-- _class: lead -->

# Custom Agents

---

## Custom Agents

- Where to Create Custom Agents
- What Are Agents?
- Start Simple
- Controlling GitHub Copilot Files

---

﻿---
marp: true
theme: default
paginate: true
---

# Custom Agents Overview || The Org Chart Your AI Actually Respects

---

## Where to Create Custom Agents

GitHub.com
  - Navigate to github.com/copilot/agents
  - Available at repository, organization, or enterprise level
  - Template-based creation process

IDEs
  - VS Code: Configure Custom Agents menu
  - .github/agents/ directory for workspace agents

::: notes
Duration ~00:03

Delivery Instructions:

Show the GitHub.com interface if doing a live demo

Emphasize that agents created on GitHub can be used across all environments

IDE-based agents are more convenient for quick personal use

Key Decision Point: Help audience understand when to use each approach:

GitHub: For team-wide or shared agents

Organization/Enterprise: For standardized agents across multiple repos

IDE: For personal experimentation and workspace-specific agents

Technical Detail:

GitHub agents go in .github/agents/ directory

Organization/enterprise agents go in root agents/ directory of .github-private repo

IDE user profile agents are local to that machine

Common Question: “Can I use the same agent in both GitHub and my IDE?” Answer: Yes! Agents created on GitHub are automatically available in supported IDEs.

Transition: “Let's walk through creating an agent on GitHub, which is the most common workflow.”
:::

---

## Creating in VS Code

1. Open GitHub Copilot Chat
2. Agents dropdown → Configure Custom Agents…
3. Click Create new custom agent
4. Choose location:
  - Workspace: .github/agents/ (project-specific)
  - User profile: Personal agents (all workspaces)
5. Enter filename
6. Configure in .agent.md file
7. Use Configure Tools… button for tool selection
8. Set model: property for AI model preference

::: notes
Duration ~00:04

VS Code Advantages:

Integrated tool configuration UI

Immediate testing in the same environment

Better for rapid iteration and experimentation

User profile agents for personal productivity

Workspace vs User Profile Decision:

Workspace (.github/agents/):

Shared with team when committed

Project-specific context

Version controlled

Recommended for team agents

User Profile:

Available across all your projects

Not version controlled

Personal productivity tools

Examples: personal note-taking agent, time tracker

Configure Tools Button:

Opens visual dialog showing all available tools

Includes built-in tools (read, edit, search, etc.)

Shows MCP server tools if configured

Click OK to add selected tools to YAML

Model Property:

Override default model per agent

Useful for cost/performance tradeoffs

Example: Use faster model for simple tasks, advanced model for complex reasoning

Live Demo Suggestion: Show the Configure Tools dialog and model dropdown

Common Questions:

“Do I need to restart VS Code?” - No, agents are detected automatically

“Can I edit the YAML directly?” - Yes, the UI is just a helper

Transition: “The process is similar in JetBrains, Eclipse, and Xcode with slight UI variations. Now let's focus on what matters most: the agent configuration itself.”
:::

---

## Using Custom Agents

On GitHub.com
  - Agents panel/tab dropdown → Select your custom agent
  - Assign custom agent to issues
  - Noted in PR descriptions when used

In IDEs
  - Chat window dropdown → Select agent
  - Switch agents mid-conversation
  - Access specialized configurations per task

GitHub Copilot CLI
  - '/agent' command to select agent
  - Reference agent in prompts
  - Command-line argument support

::: notes
Duration ~00:05

GitHub.com Usage:

Agents Panel Workflow:

Open Copilot agents panel or tab

Click dropdown (currently shows “Coding Agent”)

Select your custom agent from list

Enter your prompt or task

Agent works within its configured scope

Issue Assignment:

Assign Copilot to an issue

Choose custom agent from dropdown

Agent follows its specialized instructions

Great for repetitive tasks (bug triage, documentation updates)

PR Tracking:

When Copilot creates a PR, it notes which agent was used

Helps with attribution and understanding the approach

Example: “This PR was created by @copilot using the test-specialist agent”

IDE Usage Benefits:

Mid-Conversation Switching:

Start with planning agent

Switch to implementation agent

Switch to review agent

Maintain conversation context

Task-Specific Workflows:

Use planning agent for architecture decisions

Use coding agent for implementation

Use test agent for test coverage

Use security agent for vulnerability review

Use doc agent for documentation

Example IDE Workflow:

User: "I need to add user authentication"
[Select implementation-planner agent]
Agent: Creates detailed plan with tasks

User: "Now implement the first task"
[Switch to coding agent]
Agent: Implements based on plan

User: "Add tests for this"
[Switch to test-specialist agent]
Agent: Creates comprehensive test suite

CLI Usage (Advanced):

Basic Agent Selection:

gh copilot /agent test-specialist "add tests for authentication"

In Prompts:

gh copilot "using security-reviewer, check this PR for vulnerabilities"

Via Arguments:

gh copilot --agent=doc-writer "document the API endpoints"

Best Practices:

Choose the Right Agent:

Match agent expertise to task

Don't use generic agent when specialized one exists

Provide Context:

Custom agents still need context

Reference files, requirements, constraints

Iterate:

Refine agent instructions based on results

Agents improve as you tune them

Document Usage:

Tell team which agents to use for which tasks

Include in CONTRIBUTING.md or team wiki

Common Scenarios:

Code Review: Use review agent on PRs

Legacy Refactoring: Use planning agent first, then coding agent

Documentation Sprint: Use doc agent across multiple files

Security Audit: Use security agent on entire codebase

Test Coverage Drive: Use test agent to fill coverage gaps

Transition: “Let's wrap up with some best practices and resources to help you get started.”
:::

---

﻿---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "vscode-agents-slides-20260206"
prompt: |
  create marp slides for the content on this page: https://code.visualstudio.com/docs/copilot/agents/overview
started: "2026-02-06T18:35:00Z"
ended: "2026-02-06T18:45:00Z"
task_durations:
  - task: "content analysis"
    duration: "00:03:00"
  - task: "slide structure design"
    duration: "00:02:00"
  - task: "slide creation with speaker notes"
    duration: "00:05:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2026/02/06/vscode-agents-slides-20260206/conversation.md"
source: "johnmillerATcodemag-com"
---

# VS Code Copilot Agents Overview || Agents: Copilot With a To-Do List

::: notes
Welcome to this presentation on VS Code Copilot Agents. This session will introduce you to the revolutionary concept of autonomous AI agents that can handle complete coding tasks end-to-end.

**Key delivery points:**

- Emphasize this goes beyond simple code suggestions
- Set expectations for a comprehensive overview
- Time allocation: 2-3 minutes introduction
- Engage audience with question: "Who has used basic GitHub Copilot suggestions?"

**Transition:** "Let's start by understanding what makes agents different from traditional AI assistance..."
:::

---

## What Are Agents?

Agents handle complete coding tasks end-to-end, not just suggestions

- **Understand** your project context
- **Make changes** across multiple files
- **Execute commands** and run tests
- **Adapt** based on results and feedback
- **Self-correct** when errors occur

::: notes
Duration ~00:04

This slide establishes the fundamental difference between agents and traditional AI assistance.

**Key talking points:**

- Traditional Copilot gives you code suggestions; agents perform complete workflows
- Example: Instead of suggesting a fix for a failing test, an agent will read the error, identify the root cause across files, update code, re-run tests, and commit changes
- Agents break down high-level tasks into actionable steps
- They use various tools autonomously to achieve objectives

**Audience engagement:** Ask "What's the most time-consuming coding task you do repeatedly?" to connect with real pain points.

**Transition:** "Now let's look at the different types of agents available..."
:::

---

## Four Types of Agents

| Type            | Environment           | Mode        | Collaboration |
| --------------- | --------------------- | ----------- | ------------- |
| **Local**       | Your machine          | Interactive | No            |
| **Background**  | Your machine (CLI)    | Autonomous  | No            |
| **Cloud**       | Remote infrastructure | Autonomous  | Yes (PRs)     |
| **Third-party** | Local or Cloud        | Varies      | Depends       |

::: notes
Duration ~00:05

This comparison table helps audience understand when to use each agent type.

**Key decision factors to explain:**

- **Interactive vs. Autonomous**: Do you need real-time feedback or can the agent work independently?
- **Collaboration**: Do team members need to be involved through PRs and issues?
- **Isolation**: How important is it to keep changes separate from your main workspace?
- **Task definition**: Is the task exploratory/ambiguous or well-defined?

**Visual aid reference:** Mention that VS Code documentation includes a helpful diagram showing these relationships.

**Transition:** "Let's dive deeper into each type, starting with local agents..."
:::

---

<!-- layout: two columns -->

## Local Agents: Interactive & Immediate

✅ **Strengths:**
  - Interactive chat interface
  - Full workspace access
  - All VS Code tools and extensions
  - Custom agent personas (reviewer, tester, etc.)
  - BYOK model support

::: column

❌ **Limitations:**
  - No team collaboration
  - Direct workspace modification
  - Requires active interaction

::: notes
Duration ~00:04

Local agents are perfect for brainstorming and tasks requiring immediate feedback.

**Use case examples to share:**

- Planning new features with back-and-forth discussion
- Debugging complex issues with stack traces
- Code reviews with immediate explanations
- Exploring architectural decisions

**Technical details:**

- Operates within VS Code's chat interface
- Sessions remain active even when chat is closed
- Can access MCP servers and extension-provided tools
- Works with all models available in VS Code

**Best practices:**

- Use for tasks that are not fully defined
- Great for learning and exploration
- Ideal when you need VS Code context (linting errors, test results)
:::

---

<!-- layout: two columns -->

## Background Agents: Autonomous Execution

✅ **Strengths:**
  - Non-interactive autonomous operation
  - Git worktree isolation
  - No workspace conflicts
  - Custom agent personas

::: column

❌ **Limitations:**
  - No real-time VS Code context
  - Limited to CLI-provided models
  - No MCP or extension tools
  - No team collaboration

::: notes
Duration ~00:04

Background agents excel at implementing well-defined plans without interrupting your workflow.

**Ideal scenarios:**

- Implementing a detailed feature specification
- Refactoring code based on clear requirements
- Batch processing multiple similar changes
- Proof-of-concept development

**Technical implementation:**

- Uses Git worktrees for isolation
- CLI-based execution (Copilot CLI)
- Can reuse workspace custom agents for personas
- Runs on local machine but separated

**Workflow tips:**

- Start with local agent for planning
- Hand off to background agent for implementation
- Use isolation to experiment safely

**Common pitfall:** Don't use for tasks requiring VS Code runtime context unless manually provided.
:::

---

<!-- layout: two columns -->

## Cloud Agents: Team Collaboration

✅ **Strengths:**
  - GitHub integration
  - Pull request collaboration
  - Remote infrastructure scaling
  - Partner agent options (Claude, Codex)
  - MCP server access in cloud

::: column

❌ **Limitations:**
  - No VS Code built-in tools
  - No local runtime context
  - Asynchronous only

::: notes
Duration ~00:05

Cloud agents bridge the gap between AI assistance and team collaboration workflows.

**Key collaboration features:**

- Copilot coding agent integrates with GitHub
- Can be assigned GitHub issues directly
- Creates pull requests for team review
- Supports @copilot mentions in issues/PRs

**Partner agents:**

- Alternative AI providers beyond GitHub Copilot
- Claude Agent with specialized commands
- OpenAI Codex integration
- Each brings unique capabilities

**Team workflow example:**

1. Local agent creates implementation plan
2. Background agent creates proof of concept
3. Cloud agent implements final version in PR
4. Team reviews and collaborates on the PR

**Transition:** "Let's see how these agents work together in practice..."
:::

---

## Agent Sessions Management

**Unified Chat View for all agent types**

- **Sessions List:** Recent activity, status, file changes
- **Hand-off Support:** Delegate between agent types
- **Organized View:** Compact or side-by-side modes
- **Status Indicators:** Unread messages, in-progress work
- **Archive/Delete:** Keep workspace organized

::: notes
Duration ~00:04

The sessions management is what makes the multi-agent workflow practical and organized.

**Key management features:**

- All sessions visible regardless of where they run
- Status indicators show unread messages and active work
- Can filter by status, type, or time period
- Archive completed sessions to reduce clutter

**Workflow demonstration:**

- Show how sessions persist when you close chat
- Explain filtering and search capabilities
- Mention workspace-scoped session lists

**Hand-off capabilities:**

- Critical feature for multi-stage workflows
- Full conversation history carries over
- Original session gets archived automatically
- Example: Local planning → Background implementation → Cloud team review

**UI modes:**

- Compact: Embedded in Chat view
- Side-by-side: Dedicated sessions panel
- Automatically adapts based on Chat view width
:::

---

## Creating Agent Sessions

**Multiple ways to start working with agents**

1. **New Session Dropdown** in Chat view
2. **Command Palette** commands (Ctrl+Shift+P)
3. **Welcome Page** quick access
4. **Direct Assignment** from TODO comments
5. **GitHub Integration** via issues and mentions

**Pro Tip:** Multiple sessions can run in parallel!

::: notes
Duration ~00:04

This slide covers the practical aspects of getting started with agents.

**Step-by-step flow:**

1. Open Chat view
2. Select "New Session" dropdown (+)
3. Choose agent type from dropdown
4. Start your task description

**Command Palette options to mention:**

- "Chat: New Chat Editor/Window" for local agents
- "Chat: New Background Agent" for CLI agents
- "Chat: New Cloud Agent" for GitHub integration
- Each creates session in chat editor

**Advanced features:**

- TODO comment assignment requires GitHub PR extension
- Can mention @copilot in GitHub issues
- Welcome page provides quick access to recent sessions

**Parallel sessions workflow:**

- Each agent session focused on different task
- Previous sessions remain active
- Switch between tasks via sessions list
- Great for multitasking developers
:::

---

## Review and Apply Changes

**Track and validate agent work**

- **File Change Statistics** in session details
- **Diff Editor** for individual files
- **Multi-file Diff** for complete review
- **Apply to Workspace** options
- **Branch Checkout** for cloud agents

::: notes
Duration ~00:04

This slide addresses a critical concern: how to safely review and integrate agent changes.

**Safety and control emphasis:**

- Agents don't automatically apply changes
- Full visibility into what was modified
- Granular control over which changes to accept
- Can review before applying to main workspace

**Review workflow:**

1. Session completes with change statistics
2. Select session to view details
3. Right-click files for individual diffs
4. Use "View All Changes" for comprehensive review
5. Apply selectively or all at once

**Different agent behaviors:**

- Local agents: Direct workspace integration
- Background agents: Worktree isolation, manual apply
- Cloud agents: Pull request workflow

**Best practices:**

- Always review before applying
- Test changes in isolation first
- Use PR workflow for team visibility
- Document significant changes
:::

---

## Hand-off Workflows

**Leverage each agent type's strengths**

```mermaid
graph TD
    A["Local Agent<br/>(Planning)"] -->|Hand-off| B["Background Agent<br/>(Implementation)"]
    B -->|Delegate| C["Cloud Agent<br/>(Team Review)"]
```

**Example:**
  Planning → Proof of Concept → Production Implementation

::: notes
Duration ~00:05

This slide demonstrates the power of agent collaboration and specialization.

**Complete workflow example:**

1. **Local agent:** Interactive brainstorming and planning
- Define requirements
- Explore architecture options
- Create detailed implementation plan

2. **Background agent:** Autonomous implementation
- Create multiple proof-of-concept variants
- Test different approaches
- Implement core functionality

3. **Cloud agent:** Team collaboration
- Create production-ready implementation
- Submit pull request
- Enable team review and feedback

**Hand-off mechanics:**

- Full conversation history carries over
- Context preserved across agents
- Original session archived automatically
- New session inherits all context

**Strategic benefits:**

- Play to each agent type's strengths
- Maintain development velocity
- Include team collaboration when needed
- Scale complexity appropriately

**Transition:** "Let's wrap up with key takeaways and next steps..."
:::

---

## Key Takeaways & Next Steps

**Getting Started:**
  - Enable agents in VS Code settings ('chat.agent.enabled')
  - Start with local agents for exploration
  - Try background agents for focused tasks
  - Use cloud agents for team collaboration

**Resources:**
  - [Agents Tutorial](https://code.visualstudio.com/docs/copilot/agents/agents-tutorial)
  - [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
  - [Background Agents Guide](https://code.visualstudio.com/docs/copilot/agents/background-agents)

::: notes
Duration ~00:04

This closing slide provides clear next steps and resources for continued learning.

**Immediate action items:**

1. Check VS Code settings to enable agents
2. Try creating a simple local agent session
3. Experiment with a real coding task
4. Explore the sessions management interface

**Learning path recommendations:**

- Start with local agents to understand the interface
- Progress to background agents for autonomous work
- Implement cloud agents for team workflows
- Create custom agents for specialized tasks

**Common setup issues:**

- Organization policies may disable agents
- Need to contact admin if functionality unavailable
- Ensure GitHub Copilot subscription is active
- Check extension requirements for full functionality

**Engagement closing:**

- Ask audience about their biggest coding time-wasters
- Suggest which agent type might help most
- Encourage experimentation and gradual adoption
- Offer to answer questions about specific use cases

**Follow-up suggestions:**

- Share documentation links via chat/email
- Schedule follow-up sessions for advanced topics
- Create team guidelines for agent usage
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-21"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-create-and-use-custom-agent-20260321"
prompt: |
  create a marp exercise deck that guides student in creating, and using a custom agent
started: "2026-03-21T23:35:00Z"
ended: "2026-03-21T23:50:00Z"
task_durations:
  - task: "exercise design"
    duration: "00:06:00"
  - task: "slide authoring"
    duration: "00:07:00"
  - task: "manifest and provenance updates"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/exercise-create-and-use-custom-agent-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Create and Use a Custom Agent || Exercise: Build the AI That Does Your Job (Just This One Task)

---

## Exercise: Create and Use a Custom Agent

**Objectives**
  - Create a repository-scoped custom agent file in '.github/agents/'
  - Configure a clear agent role, description, and tool scope
  - Use the agent in Copilot Chat to complete a targeted task

**Activities**
  1. Create: Add '.github/agents/test-specialist.agent.md' with frontmatter ('name', 'description', 'tools') and focused behavior instructions
  2. Refine: Tighten scope by clarifying what the agent should do and refuse, then save and re-open chat
  3. Use: Select the new custom agent in Copilot Chat and run a prompt such as “Review this feature and propose a test plan with unit and integration tests”

::: column

**Success Criteria**
  - Agent appears in Copilot Chat agent picker after file creation
  - Agent responses stay within the declared role and tool boundaries
  - Student receives a usable, structured output aligned to the prompt goal

::: notes
Duration ~00:25

Facilitate this as a role-scoping lab, not just a file-authoring task. Start by showing students that a custom agent is essentially a reusable behavioral contract: it combines role intent, tool limits, and execution style.

In Phase 1, have learners create '.github/agents/test-specialist.agent.md' with a concise description and explicit tools list. Encourage strong verbs and constraints, for example "analyze tests, propose coverage improvements, avoid production-code refactors unless asked".

In Phase 2, ask each student to improve one weak instruction in their agent definition. Typical improvements are adding refusal boundaries, output format requirements, or quality checks such as "include risks and assumptions".

In Phase 3, students activate the agent and run one practical prompt against current repo files. Debrief by comparing outputs from default mode versus custom agent mode, then discuss where the custom agent improved consistency and where additional refinement is needed.

Timing guidance: 8 minutes create, 7 minutes refine, 8 minutes run and compare, 2 minutes recap. Close by emphasizing iterative agent tuning and least-privilege tool access as core best practices.
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "best-practices-and-qa-custom-agents-20260321"
prompt: |
  create a marp deck explaining the following content:

  ## Section 6: Best Practices and Q&A (Duration: 00:51:00 - 00:56:00)

  ### Key Topics

  - Agent design best practices
  - Tool restriction strategies
  - Team collaboration considerations
  - Questions about agent capabilities

  ### Main Discussion Points

  #### Agent Design Best Practices (Recap)

  1. **Start Simple**: One agent per specific pain point
  2. **Define Clear Responsibilities**: Explicit scope and boundaries
  3. **Restrict Tools Appropriately**: Grant minimum necessary access
  4. **Refine Based on Usage**: Iterate and improve
  5. **Create Org/Enterprise Agents**: Share common tasks
  6. **Include Examples**: Show effective usage patterns
  7. **Validate Before Rollout**: Test behavior in production scenarios
started: "2026-03-21T21:34:40Z"
ended: "2026-03-21T21:49:40Z"
task_durations:
  - task: "slide outline"
    duration: "00:03:00"
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and catalog updates"
    duration: "00:03:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/best-practices-and-qa-custom-agents-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Custom Agent Best Practices || Your AI Agent Is Not a Swiss Army Knife

---

## Start Simple

- Create one agent for one specific pain point
- Avoid trying to solve every workflow with a single "super agent"
- Narrow scope makes behavior easier to predict and improve
- Simpler agents are easier to explain to teammates

```mermaid
flowchart LR
    A[Specific pain point] --> B[Single-purpose agent]
    B --> C[Clear usage]
    C --> D[Easier refinement]
```

::: notes
Duration ~00:01

Explain that simplicity is a force multiplier in agent design. When an agent has one clear job, users know when to use it, reviewers know how to evaluate it, and the team can improve it without destabilizing unrelated workflows.  Transition by showing how explicit boundaries reinforce that simplicity.
:::

---

## Define Clear Responsibilities

- State the agent's purpose explicitly
- Define what is in scope and what is out of scope
- Make responsibilities visible in the agent instructions
- Clear boundaries reduce surprising responses and misuse

**Good boundary question**

- "What should this agent refuse or defer?"

::: notes
Duration ~00:01

Frame this slide around predictability. An agent with clear responsibilities is easier for humans to trust because they know what kind of help it is supposed to give and what it should not attempt, which reduces accidental overreach and context drift.  Transition by moving to the related issue of tool access, because boundaries are not just instructional but operational.
:::

---

## Restrict Tools Appropriately

- Give the agent the minimum tools needed for its job
- Avoid broad tool access unless the workflow genuinely requires it
- Tool restrictions reduce accidental misuse and security exposure
- Least-privilege design keeps behavior aligned with agent intent

```mermaid
flowchart TB
    A[Agent purpose] --> B[Needed actions]
    B --> C[Minimum tool set]
    C --> D[Safer execution]
```

::: notes
Duration ~00:01

Explain that tool design is one of the strongest control surfaces available when building agents. If an agent only needs to read files and analyze code, then it should not also be able to perform broad write operations or run unrelated commands, because excess capability creates unnecessary risk.  Transition by showing that even good initial designs need improvement over time.
:::

---

## Refine Based on Usage

- Watch how people actually use the agent
- Look for recurring confusion, failure modes, or missing guidance
- Update instructions, examples, and tools based on real feedback
- Treat the first version as a starting point, not a final product

::: notes
Duration ~00:01

Make the point that real-world usage will reveal gaps that design-time reasoning will miss. Teams learn a lot from where users hesitate, where the agent responds too broadly, or where people keep asking for the same clarification, and those signals should drive iteration.  Transition by broadening from personal agents to team and organization sharing.
:::

---

## Share Common Work Through Org or Enterprise Agents

- Promote frequently used workflows into shared agents
- Use org or enterprise scope for common tasks across teams
- Shared agents improve consistency and reduce duplicated setup
- Team-wide agents should have stronger review and ownership

**Typical shared scenarios**
  - security review
  - documentation updates
  - testing guidance
  - implementation planning

::: notes
Duration ~00:01

Explain that some workflows are too common to reinvent team by team. When an organization sees repeated needs such as security review or testing guidance, a shared agent can provide a standardized starting point and reduce duplicated authoring effort across repositories.  Transition by showing how examples improve agent usability once an agent exists.
:::

---

## Include Examples and Validate Before Rollout

- Add example prompts or usage patterns to show what "good" looks like
- Test the agent in realistic production-like scenarios
- Validate both behavior and boundaries before broad adoption
- Roll out only after the team can predict how the agent responds

**Validation checklist**
  [ ] prompt examples work as expected
  [ ] tool access matches intended scope
  [ ] outputs are useful and consistent
  [ ] failure cases are acceptable

::: notes
Duration ~00:01

Close with the two practices that make rollout much safer: examples and validation. Examples help users invoke the agent correctly, while validation ensures the agent behaves well under realistic conditions, including edge cases and boundary conditions, before it is trusted more broadly.  Encourage the audience to treat agents like any other product capability that needs ownership, feedback, and quality checks.
:::

---

﻿---
marp: true
theme: default
paginate: true
---

# Controlling Copilot Instruction Files || Who's Allowed at the AI Dinner Table?

---

## Controlling GitHub Copilot Files

Understanding Context Submission in AI-Assisted Development

::: notes
Duration ~00:20

Welcome to this session on controlling GitHub Copilot instruction files. This is a critical topic for teams implementing AI-assisted development workflows, as understanding how instructions are submitted with every prompt is essential for maintaining consistency, reducing token costs, and ensuring the right context reaches your AI assistant.

Today we'll cover four key areas: how the automatic inclusion system works through the applyTo field, how prompt files interact with instructions, how agents affect instruction submission, and practical strategies for controlling your context.

This session assumes you're familiar with basic GitHub Copilot usage and have worked with instruction files before. If you haven't, we recommend reviewing the “Creating Instruction Files” session first.
:::

---

<!-- layout: Two Content -->

## Prompt Files: Reference, Don't Control

Prompt files execute tasks, but they do not control automatic instruction inclusion.

**CRITICAL**: All AI-generated artifacts MUST comply with '.github/instructions/ai-assisted-output.instructions.md'

::: column

**Key distinction**

- Can reference instruction requirements in prompt content
- Cannot decide which instructions auto-include
- The target file's 'applyTo' matching still determines automatic inclusion

::: notes
This is a common source of confusion, so let's clarify: prompt files and instruction files serve different purposes and work in different ways.

Prompt files are executable tasks - they're like scripts you run to accomplish specific goals. They contain the prompt text, expected deliverables, and requirements. When you execute a prompt file, you're asking the AI to perform a specific task following specific guidelines.

However, prompt files don't control the automatic inclusion of instruction files. What happens instead is:

You execute a prompt file (say, create-api.prompt.md)

The prompt content itself can mention or reference instruction files

The AI reads those references as part of the prompt

But the automatic inclusion of instruction files is still controlled by the applyTo patterns matching the files being created or modified

Here's a practical scenario: You run a prompt to create a new TypeScript API file. The prompt mentions that security instructions must be followed. The security.instructions.md file has applyTo: “\*/.ts”. When the AI creates the new .ts file:

The prompt content enforces the requirement

The applyTo pattern causes automatic inclusion

Both work together, but through different mechanisms

Think of it this way: Prompt files are the “what to do”, instruction files are the “how to do it”, and applyTo patterns are the “when to apply the how”.

The prompt metadata can specify output paths, which helps the system know what file types to expect and therefore which instructions might become relevant, but it's still the applyTo matching that does the heavy lifting.
:::

---

<!-- layout: Two Content -->

## Agents: Persona, Not Pattern Control

Agents create specialized context, not instruction filters.

'.github/agents/security-analyzer.agent.md'

Focus: Code security, vulnerability detection

::: column

**Interaction model**

- File being edited determines 'applyTo' matches
- Matching instructions are auto-included first
- Active agent then adds persona and workflow guidance
- Final response uses both the matched instructions and the agent persona

::: notes
Agents are often misunderstood as another way to control instruction inclusion, but they actually serve a different purpose. Let's clarify their role in the context submission system.

Agents create specialized AI personas with domain expertise. When you activate an agent, you're essentially telling the AI “act as a security expert” or “act as a documentation specialist”. The agent defines:

The role and mission of the AI

Core areas of expertise

Communication style and tone

Specialized commands or workflows

Response formatting preferences

But here's the key: agents don't override or control the applyTo pattern matching system. Instead, they layer on top of it. Let's walk through the flow:

You're editing a TypeScript file (src/auth.ts)

applyTo patterns are evaluated - security.instructions.md matches

The security instructions are auto-included in context

You have the “Security Analyzer” agent active

The agent persona is added to the context

The AI now has: the file, the security instructions, AND the security expert persona

The diagram shows this flow. The file type drives instruction inclusion through pattern matching, and the agent adds a specialized persona layer on top. They're complementary, not competitive.

A practical benefit: You could have security instructions that are very technical and rule-based, while the security analyzer agent adds conversational expertise and interactive commands. The instructions say “what to check”, the agent says “how to explain findings”.

One important note: If your agent references specific instruction files in its content, those references work like any other reference - they become part of the conversation, but they don't change the automatic inclusion patterns.
:::

---

## The Control Hierarchy

Understanding the complete context assembly

```mermaid
graph TD
    A["1. File Being Edited<br/>(e.g., src/api.ts)"]
    B["2. Instruction Files<br/>(applyTo pattern matching)"]
    C["3. Active Agent<br/>(adds persona/context)"]
    D["4. Prompt Files<br/>(reference additional instructions)"]
    E["5. Manual @-mentions<br/>(explicit instruction references)"]

    A --> B
    B --> C
    C --> D
    D --> E

    style A fill:#e1f5ff
    style B fill:#f3e5f5
    style C fill:#ffe0b2
    style D fill:#f1f8e9
    style E fill:#ffe0e0
```

::: notes
Now let's bring it all together with the complete control hierarchy. This shows the order in which different elements contribute to the context that gets submitted with your Copilot prompts.

Level 1: The Foundation - The File Being Edited Everything starts with the actual file you're working on. This could be a file you have open, a file you're creating, or files you reference in conversation. This establishes the base context and triggers the pattern matching system.

Level 2: Automatic Layer - Instruction Files Based on the file from level 1, the system evaluates all applyTo patterns in your instruction files. Every instruction file whose pattern matches your current file is automatically included. This happens silently in the background - you don't see it, but it's there. This is the primary control mechanism we've been discussing.

Level 3: Persona Layer - Active agent If you have a agent active, its persona definition, methodology, and guidelines are added to the context. This doesn't replace the instructions from level 2, it augments them. Think of this as the “personality” that interprets and applies the technical instructions.

Level 4: Task Layer - Prompt Files When you execute a prompt file, its content becomes part of the conversation. Any references to instruction files in the prompt text are processed. The prompt often specifies what type of output to create, which can trigger additional applyTo matching for the target files.

Level 5: Explicit Layer - Manual @-mentions Finally, you can always manually reference specific instruction files using @-mentions in your chat. This overrides the automatic system - if an instruction file doesn't have an applyTo match but you @-mention it, it gets included anyway.

Understanding this hierarchy helps you:

Debug why certain instructions aren't being applied

Optimize token usage by avoiding redundant inclusion

Design better instruction file patterns

Structure your workflow for maximum efficiency

Pro tip: Use levels 1-2 for 90% of your work (file-driven automatic inclusion), level 3 for specialized domains (agents), and levels 4-5 for exceptional cases (specific tasks or overrides).
:::

---

## Practical Control Strategies

Four approaches to managing instruction context

Strategy | Use Case | Example
--- | --- | ---
Specific Patterns | Domain-specific guidance | src/**/\*.ts for backend TypeScript
No applyTo | Manual inclusion only | Docs that need explicit opt-in
Global with Overrides | Base + specialized | **/\* + specific overrides
Directory Isolation | Project sections | frontend/** vs backend/**

::: notes
Let's conclude with four practical strategies you can use to manage instruction context effectively. These are patterns we've seen work well in real development teams.

Strategy 1: Specific Patterns (Recommended for Most Cases) Use precise glob patterns that match only the files where instructions are relevant. For example, if you have vertical slice architecture instructions, apply them only to your backend code: “src/backend/\*/.{cs,ts,py}”. This keeps your context clean and focused. It also reduces token costs since irrelevant instructions aren't included.

When to use: This should be your default strategy. Be specific about where instructions apply. Think about the actual files developers will be editing and match those patterns.

Strategy 2: No applyTo Field (For Specialized Use) Some instruction files shouldn't automatically include anywhere. These are typically:

Very specialized instructions that rarely apply

Experimental guidelines you're testing

Documentation that needs explicit consent to follow

Instructions with high token costs that should be opt-in

When to use: For instructions that might cause confusion if automatically included, or that are so specialized that automatic inclusion would rarely be appropriate. Developers must @-mention these explicitly.

Strategy 3: Global with Overrides (Advanced) Start with global instructions that apply everywhere (like AI provenance requirements), then create more specific instruction files that override or extend them for particular domains. For example:

ai-assisted-output.instructions.md: applyTo: “\*/”

ai-assisted-code-output.instructions.md: applyTo: “\*/.{code}” The more specific file can provide additional requirements that layer on top of the global ones.

When to use: When you have a base set of universal requirements but need domain-specific extensions. Be careful not to create conflicting instructions.

Strategy 4: Directory Isolation (For Large Projects) In large monorepos or projects with distinct sections, isolate instructions by directory. Frontend, backend, mobile, docs, infrastructure - each gets its own instruction files with directory-specific patterns. This prevents cross-contamination of concerns.

When to use: Projects with clear architectural boundaries, multi-team codebases, or when different parts of your system have fundamentally different requirements.

Implementation tip: Document your strategy in your repository's README so the team understands the pattern matching approach you're using. Include examples of which files trigger which instructions.

Remember: You can see which instructions are active by checking the Copilot context window or by asking Copilot “which instruction files are currently active?”
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Instructions vs Prompts vs Custom Agents
- Managing Context
- Custom Agents
- **▶ Skills**
- MCP

---

<!-- _class: lead -->

# Skills

---

## Skills

- GitHub Copilot Skills

---

# GitHub Copilot Skills: A Practical Introduction || Skills: The API for Telling Copilot How to Think

---

## GitHub Copilot Skills

>What They Are, How to Define Them, and How They Change Copilot's Behavior

::: notes
Introduce this deck as a practical orientation to Copilot Skills rather than a deep internal architecture lecture. Explain that skills are useful because they turn repeated workflow knowledge into reusable repository assets that Copilot can load when a task matches. Spend about one minute here setting expectations that the session will cover what skills are, how they are structured, and why they meaningfully change Copilot behavior. Transition by defining the concept clearly before getting into authoring details.
:::

---

## What Are Copilot Skills?

- Self-contained capability modules for specialized tasks
- Stored as folders with instructions, scripts, examples, and resources
- Loaded automatically when Copilot determines they are relevant
- Intended for repeatable, domain-specific workflows
- Can be used across Copilot-compatible environments

**Typical environments**
  - GitHub Copilot in VS Code
  - GitHub Copilot CLI
  - GitHub Copilot coding agent
  - other skills-compatible agents

::: notes
Explain that skills are best thought of as capability bundles rather than plain prompt snippets. Unlike generic instructions, they package the guidance, assets, and procedural knowledge needed for a repeatable class of work such as testing, migration, or auditing. Spend about one minute here and stress that automatic loading is the key feature because Copilot decides when the skill is relevant instead of requiring manual activation every time. Transition by showing why that matters operationally.
:::

---

## Why Skills Exist

- Reduce repeated explanation of domain workflows
- Store procedural knowledge in portable, version-controlled form
- Support multi-step, tool-assisted, or script-assisted tasks
- Encode team guardrails and best practices
- Allow multiple skills to contribute to complex workflows

::: notes
Frame this as a response to the institutional knowledge problem. Teams often repeat the same long background prompts over and over, and skills give them a way to store that knowledge once so Copilot can reuse it when needed. Spend about one minute here and point out that version control and reviewability make skills much safer and more maintainable than ad hoc copy-pasted prompt text. Transition by showing what the file and folder structure actually looks like.
:::

---

## Skill Folder Structure

A typical skill folder:

```
.github/
  skills/
    webapp-testing/
      SKILL.md
      scripts/
      examples/
      resources/
```

'SKILL.md' is the required entry point.

::: notes
Explain that the structure is intentionally simple so teams can add skills without introducing a new toolchain. The folder name becomes the skill name, while 'SKILL.md' acts as the main definition file that tells Copilot what the skill is for and how to execute it. Spend about one minute here and mention that the extra folders are optional but powerful because they let teams attach automation, examples, and reusable references. Transition by opening up the contents of 'SKILL.md'.
:::

---

## Anatomy of 'SKILL.md'

Minimal example:

```yaml
---
name: webapp-testing
description: >
  Assists with web application test strategies and automated test creation.
  Use for topics related to testing, test, E2E.
---
```
```markdown
## Procedure
  1. Analyze the target code and determine testing strategy
  2. Create test files following the AAA pattern
  3. Run tests and verify results
```

::: notes
Walk through the two main parts of the file: metadata and procedure. The metadata helps Copilot decide when the skill is relevant, while the procedure gives Copilot a step-by-step execution path once the skill has been loaded. Spend about one minute here and reinforce that the more concrete and deterministic the procedure is, the more reliable the resulting behavior becomes. Transition by explaining how Copilot decides to bring the skill into context in the first place.
:::

---

## How Copilot Loads Skills

Copilot loads a skill when:
  - the prompt matches the skill name, keywords, or description
  - the task aligns with the defined procedure
  - the agent judges the skill to be relevant to the current goal

When loaded:
  - the instructions are injected into context
  - Copilot follows the procedure
  - scripts or resources can be used as part of the workflow

::: notes
Clarify that skill loading is semantic rather than manual. If a prompt asks for end-to-end testing, a testing-related skill may be loaded automatically because its metadata and procedure align with that request, and multiple skills may be combined when more than one is relevant. Spend about one minute here and emphasize that this selective loading improves focus while avoiding the cost of always including every possible instruction. Transition by showing how that changes Copilot's actual behavior.
:::

---

<!-- layout: two-column -->

## How Skills Change Copilot's Behavior

1. Procedural behavior
  - Copilot follows the skill's steps to produce more consistent results.
2. Expanded capabilities
  - Skills can bring in:
    - scripts
    - templates
    - examples
    - domain-specific rules

::: column

3. Context efficiency
  - Only relevant skills load, keeping context smaller and more focused.

::: notes
Make the point that skills are operational playbooks, not style guides. They push Copilot away from open-ended reactive generation and toward more structured execution, especially when the task involves repeatable steps, tools, or examples. Spend about one minute here and explain that the context-efficiency angle matters because only the relevant capability modules are loaded instead of everything at once. Transition by comparing skills to other Copilot customization mechanisms.
:::

---

## Skills vs. Other Copilot Instruction Mechanisms

| Mechanism               | Purpose                               | Scope          | When to Use                                            |
| ----------------------- | ------------------------------------- | -------------- | ------------------------------------------------------ |
| **Custom Instructions** | General behavior & preferences        | Global         | Coding style, tone, conventions                        |
| **Promptfiles**         | Task-specific instructions            | Repo or folder | Reusable prompts for common tasks                      |
| **Chat Modes**          | Custom agents                         | Repo           | Role-based behavior (e.g., "Security Reviewer")        |
| **Skills**              | Procedural, domain-specific workflows | Repo           | Repeatable tasks requiring steps, scripts, or examples |

::: notes
Explain that skills complement the other instruction layers rather than replacing them. Custom instructions shape broad behavior, promptfiles package reusable requests, and chat modes define role-oriented interaction, while skills are the mechanism specifically designed for procedural workflows that need steps and attached resources. Spend about one minute here and transition by making the jump from concept to actual creation.
:::

---

## Best Practices for Skill Authoring

- Use **clear, imperative steps** ("Do X, then Y")
- Keep procedures **short and deterministic**
- Include **examples** for complex tasks
- Use **scripts** for repeatable automation
- Add **keywords** in the description for better relevance matching
- Test skills by prompting Copilot with expected triggers

::: notes
Think of skills as operational recipes. The more deterministic and unambiguous the steps, the more reliable Copilot becomes. Spend about one minute here and frame these as reliability practices rather than stylistic preferences so the audience understands that skill quality directly affects execution quality. Transition by grounding the idea in real-world categories of work.
:::

---

## Real-World Use Cases

- Test generation and automation
- Code migrations
- Security scanning workflows
- Documentation generation
- Data pipeline validation
- Infrastructure provisioning patterns
- Compliance checklists
- Onboarding workflows

::: notes
Explain that skills are most valuable when a task is procedural, repeatable, and specific to a team's domain. These examples all share the property that there is a known workflow, supporting material, and a need for consistent execution, which is exactly where skills outperform generic chat guidance. Spend about one minute here and transition by closing with the main takeaways the audience should remember.
:::

---

<!-- layout: two-column -->

## Exercise: Create Your First Skill

Objective
  - Author and commit a working Copilot skill to your repository.

Activities
  1. Create the folder structure

```bash
mkdir -p .github/skills/my-skill
```

  2. Create 'SKILL.md' with required sections
  - Add the following to '.github/skills/my-skill/SKILL.md':
    - YAML metadata (name, description, keywords)
    - Clear description of the skill's purpose
    - Numbered procedure steps (imperative, deterministic)
    - Optional examples or attached scripts

::: column

  3. Commit and test

```bash
git add .github/skills/my-skill/
git commit -m "Add my-skill"
```

Prompt Copilot with a task matching your skill's keywords. Verify it loads correctly.

Success Criteria
  - Skill folder exists in '.github/skills/'
  - 'SKILL.md' contains all required sections
  - Changes are committed to your branch
  - Copilot recognizes and applies the skill in relevant conversations

::: notes
This is a hands-on exercise. Give participants 10–15 minutes to complete it. Walk around and help with questions. Emphasize that skills are version-controlled artifacts and should go through normal code review. The success criteria ensure they've met the baseline for a functional skill.
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-create-and-use-custom-skill-20260321"
prompt: |
  create a marp exercise deck that guides student in creating, and using a custom skill
started: "2026-03-21T23:40:00Z"
ended: "2026-03-21T23:55:00Z"
task_durations:
  - task: "exercise design"
    duration: "00:06:00"
  - task: "slide authoring"
    duration: "00:07:00"
  - task: "manifest and provenance updates"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/exercise-create-and-use-custom-skill-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Create and Use a Custom Skill || Exercise: Teach Your AI a New Trick

---

## Exercise: Create and Use a Custom Skill

**Objectives**
  - Create a repository skill folder under '.github/skills/'
  - Author a 'SKILL.md' file with a clear description and step-based procedure
  - Use Copilot with a matching prompt so the new skill can guide a real task

**Activities**
  1. Create: Add '.github/skills/slide-quality-check/SKILL.md' with metadata ('name', 'description') and a short procedure for reviewing Marp slides for provenance and speaker notes
  2. Refine: Improve the skill by adding strong trigger words such as 'Marp', 'slide', 'speaker notes', and 'provenance', then tighten the procedure so the output is deterministic
  3. Use: Prompt Copilot with a task such as 'Review slides/marp/exercise-create-and-use-custom-agent.deck.md for slide metadata and ::: notes compliance' and compare the output to a normal untuned chat response

**Success Criteria**
  - Skill folder and 'SKILL.md' exist in '.github/skills/slide-quality-check/'
  - Copilot responds with a workflow aligned to the skill procedure instead of a generic answer
  - Student receives a structured review that checks metadata, notes coverage, and suggested fixes

::: notes
Duration ~00:25

Facilitate this as a procedural-workflow lab, not just a markdown-file exercise. Start by explaining that a skill is different from a custom agent: the agent shapes role behavior, while the skill packages a repeatable method Copilot can load when the prompt matches the description.

In Phase 1, have learners create '.github/skills/slide-quality-check/SKILL.md' with a simple but concrete purpose. Encourage them to write a description that contains likely trigger phrases and a procedure with explicit steps such as inspect front matter, verify every slide has '::: notes', and report missing or weak sections.

In Phase 2, ask students to improve the skill after reading it once as if they were Copilot. Typical improvements are sharper trigger words, more deterministic steps, and output requirements such as 'return findings as pass/fail bullets with suggested fixes'.

In Phase 3, students run a prompt against an existing slide file and see whether Copilot behaves like it has loaded the skill. If the response is too generic, coach them to adjust either the prompt wording or the skill description so the relevance match is stronger.

Timing guidance: 8 minutes create, 7 minutes refine, 8 minutes use and compare, 2 minutes recap. Close by emphasizing that strong skills are concise, keyword-aware, and procedural enough to produce repeatable results without bloating every chat.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Instructions vs Prompts vs Custom Agents
- Managing Context
- Custom Agents
- Skills
- **▶ MCP**

---

<!-- _class: lead -->

# MCP

---

## MCP

- MCP: Model Context Protocol Servers

---

﻿---
ai_generated: true
model: "anthropic/claude-sonnet-4-5@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "mcp-model-context-protocol-servers-20260321"
prompt: |
  Merge three MCP slide decks (mcp-model-context-protocol-servers.md,
  mcp-servers-vscode-copilot.md, mcp-servers.md) into one authoritative deck.
  Use mcp-model-context-protocol-servers.md as the base, inject the hands-on
  install, Copilot integration sequence diagram, secure config, and exercise
  slides from the PPTX-extracted sources, and enhance the architecture slide
  with the Mermaid diagram from mcp-servers-vscode-copilot.md.
started: "2026-03-21T22:30:00Z"
ended: "2026-03-21T22:45:00Z"
task_durations:
  - task: "comparison and merge planning"
    duration: "00:05:00"
  - task: "slide authoring"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/mcp-model-context-protocol-servers-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Model Context Protocol Servers || Giving Your AI a USB Hub

---

## MCP: Model Context Protocol Servers

- Connect Copilot to databases, APIs, infrastructure tools, and custom systems
- Built on a standardized protocol so any tool can speak to Copilot

::: notes
Duration ~00:15

Open by framing MCP as Copilot's extensibility layer beyond the repository. Copilot is already powerful for code in a repo, but many real workflows require reaching outside that boundary: querying a database, checking infrastructure state, or pulling from an internal API. MCP is the standard that makes all of those integrations possible.

Transition: "Let's start with what MCP actually is."
:::

---

## What Is MCP?

- **Model Context Protocol** is a standardized communication layer between Copilot and external services
- Adds capabilities and data sources that Copilot cannot access on its own
- Any tool or service that speaks MCP can be connected to Copilot
- A large and growing library of community-built servers already exists
- Key mindset: **configure and consume** — not build from scratch

```mermaid
flowchart LR
    A[GitHub Copilot\nClient]:::blue -- MCP Protocol --> B[MCP Server]:::green
    B -- Resources --> A
    B -- Tools --> A

    classDef blue fill:#4A90E2,stroke:#333,color:#fff
    classDef green fill:#50C878,stroke:#333,color:#fff
```

::: notes
Duration ~00:02

Explain MCP as an open protocol rather than a proprietary plugin system. The key idea is standardization: any team can build a server that exposes data or capabilities to Copilot using the same protocol, which means the ecosystem grows without waiting for first-party integrations.

MCP servers are like npm packages — install and use. Configuration is simple JSON — no coding required.

Examples:

- GitHub MCP Server: Access repos and issues
- Postgres MCP Server: Query your database
- Filesystem MCP Server: Safe file access for Copilot
- Slack MCP Server: Read channels and messages

Transition: "Let's look at the architecture in detail."
:::

---

<!-- layout: Two Content -->

## Architecture: Five Components

```mermaid
graph TB
  A[VS Code<br/>Copilot<br/>Client] <-->|JSON-RPC| B[MCP Server<br/>Transport Layer]
  B <-->|Protocol| C[Resources<br/>Files, APIs,<br/>Databases]
  style A fill:#0078d4,color:#fff
  style B fill:#68217a,color:#fff
  style C fill:#107c10,color:#fff
```

::: column

**Components**
- **Client** — VS Code / GitHub Copilot sends requests
- **Server** — MCP server provides capabilities and data
- **Protocol** — standard message format between both sides
- **Resources** — data exposed to Copilot
- **Tools** — callable functions the server permits

::: notes
Duration ~00:03

Walk through each component methodically. The client is already familiar — VS Code with Copilot enabled. The server is what you install. The protocol is what makes them interoperable. Resources are data that can be read into context; tools are actions that Copilot can invoke on behalf of the user.

Consumer focus: think "install and configure" not "build and deploy" — like VS Code extensions from the marketplace.

Transition: "Let's see why you'd want MCP in your workflow."
:::

---

## Use Cases

**External Data Access**
  - Query live databases and include results in Copilot's context
  - Pull from internal APIs or documentation systems

**Tool Integration**
  - Control infrastructure tools like Terraform or Kubernetes directly from the editor
  - Interact with cloud provider APIs without leaving VS Code

**Custom Solutions**
  - Build a server for proprietary internal systems
  - Expose institutional data that no public server covers

::: notes
Duration ~00:01

Use this slide to show why MCP matters in practice. The most compelling cases are often ones where the developer needs real state that lives outside the repo: the current schema of a production database, the live status of a Kubernetes deployment, or data from an internal system.

Encourage the audience to think about what data sources or tools they access repeatedly that could be connected to Copilot through an MCP server.

Transition: "Let's look at what servers are available today."
:::

---

## Available Pre-Built Servers

- **GitHub Repos** — repository metadata, issues, pull requests
- **Database Systems** — Postgres, MySQL, SQLite, MongoDB
- **Terraform** — infrastructure state and plan output
- **Kubernetes** — cluster status and resource inspection
- **Cloud Provider APIs** — AWS, Azure, GCP integrations
- **Web & APIs** — REST, GraphQL, browser automation (Puppeteer)

> Community-maintained libraries add new servers regularly

::: notes
Duration ~00:01

Emphasize that you do not need to build a server to benefit from MCP. Most common integration points already have a server available.

Specific package names to mention:

- @modelcontextprotocol/server-github — Full GitHub integration
- @modelcontextprotocol/server-postgres — Direct database queries
- @modelcontextprotocol/server-filesystem — Workspace file access
- @modelcontextprotocol/server-brave-search — Web search integration
- @modelcontextprotocol/server-puppeteer — Browser automation

The infrastructure-focused servers — Terraform and Kubernetes — tend to generate the most interest in DevOps or platform engineering teams.

Transition: "Now let's find the right server for your needs."
:::

---

## Finding MCP Servers

**VS Code Extension Gallery**
  - Search 'MCP' in the extensions panel
  - Read the description to confirm what resources and tools are exposed

**Model Context Protocol Website**
  - 'modelcontextprotocol.io' — canonical registry and documentation

**GitHub Community Repository**
  - 'github.com/modelcontextprotocol/servers' — community-maintained collection with usage examples

::: notes
Duration ~00:01

Make this actionable. The VS Code extension gallery is the fastest entry point because it is already open. The MCP website is the authoritative source for documentation and the full server registry.

Suggest that attendees check the extension gallery for the tool they care most about as a next-step exercise.

Transition: "Let's install your first MCP server."
:::

---

<!-- layout: Two Content -->

## Copilot + MCP Integration

**Enhanced capabilities**
  - **Context-aware completions** — access project-specific patterns
  - **Tool use** — Copilot can invoke server tools on your behalf
  - **Security boundaries** — controlled, audited resource access

::: column

```mermaid
sequenceDiagram
  participant Dev as Developer
  participant Copilot as GitHub Copilot
  participant MCP as MCP Server
  participant Res as Resources

  Dev->>Copilot: "Create user auth"
  Copilot->>MCP: Request context
  MCP->>Res: Fetch schema, patterns
  Res-->>MCP: Return context
  MCP-->>Copilot: Structured context
  Copilot-->>Dev: Code matching your patterns
```

::: notes
Duration ~00:04

Emphasize the "before and after" — without MCP, completions are based only on training data. With MCP, completions match YOUR codebase patterns.

Examples:

- Database connection: MCP provides your actual schema and connection pattern
- API calls: MCP shares your error handling approach
- Testing: MCP provides your test framework and fixture patterns

Security note: MCP servers can implement rate limiting. Audit logs track what context was provided. The permission model prevents unauthorized access.

Transition: "Let's talk about configuring these safely."
:::

---

<!-- layout: Two Content -->

## Configuring Servers Securely

**Security checklist**
  - Use environment variables for credentials
  - Grant minimum necessary permissions
  - Review server source before installing
  - Configure allowed paths and resources explicitly
  - Never use admin credentials when reader access is sufficient

::: column

**Best practices**
  - Start with read-only servers
  - Use scoped tokens such as 'repo:read'
  - Enable only the capabilities you actually need
  - Test in non-production first
  - Keep servers updated

::: notes
Duration ~00:04

Security from the consumer perspective — this is all about what YOU control in configuration.

Good config examples:

// Good: Scoped GitHub token
"env": { "GITHUB_TOKEN": "${env:GH_READ_TOKEN}" }

// Good: Limited database access
"env": { "DATABASE_URL": "postgresql://readonly-user@host/db" }

// Bad: Full access token hardcoded
"env": { "TOKEN": "ghp_admintoken123456" }

Common mistakes:

- Using admin credentials when a reader role is sufficient
- Granting access to the entire filesystem instead of the workspace folder
- Not checking what data the server actually sends to AI

Transition: "Let's put this into practice."
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-21"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-mcp-server-create-test-use-20260321"
prompt: |
  create a marp exercise deck that guides student in creating, testing, and using this mcp server
started: "2026-03-21T23:10:00Z"
ended: "2026-03-21T23:30:00Z"
task_durations:
  - task: "exercise design"
    duration: "00:08:00"
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and README updates"
    duration: "00:03:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2026/03/21/exercise-mcp-server-create-test-use-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Create, Test, and Use an MCP Server || Exercise: Build the Bridge Between Copilot and Everything Else

---

## Exercise: Create, Test, and Use a Local MCP Server

**Objectives**
  - Create a minimal PowerShell MCP server that supports 'initialize', 'tools/list', and 'tools/call'
  - Validate protocol behavior with an end-to-end smoke test script
  - Connect the server to VS Code and use the 'echo' tool from Copilot

**Activities**
  1. **Create**: Build 'scripts/mcp/simple-mcp-server.ps1' with JSON-RPC framing and MCP method routing
  2. **Test**: Run 'scripts/mcp/test-simple-mcp-server.ps1' and verify initialize/tools/list/tools/call responses
  3. **Use**: Confirm '.mcp.json' points to the local server, then prompt Copilot to call the 'echo' tool

**Success Criteria**
  - Server starts without errors and responds with valid MCP JSON-RPC envelopes
  - Test output reports 'MCP test passed.' and confirms all three checkpoints
  - Copilot can discover the 'echo' tool and return the expected echoed text

::: notes
Duration ~00:30

Facilitate this as a lab where students progress from implementation to verification to real usage. Start by framing MCP as a local integration pattern: the server reads JSON-RPC over stdio, advertises tools, and returns structured results.

For Phase 1, have students create 'scripts/mcp/simple-mcp-server.ps1' with helper functions for 'Content-Length' framing, plus handlers for 'initialize', 'tools/list', and 'tools/call'. Emphasize that 'tools/list' should return the 'echo' tool schema and 'tools/call' should validate 'name == "echo"' and required 'arguments.text'.

For Phase 2, run 'pwsh -NoLogo -NoProfile -File .\scripts\mcp\test-simple-mcp-server.ps1' from repo root. Students should verify three checks in output: initialize success, echo tool listing, and echo text round-trip. If test fails, inspect malformed headers, missing 'id' correlation, or invalid response shape.

For Phase 3, confirm '.mcp.json' includes command 'pwsh' and args '-NoProfile -File scripts/mcp/simple-mcp-server.ps1'. In Copilot Chat, ask for a tool call using text like: "Use the echo MCP tool and send the text 'MCP lab check'." Debrief by asking students where they would replace echo with a real internal API or automation tool.

Timing guidance: 10 minutes create, 10 minutes test/debug, 8 minutes use and discuss, 2 minutes recap. During recap, connect this lab to production hardening topics: auth, input validation, audit logs, and tool least-privilege design.
:::