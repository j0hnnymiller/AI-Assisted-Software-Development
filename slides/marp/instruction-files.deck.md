---
marp: true
theme: default
paginate: true
---

# Instruction Files || The .editorconfig for Your AI's Soul

::: notes

**Opening**: This is the title slide introducing the concept of instruction files. **Keep It Brief**: Simply say "Let's talk about instruction files—a powerful way to guide AI behavior persistently across your projects." **Visual Cue**: Let the title appear, pause for 2-3 seconds. **No Content Yet**: Don't explain what they are—that's the next slide's job. **Transition**: "First, let me frame what we mean by 'persistent AI behavioral guidelines'..."

**Frame the Concept**: This subtitle slide sets up the key mental model. **Persistent**: Emphasize that unlike one-time prompts, these rules stay active across multiple interactions. **Behavioral**: These files tell AI _how_ to work, not _what_ to build. **Guidelines vs Commands**: "Think of instruction files as automated code review rules that apply every time AI generates code." **Analogy**: "Like .editorconfig or .eslintrc files, but for AI behavior instead of code formatting." **Transition**: "So what exactly are instruction files? Let's define them..."
:::

---

## What Are Instruction Files?

- Persistent configuration files that define AI behavior patterns
- Applied automatically across multiple interactions
- Establish consistent working standards and constraints

Key Characteristics
- Scope: Repository-wide or context-specific
- Persistence: Active across all relevant AI interactions
- Purpose: Define “how” AI should work, not “what” to do

::: notes
**Definition Emphasis**: Read the definition slowly—this is foundational. **Configuration Metaphor**: "Just like you configure your IDE or linter, you configure your AI assistant with instruction files." **Automatic Application**: Key point: once created, they're automatically applied. No need to paste instructions repeatedly. **Standards Example**: "Example: All Azure code must use managed identities, no hardcoded keys. Put that in azure-dev.instructions.md, and AI will follow it automatically." **Scope Explanation**: Can apply broadly (`applyTo: "**"`) or narrowly (`applyTo: "*.cs"`). **How vs What**: Clarify: Instructions define _style_ ("use dependency injection") not _tasks_ ("build a login system"). **Audience Check**: "Does this distinction make sense—how versus what?" **Transition**: "Let me show you what one looks like..."
:::

---

## Instruction Files: Use Cases

Perfect For:
- Coding Standards → Consistent style across projects
- Security Policies → Enforce security practices
- Quality Gates → Define testing and review requirements
- Technology Constraints → Specify approved frameworks/tools

Examples:
- azure-development.instructions.md
- testing-standards.instructions.md
- security-requirements.instructions.md

::: notes
**Use Cases Overview**: These are the "why" behind instruction files. **Coding Standards**: "Every team has style preferences—indentation, naming, file organization. Instruction files codify this for AI." **Security Example**: "You can mandate: 'Never log passwords', 'Always sanitize user input', 'Use parameterized queries'. AI will follow these rules automatically." **Quality Gates**: "Require test coverage thresholds, code review checklists, documentation standards." **Technology Constraints**: "Enterprise scenario: only approved libraries/frameworks allowed. Instruction file enforces this." **Real Examples**: Point to each example filename and briefly explain: azure-development covers cloud-specific patterns, testing-standards defines test structure, security-requirements enforces security policies. **Team Benefit**: "This is especially powerful for teams—everyone's AI assistant follows the same rules, producing consistent output." **Transition**: "Before we move on, let me share some best practices..."
:::

