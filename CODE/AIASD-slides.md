---
marp: true
_class: lead
paginate: true
backgroundColor: #fff
---

# AI Assisted Software Development

## John Michael Miller

Senior Software Engineer at Code Staffing

Played roles of developer, architect, devops engineer, platform engineer, test architect, release manager

AI/ML Enthusiast and advocate for Effectively using AI to write code

- LinkedIn: `www.linkedin.com/in/johnmichaelmiller`
- Email: `john.miller@codestaffing.com`
- Blog: `https://codemag.com/blog/AIPractitioner`

---

## Day One

- Welcome
- Introductions
  - Who you are
  - What you do
  - What you've done with AI tools
  - What you want to learn

::: notes
Day One: Outline the day's goals and emphasize participation and hands-on exercises.
:::

---

## Agenda

- Overview
- AI Assisted Software Development
- General Introduction to LLMs
- LLM Architecture for Code Generation
- GitHub Copilot for Teams: Key Considerations for Adoption
- GitHub Copilot Overview
- Hands-On with GitHub Copilot
- Vibe Coding with Copilot
- Exercises

::: notes
Agenda: Quick walkthrough of topics; highlight hands-on demos and exercises.
:::

---

## Overview

**Course Objective**: Understand how to manipulate Copilot into successfully modifying legacy codebases

**Course Perspective**: Focus on AI assistance and assisting the AI

- Less emphasis on syntax
- More emphasis on architecture, design, code quality, refactoring
- Moving faster with less risk
  ::: notes
  State course objective: practical skills for using Copilot responsibly on legacy codebases.
  :::

---

## Why AI Assisted Software Development

- Is revolutionizing software development
- It will ruin some careers and revitalize others
- If used effectively, it will give you superpowers
  - The courage to
    - Take on codebases that few would touch
    - Use technologies you should know but don't
    - Write more high-quality code than you have ever written before
    - Take on the nice to haves

::: notes
**Revolutionary Impact:**

- AI is fundamentally changing how we write, maintain, and understand code
- Similar to how IDEs replaced text editors, AI assistance is becoming essential
- Speed of development has increased 30-60% for many developers using AI tools effectively

**Career Transformation:**

- Those who adapt: become 10x more productive, tackle bigger challenges, expand skill sets
- Those who resist: may find themselves struggling with modern development expectations
- New roles emerging: AI prompt engineers, AI code reviewers, AI-assisted architects

**Superpowers Explained:**

- **Legacy codebases**: AI can quickly understand and explain complex, undocumented systems
- **New technologies**: Learn frameworks/languages faster with AI as a coding partner
- **Code quality**: AI suggests improvements, catches bugs, generates comprehensive tests
- **Nice to haves**: Features that were "too time-consuming" become feasible

**Examples to share:**

- Developer who used AI to modernize a 15-year-old PHP codebase in weeks instead of months
- Team that adopted a new framework (React to Vue) with AI assistance in days
- 80% reduction in boilerplate code writing time
- Comprehensive test suites generated automatically

**Key message**: AI doesn't replace developers—it amplifies their capabilities
:::

---

## General Introduction to LLMs

- Large Language Models
- Conceptual overview of how LLMs work
- Capabilities and limitations of LLMs in coding
- Software engineering with AI as a tool vs. "Vibe Coding"
- Do's and Don'ts

::: notes
Introduce LLMs at a high level: what they are, how they're trained, and why they matter for developers.
:::

---

## Conceptual Overview of LLMs

- LLMs are trained on massive datasets of code and natural language
- They use transformer architecture to understand patterns
- Token-based processing: code is broken into tokens
- Attention mechanisms help models focus on relevant parts of context
- Generate probabilistic next-token predictions based on training patterns
- No true "understanding" - pattern matching at massive scale

::: notes

