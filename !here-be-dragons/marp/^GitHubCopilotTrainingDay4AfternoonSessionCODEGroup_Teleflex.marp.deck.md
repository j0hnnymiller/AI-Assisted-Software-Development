---
marp: true
theme: default
paginate: true
---

# GitHub Copilot Training Day 4 Afternoon Session

::: notes
Session covers requirements-driven development, calculator app requirements, and repo management strategies. Exercises focus on requirements analysis and project reset workflows.
:::

---




# Session Topics

- Importance of starting with clear requirements
- Creating requirements documents for new applications
- Using AI to draft and refine requirements
- Managing project history and branches in Git
- Strategies for resetting or reverting a repository

::: notes

- Key points: Start with requirements, avoid using old implementations, use AI for comprehensive drafts, pare down as needed, repo management (reset vs revert).
:::

---




# Creating Requirements Documents

- Begin with a well-known domain for easier requirements gathering
- Use AI to generate a comprehensive first draft
- Refine requirements to match project scope
- Example: Calculator desktop application

::: notes

- Speaker discussed using the prompt: "Create a requirements document for a new calculator desktop application and then I added don't use any of the existing implementation format."
- AI-generated requirements are more comprehensive; easier to pare down than build up from scratch.
:::

---




# Calculator Application Requirements (Key Points)

- Standalone desktop app (Windows, Mac OS, Linux)
- Basic arithmetic and scientific functions
- Memory operations and calculation history
- Intuitive graphical user interface
- Error handling and validation
- User classes: general users, students, professionals
- Non-functional: reliability, usability, scalability, portability

::: notes

- Prompt: Create a requirements document for a new calculator desktop application and then I added don't use any of the existing implementation format.
- Acceptance criteria: correct results, usability without training, quick startup, compatibility and security testing.
:::

---




# Repo Management Strategies

- Use branches to isolate new work
- Remove old implementations for clean starts
- Hard reset vs revert: reset removes commits, revert undoes changes but preserves history
- Manual repo management can be simpler for some workflows

::: notes

- Speaker notes: Discussed approaches to resetting repo, keeping history, and using Visual Studio for manual management.
- Prompt: Reset the repo.
:::

---

# Exercise: Requirements Analysis

**Objectives:**

- Analyze requirements for a new calculator application
- Identify gaps or ambiguities
- Suggest improvements or clarifications

**Activities:**

1. Review the provided requirements document
2. List any missing features or unclear points
3. Propose refinements or additions

**Success Criteria:**

- Comprehensive list of requirements gaps
- Clear suggestions for improvement
- Documented rationale for changes

::: notes
Duration ~00:20

Prompt: Create a requirements document for a new calculator desktop application and then I added don't use any of the existing implementation format.
:::

---

# Exercise: Repo Reset Workflow

**Objectives:**

- Practice resetting or reverting a repository
- Understand implications of each approach
- Maintain useful instruction files and history

**Activities:**

1. Identify the initial commit or clean branch
2. Perform a reset or revert (manual or via tool)
3. Restore or recreate necessary instruction files

**Success Criteria:**

- Repo is reset or reverted as intended
- Instruction files are preserved or restored
- Project history is maintained appropriately

::: notes
Duration ~00:15

Prompt: Reset the repo.
:::

---




# Q&A and Discussion

- Questions about requirements documents
- Comments on repo management strategies
- Sharing experiences with AI-assisted development

::: notes
Encourage participants to discuss their approaches, challenges, and lessons learned from requirements analysis and repo management.
:::
