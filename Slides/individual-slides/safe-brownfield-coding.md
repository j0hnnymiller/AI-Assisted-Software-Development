---
marp: true
theme: default
paginate: true
---

## Safe Brownfield Coding

Using feature flags to minimize risk
As-Is and To-Be test suites
Testing in production
Retiring feature flags
Exercise: Implementing a feature flag

::: notes
Introduce this module as a practical guide to modifying brownfield systems safely. Emphasize that the goal is not speed — it's controlled, observable, reversible change. Feature flags, test suites, and production-safe practices form the backbone of safe modernization.
:::

---




## Using Feature Flags

Why feature flags matter
Enable incremental rollout
Allow instant rollback
Reduce blast radius
Support A/B testing and shadow traffic
Decouple deployment from release
Best practices
Keep flags short-lived
Name flags clearly
Document intent and retirement criteria

::: notes
Feature flags are one of the most powerful tools for brownfield modernization. They allow teams to introduce changes gradually, observe behavior, and roll back instantly if needed. Stress that flags must be managed intentionally to avoid long-term complexity.
:::

---




## Retiring Feature Flags

Why retirement matters
Prevents flag bloat
Reduces cognitive load
Simplifies code paths
Ensures long-term maintainability
Retirement workflow
Validate stability
Remove old code paths
Update documentation
Add provenance to the change

::: notes
Feature flags are temporary scaffolding. If not retired, they become technical debt. Encourage teams to treat flag retirement as a first-class engineering task.
:::

---




## As-Is and To-Be Test Suites

As-Is tests
Capture current behavior
Protect against regressions
Document legacy expectations
To-Be tests
Define desired future behavior
Guide modernization
Validate new patterns and architecture

::: notes
Explain that As-Is tests freeze the current system's behavior, while To-Be tests define the target state. This dual-suite approach allows teams to modernize safely without losing critical legacy behavior.
:::

---




## Testing in Production

Safe production testing techniques
Feature-flag-controlled exposure
Shadow traffic
Canary releases
Observability dashboards
Error-budget-based rollout
Benefits
Real-world validation
Early detection of edge cases
Reduced risk of full-scale failures

::: notes
Testing in production is not reckless when done correctly. With feature flags, observability, and controlled exposure, teams can validate changes under real conditions while minimizing risk.
:::

---

## Exercise: Implementing a Feature Flag

Objectives
Learn how to introduce a safe, reversible change
Practice designing a feature flag workflow
Understand As-Is and To-Be test implications
Document rollout and retirement criteria
Activities
Select a small brownfield function or module.
Identify a safe, incremental change to introduce.
Design a feature flag with:

- Name
- Description
- Rollout plan
- Rollback plan
- Retirement criteria
  Write As-Is and To-Be test cases.
  Document the change with provenance metadata.
  Success Criteria
  Feature flag is clearly defined and scoped
  Rollout and rollback plans are explicit
  As-Is and To-Be tests are correct and meaningful
  Retirement criteria are documented

::: notes
Duration ~00:20

Encourage participants to choose a real module from their brownfield system. The goal is to practice safe, reversible change — not to implement a large feature. Reinforce that feature flags are scaffolding, not permanent architecture.
:::

---




## Essential Safety Measures

AI accelerates development, but it also accelerates mistakes
Strong safety nets must be in place before introducing AI into a brownfield codebase
These practices reduce risk, increase confidence, and protect production systems

::: notes
This slide sets the stage: AI doesn't replace engineering discipline — it amplifies it.

Before we let AI touch a brownfield system, we need guardrails.

These safety measures aren't optional; they're what make AI-assisted development sustainable and safe.

Think of them as the foundation that keeps modernization from turning into accidental rewrites or regressions.
:::

---




## Backup & Rollback Strategies

Use branching strategies that isolate AI-generated changes
Commit early and often to create natural rollback points
Archive snapshots of critical modules before modernization
Ensure you can revert any AI-assisted change without drama
Use feature flags to separate release from deployment

::: notes
AI can produce large changes quickly.

That's powerful — and dangerous without rollback.

Branches, frequent commits, and archives give you a safety net.

The goal is simple: no AI-generated change should ever put you in a position where you can't easily go back.

Rollback confidence is what enables experimentation
:::

---




## Confidence Frameworks

Strong tests are the backbone of safe AI-assisted refactoring
Unit, integration, and behavioral tests validate AI output
Coverage matters less than signal quality
Tests should detect regressions, not just assert happy paths
If all of the test automation passes, how confident are you to deploy to production?

::: notes
AI can help generate tests, but you need a baseline first.

Without a reliable test suite, you're flying blind.

The goal isn't 100% coverage — it's meaningful coverage.

Tests should give you confidence that AI-generated changes behave the same as before unless intentionally modified.

This is what makes modernization safe instead of risky
:::

---




## Change Review Processes