- Emphasize that LLMs don't actually "understand" code like humans do
- They use transformer architecture to recognize patterns and context
- Token-based processing: code is broken into tokens (words, symbols, operators)
- Explain that attention mechanisms are what make modern LLMs so powerful
- The scale is what makes the difference - billions of parameters
- When we say LLMs "understand" relationships, we mean they can statistically correlate patterns across tokens
- This pattern matching is extremely sophisticated but lacks true semantic comprehension
- Example: An LLM can recognize that a variable declared early in a function should be referenced later, not because it understands variables conceptually, but because it has seen this pattern millions of times in training
- The "understanding" is really about statistical associations between code patterns, not conceptual knowledge
- This is why LLMs can generate syntactically correct code that is logically flawed - they match patterns without true comprehension of the underlying logic
  :::

---

## Capabilities

- Code completion and generation from natural language
- Refactoring and code optimization suggestions
- Bug detection and fixing recommendations
- Documentation generation
- Test case creation
- Code explanation and commenting
- Multi-language support and translation between languages

::: notes
Capabilities: Describe common uses (completion, refactoring, tests) and show a quick live example if time permits.
:::

---

## Limitations

- No real-time knowledge updates (training cutoff dates)
- Can generate syntactically correct but logically flawed code
- Hallucination: confident-sounding but incorrect suggestions
- Context window limitations (finite memory)
- Does not "understand" business logic or domain-specific requirements
- Security vulnerabilities if not carefully reviewed
- Bias from training data

::: notes
Limitations: Emphasize hallucination, context limits, and the need for human review and testing.
:::

---

## Software Engineering vs "Vibe Coding":

- Engineering approach: systematic, tested, documented, maintainable
- Vibe coding: quick and dirty, "it works" mentality, technical debt accumulation
- AI should enhance engineering practices, not replace them
- Proper testing, code review, and architecture still essential

::: notes
Contrast disciplined engineering practices with quick "vibe" coding; stress that AI should augment engineering rigor, not replace it.
:::

---

## Do's

- Use AI for boilerplate and repetitive tasks
- Always review and test AI-generated code
- Provide clear, specific prompts with context
- Use AI to explore different implementation approaches
- Leverage AI for documentation and test generation

::: notes
Do's: Give practical tips—clear prompts, review, testing, and using AI for repetitive work.
:::

---

## Don'ts

- Blindly accept AI suggestions without review
- Skip testing because "AI wrote it"
- Use AI for critical security or safety-critical code without extensive validation
- Rely on AI for architectural decisions without human oversight
- Generate code without understanding the underlying logic

::: notes
Don'ts: Warn against blind acceptance of suggestions, entering sensitive data in prompts, and skipping tests.
:::

---

## LLM Architecture for Code Generation

[LLM Architecture Diagram](LLM-Architecture-Diagram.png)
![LLM Architecture Diagram](LLM-Architecture-Diagram.png)

::: notes
**Input Processing**:

- Developer provides natural language prompts + existing code context
- Input is tokenized into discrete units the model can process
- Tokens are converted to numerical vectors (embeddings)

**Core Processing**:

- Transformer layers use self-attention to understand relationships
- Context window maintains recent conversation/code history
- Pattern recognition identifies relevant code structures and syntax

**Output Generation**:

- Model generates probability distributions for next tokens
- Decoding strategies determine how to select from probabilities
- Output is converted back to readable code

**Human in the Loop**:

- Critical validation step - AI is a tool, not a replacement
- Feedback loop for prompt refinement and learning

**Training Influence**:

- Large code repositories provide pattern knowledge
- Fine-tuning specializes models for coding tasks
- Quality of training data directly impacts output quality
  :::

---

## GitHub Copilot for Teams: Key Considerations for Adoption

_Empowering developers with AI while protecting your codebase_

::: notes
Outline governance, admin controls, and adoption factors (training, policy, developer onboarding).
:::

---

## What Prompted This Deck?

> I want to know how GitHub copilot protects the intellectual property in the code and documentation submitted to the model. Is this information isolated from other users? Is it incorporated into the model and leaked to other users? How can I protect my IP while using GitHub Copilot?

::: notes
Explain the motivating questions about IP, privacy, and safe use that led to this presentation.
:::

---

## Benefits for Organizations

- Accelerated Development: Faster prototyping, fewer boilerplate tasks
- Improved Documentation: Auto-generates comments and README content
- Enhanced Testing: Suggests unit tests and edge cases
- Team Productivity: Reduces cognitive load, supports onboarding

