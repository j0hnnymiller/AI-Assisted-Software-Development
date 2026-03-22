---
marp: true
theme: default
paginate: true
---

## Addressing Technical Debt

Prompting Copilot to address debt
Assigning issues to Copilot
What Copilot does with assigned issues
Exercises for hands-on practice

::: notes
Introduce this module as the moment where AI becomes an active contributor to modernization. Technical debt is inevitable in brownfield systems, but AI can help teams address it safely, incrementally, and with strong guardrails.
:::

---

## Prompting Copilot to Address Technical Debt

Effective prompts include:
Clear description of the debt
Constraints and architectural rules
Expected outcomes
Required tests and documentation updates
Provenance requirements
Benefits
Faster remediation
Consistent application of patterns
Reduced manual effort

::: notes
Explain that Copilot responds best to structured, high-signal prompts. The more explicit the constraints, the safer and more predictable the remediation.
:::

---

## Assigning Issues to Copilot

How assignment works
Convert technical debt into GitHub issues
Provide context, constraints, and acceptance criteria
Use Copilot to draft remediation steps
Let Copilot propose code changes in PRs
Why assign issues?
Creates a repeatable workflow
Keeps humans in the reviewer role
Ensures traceability and provenance

::: notes
Assigning issues to Copilot formalizes the workflow. It treats Copilot like a junior developer who receives tasks, produces drafts, and awaits review.
:::

---

## What Copilot Does With Assigned Issues

Copilot reads the issue description and linked context
Generates a proposed plan or implementation approach
Creates or updates pull requests with code changes
Adds explanations, tests, and documentation as needed
Iterates based on review comments
Maintains traceability between issue → PR → commits

::: notes
::: notes**Overview**  When you assign an issue to GitHub Copilot on GitHub.com, Copilot behaves like a managed junior developer. It doesn't magically “solve” the issue — it follows a structured workflow grounded in the issue description and repository context.**Reads the Issue and Context**  Copilot parses the issue body, labels, linked discussions, and any referenced files. The quality and specificity of the issue strongly influence the quality of the output.**Generates a Work Plan**  Copilot drafts an implementation plan. This may include steps, architectural notes, or a breakdown of required changes. It uses repository code, patterns, and conventions to stay consistent.**Creates or Updates Pull Requests**  Copilot opens a PR with proposed changes. These changes often include code, tests, and documentation updates. It may also update an existing PR if the issue is already in progress.**Responds to Feedback**  When maintainers leave comments, Copilot can revise the PR. It treats comments as instructions, similar to how a junior developer would respond to review notes.**Maintains Traceability**  Copilot links the PR back to the issue, references commits properly, and ensures the work is tracked through GitHub's normal workflow. This supports auditability and provenance — something you and I both care about deeply.**Key Takeaway**  Copilot doesn't replace engineering judgment. It accelerates the mechanical parts of implementation while relying on humans for direction, review, and acceptance.:::
:::

---

## Exercise: Prompt Copilot to Address Technical Debt

Duration
10 minutes
Objectives
Practice writing high-signal prompts
Apply architectural constraints
Produce safe, incremental remediation requests
Activities
Select a small piece of technical debt.
Write a prompt that includes:
  - Description of the debt
  - Constraints and rules
  - Expected behavior
  - Required tests and documentation
Ask Copilot to propose a remediation.
Review the output for correctness.
Success Criteria
Prompt is clear, scoped, and actionable
Copilot produces a safe, incremental change
Output aligns with architectural rules
Provenance metadata is included

::: notes
Encourage participants to choose a real example from their brownfield system. The goal is clarity and safety, not complexity.
:::

---

## Exercise: Assigning an Issue to Copilot

Duration
10 minutes
Objectives
Convert technical debt into a structured issue
Provide Copilot with actionable context
Practice writing acceptance criteria
Activities
Select a technical debt item.
Create a GitHub-style issue with:
  - Title
  - Description
  - Impact and risk
  - Acceptance criteria
  - Provenance metadata
Assign the issue to Copilot.
Review Copilot's proposed remediation.
Success Criteria
Issue is clear and well-structured
Acceptance criteria are testable
Copilot produces a relevant draft
Provenance metadata is present

::: notes
This exercise reinforces the workflow of treating Copilot as a junior developer who receives tasks and produces drafts.
:::

---

## Exercise: Delegating Work to Copilot

Duration
15 minutes
Objectives
Practice delegating multi-step tasks
Ensure Copilot follows architectural rules
Validate AI-generated remediation plans
Activities
Select a multi-step technical debt item.
Ask Copilot to:
  - Analyze the problem
  - Propose a remediation plan
  - Generate code changes
  - Update tests
  - Update documentation
Review Copilot's output.
Identify missing context or risks.
Success Criteria
Delegation prompt is complete and structured
Copilot produces a multi-step plan
Output is safe, incremental, and reversible
Human review identifies any gaps

::: notes
This exercise builds confidence in delegating larger tasks while maintaining safety and architectural alignment. Emphasize that humans remain the final reviewers.
:::

---
