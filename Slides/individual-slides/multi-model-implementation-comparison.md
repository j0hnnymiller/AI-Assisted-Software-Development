---
marp: true
theme: default
paginate: true
---

## Multi-Model Implementation Comparison

Implementing changes with different AI models
Comparing approaches and outcomes
Risk assessment and quality evaluation
Best practice synthesis
Exercises for hands-on practice

::: notes
Introduce this module as a way to help teams understand how different AI models behave when given the same task. Emphasize that multi-model comparison is a powerful guardrail: it reduces hallucinations, improves quality, and helps teams choose the right model for the right job.
:::

---




## Implementing Changes With Different AI Models

Why use multiple models?
Different reasoning styles
Different strengths (refactoring, documentation, architecture)
Cross-validation reduces risk
Helps detect missing context or contradictions
Typical use cases
Refactoring comparisons
Documentation consistency checks
Architecture proposal validation

::: notes
Explain that no single model is perfect. Using multiple models gives teams a broader perspective and helps catch errors or blind spots that one model alone might miss.
:::

---




## Comparing Approaches & Outcomes

What to compare
Code structure and clarity
Architectural alignment
Test quality
Documentation completeness
Risk level of proposed changes
Benefits
Identifies the safest implementation
Surfaces hidden assumptions
Highlights model-specific biases

::: notes
Encourage participants to treat model outputs like multiple drafts from different engineers. The goal is not to pick a winner — it's to synthesize the best ideas.
:::

---




## Risk Assessment & Quality Evaluation

Risk indicators
Missing tests
Large or unnecessary refactors
Violations of instruction files
Unclear or undocumented behavior
Quality indicators
Small, incremental changes
Clear reasoning
Strong test coverage
Alignment with evergreen principles

::: notes
Reinforce that risk assessment is essential in brownfield systems. Even if a model produces elegant code, it may be too risky without proper guardrails.
:::

---




## Best Practice Synthesis

Combine the strengths of each model
Use one model for architecture
Another for implementation
Another for documentation
Cross-validate tests and reasoning
Outcome
Higher quality
Lower risk
More predictable modernization

::: notes
Explain that synthesis is the real power of multi-model workflows. Teams can build a composite solution that is better than any single model's output.
:::

---

## Exercise: Prompt Multiple Models to Address Technical Debt

Objectives
Compare outputs from different models
Identify strengths and weaknesses
Evaluate risk and quality
Activities
Select a small technical debt item.
Prompt two or more models to propose a fix.
Compare outputs for:

- Safety
- Clarity
- Test coverage
- Architectural alignment
  Synthesize the best elements into a final solution.
  Success Criteria
  Differences between models are clearly identified
  Risks and strengths are evaluated
  Final synthesized solution is safe and incremental
  Provenance metadata is included

::: notes
Duration ~00:15

Encourage participants to think like reviewers comparing multiple PRs. The goal is to understand model behavior, not to pick a favorite.
:::

---

## Exercise: Assigning an Issue to Multiple Models

Objectives
Practice delegating the same issue to different models
Evaluate how each model interprets constraints
Identify missing context
Activities
Create a GitHub-style issue describing a technical debt item.
Assign the issue to two different models.
Compare their proposed remediation plans.
Identify missing context or contradictions.
Success Criteria
Issue is clear and well-structured
Each model produces a distinct approach
Missing context is identified and documented
A preferred plan is selected based on safety and clarity

::: notes
Duration ~00:10

This exercise helps participants see how different models interpret the same instructions — a key skill for multi-model workflows.
:::

---

## Exercise: Delegating Work to Multiple Models

Objectives
Practice multi-model delegation
Evaluate multi-step reasoning
Synthesize best practices into a unified plan
Activities
Select a multi-step modernization task.
Ask multiple models to:

- Analyze the problem
- Propose a remediation plan
- Suggest tests
- Suggest documentation updates
  Compare the outputs.
  Synthesize a final, safe, incremental plan.
  Success Criteria
  Multi-model differences are clearly understood
  Final plan is incremental, reversible, and well-tested
  Documentation and provenance are included
  Risks are identified and mitigated

::: notes
Duration ~00:20

This exercise builds confidence in orchestrating multiple models as collaborators. The goal is synthesis, not competition.
:::
