---
marp: true
theme: default
paginate: true
---

# GitHub Copilot Training Day 5 Afternoon Session

::: notes
Session covers vertical slice implementation review, test coverage, architecture, troubleshooting, and lessons learned from the calculator app project. Exercises focus on architecture review and troubleshooting build/run issues.
:::

---

# Session Topics

- Review of vertical slice implementation (Slice 1)
- Test coverage and validation results
- Architecture overview: layers and patterns
- Performance and development best practices
- Troubleshooting build and run issues
- Lessons learned and next steps

::: notes

- Key points: Completed Slice 1, 100% test coverage, robust architecture, performance optimizations, troubleshooting pathing and build issues.
:::

---

# Vertical Slice Implementation Review

- Slice 1 completed: number entry, display, clear, backspace
- 36/30 tests passing, 100% test coverage
- Performance optimized with compiled bindings
- Error handling and cross-platform readiness
- Architecture validated on Windows

::: notes

- Success criteria: Enter single/multiple digit, decimal, negative numbers; display updates; clear/backspace work.
- Prompt: Showcase for slice one.
:::

---

# Architecture Overview

- Business/Object layer: core features, shared domain models, state management
- Presentation layer: MAUI, MVVM, XAML UI, value converters
- Test project: comprehensive feature and integration tests
- Patterns: CQRS, Mediator, MVVM, dependency injection, vertical slice

::: notes

- Key design patterns: CQRS, Mediator, MVVM, DI, vertical slice.
- Prompt: Talk me through the architecture and showcase.
:::

---

# Test Coverage & Validation

- 100% test coverage: 30 handler tests, 6 end-to-end workflows
- Scenarios: digit/decimal entry, clear, backspace, base operations, error conditions
- Validation: all tests pass, no memory leaks, UI responsiveness, proper DI

::: notes

- Functional and technical validation: all features and technical requirements met.
:::

---

# Performance & Best Practices

- Compiled XAML bindings, singleton state service, async operations
- Efficient state updates, SOLID principles, clean code
- Graceful error handling, testability, minimal code duplication
- XML documentation

::: notes

- Performance: core build ~5s, full build ~15s, tests ~2.4s, total ~11s.
:::

---

# Troubleshooting Build & Run Issues

- Pathing issues with terminal and VS Code settings
- Profile and workspace folder conflicts
- Strategies: adjust settings, specify project/solution in commands, check bin/obj folders
- Collaboration and iterative troubleshooting

::: notes

- Prompt: Troubleshoot build/run issues, adjust VS Code and PowerShell settings, specify project paths.
:::

---

# Lessons Learned & Next Steps

- Vertical slice architecture supports incremental, test-driven development
- Shared state service and CQRS enable clean separation of concerns
- Comprehensive testing catches edge cases early
- Ongoing need to refine build/run workflows and environment settings

::: notes

- Conclusion: Robust, future-ready architecture; continue refining workflows and troubleshooting environment issues.
:::

---

# Exercise: Architecture Review

**Duration:** 20 minutes

**Objectives:**

- Analyze the vertical slice architecture and design patterns
- Identify strengths and areas for improvement
- Relate patterns to project requirements

**Activities:**

1. Review the architecture and design patterns used
2. List strengths and potential improvements
3. Map patterns to project requirements

**Success Criteria:**

- Clear understanding of architecture
- Identified strengths and improvement areas
- Patterns mapped to requirements

::: notes
Prompt: Review and analyze the vertical slice architecture and design patterns.
:::

---

# Exercise: Troubleshooting Build/Run Issues

**Duration:** 15 minutes

**Objectives:**

- Practice diagnosing and resolving build/run issues
- Apply troubleshooting strategies to environment and settings
- Document solutions and lessons learned

**Activities:**

1. Simulate a build/run issue (e.g., pathing, settings conflict)
2. Apply troubleshooting steps (settings, commands, folder checks)
3. Record the solution and share with the group

**Success Criteria:**

- Issue diagnosed and resolved
- Solution documented
- Lessons learned shared

::: notes
Prompt: Troubleshoot and resolve build/run issues in the project environment.
:::

---

# Q&A and Wrap-Up

- Questions on architecture, testing, troubleshooting
- Discussion of lessons learned and next steps
- Final thoughts on the project and course

::: notes
Encourage participants to share experiences, ask questions, and discuss how to apply lessons learned in future projects.
:::
