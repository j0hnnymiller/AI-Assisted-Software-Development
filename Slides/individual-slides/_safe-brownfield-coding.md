---
marp: true
theme: default
paginate: true
---

## Safe Brownfield Coding

Using feature flags to minimize risk
As‑Is and To‑Be test suites
Testing in production
Retiring feature flags
Exercise: Implementing a feature flag

::: notes
Introduce this module as a practical guide to modifying brownfield systems safely. Emphasize that the goal is not speed — it’s controlled, observable, reversible change. Feature flags, test suites, and production‑safe practices form the backbone of safe modernization.
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
Keep flags short‑lived
Name flags clearly
Document intent and retirement criteria

::: notes
Feature flags are one of the most powerful tools for brownfield modernization. They allow teams to introduce changes gradually, observe behavior, and roll back instantly if needed. Stress that flags must be managed intentionally to avoid long‑term complexity.
:::

---

## Retiring Feature Flags

Why retirement matters
Prevents flag bloat
Reduces cognitive load
Simplifies code paths
Ensures long‑term maintainability
Retirement workflow
Validate stability
Remove old code paths
Update documentation
Add provenance to the change

::: notes
Feature flags are temporary scaffolding. If not retired, they become technical debt. Encourage teams to treat flag retirement as a first‑class engineering task.
:::

---

## As‑Is and To‑Be Test Suites

As‑Is tests
Capture current behavior
Protect against regressions
Document legacy expectations
To‑Be tests
Define desired future behavior
Guide modernization
Validate new patterns and architecture

::: notes
Explain that As‑Is tests freeze the current system’s behavior, while To‑Be tests define the target state. This dual‑suite approach allows teams to modernize safely without losing critical legacy behavior.
:::

---

## Testing in Production

Safe production testing techniques
Feature‑flag‑controlled exposure
Shadow traffic
Canary releases
Observability dashboards
Error‑budget‑based rollout
Benefits
Real‑world validation
Early detection of edge cases
Reduced risk of full‑scale failures

::: notes
Testing in production is not reckless when done correctly. With feature flags, observability, and controlled exposure, teams can validate changes under real conditions while minimizing risk.
:::

---

## Exercise: Implementing a Feature Flag

Duration
20 minutes
Objectives
Learn how to introduce a safe, reversible change
Practice designing a feature flag workflow
Understand As‑Is and To‑Be test implications
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
Write As‑Is and To‑Be test cases.
Document the change with provenance metadata.
Success Criteria
Feature flag is clearly defined and scoped
Rollout and rollback plans are explicit
As‑Is and To‑Be tests are correct and meaningful
Retirement criteria are documented

::: notes
Encourage participants to choose a real module from their brownfield system. The goal is to practice safe, reversible change — not to implement a large feature. Reinforce that feature flags are scaffolding, not permanent architecture.
:::

---
