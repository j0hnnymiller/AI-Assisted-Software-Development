---
marp: true
theme: default
paginate: true
title: Addressing Technical Debt
---

# **Addressing Technical Debt**

- Prompting Copilot to address debt
- Assigning issues to Copilot
- What Copilot does with assigned issues
- Exercises for hands-on practice

::: notes
Introduce this module as the moment where AI becomes an active contributor to modernization. Technical debt is inevitable in brownfield systems, but AI can help teams address it safely, incrementally, and with strong guardrails.
:::

---

# **Prompting Copilot to Address Technical Debt**

### Effective prompts include:

- Clear description of the debt
- Constraints and architectural rules
- Expected outcomes
- Required tests and documentation updates
- Provenance requirements

### Benefits

- Faster remediation
- Consistent application of patterns
- Reduced manual effort

::: notes
Explain that Copilot responds best to structured, high-signal prompts. The more explicit the constraints, the safer and more predictable the remediation.
:::

---

# **Assigning Issues to Copilot**

### How assignment works

- Convert technical debt into GitHub issues
- Provide context, constraints, and acceptance criteria
- Use Copilot to draft remediation steps
- Let Copilot propose code changes in PRs

### Why assign issues?

- Creates a repeatable workflow
- Keeps humans in the reviewer role
- Ensures traceability and provenance

::: notes
Assigning issues to Copilot formalizes the workflow. It treats Copilot like a junior developer who receives tasks, produces drafts, and awaits review.
:::

---

# **What Copilot Does With Assigned Issues**

### Copilot can:

- Generate proposed fixes
- Update tests
- Add documentation
- Suggest safer alternatives
- Flag missing context
- Produce PR descriptions with provenance

### Human responsibilities:

- Validate correctness
- Ensure architectural alignment
- Approve or request changes

::: notes
Reinforce that Copilot accelerates the work but does not replace human judgment. The human reviewer remains the final authority.
:::
