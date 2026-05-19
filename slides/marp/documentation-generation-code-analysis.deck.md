---
marp: true
theme: default
paginate: true
---

# Documentation Generation and Code Analysis || The README That Writes Itself (Finally)

---

## Documentation Generation & Code Analysis

- Automated README and documentation updates
- Architecture diagram generation
- Complex code explanation and mapping
- Identifying technical debt hot-spots
- Exercises for hands-on practice

::: notes
Introduce this module as a practical demonstration of how AI can accelerate documentation, analysis, and modernization in brownfield systems. Emphasize that documentation is not a side activity — it is a core guardrail for safe AI-assisted development.
:::

---

## Automated README & Documentation Updates

Capabilities

- Generate or update README files
- Create module-level documentation
- Produce API references and usage examples
- Keep documentation aligned with code changes

> Create a documentation instruction file?

::: notes
Explain that AI can maintain documentation continuously, reducing drift between code and docs.

This is especially valuable in brownfield systems where documentation is often outdated or missing.

Prompts:

Update the README file with the current state of the project

Update the documentation for CalculatorService.cs

Create a README for the Services component web-calculator\Services

Create a prompt file that creates an instruction file for documenting the project
:::

---

## Create Architecture Diagrams

AI-generated diagrams include:

- System boundaries
- Module interactions
- Data flows
- Deployment environments

::: notes
Encourage participants to treat diagrams as drafts – AI can generate the structure, but humans refine accuracy.
:::

---

## Architecture Diagram Generation

What AI can generate

- High-level system diagrams
- Module dependency graphs
- Data flow diagrams
- Deployment topologies

::: notes
AI can infer architecture from code structure, configuration files, and naming conventions.

These diagrams help teams understand legacy systems quickly and safely.

Prompts:

Create mermaid C4 diagrams for the project
:::

---

## Complex Code Explanation & Mapping

AI can help with:

- Explaining unfamiliar or legacy code
- Mapping call chains and dependencies
- Identifying hidden coupling
- Translating code into human-readable narratives

::: notes
This is one of the most powerful uses of AI in brownfield modernization.

It reduces onboarding time and helps engineers understand risky areas before making changes.
:::

---

## Identifying Technical Debt Hot-spots

AI can detect:

- Outdated patterns
- Duplicate logic
- Missing tests
- High-complexity functions
- Security risks

::: notes
AI can scan large codebases and surface hotspots that deserve attention.

This helps teams prioritize modernization work and avoid guesswork.
:::

---

## Generate Development & Deployment Guides

AI can produce:

- Setup instructions
- Local development workflows
- CI/CD pipeline explanations
- Deployment steps and rollback procedures

::: notes
These guides reduce onboarding time and ensure consistent workflows across teams.

They also help prevent tribal knowledge loss.
:::

---

## Update Project Documentation

AI can update:

- `CHANGELOGs`
- `CONTRIBUTING` guides
- `API` references
- Module-level docs

::: notes
AI helps keep documentation evergreen by updating it alongside code changes.

This reduces drift and improves maintainability.
:::

---

## Cross-Validate With Multiple AI Models

Why cross-validate?

- Reduce hallucinations
- Catch inconsistencies
- Improve accuracy
- Validate architectural assumptions

::: notes
Different models have different strengths.

Cross-validation is a powerful guardrail for correctness, especially in brownfield systems.
:::
