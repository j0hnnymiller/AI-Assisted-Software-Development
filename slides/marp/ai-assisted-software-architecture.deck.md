---
ai_generated: true
model: "anthropic/claude-sonnet-4.5@2026-03-18"
operator: "johnmillerATcodemag-com"
chat_id: "ai-assisted-software-architecture-20260925"
prompt: |
  create a marp slide deck on AI assisted software architecture
started: "2026-09-25T00:00:00Z"
ended: "2026-09-25T00:20:00Z"
task_durations:
  - task: "content outline"
    duration: "00:05:00"
  - task: "slide creation"
    duration: "00:10:00"
  - task: "speaker notes"
    duration: "00:05:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2026/09/25/ai-assisted-software-architecture-20260925/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# AI-Assisted Software Architecture || Designing Systems with an AI Co-Architect

---

## What Is AI-Assisted Software Architecture?

- Using AI as a collaborator across architectural decision-making, not just code generation
- AI participates in requirements analysis, pattern selection, tradeoff evaluation, and diagramming
- Human architects remain accountable for final decisions and system integrity
- Distinct from AI writing code: this is AI reasoning about structure, boundaries, and quality attributes

::: notes
Duration ~00:02

Open by framing the difference between AI-assisted coding (which most attendees already know) and AI-assisted architecture, which is a less familiar but rapidly growing practice.

**Key Points**:

- Architecture decisions have longer-lasting impact than individual code changes, so AI involvement here carries more risk and more value
- AI can rapidly explore tradeoff spaces (e.g., CQRS vs. CRUD, monolith vs. microservices) that would take a human hours to research
- The architect's role shifts from sole author to reviewer/curator of AI-proposed options

**Delivery**: Ask the audience how many currently use AI only for code completion vs. design discussions. Use their answer to set expectations for this module.

**Transition**: "Let's look at exactly where in the architecture lifecycle AI adds value."
:::

---

## Where AI Fits in the Architecture Lifecycle

| Lifecycle Stage       | AI Contribution                                                           |
| --------------------- | ------------------------------------------------------------------------- |
| Requirements analysis | Extracts business rules, identifies ambiguity, drafts acceptance criteria |
| Pattern selection     | Proposes candidate patterns (CQRS, event-driven, layered) with tradeoffs  |
| Decision records      | Drafts ADRs, documents alternatives considered and rejected               |
| Diagramming           | Generates C4/Mermaid diagrams from code or descriptions                   |
| Validation            | Flags inconsistencies between docs, diagrams, and implementation          |

::: notes
Duration ~00:03

This table is the backbone of the module — refer back to it as later slides go deeper on each row.

**Key Points**:

- AI contribution scales with how well-specified the input is; vague requirements produce vague architecture proposals
- Diagramming and ADR drafting are the fastest wins because they are largely mechanical once a decision is made
- Validation (catching drift between docs and code) is an underused but high-value use case

**Delivery**: Walk through each row briefly, noting that later slides expand on ADRs, tradeoff analysis, and diagramming specifically.

**Transition**: "Let's start with architecture decision records, since that's where most teams get immediate value."
:::

---

## AI for Architecture Decision Records (ADRs)

- AI drafts the standard ADR sections: Context, Decision, Consequences, Alternatives Considered
- Prompts can pull directly from instruction files, requirements docs, or existing code
- Human architect reviews and edits before the ADR is merged — AI drafts, humans decide
- Consistent ADR format makes AI-assisted history mining possible later (e.g., "why did we choose X?")

::: notes
Duration ~00:03

ADRs are one of the highest-leverage places to introduce AI because the format is repetitive and well-defined.

**Key Points**:

- Emphasize the "AI drafts, humans decide" principle — this recurs throughout the module and is core to governance
- A consistent ADR template lets AI later answer questions like "why did we choose CQRS over CRUD in the billing service?"
- Encourage teams to store ADRs in version control alongside code so AI tooling can reference them during future design work

**Delivery**: Show a short example ADR title/decision pair if time allows, or reference the CQRS Architecture deck as a related example.

**Transition**: "Once a decision is on the table, AI can also help evaluate the tradeoffs before you commit to an ADR."
:::

---

<!-- layout: Two Content -->

## AI-Assisted Tradeoff Analysis

**Where AI Helps**

- Enumerating pros/cons for competing patterns
- Surfacing non-functional requirements (scalability, consistency, latency)
- Identifying hidden coupling or shared-state risks
- Estimating relative implementation complexity

::: column

**Where Humans Must Lead**

- Weighing business priorities and organizational constraints
- Final risk tolerance decisions (e.g., eventual consistency acceptable?)
- Judging team skill and operational maturity
- Approving irreversible or costly architectural commitments

