---
marp: true
theme: default
paginate: true
---

## Evergreen Software Development - Core Principles

Intent‑First Design
  - Define the system’s purpose, invariants, and boundaries before writing code to ensure long‑term clarity.
Stable Interfaces, Evolving Internals
  - Keep contracts predictable while allowing implementations to improve continuously.
Continuous Regeneration with Guardrails
  - Use AI to rewrite or extend components safely, backed by tests, specs, and architectural constraints.
Modular, Replaceable Components
  - Structure the system so any part can be regenerated, swapped, or upgraded without cascading breakage.
Lifecycle Governance
  - Maintain quality through automated tests, versioning discipline, and human‑in‑the‑loop validation.

---

## Why Software Fails to Be Evergreen

Intent Rot
  - The original purpose, constraints, and invariants are undocumented or lost, making safe regeneration impossible.
Unstable or Leaky Interfaces
  - APIs, data contracts, and boundaries change unpredictably, causing cascading breakage when internals evolve.
Tightly Coupled Architecture
  - Components depend on each other’s internal details, preventing isolated regeneration or replacement.
Insufficient Guardrails
  - Missing tests, specs, or validation layers mean AI‑assisted regeneration can’t be trusted to preserve behavior.
One‑Off Patches and Drift
  - Ad‑hoc fixes accumulate, diverging the system from its intended design and making regeneration unsafe.