::: notes
Highlight productivity, documentation, test generation, and onboarding benefits with brief examples.
:::

---

## Risks to Consider

- **IP Leakage Concerns**
  - Copilot may suggest code similar to public repositories
  - Risk of inadvertently using copyrighted or licensed code
  - Mitigation: Enable public code filters and review suggestions carefully

- **Code Quality and Accuracy**
  - AI-generated code may contain bugs, inefficiencies, or security flaws
  - Always validate and test before deployment
  - Treat Copilot as a drafting tool, not a source of truth

- **Developer Overreliance**
  - Risk of reduced understanding or critical thinking
  - Encourage code reviews and pair programming to maintain rigor

::: notes
Cover IP leakage, code quality risks, and developer overreliance; suggest mitigations for each.
:::

---

## Governance and Compliance Risks

- **Regulatory Compliance**
  - Generated code may not meet industry-specific standards (e.g., HIPAA, PCI-DSS)
  - Organizations must enforce coding policies and audits

- **Data Privacy and Security**
  - Sensitive data should never be typed into prompts
  - Use Copilot in secure environments with clear usage guidelines

- **Licensing Ambiguity**
  - Copilot suggestions may resemble code under restrictive licenses
  - Legal teams should define acceptable use policies and monitor compliance

::: notes
Discuss regulatory impacts, auditability, and how to enforce coding policies with automated checks.
:::

---

## IP and Data Protection

- Your code is **not used to retrain the model** (with Copilot for Business/Enterprise)
- Suggestions are generated locally — no code is shared unless feedback is submitted
- No leakage between users: your private code is **not exposed to others**
- Admins can **disable suggestions matching public code** for added safety

::: notes
Clarify data flows, model retraining policy for enterprise plans, and recommended org controls to protect IP.
:::

---

## Licensing and Legal Considerations

- Copilot may suggest code similar to public repositories
- GitHub provides a **filter to block matching public code**
- Organizations should review Copilot's [Terms of Service](https://docs.github.com/en/copilot/overview/copilot-terms-of-service) and [Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)

::: notes
Explain risks of suggested code resembling public repos and recommend legal review and filter settings.
:::

---

## Deployment Options

| Plan                   | Key Features                       | IP Protection |
| ---------------------- | ---------------------------------- | ------------- |
| Copilot Individual     | Personal use, no admin controls    | Limited       |
| Copilot for Business   | Admin controls, policy enforcement | Strong        |
| Copilot for Enterprise | Org-wide policy, audit tools       | Strongest     |

::: notes
Summarize plan differences and pick considerations (control, audit, scale) for each offering.
:::

---

## Best Practices for Safe Use

- Enable public code filters
- Review suggestions before committing
- Educate teams on responsible use and licensing awareness

::: notes
Practical checklist: avoid secrets in prompts, enable public-code filters, and establish review processes.
:::

---

## Resources