::: notes
Duration ~00:03

Tradeoff analysis is where AI is most useful as a research assistant, not a decision-maker.

**Key Points**:

- AI is good at breadth — listing many options and their known tradeoffs quickly
- Humans are needed for depth — judging which tradeoffs matter most in this specific organizational context
- A common failure mode is accepting an AI-proposed tradeoff table without validating it against real constraints (team size, budget, compliance)

**Delivery**: Use a live example if possible — ask Copilot to compare two patterns relevant to the audience's domain and critique the output together.

**Transition**: "Let's ground this in a pattern most of you already know: vertical slice architecture."
:::

---

## Vertical Slice Architecture + AI

- AI-assisted architecture pairs naturally with vertical slices: each slice is a self-contained unit AI can reason about end-to-end
- AI can scaffold a new slice (command, handler, validation, tests) from a single feature description
- Slice boundaries constrain AI's blast radius — changes stay contained to one feature at a time
- Reduces the risk of AI introducing cross-cutting architectural drift

::: notes
Duration ~00:03

Connect this back to the repository's own vertical-slice.instructions.md conventions so the audience sees the pattern applied consistently.

**Key Points**:

- Vertical slices give AI a bounded context, which produces more accurate and less risky suggestions than open-ended "add a feature" prompts
- Each slice can be independently tested and reviewed, which fits well with AI-generated scaffolding
- This is a good pattern to introduce AI-assisted architecture gradually, one slice at a time, rather than all at once

**Delivery**: If the audience has seen the CQRS Architecture deck, reference it directly — CQRS and vertical slices are frequently combined.

**Transition**: "Speaking of CQRS, let's look at how AI assists with event-driven and CQRS-style architectures specifically."
:::

---

## CQRS and Event-Driven Patterns with AI Assistance

- AI can propose command/query separation boundaries based on read vs. write access patterns in existing code
- Helps identify candidate events, aggregates, and consistency boundaries for event-driven designs
- Generates skeleton handlers, projections, and event schemas from natural-language descriptions
- Still requires human validation of eventual-consistency implications and failure-mode handling

::: notes
Duration ~00:02

Keep this slide brief since a full CQRS deck already exists — this is a bridge, not a deep dive.

**Key Points**:

- AI is effective at pattern-matching existing code to suggest where CQRS boundaries might already exist implicitly
- Event schema generation is a strong AI use case: it's mechanical, well-structured, and easy to validate
- Warn that AI will not reliably reason about eventual consistency failure modes — that's a human review responsibility

**Delivery**: Point attendees to the dedicated CQRS Architecture slide deck for a deeper treatment of this pattern.

**Transition**: "Beyond code and patterns, AI can also generate and validate the diagrams that document your architecture."
:::

---

## Generating and Validating Architecture Diagrams with AI

- AI generates C4 and Mermaid diagrams directly from code, requirements, or verbal descriptions
- Diagrams can be regenerated on demand, keeping documentation closer to the current state of the system
- AI can compare a diagram against the actual codebase and flag drift (missing components, stale relationships)
- Diagrams-as-code (Mermaid in Markdown) keep architecture visuals version-controlled alongside source

::: notes
Duration ~00:03

This is a highly visual, easy-to-demo capability — use it to re-energize the room if attendee attention is fading.

**Key Points**:

- Diagrams-as-code means architecture diagrams are reviewed in pull requests just like code, catching drift early
- AI-generated diagrams are a starting point, not a final artifact — always have an architect confirm accuracy
- Regenerating diagrams from code is far cheaper than manually maintaining hand-drawn diagrams that go stale

**Delivery**: If time allows, live-generate a small Mermaid C4 diagram from a snippet of repository code.

**Transition**: "All of this AI involvement in architecture only works safely with proper governance — let's cover that next."
:::

---

## Governance: Provenance, Guardrails, and Human-in-the-Loop

- Every AI-assisted architecture artifact (ADR, diagram, tradeoff analysis) should carry provenance metadata
- Instruction files and chat modes constrain how AI proposes architecture changes (see `.github/instructions/`)
- Human-in-the-loop review is mandatory before any AI-proposed architecture decision is merged
- Architecture review boards should treat AI-authored ADRs the same as human-authored ones — same scrutiny, same sign-off

::: notes
Duration ~00:03

This slide ties the module back to the repository's broader AI governance policies.

**Key Points**:

- Provenance metadata (model, operator, chat log) makes AI-assisted architecture decisions auditable later
- Instruction files act as guardrails — they encode organizational architecture standards the AI must follow
- Emphasize that "AI-authored" does not mean "lower scrutiny" — if anything, architecture decisions warrant more review, not less