Treat AI as a junior developer: everything gets reviewed
Use human-in-the-loop validation for correctness and intent
Require architectural review for structural changes
Enforce standards through linters, static analysis, and policy checks
Leverage AI to reduce the review burden

::: notes
AI is fast, but it's not authoritative.

Every change needs review — not because AI is untrustworthy, but because context matters.

Humans validate intent, architecture, and alignment with business rules.

Automated checks enforce consistency.

Together, they create a multi-layered review process that keeps quality high.
:::

---




## Incremental Change Methodology

Break modernization into small, safe, reversible steps
Avoid “big bang” refactors – they're brittle and risky
Use iterative loops: propose → validate → refine → commit
Let AI assist with each step rather than entire subsystems at once
Working Effectively with Legacy Code | Hacker News Books

::: notes
Incrementalism is the antidote to brownfield fear.

AI makes it tempting to modernize huge sections at once, but that's where risk spikes.

Instead, treat modernization as a series of controlled, reversible steps.

Each step builds confidence.

Each step is testable.

Each step is safe.

This is how evergreen systems emerge.
:::

---




## Keeping Change Sets Small

Small diffs are easier to review and validate
Small changes reduce merge conflicts and regression risk
AI should be instructed to limit scope intentionally
Small changes accumulate into large improvements over time
Beware: AI can produce huge amounts of code quickly

::: notes
AI tends to produce large outputs unless constrained.

Your job is to keep the scope tight.

Small change sets are easier to understand, easier to test, and easier to roll back.

They also reduce cognitive load for reviewers.

This is how you maintain control while still benefiting from AI's speed
:::

---




## Respecting Brownfield Code

Brownfield systems are valuable – they run the business
Avoid assumptions that “old” means “wrong”
Understand the constraints that shaped the existing design
Modernize with empathy, not aggression

::: notes
Respect is a core principle.

Brownfield systems have survived real-world conditions.

They contain institutional knowledge and business logic that may not be documented anywhere else.

AI can help modernize them, but only if we approach them with humility.

The goal is not to erase the past – it's to evolve it safely.
:::

---




## Building Safety Nets

Protecting brownfield codebases
Leveraging AI code reviews
Effective human code reviews
The role of test automation
Exercise: Building safety nets in practice

::: notes
Introduce this module as the backbone of safe AI-assisted development. Safety nets ensure that modernization efforts do not destabilize working systems. Emphasize that brownfield systems deserve respect, and safety nets are how we honor that reality.
:::

---




## Protecting Brownfield Codebases

Key Practices
Preserve existing behavior unless intentionally changed
Avoid large, risky refactors
Use incremental modernization
Maintain architectural boundaries
Document every AI-assisted change
Why it matters
Brownfield systems run the business
Stability is more important than novelty
Safety nets reduce fear and increase confidence

::: notes
Reinforce that brownfield systems are valuable assets, not liabilities. Protection means minimizing risk, maintaining continuity, and ensuring that modernization is deliberate rather than accidental.
:::

---




## Leveraging AI Code Reviews

AI can assist by:
Highlighting risky changes
Detecting missing tests
Identifying architectural violations
Suggesting safer alternatives
Surfacing potential regressions
Benefits
Faster feedback loops
More consistent review quality
Early detection of drift

::: notes
AI code reviews are not replacements for human reviews — they are accelerators. They help catch issues early and provide a second set of eyes that never gets tired.
:::

---




## Effective Human Code Reviews

Human reviewers focus on:
Intent and correctness
Architectural alignment
Business logic validation
Risk assessment
Ensuring changes are incremental and reversible
Best practices
Review small change sets
Ask for context when missing
Validate AI-generated code with skepticism and curiosity

::: notes
Humans bring judgment, domain knowledge, and intuition — things AI cannot replicate. The combination of AI and human review creates a multi-layered safety net.
:::

---




## The Role of Test Automation

Test automation provides:
Behavioral guarantees
Regression detection
Confidence for modernization
Guardrails for AI-assisted refactoring
Types of tests
Unit tests
Integration tests
End-to-end tests
Snapshot and contract tests

::: notes
Test automation is the ultimate safety net. Without tests, AI-assisted development becomes guesswork. With tests, it becomes a controlled, predictable process.
:::

---

## Exercise: Building the Safety Nets

Objectives
Identify missing safety nets in a brownfield system
Strengthen protection using AI and human review practices
Apply test automation principles
Produce actionable improvements
Activities
Select a brownfield module or file.
Identify existing safety nets (tests, reviews, documentation).
Ask AI to identify missing or weak safety nets.
Strengthen the safety nets by:

- Adding or updating tests
- Drafting review checklists
- Documenting architectural constraints
  Share findings with a partner for validation.
  Success Criteria
  Missing safety nets are clearly identified
  Proposed improvements are safe and incremental
  Test coverage or clarity is improved
  Review and documentation guardrails are strengthened

::: notes
Duration ~00:20

Encourage participants to treat this as a real modernization planning session. The goal is not to fix everything — it's to identify gaps and build a roadmap for safer development.
:::
