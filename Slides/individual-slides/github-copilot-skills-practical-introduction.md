---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "github-copilot-skills-practical-introduction-20260321"
prompt: |
  create a marp deck explaining the following content:

  Below is a complete **Marp slide deck** (Markdown) with **Pandoc-style speaker notes** that synthesizes the *latest GitHub Copilot Skills documentation* based on the search results you requested.
  Citations appear where required.

  ---

  ```markdown
  ---
  marp: true
  title: "GitHub Copilot Skills: A Practical Introduction"
  paginate: true
  theme: default
  ---

  # GitHub Copilot Skills
  ### What They Are, How to Define Them, and How They Change Copilot's Behavior

  ---

  # What Are Copilot Skills?

  - **Self-contained capability modules** that teach Copilot how to perform specialized tasks.
  - Each skill is a **folder** containing instructions, scripts, examples, and resources.
  - Copilot loads a skill **automatically when relevant** to the user's prompt.
  - Skills work across:
    - GitHub Copilot in VS Code
    - GitHub Copilot CLI
    - GitHub Copilot coding agent
    - Other skills-compatible agents
  - They provide **repeatable, domain-specific workflows** beyond general coding assistance.

  *Speaker Notes:*
  Skills are a new extensibility layer for Copilot. Unlike custom instructions or promptfiles, skills are *procedural knowledge bundles*. Copilot decides when to load them based on prompt relevance. This allows teams to encode repeatable workflows-testing, migrations, deployments, audits, etc.-and have Copilot execute them consistently.


  ---

  # Why Skills Exist

  - Reduce repeated explanations of domain workflows
  - Provide **portable**, **version-controlled**, **auditable** procedural knowledge
  - Enable **multi-step**, **tool-assisted**, or **script-assisted** tasks
  - Allow organizations to encode **best practices** and **guardrails**
  - Compose multiple skills to build complex workflows

  *Speaker Notes:*
  Skills solve the "institutional knowledge" problem. Instead of repeatedly prompting Copilot with long instructions, you store them once in a skill. Copilot then loads them only when needed, keeping context windows small and behavior predictable.


  ---

  # Skill Structure

  A typical skill looks like this:

  ```
  .github/
    skills/
      webapp-testing/
        SKILL.md
        scripts/
        examples/
        resources/
  ```

  **SKILL.md** is the required entry point.

  *Speaker Notes:*
  The folder name is the skill name. Copilot scans `.github/skills/` for subfolders. Each folder must contain a `SKILL.md` file with metadata and procedural steps. Additional files-scripts, templates, examples-are optional but powerful.


  ---

  # Anatomy of `SKILL.md`

  A minimal example:

  ```
  ---
  name: webapp-testing
  description: >
    Assists with web application test strategies and automated test creation.
    Use for topics related to testing, test, E2E.
  ---

  ## Procedure
  1. Analyze the target code and determine testing strategy
  2. Create test files following the AAA pattern
  3. Run tests and verify results
  ```

  *Speaker Notes:*
  The YAML frontmatter defines metadata Copilot uses for relevance detection. The body defines the procedure-step-by-step instructions Copilot will follow. You can include examples, scripts, or templates referenced by the procedure.


  ---

  # How Copilot Loads Skills

  Copilot automatically loads a skill when:

  - The user's prompt matches the skill's **name**, **keywords**, or **description**
  - The task aligns with the skill's **procedure**
  - The agent determines the skill is **relevant** to the current goal

  When loaded:

  - The skill's instructions are injected into Copilot's context
  - Copilot follows the defined procedure
  - Copilot may use included scripts or resources

  *Speaker Notes:*
  This is not manual activation. Copilot performs semantic matching. If your prompt says "generate E2E tests," Copilot may load the `webapp-testing` skill. If multiple skills match, Copilot composes them.


  ---

  # How Skills Change Copilot's Behavior

  Skills modify Copilot in three major ways:

  ### 1. **Procedural Behavior**
  Copilot follows the steps in the skill's `Procedure` section, producing consistent, repeatable outputs.

  ### 2. **Expanded Capabilities**
  Skills can include:
  - Scripts
  - Templates
  - Examples
  - Domain-specific rules

  ### 3. **Context Efficiency**
  Only relevant skills load, keeping the context window small and focused.

  *Speaker Notes:*
  Skills are not "style guides"-they are operational playbooks. They shift Copilot from reactive text generation to structured task execution.


  ---

  # Skills vs. Other Copilot Instruction Mechanisms

  | Mechanism | Purpose | Scope | When to Use |
  |----------|---------|-------|-------------|
  | **Custom Instructions** | General behavior & preferences | Global | Coding style, tone, conventions |
  | **Promptfiles** | Task-specific instructions | Repo or folder | Reusable prompts for common tasks |
  | **Chat Modes** | Custom agents | Repo | Role-based behavior (e.g., "Security Reviewer") |
  | **Skills** | Procedural, domain-specific workflows | Repo | Repeatable tasks requiring steps, scripts, or examples |

  *Speaker Notes:*
  Skills complement-not replace-other instruction layers. They are the only mechanism designed for procedural, multi-step workflows.


  ---

  # Creating Your First Skill

  ### 1. Create the folder
  ```
  mkdir -p .github/skills/my-skill
  ```

  ### 2. Add `SKILL.md`
  Include:
  - YAML metadata
  - Description
  - Procedure steps
  - Optional examples or scripts

  ### 3. Commit to your repository
  Copilot will automatically detect and load it when relevant.

  *Speaker Notes:*
  Skills are version-controlled like any other code artifact. This makes them auditable and reviewable-critical for team workflows and compliance.


  ---

  # Best Practices for Skill Authoring

  - Use **clear, imperative steps** ("Do X, then Y")
  - Keep procedures **short and deterministic**
  - Include **examples** for complex tasks
  - Use **scripts** for repeatable automation
  - Add **keywords** in the description for better relevance matching
  - Test skills by prompting Copilot with expected triggers

  *Speaker Notes:*
  Think of skills as "operational recipes." The more deterministic and unambiguous the steps, the more reliable Copilot becomes.


  ---

  # Real-World Use Cases

  - Test generation and automation
  - Code migrations
  - Security scanning workflows
  - Documentation generation
  - Data pipeline validation
  - Infrastructure provisioning patterns
  - Compliance checklists
  - Onboarding workflows

  *Speaker Notes:*
  Skills shine when the task is procedural, repeatable, and domain-specific. They are especially powerful for enterprise workflows and team-wide consistency.

  ---

  # Summary

  - Skills are **modular, procedural knowledge bundles** for Copilot
  - Defined via `.github/skills/<name>/SKILL.md`
  - Loaded **automatically** when relevant
  - Enable **repeatable**, **auditable**, **domain-specific** workflows
  - Work across Copilot agents and environments
  - Provide a powerful new layer of extensibility

  *Speaker Notes:*
  Skills represent a major evolution in Copilot's architecture-moving from reactive assistance to structured, agentic execution. They allow teams to encode institutional knowledge directly into the repository.
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

<!-- _class: lead -->

# GitHub Copilot Skills

## What They Are, How to Define Them, and How They Change Copilot's Behavior

::: notes
Introduce this deck as a practical orientation to Copilot Skills rather than a deep internal architecture lecture. Explain that skills are useful because they turn repeated workflow knowledge into reusable repository assets that Copilot can load when a task matches. Spend about one minute here setting expectations that the session will cover what skills are, how they are structured, and why they meaningfully change Copilot behavior. Transition by defining the concept clearly before getting into authoring details.
:::

---

# What Are Copilot Skills?

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

# Why Skills Exist

- Reduce repeated explanation of domain workflows
- Store procedural knowledge in portable, version-controlled form
- Support multi-step, tool-assisted, or script-assisted tasks
- Encode team guardrails and best practices
- Allow multiple skills to contribute to complex workflows

::: notes
Frame this as a response to the institutional knowledge problem. Teams often repeat the same long background prompts over and over, and skills give them a way to store that knowledge once so Copilot can reuse it when needed. Spend about one minute here and point out that version control and reviewability make skills much safer and more maintainable than ad hoc copy-pasted prompt text. Transition by showing what the file and folder structure actually looks like.
:::

---

# Skill Structure

A typical skill folder:

```text
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

