---
marp: true
theme: default
paginate: true
---


AI-First vs. Prompt-First Development

---

## AI-First vs. Prompt-First Development

::: notes
This deck introduces the distinction between AI-First and Prompt-First development. The goal is to clarify strategy vs. interface, and show how both fit into modern AI-assisted engineering.
:::

---

## Definitions

AI-First Development
A software engineering philosophy where AI is embedded across the entire SDLC—requirements, design, implementation, testing, documentation, compliance, and maintenance.
Prompt-First Development
A workflow pattern where prompts, instruction files, and chat modes are treated as first-class, version-controlled artifacts.

::: notes
AI-First is the broad philosophy. Prompt-First is the tactical layer that enables predictable AI behavior. You can do Prompt-First without being AI-First, but not the reverse.
:::

---

## What Each Optimizes For

Focus Area | AI-First | Prompt-First
--- | --- | ---
Scope | Entire SDLC | Interaction layer
Goal | Lifecycle integration | Deterministic AI behavior
Optimization | Velocity, governance | Prompt quality, reproducibility
Risk Controls | Human-in-loop, provenance | Versioned prompts, context control

::: notes
This table is the heart of the comparison. AI-First is about organizational and architectural change. Prompt-First is about artifact discipline and predictable outputs.
:::

---

## How They Treat Artifacts

AI-First
Requirements written with AI collaboration in mind
AI-generated scaffolds, tests, docs
Provenance enforced across all AI outputs
Architecture assumes AI participation
Prompt-First
Prompts and instruction files are version-controlled
Prompts define behavioral contracts
Reusable prompt modules
Chat modes define safe, predictable interactions

::: notes
AI-First changes what you build and how you build it. Prompt-First changes how you communicate intent to the AI.
:::

---

## Relationship Between the Two

Prompt-First is a subset of AI-First.
Prompt-First = mechanics
AI-First = philosophy + architecture + lifecycle integration

::: notes
This is the conceptual hierarchy. Prompt-First is necessary but not sufficient for AI-First maturity.
:::

---

## Concrete Examples

Prompt-First Example
Promptfile for generating unit tests
Instruction file for documentation
Chat mode for brownfield developers
AI-First Example
Requirements → AI-generated scaffolds
Code changes → AI-assisted reviews
Docs → continuously AI-generated
Modernization → AI-guided refactoring plans
Provenance → enforced everywhere

::: notes
Use these examples to help teams visualize the difference. Prompt-First is about interfaces; AI-First is about the entire workflow.
:::

---

## Shortest Summary

AI-First = philosophy + architecture + lifecycle integration
Prompt-First = structured, version-controlled interfaces for interacting with AI

::: notes
End with this summary to reinforce the distinction. It's the cleanest way to remember the relationship.
:::
