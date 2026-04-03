---
marp: true
theme: default
paginate: true
---

## Exercise: Implementing a Feature Flag

**Objectives**

- Learn how to introduce a safe, reversible change
- Practice designing a feature flag workflow
- Understand As-Is and To-Be test implications
- Document rollout and retirement criteria

**Activities**

1. Select a small brownfield function or module
2. Identify a safe, incremental change to introduce
3. Design a feature flag with name, description, rollout plan, rollback plan, and retirement criteria
4. Write As-Is and To-Be test cases
5. Document the change with provenance metadata

**Success Criteria**: flag is scoped, rollout/rollback plans are explicit, tests are correct, retirement criteria are documented

::: notes
Duration ~00:20

Give students 20 minutes. Encourage them to select something real from their own codebases if possible — the exercise is more meaningful with familiar code. The feature flag design is more important than the implementation: students should be able to articulate why the flag exists, who can see the new behavior, and what evidence will trigger retirement. Circulate and ask teams to describe their rollback plan. Debrief: what made the boundary hard to define? What surprised you about writing As-Is tests?
:::