- [Copilot Documentation](https://docs.github.com/en/copilot)
- [Copilot for Business Overview](https://github.com/features/copilot-for-business)
- [Security and Privacy FAQ](https://docs.github.com/en/copilot/security)

::: notes
Point attendees to official docs and FAQs; recommend follow-up reading links on the slide.
:::

---

## GitHub Copilot Overview

- Copilot UI in VS Code
- Key features
  - `#` - Add Context
  - `@` - Extensions
  - `/` - Commands
- Modes and models
  - Ask, Edit, Agent, and custom chat modes
- Instructions and Prompts
  - How to use instructions effectively
- How to add context

::: notes
Quick demo plan: show VS Code integration, suggestion modes, and settings.
:::

---

## Instructions vs Prompts vs Custom Chat Modes

| Feature      | Instruction File                                 | Prompt File                                      | Custom Chat Mode                                    |
| ------------ | ------------------------------------------------ | ------------------------------------------------ | --------------------------------------------------- |
| **Scope**    | Workspace-wide guidance                          | File-specific or task-specific nudging           | Interactive behavior tuning for Copilot Chat        |
| **Format**   | JSON or YAML (`.copilot.json`)                   | Markdown or plain text (`copilot-prompt.md`)     | Configurable via UI or `.copilot-chat.json`         |
| **Purpose**  | Define goals, conventions, and tasks for Copilot | Provide localized context to improve completions | Shape Copilot Chat's tone, role, and response style |
| **Audience** | Copilot autocomplete engine                      | Copilot autocomplete engine                      | Copilot Chat interface                              |
| **Location** | Root or `.vscode/` folder                        | Root, `.github/`, inline comments                | Root or `.vscode/` folder                           |

---

## Hands-On with GitHub Copilot

- Installation and configuration
  - Installing the extension
  - Setting up authentication
  - Configuring settings
- Sharing configuration across an organization
  - Shared configuration templates (e.g., .copilot/settings.json) can be distributed across projects to standardize behavior.

::: notes
Walk through installation, auth, and a quick coding session; encourage participants to follow along.
:::

---

## Following along

- Create a new folder outside of the course repos
- Some of the demos/exercises are written for golang
  - If you don't have Golang installed, Copilot can help with that too
  - Just ask it to write the installation commands for you
  - Or wait and Copilot will help you install it during the exercises

**Prompt**: Help me install Golang on Windows/Mac/Linux

---

## Using Copilot in different modes

- Simple prompt completion and inline suggestions (Ask Mode)
- Automatic file edits (Edit Mode)

::: notes
Explain Ask vs Edit modes and when each is most useful.
Speak to Agent Mode and Custom Chat Modes briefly.
We'll work with those later.
:::

---

## Exercise #1 -- Fork the repos

**Objective**: Fork the course repos
**Tasks**

- Search GitHub for
  - AI-Assisted-Software-Development
- Fork this repo
  - This will create a personal copy under your GitHub account
  - You can make changes without affecting the original repo

::: notes
Speaker Notes:

A zip with the slides, examples, demos will be provided after the course
:::

---

## Homework

- Find a repo that could use some help
  - In a language you are famliar
  - A personal project is cool, but a project you are not familiar with is better
  - Fork it
    - It allows you to experiment without affecting the original codebase
  - Don't use a company repo
- We'll use it in the legacy code portion of the course

**Prompt**: I'm looking for a small GitHub Golang project that has a lot of open issues. Can you recommend one?

::: notes
Assign finding a repo and preparing it for the legacy code session; remind them to choose familiar languages.
:::

---

## Exercise #2 -- Implement a Simple Calculator

**Objective**: Create a simple calculator using Ask Mode. Expand on the calculator in Edit mode.

**Prompt** Implement a simple command line calculator in Golang

::: notes
There are two speaker objectives for this exercise:

1. Get everyone a feel for what it's like to develop assisted by Copilot
2. Demonstrate the perils of vibe coding with instruction files and chat modes

I've found it doesn't take long for the AI to start going off the rails.

At the end of the day prompt the AI to list all the reasons why the calculator is not evergreen.

Prompt: Review the code in the class repo and list all the reasons why it is not evergreen.

Use this as a teaching moment to show that code is already legacy and how tomorrow we work on making it evergreen and more importantly how to keep it evergreen.

Here are some suggested prompts to guide the exercise:

Add support for calculating square roots

Create unit tests for the simple calculator

Using test driven development, add tests for a new memory function to store previous calculations. Don't implement the new feature. Show that the tests fail

Implement shells of the missing methods so that code compiles. Don't implement the functionality

Create documentation for the simple calculator

Add mermaid architecture diagrams to the documentation

Implement the add memory function in the simple calculator but no other functionality

Implement the rest of the memory functions and update the documentation

Using tdd, create tests for a new logging function in the simple calculator

Using tdd, test that the log file resides in the log folder under the root of the project

Create tests that verify that once created, the log is not deleted

Using tdd, create tests that verify that the log is loaded into memory when the calculator starts

Can you list the last 10 prompts I've given?

Load the log into memory when the calculator starts

After running the calculator I expected to see a list of the calculations. but the calc-default.log does not contain them. is that what you expected? (REPL transcript)

I want to implement #2, but first change the tests to expect #2

Update the tests to use a distinct test-only logfile name. I expect that these tests will initially fail. I also expect to see them executed

#terminalLastCommand I only see that TestEvalAndStoreCreatesAndPersistsLogInCwdLog is failing because the file doesn't exist. are there test that verify if the log file exists: 1. that it can be read into memory 2. that what is read is correct

I want tests that verify that the expected behavior (not yet implemented) is correct. I expect to see a test that creates a logfile, runs the load into memory logic and verifies that it's correct. That test(s) should execute and fail until the implementation is completed

:::

---

## Day Two & Three

Working Effectively with Legacy Code, with AI assistance

::: notes
Day Two: Focus on legacy code manipulation with Copilot, instruction files, and safe editing practices.

preparing for exercises
cd "c:\git\blogcode\Zeus.Code.Presents“
git switch main
git branch --list
git branch -D gpt4o
git branch -D sonnet4
git branch -D fixes
git clean -fdx
clear
git branch --list

close all editors
clear terminal
new chat
:::

---

## Agenda -- Legacy Development

- Overview
  - What is and isn't legacy code
  - What is Evergreen Code
- Before engaging Copilot
- Managing Copilot Context
  - Instructions, ChatModes, and Prompts
- Read Only Techniques
  - explain, review, document, test
- Modifying legacy code with AI assistance
- Managing Change Risk
  - small changes, refactoring, safety nets
- Exercises

::: notes
Preview themes: understanding legacy code, instruction files, and exercises focused on safe edits.
:::

---

## Overview

**Course Objective**: Understand how to work with AI in modifying legacy codebases

**Course Perspective**: Focus on AI assistance and assisting the AI

- Less emphasis on syntax
- More emphasis on architecture, design, code quality, refactoring
- Moving faster with less risk

**Must Read**: [Working Effectively with Legacy Code](https://archive.org/details/working-effectively-with-legacy-code)

::: notes
State course objective: practical skills for using Copilot effectively on legacy codebases.
Part 1: Understanding legacy code and its challenges
Part 2: Techniques for safely modifying legacy code with AI assistance
:::

---

## Exercise #1.1 -- Fork the repos

**Objective**: Fork the course repos

- Search GitHub for
  - AI-Assisted-Software-Development
- Fork the repo
  - This will create a personal copy under your GitHub account
  - You can make changes without affecting the original repo

---

## Exercise #1.2 -- Fork the target repo

**Objective**: Fork the repo for the legacy code exercises

- Find a repo that could use some help
  - Choose a language you are familiar with
  - A personal project is cool, but a project you are not familiar with is better
  - Don't use a company repo
  - Fork it
    - It allows you to experiment without affecting the original codebase

**Prompt**: I'm looking for a small GitHub Golang project that has a lot of open issues. Can you recommend one?

::: notes
Speaker Notes:

A zip with the slides, examples, demos will be provided after the course
:::

---

## What is legacy code

- No universally accepted definition
- Easier to define what is _not_ legacy code

::: notes
Try this in quick chat:

- "what are three definitions of legacy code?"
- "what are 10 definitions of legacy code?"
- "what are 25 definitions of legacy code?"

Ask the audience: "Who recognizes these definitions in their work?"

Encourage discussion about their experiences with legacy code.
:::

---

## What is not legacy code

- All codebases start as greenfield
- Few codebases are evergreen

<!--
Try this in quick chat:
what are three definitions of code that is not legacy?
-->

::: notes
Explain greenfield characteristics and why "not legacy" is rare at scale.
:::

---

## Codebases degrade over time

Due to changes in:

- Technology
- Practices
- People
- Business rules
- Workflows
- Architecture

::: notes
Discuss drivers of decay (tech, people, rules) and give a brief example.
:::

---

## What is Evergreen Code

- Evergreen code actively resists technical debt
- Evergreen ≠ Legacy; everything else is
- Evergreen is the goal
  - If we were to write all over again, it would turn out just like it is

::: notes
Describe evergreen goals: maintainability, minimal debt, and consistent patterns.
:::

---

## Legacy code needs respect not fear

- It works - Don't break it!
- It works - Well-tested (by users)
- It works - It is, what it is
  - "You get what you get and you don't throw a fit"

::: notes
Emphasize safety-first approach: back up, test, and validate before large changes.
:::

---

## Prelude -- before engaging Copilot

- Have a strategy for backing out of changes
  - Branching, Commit SHA, Archiving, Zipping
- Have a strategy for testing the code
  - No matter who or what wrote it
  - You need to have confidence that your test automation will catch issues before they reach production
  - If you don't have that confidence, stop and build it first
- Have a strategy for reviewing changes
  - Peer review, AI review, Static analysis
  - You are going to be reviewing a lot of code. Make sure you have a plan to do it effectively
- Change sets as small as possible
  - Make incremental changes and validate frequently
  - AI can get carried away. Don't let it.

::: notes
Checklist: backups, testing strategy, and rollback plan before using AI to modify critical code.
:::

---

## Managing Copilot

- Treat Copilot as a highly skilled, junior developer who needs effective management to succeed
- Clear instructions + careful review = great outcomes

::: notes
Treat Copilot as a junior dev: give clear tasks, review output, and enforce style guidelines.
:::

---

## Managing Context

- The importance of context
  - Too little
  - Too much
- Prompts
  - Crafting effective prompts
  - Prompt engineering
- Adding context
  - Instructions markdown
  - File-based custom instructions, automatic context injection, instruction scopes, structure and authoring best practices, structure and authoring best practices
- Custom chat modes
  - Mode definition, tool integration, quick mode switching, workspace and user scope, persona-driven workflows, enhanced productivity and consistency

---

## Adding Context

Open editors
Files & folders ...
Instructions ...
MCP resources …
Problems ...
Symbols ...
Image from clipboard
Screenshot window
Tools ...

---

## MCP Servers and Tools

![MCP Architecture](MCP-Architecture.png)

---

## Adding Context - Tools

- Configure Tools…
- Built-in and not
- Selecting and Unselecting Tools
  - 128 Tool limit

---

## Raising the Bar -- with Instruction Files

- What are instruction files?
- Provide context and guidance to Copilot and
- Can include:
  - Project-specific instructions
  - Tech-specific instructions
  - Standards and practices
- They need to be consistent and not contradictory

::: notes
Explain instruction files purpose and show examples of project-level guidance.
:::

---

## Instruction File Locations

- Personal - `$home\.github\copilot-instructions.md`
- Project - .github\instructions
- File names should be `*.instructions.md`

::: notes
Point out file locations and naming conventions; advise on consistent team distribution.
:::

---

## Meta Instructions

| Instructions File                  | Description                                              |
| ---------------------------------- | -------------------------------------------------------- |
| ai-assisted-output.instructions.md | Instructions for generating AI-assisted output           |
| copilot-instructions.md            | Instructions for using Copilot effectively               |
| instruction-prompt.instructions.md | Instructions for creating effective prompts              |
| prompt-file.instructions.md        | Instructions for prompt files that generate instructions |

Copy these files into the .github/instructions folder of your project to guide Copilot in the creation of prompts that create instruction files.

---

# AI-Assisted Output Policy — At a Glance

- Purpose: enforce provenance for all AI-assisted artifacts
- Requires: embedded YAML front matter (ai_generated, model, operator, chat_id, ai_log, timestamps)
- Workflow: new chat → `ai-logs/yyyy/mm/dd/<chat-id>/conversation.md` + `summary.md`
- Enforcement: CI/PR checks should fail files with `ai_generated: true` missing `chat_id` or `ai_log`

<footer style="font-size:0.8em">See: .github/instructions/ai-assisted-output.instructions.md</footer>

---

# GitHub Copilot Instructions — At a Glance

- Scope: Guidance for GitHub Copilot usage and AI provenance across the repo
- Model rule: always use underlying model format "provider/model@version"
- Metadata: embed YAML front matter (ai_generated, model, operator, chat_id, prompt, started, ended, task_durations, total_duration, ai_log, source)
- Chat/logging: New chat → new ai-logs/yyyy/mm/dd/<chat-id>/conversation.md + summary.md
- Post-creation: update ai-logs, create summary.md, and add README entry for notable artifacts
- CI check: fail PRs when ai_generated artifacts lack chat_id or ai_log or referenced ai_log missing

<footer style="font-size:0.8em">See: .github/instructions/copilot-instructions.md</footer>

## Generating the Prompt for Evergreen Software Development

**Meta Prompt**: Create a prompt file that generates an instruction file for evergreen software development

- Keep `main` buildable, secure, releasable
- Automate dependency updates & CI (Dependabot, SCA)
- Merge small, frequent changes; pin and monitor deps
- PR checklist: CI green, security review, changelog
- Enforcement: GitHub Action "Evergreen check" (deps + tests)

---

## Generating the Evergreen Instruction Files

**Prompt**: #file:create-evergreen-instructions.prompt.md create the instruction file for evergreen software development

- Prompts to generate instructions
  - Instructions on generating instruction files
- Use current codebase as context
- Keeping instruction files fresh
- Prompts for updates
- Copilot suggestions based on codebase changes

::: notes
Show prompts and workflow to generate and maintain instruction files with Copilot.
:::

---

## Meta Prompts

---

## Exercise #3 -- Create Instruction Files

**Objective**: Create instruction files manually and with Copilot assistance

- Manually create instructions with:
  - Business rules
  - Workflows
  - Purpose
  - Tech stack
  - Architecture
- Use Copilot to generate instruction files using the codebase

- **Bonus**
- Review for errors, omissions and inconsistencies
- Ask Copilot for updates instructions based on tech/practice changes

::: notes
Task: manually author then use Copilot to refine; review for inconsistencies and policy gaps.
:::

---

## Understanding legacy code

- Generating documentation
- Update README files
- Generate architecture diagrams
- Identify and explain complex or confusing code

::: notes
Demonstrate generating architecture summaries, README updates, and code explanations with AI.
:::

---

## Exercise #4 -- Understanding legacy code

**Objective**: Create documentation for a legacy project using Copilot.

- Update or create:
  - Development guide
  - Deployment guide
  - README
  - Architecture diagrams
- Execute prompts to update documentation
- Review for errors and omissions
- **Bonus**: Use another model to review the documentation

::: notes
Task instructions: use Copilot to produce docs, run quick verification, and iterate.
:::

---

## Meta-Instructions

---

## Keeping Code Evergreen

**Prompt**:

- Create an instruction file for an evergreen project. put it in the .github\instructions folder. It should be technology agnostic
- Create an instruction file for an evergreen golang backend. put it in the .github\instructions folder. It should be technology focus on golang and not repeat instructions in the #file:evergreen.instructions.md
- Review the code in the Fundamentals\examples\.sav.calculator folder and create issues for bringing the in compliance with the instructions. Prioritize and categorize the issues.

---

# Day Three -- Legacy Development

---

## Creating a safety net

- Linting
- What AI can do beyond static tools
- Create and execute linting rules with AI

## Test automation

- Unit, integration, E2E, and other tests
- Generating tests
- How many tests are enough?

::: notes
Focus: building safety nets (linting, tests) and using AI for improvements without breaking behavior.
:::

---

## Exercise #5 -- Generate Tests

Objective: Same as earlier---focus on test creation and review.

**Bonus**: Use another model to review the tests

::: notes
Generate unit and integration tests with Copilot, then run to validate behavior and coverage.
:::

---

## Identifying Instruction Compliance Gaps

- Compare current implementation to instructions
- Generate issues from gaps
- Identify low-hanging fruit

::: notes
Show how to compare implementation against instruction files and produce actionable issues.
:::

---

## Exercise #6 -- Identify Gaps

**Objective**: Use Copilot to compare the implementation with the instruction files.

- Create prompt to identify deviations
- Review response

**Bonus**: Generate GitHub issues from findings

<!-- Note: It's better to fork the repo than clone -->

::: notes
Hands-on: craft prompts to find deviations and export findings to tickets for triage.
:::

---

## Exercise #7 -- Address a Compliance Gap

**Objective**: Create a plan to address a deviation found in Exercise #6.

- Ask Copilot to create a remediation plan
- Review the plan

**Bonus**: Ask a different model to review the plan

::: notes
Create a remediation plan, implement in a branch, and validate with tests and reviews.
:::

---

## Comparing Implementations

- Implement the same change with multiple models
- Ask Copilot to summarize pros and cons

::: notes
Run the same change using multiple models and compare outcomes for quality and maintainability.
:::

---

## Exercise #8 -- Compare Implementations

**Objective**: Use two models to implement a change and compare results.

- Create branches for each model
- Implement fix using different models
- Compare implementations

**Bonus**: Ask a second model to compare and report pros/cons

::: notes
Practical: create branches per model, implement changes, run comparisons, and document differences.
:::

---

# Day Four -- New Development

---

## Exercise #1 -- Fork the repos

**Objective**: Fork the course repos

- Search GitHub for
  - AI-Assisted-Software-Development
  - zeus.academia.2
  - zeus.academia.3a
- Fork the repos
  - This will create a personal copy under your GitHub account
  - You can make changes without affecting the original repo

---

## Starting with Project Requirements

- Business rules
- Workflows
- Tech stack
- Architecture

::: notes
Shift to greenfield best practices: requirements, prompts, and verification workflows.
:::

---

## Exercise #9 -- Create Project Requirement Instructions

- **Objective**: Create project requirement instructions, some
  project-specific, some generic, using both manual and Copilot-assisted
  methods.

- Manually create a copilot-instructions.md file and add:
  - Business rules
  - Workflows
  - Purpose
  - Tech stack
  - Architecture

- Use Copilot to generate instruction files using the
  copilot-instructions.md and the codebase for context.

**Bonus**:

- Review instruction files for errors and omissions.
- Ask Copilot to suggest changes based on evolving tech and practices.

::: notes
Author requirement docs, then use Copilot to generate scaffolding and validate alignment.
:::

---

## Creating Instructions

- What are instructions?
  - Locations:
  - Project
  - User
- AI-assisted instruction generation

::: notes
Clarify what instruction files are and how to keep them relevant to the codebase.
:::

---

# Day Five Agenda -- New Development

- Creating Custom Chat Modes
- Generating Implementation Prompts & Verification
- Exercises
- Wrap-Up and Open Q&A

::: notes
Final day: custom chat modes, verification prompts, and wrap-up exercises.
:::

---

## Exercise #10 -- Generate Instruction Files

**Objective**: Create instruction files, some project-specific, some
generic, using both manual and Copilot-assisted methods.

- Manually create a copilot-instructions.md file and add:
  - Business rules
  - Workflows
  - Purpose
  - Tech stack
  - Architecture
- Use Copilot to generate instruction files using the
  copilot-instructions.md and the codebase for context.

**Bonus**:

- Review instruction files for errors and omissions.
- Ask Copilot to suggest changes based on evolving tech and practices.

::: notes
Generate both project-specific and generic instructions; review and iterate.
:::

---

## Creating Custom Chat Modes

- Personas
- Workflows
- Examples
- Agents
- Allowing agents to take autonomous action
- agent.json
  - Safe commands
  - Unsafe commands

::: notes
Discuss persona design, safe command lists, and agent.json structure for safe automation.
:::

---

## Exercise #11 -- Creating Custom Chat Modes

**Objective**: Create custom chat modes for the project.

- Define personas and workflows for each chat mode.
- Implement chat modes using Copilot assistance.
- Create an agent.json file with safe commands.
- Test the agent's ability to execute safe commands.

::: notes
Practical steps: define personas, implement agent.json, and test allowed actions in a sandbox.
:::

---

## Generating Implementation Prompts & Verification

- Implementation prompts
- Implementation verification

::: notes
Teach how to craft reproducible prompts and verification checks to validate generated code.
:::

---

## Exercise #12 -- Executing Prompts

**Objective**: Execute implementation prompts using custom chat modes.

- Review the implementation prompts created earlier.
- Use prompts to guide agent actions.
- Test agent responses to prompts.
- Verify implementation passes verification checks.

::: notes
Execute prompts in custom modes, verify outputs, and refine prompts based on failures.
:::

---

## Wrap-Up and Open Q&A

- Review the day's learning outcomes.
- Address questions or concerns.
- Discuss next steps and future learning opportunities.

::: notes
Summarize key takeaways, next steps, and open the floor for questions and feedback.
:::
