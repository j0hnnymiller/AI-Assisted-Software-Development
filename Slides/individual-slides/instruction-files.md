---
marp: true
theme: default
paginate: true
---

## Instruction Files

::: notes
**Opening**: This is the title slide introducing the concept of instruction files. **Keep It Brief**: Simply say "Let's talk about instruction files—a powerful way to guide AI behavior persistently across your projects." **Visual Cue**: Let the title appear, pause for 2-3 seconds. **No Content Yet**: Don't explain what they are—that's the next slide's job. **Timing**: 10-15 seconds. **Transition**: "First, let me frame what we mean by 'persistent AI behavioral guidelines'..."
:::

---

## Persistent AI Behavioral Guidelines

::: notes
**Frame the Concept**: This subtitle slide sets up the key mental model. **Persistent**: Emphasize that unlike one-time prompts, these rules stay active across multiple interactions. **Behavioral**: These files tell AI _how_ to work, not _what_ to build. **Guidelines vs Commands**: "Think of instruction files as automated code review rules that apply every time AI generates code." **Analogy**: "Like .editorconfig or .eslintrc files, but for AI behavior instead of code formatting." **Timing**: 30 seconds. **Transition**: "So what exactly are instruction files? Let's define them..."
:::

---

## What Are Instruction Files?

Definition
Persistent configuration files that define AI behavior patterns
Applied automatically across multiple interactions
Establish consistent working standards and constraints
Key Characteristics
Scope: Repository-wide or context-specific
Persistence: Active across all relevant AI interactions
Purpose: Define “how” AI should work, not “what” to do
::: notes
**Definition Emphasis**: Read the definition slowly—this is foundational. **Configuration Metaphor**: "Just like you configure your IDE or linter, you configure your AI assistant with instruction files." **Automatic Application**: Key point: once created, they're automatically applied. No need to paste instructions repeatedly. **Standards Example**: "Example: All Azure code must use managed identities, no hardcoded keys. Put that in azure-dev.instructions.md, and AI will follow it automatically." **Scope Explanation**: Can apply broadly (`applyTo: "**"`) or narrowly (`applyTo: "*.cs"`). **How vs What**: Clarify: Instructions define _style_ ("use dependency injection") not _tasks_ ("build a login system"). **Audience Check**: "Does this distinction make sense—how versus what?" **Timing**: 2 minutes. **Transition**: "Let me show you what one looks like..."
:::

---

## Instruction File Structure

```markdown
---
description: Azure best practices for AI development
applyTo: "**" # File pattern scope
---

## Core Instructions

- Use Azure Tools when handling Azure requests
- Follow security best practices
- Implement proper error handling
- Generate comprehensive documentation

## Code Generation Rules

- Write tests before implementation
- Use dependency injection patterns
- Follow naming conventions
- Include proper logging
```

::: notes
**Walk Through Example**: Go section by section, don't rush. **YAML Front Matter**: "Every instruction file starts with metadata. Description explains purpose, applyTo defines scope." **ApplyTo Pattern**: Explain glob patterns—`"**"` means all files, `"*.py"` means Python only, `"src/**/*.ts"` means TypeScript in src folder. **Core Instructions**: "This section defines high-level principles—use Azure-specific tools, enforce security, proper error handling." **Code Generation Rules**: "This section gets tactical—TDD approach, dependency injection, naming standards, logging requirements." **Live Demo Opportunity**: If time permits, show a real instruction file from the repo. **Practical Point**: "AI reads this file automatically when working in your repo—no copy-paste needed." **Timing**: 3 minutes. **Transition**: "When should you use instruction files? Let's look at common use cases..."
:::

---

## Instruction Files: Use Cases

Perfect For:
Coding Standards → Consistent style across projects
Security Policies → Enforce security practices
Quality Gates → Define testing and review requirements
Technology Constraints → Specify approved frameworks/tools
Examples:
azure-development.instructions.md
testing-standards.instructions.md
security-requirements.instructions.md

::: notes
**Use Cases Overview**: These are the "why" behind instruction files. **Coding Standards**: "Every team has style preferences—indentation, naming, file organization. Instruction files codify this for AI." **Security Example**: "You can mandate: 'Never log passwords', 'Always sanitize user input', 'Use parameterized queries'. AI will follow these rules automatically." **Quality Gates**: "Require test coverage thresholds, code review checklists, documentation standards." **Technology Constraints**: "Enterprise scenario: only approved libraries/frameworks allowed. Instruction file enforces this." **Real Examples**: Point to each example filename and briefly explain: azure-development covers cloud-specific patterns, testing-standards defines test structure, security-requirements enforces security policies. **Team Benefit**: "This is especially powerful for teams—everyone's AI assistant follows the same rules, producing consistent output." **Timing**: 2-3 minutes. **Transition**: "Before we move on, let me share some best practices..."
:::

---

## Instruction Files Best Practices

✅ Do This:
Keep instructions clear and actionable
Use file patterns (applyTo: '\*\*') for broad scope
Version control and document changes
Test instruction effectiveness regularly
❌ Avoid This:
Overly complex or contradictory rules
Too many instructions (cognitive overload)
Instructions that conflict with prompt files
Hardcoded values instead of parameters
::: notes
**Best Practices Summary**: This slide prevents common mistakes. **Clear and Actionable**: Bad: "Code should be good." Good: "Use async/await for I/O operations." Be specific. **File Patterns**: Explain `applyTo` strategy—broad patterns for general rules, narrow patterns for specific contexts. **Version Control**: "Instruction files are code. Commit them, review changes, track evolution." **Test Effectiveness**: "After creating an instruction file, test it—ask AI to generate code and verify it follows the rules." **Avoid Complexity**: "If AI can't understand your instructions, they won't work. Keep language simple, rules unambiguous." **Cognitive Overload**: "Don't create 50 instruction files. AI (like humans) can only track so much. Consolidate related rules." **Conflicts**: "Instruction files apply automatically, prompts are one-time. Make sure they don't contradict each other." **No Hardcoding**: "Use parameters and environment variables, not hardcoded URLs or credentials." **Practical Advice**: "Start small—one or two instruction files. Expand based on team needs." **Timing**: 3 minutes. **Transition**: Depending on agenda, either "Let's see this in action with a hands-on demo..." or "Questions about instruction files before we move on?"
:::
