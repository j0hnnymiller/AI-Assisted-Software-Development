---
marp: true
theme: default
paginate: true
---

# GitHub Copilot Training Day 5 Morning Session

::: notes
Session focuses on custom chat modes, comparison with instruction and prompt files, and practical integration for AI-assisted development. Exercises include chat mode creation and integration analysis.
:::

---

# Session Topics

- Overview of instruction files, prompt files, and custom chat modes
- Comparison of their purposes, scope, and use cases
- Decision framework for choosing between them
- Real-world integration examples
- Q&A on chat mode expertise and implementation

::: notes

- Key points: Instruction files = persistent behavioral guidelines; Prompt files = executable task templates; Custom chat modes = specialized conversational context.
- Discussed when to use each, how to combine them, and how to focus AI expertise.
:::

---

# Instruction Files

- Define persistent AI behavior and standards
- Applied repository-wide or to specific contexts
- Used for coding standards, security policies, quality gates
- Not task-specific, but set the rules for all AI interactions

::: notes

- Instruction files establish consistent working standards and constraints.
- File patterns can be used to scope instructions.
- Version control and regular testing are recommended.
:::

---

# Prompt Files

- Structured templates for repeatable, specific tasks
- Contain detailed instructions for objectives
- Run on demand for code generation, documentation, reviews, audits
- High reusability for task templates

::: notes

- Prompt files are single-focus, run on demand, and standardize complex workflows.
- Examples: implement authentication, generate test suites, create deployment pipelines.
:::

---

# Custom Chat Modes

- Pre-configured AI personas for specific domains or roles
- Provide contextual expertise and focused knowledge
- Used for domain expertise, role planning, educational conversations
- Medium reusability, rich contextual knowledge

::: notes

- Custom chat modes constrain AI to a specific set of skills or expertise.
- Can be created by users to focus on particular problems or roles.
- Not third-party models, but configurations of existing AI.
:::

---

# Comparison Matrix & Decision Framework

- Instruction files: persistent, repo-wide, simple rules
- Prompt files: task-specific, on-demand, detailed procedures
- Custom chat modes: session-based, role/domain-specific, rich context
- Use instruction files for standards, prompt files for repeatable tasks, chat modes for specialized expertise

::: notes

- Decision framework: Use instruction files for consistency, prompt files for structured tasks, chat modes for domain expertise.
- Can be layered for comprehensive workflows.
:::

---

# Real-World Integration Example

- Implementing user authentication:
  - Instruction files: coding/testing/documentation standards
  - Prompt file: step-by-step OAuth2 implementation
  - Custom chat mode: security architect expertise
- Result: Specialized expert using standardized processes

::: notes

- Example shows how all three approaches combine for robust, AI-assisted development.
:::

---

# Exercise: Create a Custom Chat Mode

**Duration:** 20 minutes

**Objectives:**

- Design a custom chat mode for a specific domain or role
- Define the expertise and constraints for the persona
- Document the configuration and intended use

**Activities:**

1. Choose a domain or role (e.g., security architect, UX designer)
2. Specify the knowledge and constraints for the chat mode
3. Write a configuration or description for the chat mode

**Success Criteria:**

- Clear persona definition and expertise
- Documented configuration and use case
- Ready to use in an AI-assisted workflow

::: notes
Prompt: Create a custom chat mode for a specific domain or role with defined expertise and constraints.
:::

---

# Exercise: Integration Analysis

**Duration:** 15 minutes

**Objectives:**

- Analyze how instruction files, prompt files, and chat modes interact
- Identify benefits and challenges of integration
- Propose improvements for workflow

**Activities:**

1. Review a sample project using all three approaches
2. Map out the flow and interactions
3. Suggest optimizations or clarifications

**Success Criteria:**

- Clear analysis of integration points
- Identified benefits and challenges
- Actionable suggestions for improvement

::: notes
Prompt: Analyze the integration of instruction files, prompt files, and custom chat modes in an AI-assisted project.
:::

---

# Q&A and Wrap-Up

- Open discussion on chat mode expertise
- Questions about implementation and best practices
- Course wrap-up and next steps

::: notes
Encourage participants to share experiences, ask questions, and discuss how they will apply these concepts in their own projects.
:::
