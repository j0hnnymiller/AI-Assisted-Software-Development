---
marp: true
theme: default
paginate: true
title: Building Safety Nets
---

# **Building Safety Nets**

- Protecting brownfield codebases
- Leveraging AI code reviews
- Effective human code reviews
- The role of test automation
- Exercise: Building safety nets in practice

::: notes
Introduce this module as the backbone of safe AI-assisted development. Safety nets ensure that modernization efforts do not destabilize working systems. Emphasize that brownfield systems deserve respect, and safety nets are how we honor that reality.
:::

---

# **Protecting Brownfield Codebases**

### Key Practices

- Preserve existing behavior unless intentionally changed
- Avoid large, risky refactors
- Use incremental modernization
- Maintain architectural boundaries
- Document every AI-assisted change

### Why it matters

- Brownfield systems run the business
- Stability is more important than novelty
- Safety nets reduce fear and increase confidence

::: notes
Reinforce that brownfield systems are valuable assets, not liabilities. Protection means minimizing risk, maintaining continuity, and ensuring that modernization is deliberate rather than accidental.
:::

---

# **Leveraging AI Code Reviews**

### AI can assist by:

- Highlighting risky changes
- Detecting missing tests
- Identifying architectural violations
- Suggesting safer alternatives
- Surfacing potential regressions

### Benefits

- Faster feedback loops
- More consistent review quality
- Early detection of drift

::: notes
AI code reviews are not replacements for human reviews — they are accelerators. They help catch issues early and provide a second set of eyes that never gets tired.
:::

---

# **Effective Human Code Reviews**

### Human reviewers focus on:

- Intent and correctness
- Architectural alignment
- Business logic validation
- Risk assessment
- Ensuring changes are incremental and reversible

### Best practices

- Review small change sets
- Ask for context when missing
- Validate AI-generated code with skepticism and curiosity

::: notes
Humans bring judgment, domain knowledge, and intuition — things AI cannot replicate. The combination of AI and human review creates a multi-layered safety net.
:::

---

# **The Role of Test Automation**

### Test automation provides:

- Behavioral guarantees
- Regression detection
- Confidence for modernization
- Guardrails for AI-assisted refactoring

### Types of tests

- Unit tests
- Integration tests
- End-to-end tests
- Snapshot and contract tests

::: notes
Test automation is the ultimate safety net. Without tests, AI-assisted development becomes guesswork. With tests, it becomes a controlled, predictable process.
:::

---

# **Exercise: Building the Safety Nets**

### Duration

20 minutes

### Objectives

- Identify missing safety nets in a brownfield system
- Strengthen protection using AI and human review practices
- Apply test automation principles
- Produce actionable improvements

### Activities

1. Select a brownfield module or file.
2. Identify existing safety nets (tests, reviews, documentation).
3. Ask AI to identify missing or weak safety nets.
4. Strengthen the safety nets by:
   - Adding or updating tests
   - Drafting review checklists
   - Documenting architectural constraints
5. Share findings with a partner for validation.

### Success Criteria

- Missing safety nets are clearly identified
- Proposed improvements are safe and incremental
- Test coverage or clarity is improved
- Review and documentation guardrails are strengthened

::: notes
Encourage participants to treat this as a real modernization planning session. The goal is not to fix everything — it's to identify gaps and build a roadmap for safer development.
:::