# Anatomy of `SKILL.md`

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

# How Copilot Loads Skills

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

# How Skills Change Copilot's Behavior

### 1. Procedural behavior

Copilot follows the skill's steps to produce more consistent results.

### 2. Expanded capabilities

Skills can bring in:

- scripts
- templates
- examples
- domain-specific rules

### 3. Context efficiency

Only relevant skills load, keeping context smaller and more focused.

::: notes
Make the point that skills are operational playbooks, not style guides. They push Copilot away from open-ended reactive generation and toward more structured execution, especially when the task involves repeatable steps, tools, or examples. Spend about one minute here and explain that the context-efficiency angle matters because only the relevant capability modules are loaded instead of everything at once. Transition by comparing skills to other Copilot customization mechanisms.
:::

---

# Skills vs. Other Copilot Instruction Mechanisms

| Mechanism | Purpose | Scope | When to use |
| --- | --- | --- | --- |
| Custom Instructions | General behavior and preferences | Global | Style, tone, conventions |
| Promptfiles | Task-specific instructions | Repo or folder | Reusable prompts for common tasks |
| Chat Modes | Custom agents | Repo | Role-based behavior |
| Skills | Procedural, domain-specific workflows | Repo | Repeatable tasks with steps, scripts, or examples |

::: notes
Explain that skills complement the other instruction layers rather than replacing them. Custom instructions shape broad behavior, promptfiles package reusable requests, and chat modes define role-oriented interaction, while skills are the mechanism specifically designed for procedural workflows that need steps and attached resources. Spend about one minute here and highlight that choosing the right mechanism depends on the kind of control you need. Transition by making the jump from concept to actual creation.
:::

