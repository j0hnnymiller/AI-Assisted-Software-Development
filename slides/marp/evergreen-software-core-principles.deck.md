---
marp: true
theme: default
paginate: true
---
## Evergreen Software Development - Core Principles

Intent-First Design

- Define the system's purpose, invariants, and boundaries before writing code to ensure long-term clarity.
  Stable Interfaces, Evolving Internals
- Keep contracts predictable while allowing implementations to improve continuously.
  Continuous Regeneration with Guardrails
- Use AI to rewrite or extend components safely, backed by tests, specs, and architectural constraints.
  Modular, Replaceable Components
- Structure the system so any part can be regenerated, swapped, or upgraded without cascading breakage.
  Lifecycle Governance
- Maintain quality through automated tests, versioning discipline, and human-in-the-loop validation.

::: notes
Duration ~00:05

  Introduce Evergreen Software Development as a philosophy for building systems that can evolve indefinitely without degrading. This is crucial for AI-assisted development.

Explain each principle:

1. Intent-First Design: Document WHY before WHAT. AI can regenerate code but needs clear intent.
2. Stable Interfaces: Public contracts stay stable while implementations improve continuously.
3. Continuous Regeneration: AI can safely rewrite components when guardrails (tests, specs) exist.
4. Modular Components: Any piece can be regenerated without breaking the system.
5. Lifecycle Governance: Quality maintained through automation and human oversight.

Key insight: Traditional software rots over time. Evergreen software is designed to be continuously regenerated and improved.

Transition: "Let's see why software fails to be evergreen..."
:::

---

## Why Software Fails to Be Evergreen

Intent Rot

- The original purpose, constraints, and invariants are undocumented or lost, making safe regeneration impossible.
  Unstable or Leaky Interfaces
- APIs, data contracts, and boundaries change unpredictably, causing cascading breakage when internals evolve.
  Tightly Coupled Architecture
- Components depend on each other's internal details, preventing isolated regeneration or replacement.
  Insufficient Guardrails
- Missing tests, specs, or validation layers mean AI-assisted regeneration can't be trusted to preserve behavior.
  One-Off Patches and Drift
- Ad-hoc fixes accumulate, diverging the system from its intended design and making regeneration unsafe.

::: notes
Duration ~00:05

  Explain the common anti-patterns that prevent software from being evergreen. These are the enemies of long-term maintainability.

1. Intent Rot: Documentation becomes outdated or nonexistent. AI can't regenerate code when it doesn't know the purpose.
2. Unstable Interfaces: Breaking changes cascade through the system. AI regeneration requires stable contracts.
3. Tight Coupling: Changes in one component break others. AI can't safely regenerate tightly coupled code.
4. Insufficient Guardrails: Without tests and specs, AI-generated code can't be validated.
5. Drift: Ad-hoc fixes create divergence from the design. The system becomes unpredictable.

Real-world examples:

- Legacy system with no documentation (intent rot)
- Microservices with frequently changing APIs (unstable interfaces)
- Monolith with circular dependencies (tight coupling)

Transition: "Let's see how to avoid these pitfalls..."
:::
