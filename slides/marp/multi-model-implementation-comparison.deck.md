---
marp: true
theme: default
paginate: true
---

# Multi-Model Implementation Comparison || Ask Three AIs, Get Four Opinions

---

## Multi-Model Implementation Comparison

- Implementing changes with different AI models
- Comparing approaches and outcomes
- Risk assessment and quality evaluation
- Best practice synthesis
- Exercises for hands-on practice

::: notes
Introduce this module as a way to help teams understand how different AI models behave when given the same task. Emphasize that multi-model comparison is a powerful guardrail: it reduces hallucinations, improves quality, and helps teams choose the right model for the right job.
:::

---

## Implementing Changes With Different AI Models

Why use multiple models?
  - Different reasoning styles
  - Different strengths (refactoring, documentation, architecture)
  - Cross-validation reduces risk
  - Helps detect missing context or contradictions

Typical use cases
  - Refactoring comparisons
  - Documentation consistency checks
  - Architecture proposal validation

::: notes
Explain that no single model is perfect. Using multiple models gives teams a broader perspective and helps catch errors or blind spots that one model alone might miss.
:::

---

## Comparing Approaches & Outcomes

What to compare
  - Code structure and clarity
  - Architectural alignment
  - Test quality
  - Documentation completeness
  - Risk level of proposed changes

Benefits
  - Identifies the safest implementation
  - Surfaces hidden assumptions
  - Highlights model-specific biases

::: notes
Encourage participants to treat model outputs like multiple drafts from different engineers. The goal is not to pick a winner — it's to synthesize the best ideas.
:::

---

## Risk Assessment & Quality Evaluation

Risk indicators
  - Missing tests
  - Large or unnecessary refactors
  - Violations of instruction files
  - Unclear or undocumented behavior

Quality indicators
  - Small, incremental changes
  - Clear reasoning
  - Strong test coverage
  - Alignment with evergreen principles

::: notes
Reinforce that risk assessment is essential in brownfield systems. Even if a model produces elegant code, it may be too risky without proper guardrails.
:::