**Delivery**: Reference this repository's own `ai-assisted-output.instructions.md` and `copilot-instructions.md` as a working example of governance in practice.

**Transition**: "Governance exists because AI-assisted architecture has real failure modes — let's name them directly."
:::

---

## Risks and Anti-Patterns

- **Hallucinated dependencies**: AI references libraries, services, or patterns that don't exist in the actual codebase
- **Over-engineering**: AI defaults to complex patterns (CQRS, microservices) when a simpler design would suffice
- **Stale pattern bias**: AI trained on older codebases may suggest outdated idioms for the current stack
- **Rubber-stamp review**: Reviewers approving AI-generated ADRs without genuinely evaluating tradeoffs
- **Undocumented drift**: Diagrams or ADRs generated once and never regenerated as the system evolves

::: notes
Duration ~00:03

This is the "yellow flag" slide — be direct about failure modes so the audience trusts the rest of the module.

**Key Points**:

- Hallucinated dependencies are especially dangerous in architecture because they can shape entire designs around something that doesn't exist
- Over-engineering is common because AI has seen many examples of "impressive" patterns and may over-apply them
- Rubber-stamp review is a process failure, not an AI failure — it's on the humans to maintain real scrutiny

**Delivery**: Ask if anyone has seen AI suggest a pattern that was clearly overkill for the problem — use their story as a discussion point.

**Transition**: "With those risks in mind, here's a practical end-to-end workflow for using AI safely in architecture work."
:::

---

## Practical Workflow: From Requirements to Architecture

1. Capture requirements and constraints in a structured document (business rules, NFRs, constraints)
2. Ask AI to propose 2-3 candidate architecture patterns with tradeoffs, not a single answer
3. Human architect selects a direction and asks AI to draft the ADR and initial diagram
4. Review ADR and diagram against real constraints (team skill, budget, compliance, timeline)
5. Use AI to scaffold the first vertical slice implementing the chosen pattern
6. Validate the implementation against the ADR and diagram; regenerate diagrams as the system evolves

::: notes
Duration ~00:03

This is the actionable takeaway slide — attendees should be able to follow this sequence directly after the session.

**Key Points**:

- Step 2 is critical: always ask for multiple options, never accept a single AI-proposed answer as the only path
- Step 4 is where governance and human judgment are non-negotiable
- Step 6 closes the loop — architecture artifacts should never be "write once, never touch again"

**Delivery**: Encourage attendees to try this workflow on a small, low-risk feature first before applying it to critical systems.

**Transition**: "Let's wrap up with a concise checklist you can take back to your team."
:::

---

## Best Practices Checklist

- [ ] Always request multiple architecture options from AI, not a single recommendation
- [ ] Store ADRs, diagrams, and tradeoff analyses in version control with provenance metadata
- [ ] Require human sign-off on every AI-proposed architecture decision
- [ ] Validate AI-generated diagrams against the actual codebase before publishing
- [ ] Prefer vertical slices to bound AI's reasoning and limit blast radius
- [ ] Regenerate diagrams and ADRs as the system evolves — treat them as living artifacts
- [ ] Watch for over-engineering; ask AI to justify complexity, not just propose it

::: notes
Duration ~00:02

Use this as a leave-behind slide — attendees should be able to screenshot or reference this list after the session.

**Key Points**:

- This checklist consolidates every principle covered in the module into actionable items
- Encourage teams to adapt this checklist into their own architecture review templates
- Reinforce that the goal is faster, better-documented architecture decisions — not fewer human decisions

**Delivery**: Give the audience a moment to read the list, then ask which item they think their team is weakest on today.

**Transition**: "Let's close with the key takeaways from this module."
:::

---

## Key Takeaways

- AI-assisted software architecture extends AI collaboration beyond code into design, decisions, and documentation
- AI accelerates research and drafting (ADRs, diagrams, tradeoff tables); humans retain final decision authority
- Governance and provenance make AI-assisted architecture decisions auditable and trustworthy over time
- Vertical slices and clear instruction files bound AI's reasoning and reduce architectural drift risk

::: notes
Duration ~00:02

Close the module by reinforcing the central theme: AI as co-architect, not autonomous architect.

**Key Points**:

- Summarize the "AI drafts, humans decide" principle one final time — it is the single most important takeaway
- Remind attendees that this module connects directly to CQRS Architecture and Vertical Slicing modules already covered
- Invite questions before moving to the next module

**Delivery**: Open the floor for questions and relate any question back to the practical workflow slide if attendees ask "how do I actually start doing this?"

**Transition**: "This wraps up AI-Assisted Software Architecture — next we'll move into [next module]."
:::