---

# Creating Your First Skill

### 1. Create the folder

```bash
mkdir -p .github/skills/my-skill
```

### 2. Add `SKILL.md`

Include:

- YAML metadata
- description
- procedure steps
- optional examples or scripts

### 3. Commit it

Copilot can then detect and load it when relevant.

::: notes
Present this as a low-friction authoring path. A team does not need a special service or registry to begin; it just adds a skill folder to the repository, writes a `SKILL.md`, and versions it like any other artifact so it can be reviewed, improved, and audited over time. Spend about one minute here and point out that this makes skills fit naturally into existing Git workflows. Transition by showing what separates a good skill from a weak one.
:::

---

# Best Practices for Skill Authoring

- Use clear, imperative steps
- Keep procedures short and deterministic
- Include examples for complex tasks
- Use scripts for repeatable automation
- Add keywords to improve relevance matching
- Test likely triggers by prompting Copilot directly

::: notes
Frame these as reliability practices rather than stylistic preferences. A good skill reads like an operational recipe: specific, testable, and explicit enough that Copilot can execute it with minimal ambiguity, while examples and scripts anchor the procedure in concrete artifacts. Spend about one minute here and encourage the audience to validate skills using likely trigger phrases so they can see whether loading behavior matches expectations. Transition by grounding the idea in real-world categories of work.
:::

---

# Real-World Use Cases

- Test generation and automation
- Code migrations
- Security scanning workflows
- Documentation generation
- Data pipeline validation
- Infrastructure provisioning patterns
- Compliance checklists
- Onboarding workflows

::: notes
Explain that skills are most valuable when a task is procedural, repeatable, and specific to a team's domain. These examples all share the property that there is a known workflow, supporting material, and a need for consistent execution, which is exactly where skills outperform generic chat guidance. Spend about one minute here and mention that enterprise teams benefit especially because they can encode institutional process directly in the repository. Transition by closing with the main takeaways the audience should remember.
:::

---

# Summary

- Skills are modular, procedural knowledge bundles for Copilot
- Defined in `.github/skills/<name>/SKILL.md`
- Loaded automatically when relevant
- Enable repeatable, auditable, domain-specific workflows
- Work across Copilot agents and environments
- Add a powerful extensibility layer beyond basic prompting

::: notes
Close by reinforcing that skills represent a shift from one-off prompting toward reusable operational knowledge. The big idea is that teams can package their best workflows into repository assets that Copilot can discover and apply at the right time, producing more consistent results with less repeated explanation. Spend about one minute here and end on the idea that skills help turn institutional knowledge into something executable, reviewable, and maintainable.
:::
