---
marp: true
theme: default
paginate: true
---
# Conformance and Gap Analysis || The Architectural Rules Lawyer Is In

## Conformance & Gap Analysis

Comparing implementations against instruction files
Automated issue generation from conformance gaps
Prioritizing technical debt remediation
Creating actionable remediation plans
Exercises for hands-on practice

::: notes
Introduce this module as the bridge between architectural intent and real code. Conformance analysis ensures that AI-assisted and human-written code stays aligned with the rules defined in instruction files. This is how teams maintain evergreen quality in brownfield systems.
:::

---




## Comparing Implementations Against Instruction Files

What to compare
Coding standards
Architectural boundaries
Allowed/disallowed patterns
Domain rules
Documentation and provenance requirements
Why it matters
Prevents drift
Ensures consistency
Enables safe modernization

::: notes
Instruction files define the “north star” for your codebase. Conformance checks ensure that every change — AI-generated or human — aligns with those rules. This is essential for maintaining predictability in brownfield systems.
:::

---




## Automated Issue Generation From Conformance Gaps

AI can generate:
Issue titles
Detailed descriptions
Violated rules
Suggested fixes
Acceptance criteria
Provenance metadata
Benefits
Faster backlog creation
Consistent issue structure
Reduced manual review effort

::: notes
Automation accelerates the conformance workflow. Instead of manually writing issues, AI can draft them instantly, leaving humans to validate and prioritize.
:::

---




## Prioritizing Technical Debt Remediation

Prioritization factors
Risk to stability
Frequency of use
Security implications
Architectural importance
Effort vs. impact
Approaches
Impact/effort matrix
Risk scoring
Dependency analysis

::: notes
Not all technical debt is equal. Prioritization ensures that teams focus on the highest-value remediation work first, rather than chasing low-impact issues.
:::

---




## Creating Actionable Remediation Plans

A strong remediation plan includes:
Clear problem definition
Root cause analysis
Proposed solution
Step-by-step implementation plan
Rollback strategy
Test updates
Provenance metadata

::: notes
Remediation plans turn issues into action. They provide clarity, reduce risk, and ensure that modernization work is incremental and reversible.
:::
