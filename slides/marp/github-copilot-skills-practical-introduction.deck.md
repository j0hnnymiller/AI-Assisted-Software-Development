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

`SKILL.md` is the required entry point.

::: notes
Explain that the structure is intentionally simple so teams can add skills without introducing a new toolchain. The folder name becomes the skill name, while `SKILL.md` acts as the main definition file that tells Copilot what the skill is for and how to execute it. Spend about one minute here and mention that the extra folders are optional but powerful because they let teams attach automation, examples, and reusable references. Transition by opening up the contents of `SKILL.md`.
:::

---

## Anatomy of `SKILL.md`

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
