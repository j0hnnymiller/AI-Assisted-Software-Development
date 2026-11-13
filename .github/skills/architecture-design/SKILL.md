---
name: architecture-design
description: "Create requirements-grounded system architecture designs covering components, data flows, security, deployment, technology choices, and implementation roadmaps. Use when designing a new system or reshaping an existing architecture; identifies missing constraints and labels recommendations and assumptions explicitly."
metadata:
  ai_generated: "true"
  model: "OpenAI/gpt-6.1-sol@unknown"
  operator: "jMM-at-CODETraining"
  chat_id: "7c5afae0-9dc2-465f-a19e-58cc8812f033"
  prompt: "update the architecture design skill to use semantic coloring in the mermaid diagrams"
  started: "2026-11-12T20:30:15-08:00"
  ended: "2026-11-12T20:30:19-08:00"
  task_durations: "Semantic diagram coloring guidance: 00:00:04"
  total_duration: "00:00:04"
  ai_log: "ai-logs/2026/11/12/7c5afae0-9dc2-465f-a19e-58cc8812f033/conversation.md"
  source: "user request; .github/instructions/mermaid.instructions.md"
  original_chat_id: "5f3c21d2-9cc6-4db3-b0dc-dd4ce14e99f7"
  original_source: ".github/prompts/architecture-design.prompt.md"
---

# Comprehensive System Architecture Design

Analyze the user's requirements and design a system architecture that makes its scope, components, data flows, quality attributes, and trade-offs clear. Ground decisions in supplied requirements and repository evidence where available.

## Procedure

1. **Clarify scope and requirements.** Identify functional needs, quality attributes, constraints, success criteria, and known current-state context. Ask concise questions when missing answers would materially change the design. Otherwise proceed with clearly stated assumptions.
2. **Assess the current state.** For brownfield work, review relevant systems, technologies, integrations, technical debt, team expertise, and resource constraints. Distinguish observed evidence from supplied claims and unknowns.
3. **Define architecture boundaries.** State system scope, actors, external dependencies, trust boundaries, and major data flows.
4. **Design components and interfaces.** Describe components, responsibilities, APIs or protocols, persistence, caching, and integration approaches. Avoid unnecessary complexity and specify alternatives where a requirement is unresolved.
5. **Evaluate patterns and quality attributes.** Explain pattern fit and trade-offs for scalability, maintainability, security, observability, resilience, and cost efficiency. Do not treat any principle as an unconditional design rule.
6. **Cover security and deployment.** Describe threat considerations, authentication/authorization, data protection, compliance questions, environments, runtime infrastructure, monitoring, logging, and recovery needs. Treat regulatory applicability as unconfirmed unless the user provides it.
7. **Recommend technologies carefully.** Tie choices to stated constraints and required capabilities. If current product features, prices, or support status are unknown, provide selection criteria instead of asserting current vendor facts.
8. **Create a phased roadmap.** Identify implementation phases, dependencies, validation criteria, risks, and success measures. Use TBD for unsupported owners, dates, costs, or performance targets.
9. **Summarize assumptions and open decisions.** List unknowns that could materially change the architecture and the evidence needed to resolve them.
10. **Validate diagrams.** Use Mermaid with semantic coloring for all architecture diagrams, not ASCII art or diagrams in plain-text code blocks. Follow the [Mermaid authoring instructions](../../instructions/mermaid.instructions.md), including target-renderer validation; report any unavailable rendering checks explicitly. This skill requires semantic coloring even though the general instructions make color optional.

## Output Format

### Architecture overview
System boundaries, actors, external integrations, core principles, and a high-level Mermaid diagram with semantic coloring. Use a fenced `mermaid` block in Markdown, never a plain-text or ASCII architecture diagram. Keep labels tied to described components.

### Requirements and constraints
Functional requirements, quality attributes, technical/business/regulatory/organizational constraints, success criteria, and assumptions.

### Component design
Components, responsibilities, APIs/protocols, data stores, persistence, caching, and key data flows.

### Architectural patterns
Selected patterns, fit, trade-offs, complementary patterns, and anti-patterns to avoid.

### Performance and scalability
Scaling approach, required metrics and targets, load distribution, caching, and known or potential bottlenecks. Clearly mark targets as supplied, measured, proposed, or TBD.

### Security and compliance
Threat considerations, identity and access, data protection, encryption, audit, resilience, and compliance questions. Do not claim compliance from design intent alone.

### Deployment and operations
Infrastructure/deployment model, environments, observability, monitoring, logging, recovery, and operational responsibilities.

### Technology recommendations
Recommended capabilities and, when evidence permits, candidate technologies with justification and alternatives.

### Implementation roadmap
Phases, dependencies, risks, validation gates, success measures, and any known resource or schedule constraints. Mark unsupported estimates TBD.

### Assumptions and open questions
List unresolved requirements and decisions that could change the design.

## Diagram Format

- Use Mermaid flowcharts for system/component boundaries and data flow, sequence diagrams for interactions, and ER diagrams for data relationships when those views help explain the design.
- Keep explanatory prose and tables; Mermaid replaces text-based diagrams, not the written specification.
- Keep diagrams focused and consistent with the documented design. Do not invent components or relationships to fill a diagram.
- If Mermaid rendering is unavailable, retain the Mermaid source and disclose the limitation rather than substituting an ASCII diagram.

### Semantic coloring

- Map colors to architectural roles or outcomes, never node order or decoration. Use the repository's semantic palette for decisions, success, warnings/retries, failures/rollback, and external systems when those roles occur; keep ordinary elements neutral.
- For component roles not covered by that palette, define a small, labeled mapping (for example, client, application, and data store). Reuse each role's meaning and colors across related diagrams and include a legend or adjacent explanation.
- Use reusable `classDef`/`class` roles where supported. For other diagram types, use styling supported by the target renderer; do not copy flowchart-only syntax into sequence or ER diagrams. If semantic styling is unsupported, disclose the limitation and retain explicit role labels rather than emitting invalid syntax.
- Set fill, stroke, and text colors together. Verify at least 4.5:1 normal-text contrast against its fill, and check light/dark themes and exports where relevant.
- Preserve meaning through labels, shapes, or branch text, not color alone. Inspect rendered labels, edges, clipping, and layout; disclose unavailable rendering or accessibility checks.

## Design Principles

- **Scalability**: Choose scaling mechanisms in response to workload and growth requirements, not by default.
- **Maintainability**: Prefer clear boundaries and modular responsibilities.
- **Security by design**: Identify trust boundaries and security controls early; avoid unsupported compliance claims.
- **Observability**: Define how operational behavior will be measured and diagnosed.
- **Resilience**: Address failure modes, recovery, and service continuity.
- **Cost efficiency**: Explain trade-offs, but do not invent pricing or savings.

## Boundaries

- This is an architecture design workflow, not an implementation request; do not modify code or infrastructure.
- Do not make external calls or claim current product capabilities, pricing, or regulatory requirements without evidence in the available context.
- Do not invent requirements, user volumes, performance targets, budgets, team capacity, owners, or timelines; ask or mark them TBD.
- State uncertainty and alternatives where evidence is insufficient.
