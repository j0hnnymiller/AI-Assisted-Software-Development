---
marp: true
theme: default
paginate: true
---

﻿---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "welcome-back-slide-20260314"
prompt: |
  create a marp deck containing a slide welcoming attendees back. include a point for questions
started: "2026-03-14T15:46:54Z"
ended: "2026-03-14T15:47:00Z"
task_durations:
  - task: "draft"
    duration: "00:00:06"
total_duration: "00:00:06"
ai_log: "ai-logs/2026/03/14/welcome-back-slide-20260314/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Welcome Back || The Return of the Prompter

## Welcome Back to AI-Assisted Software Development

- Ready to continue where we left off
- Today's session builds on what we've covered
- We're all in this together — participation welcome
- **Questions are always welcome — ask anytime!**

::: notes
Duration ~00:02

Welcome everyone back to the session. Take a moment to let people settle in before diving into content. Acknowledge that it's great to see everyone back and express enthusiasm for the session ahead.

Key talking points:

- Remind attendees of the previous session's topics briefly
- Emphasize that questions are encouraged at any point — not just at the end
- Set a positive, inclusive tone for the session
- If this is after a break, give people 30 seconds to get re-focused

Transition: "Let's pick up right where we left off..."
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- **▶ Specification Driven Software Development**
- Architecture Specification
- Technology Specification
- Implementation Specification
- Implementation Planning
- Implementation Prompts
- Vertical Slice Implementation
- Code Review with GitHub Copilot

---

<!-- _class: lead -->

# Specification Driven Software Development

---

## Specification Driven Software Development

- High Level AI Assisted Workflow
- Starting with Project Requirements

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "convert-getting-started-checklist-20260326"
prompt: |
  convert "slides\pptx\_Getting Started Checklist.pptx" into a marp deck using #file:extract_pptx_to_marp.py
started: "2026-03-26T02:16:00Z"
ended: "2026-03-26T02:24:00Z"
task_durations:
  - task: "pptx extraction"
    duration: "00:02:00"
  - task: "deck normalization"
    duration: "00:04:00"
  - task: "provenance logging"
    duration: "00:02:00"
total_duration: "00:08:00"
ai_log: "ai-logs/2026/03/26/convert-getting-started-checklist-20260326/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Getting Started Checklist || The Recipe Before the Meal

## High Level AI Assisted Workflow

### From Requirements to a Solution

Stakeholders such as SMEs, architects, SREs, and DBAs define the requirements with AI assistance.

AI transforms the requirements into implementation instruction files that guide the work.

- Stakeholders review, improve, and approve the instruction files.

AI uses those instruction files to create prompts that implement the business requirements.

- Implementation prompts explain how the feature should be built and how acceptance criteria should be verified.
- Stakeholders review, improve, and approve the implementation prompts.

Submitting the implementation prompts produces an implementation that conforms to the instruction files and meets the acceptance criteria.

- Stakeholders review and approve the resulting implementation.

![Slide 3 image](marp/images/_Getting_Started_Checklist_slide03_5.png)

::: notes
Walk the audience through the lifecycle from left to right and keep the focus on the review gates between each AI-generated artifact. Stress that requirements are not handed directly to code generation; instead, they are refined into instruction files and then into implementation prompts, with stakeholder approval at each stage. Use the diagram to reinforce that this is a controlled pipeline where AI accelerates each step but humans still own correctness, safety, and acceptance. End by linking this workflow back to the checklist on the previous slides: foundation, automation, specialization, and integration all support this end-to-end model.
:::

---

# Starting with Requirements || Build the Right Thing Before Building the Thing Right

## Starting with Project Requirements

::: notes
Shift to greenfield best practices: requirements, prompts, and verification workflows.
:::

---




## Business Rules as Requirements

![Slide 2 image](marp/images/_Starting_with_Project_Requirements_slide02_4.png)

---




## Conceptual Models

Technology Agnostic
  - Transformable into Logical Models
Clarity
Expressive
Formal
Conceptual Models are not a requirement

---




## Object Role Models

A type of conceptual model
Supported by a Visual Studio Extension (NORMA)
Object Role Models are textual and visual
  - Text can be visualized
  - Diagrams can be verbalized
Textual representation is in a formal natural language that can be validated by subject matter experts

---




## Zeus.Academia.3b

Based on a publicly available model of a commonly understood domain
  - https://orm.net/pdf/ORMwhitePaper.pdf
Allows us to quickly move from requirements to implementation
  - https://github.com/johnmillerATcodemag-com/zeus.academia.3b
Why 3b?
  - Third Iteration in progress
  - If something is hard, do it often

---




## Use Cases

Use cases are specific scenarios that guide data capture and processing in the application
  - Promote a Lecturer to Senior Lecturer
  - Promote a Senior Lecturer to Associate Professor
  - Promote an Associate Professor to Professor
  - Assign a Class to an Academic
  - Add a new Academic to the faculty capturing all required information and allowing the capture of optional information

---

## Exercise: Generate Business Requirements

Objectives:
Use the Product Manager chat mode to create a requirements document for a calculator
Activities:
Activate the Product Manager chat mode
Prompt the AI to create a requirements document
Review the requirements
Add an implementation plan using vertical slices
Review the changes
Add a diagram showing the relationship between Phases, Slices, and User Stories
Success Criteria
The requirements document exists and passes review

::: notes
Duration ~00:20

Author requirement docs, then use Copilot to generate scaffolding and validate alignment.

Prompt: create a requirements document for a simple calculator application
:::

---

## Exercise: Generate Business Requirements

Objectives:
Use the Product Manager chat mode to update the requirements document to implement using vertical slices
Activities:
Activate the Product Manager chat mode
Prompt the AI to add a vertical slices implementation plan
Review the changes
Add a diagram showing the relationship between Phases, Slices, and User Stories
Success Criteria
The implementation plan passes review

::: notes
Duration ~00:20

Prompts:

using #file:business-rules-to-slices.instructions.md update the #file:calculator-app-requirements.md implementation plan to implement using vertical slices

what is the difference between the phases and vertical slices?

update the plan to make this distinction clear

add a diagram that shows the phases -> slices -> use cases

which of the slices can be implemented in parallel and which have a dependancy on another slice
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "business-requirements-generation-exercise-20260321"
prompt: |
  create an exercise marp slide using the slides\exercise-template.pptx template for the following:

  ## Section 2: Business Requirements Generation Exercise (Duration: 00:17:04) [x]

  ### Key Topics

  - Hands-on exercise: Creating business requirements document
  - Using product manager agent
  - Working with instruction files
  - Version control and branching strategy
  - Individual work on requirements documents

  ### Subsections

  #### 2.1: Exercise Instructions (Duration: 00:03:00)

  - Create personal branch from Greenfield branch
  - Use product manager agent to generate requirements
  - Utilize existing instruction files
  - Build calculator requirements document

  #### 2.2: Questions and Clarifications (Duration: 00:05:00)

  - Repository clarification (AIASD-2026 class repo, not Zeus Academia 3)
  - Branch strategy: personal branches off Greenfield
  - Differences between Visual Studio and VS Code performance discussion
  - Existing PRD handling

  #### 2.3: Working Time and Support (Duration: 00:09:04)

  - Students work independently on requirements generation
  - Instructor available for questions
  - Periodic check-ins for completion status
  - Discussion of instruction file effectiveness
started: "2026-03-21T08:40:31.8154189-07:00"
ended: "2026-03-21T08:47:31.8154189-07:00"
task_durations:
  - task: "template mapping"
    duration: "00:02:00"
  - task: "exercise authoring"
    duration: "00:03:00"
  - task: "provenance and catalog updates"
    duration: "00:02:00"
total_duration: "00:07:00"
ai_log: "ai-logs/2026/03/21/business-requirements-generation-exercise-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Exercise: Business Requirements Generation || Exercise: Let the AI Write the Requirements for Once

## Exercise: Business Requirements Generation

Objectives

- Create a business requirements document for the calculator project
- Use the Product Manager agent with existing instruction files
- Apply the expected branch and repository workflow for Greenfield work
- Validate the requirements draft through review, clarification, and independent iteration

Activities

1. Create a personal branch from the Greenfield branch in the class repository.
2. Use the Product Manager agent to generate a calculator requirements document.
3. Apply the existing instruction files to improve scope, structure, and consistency.
4. Confirm repository choice, branching strategy, and how to handle any existing PRD content before continuing.
5. Work independently on the requirements document while the instructor provides check-ins and support.

Success Criteria

- A calculator business requirements document exists on the correct personal branch
- The Product Manager agent and instruction files are both used effectively
- Repository and branching decisions are applied correctly and consistently
- Participants can explain what changed after clarifications and independent refinement

::: notes
Duration ~00:17

## Business Requirements Generation Exercise Instructions

**Prerequisites:** Access to the Greenfield branch, ability to create a personal branch, and access to the Product Manager agent plus the repository instruction files

Use this exercise to establish the Greenfield workflow discipline early. Start by making participants branch from Greenfield before they do any prompting so the requirements artifact has a clean ownership path and can be reviewed independently later. In the first few minutes, emphasize that the goal is not to produce a perfect PRD in one pass, but to create a usable calculator requirements document using the Product Manager agent together with repository guidance. During the clarification window, call out the common confusion points explicitly: correct repository, personal branch strategy, what to do with any existing PRD material, and that tooling differences between Visual Studio and VS Code are secondary to getting the requirements quality right. For the working block, let students operate independently, but use periodic check-ins to see whether instruction files improved the output and whether anyone is stuck on scope, branching, or prompt quality. Transition from this exercise by connecting the completed requirements document to the next Greenfield planning steps, especially technology instructions, slice planning, and implementation prompts.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Specification Driven Software Development
- **▶ Architecture Specification**
- Technology Specification
- Implementation Specification
- Implementation Planning
- Implementation Prompts
- Vertical Slice Implementation
- Code Review with GitHub Copilot

---

<!-- _class: lead -->

# Architecture Specification

---

## Architecture Specification

- Command Query Responsibility Segregation Architecture

---

﻿---
ai_generated: true
model: "anthropic/claude-sonnet-4.5@2026-03-18"
operator: "johnmillerATcodemag-com"
chat_id: "merge-marp-decks-20260318"
prompt: |
  Follow instructions in merge-marp-decks.prompt.md — create individual Marp slide deck
  from .github/instructions/cqrs-architecture.instructions.md
started: "2026-03-18T22:41:07Z"
ended: "2026-03-18T22:55:00Z"
task_durations:
  - task: "content analysis"
    duration: "00:03:00"
  - task: "slide creation"
    duration: "00:08:00"
  - task: "speaker notes"
    duration: "00:03:00"
total_duration: "00:14:00"
ai_log: "ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md"
source: ".github/prompts/merge-marp-decks.prompt.md"
marp: true
theme: default
paginate: true
---
# CQRS Architecture || Reads and Writes: Better Apart, Like Most Couples

## Command Query Responsibility Segregation Architecture

_AI-Assisted Software Development_

::: notes
Duration ~00:01

Welcome to the CQRS Architecture module. This session covers Command Query Responsibility Segregation — a pattern that separates read and write operations into distinct models to improve scalability and maintainability.

**Key Points**:

- CQRS separates write (command) operations from read (query) operations
- Enables independent scaling and optimization of each model
- Useful when read and write workloads have very different characteristics

**Delivery**: Begin by asking the audience about pain points with traditional CRUD APIs — high query complexity, slow writes due to query-optimized schemas, or contention between reads and writes.

**Transition**: "Let's start with when CQRS makes sense — and when it doesn't."
:::

---

## When to Use CQRS

**✅ Use CQRS when:**

- Read and write workloads scale differently
- Read models need denormalization, caching, or projections
- Write model needs strong invariants and task-focused workflows
- Auditing or event sourcing is required
- Query complexity slows transactional throughput

**❌ Avoid CQRS when:**

- Domain is small and reads/writes are balanced
- No clear boundary between commands and queries
- Operational overhead is not justified

::: notes
Duration ~00:03

CQRS is a powerful pattern but it adds operational complexity. Use it only when the benefits outweigh the costs.

**Key Points**:

- The classic CRUD pattern couples reads and writes to the same model — fine for simple domains
- CQRS shines when the query model needs to be radically different from the write model
- Event sourcing almost always pairs with CQRS
- Small teams or simple domains should avoid CQRS due to added complexity

**Real-World Example**: An e-commerce order system where writes go through strict business validation but reads need highly denormalized views for catalog search, order history dashboards, and analytics.

**Audience Question**: "Has anyone implemented something like CQRS without knowing it had a name?"

**Transition**: "Let's look at the core principles that underpin CQRS."
:::

---

## Core Principles

| Principle        | Detail                                            |
| ---------------- | ------------------------------------------------- |
| **Separation**   | Commands change state; queries never change state |
| **Invariants**   | Write model enforces all business rules           |
| **Optimization** | Read model is shaped for query use cases          |
| **Independence** | Models can evolve separately                      |
| **Consistency**  | Eventual consistency between write and read       |

> Commands can fail. Queries should not.

::: notes
Duration ~00:02

These five principles guide every CQRS implementation decision.

**Key Points**:

- The read/write separation is absolute — queries must be side-effect free
- Write model is where business logic lives — all invariants enforced here
- Read models are projections built from the write model's events
- Independence is key — you can evolve the read schema without touching write logic
- Eventual consistency is usually acceptable; design for it intentionally

**Common Misconception**: CQRS does not require separate databases. You can start with a single database and separate logical models before introducing physical separation.

**Transition**: "What are the actual architectural components we need to build?"
:::

---

<!-- layout: Two Content -->

## Architecture Components

```
┌─────────────┐    ┌──────────────────┐    ┌────────────┐
│  Command    │───▶│  Command Handler  │───▶│ Write Store│
│    API      │    │  (Domain Logic)   │    │  (OLTP)    │
└─────────────┘    └──────────────────┘    └─────┬──────┘
             │ Events
       ┌──────────────────┐          ▼
┌─────────────┐    │    Projection    │    ┌────────────┐
│  Query API  │◀───│    Updater       │◀───│  Publisher │
└─────────────┘    └──────────────────┘    └────────────┘
  │                                  ┌────────────┐
  └─────────────────────────────────▶│ Read Store │
             │  (OLAP)    │
             └────────────┘
```

::: column

**Minimum components**

- **Command API** — receives write requests
- **Command Handler** — enforces domain rules
- **Write Store** — authoritative OLTP system
- **Publisher** — emits events reliably
- **Projection Updater** — rebuilds read models
- **Query API** — serves optimized reads
- **Read Store** — denormalized query model

::: notes
Duration ~00:03

This diagram shows the minimum components for a CQRS implementation.

**Walk Through the Diagram**:

1. Command API receives write requests and routes to handlers
2. Command Handler orchestrates domain logic and writes to the Write Store
3. Events are published after successful writes
4. Projection Updater subscribes to events and updates the Read Store
5. Query API serves the Read Store with fast, optimized queries

**Key Components**:

- **Command API**: Validates input, routes to appropriate handler
- **Command Handler**: Enforces invariants, orchestrates domain operations
- **Write Store**: OLTP database for aggregates and consistency
- **Event Publisher**: Reliable event emission (use outbox pattern)
- **Projection Updater**: Maintains read models from events
- **Query API**: Serves denormalized, query-optimized data
- **Read Store**: OLAP or document store optimized for reads

**Transition**: "Let's look at command model design in more detail."
:::

---

## Command Model Design

**Commands** — task-based, intention-revealing names:

- 'CreateOrder' / 'ApproveOrder' / 'CancelOrder'
- 'RegisterUser' / 'UpdateShippingAddress'

**Rules**:

1. Validate at the command boundary — reject early
2. Use aggregates to enforce invariants and consistency
3. Keep handlers deterministic and side-effect controlled
4. Write to a single source of truth
5. One command targets one aggregate root

::: notes
Duration ~00:03

Good command design is the foundation of a maintainable CQRS system.

**Key Points**:

- Task-based command names reveal business intent — much better than 'UpdateOrder'
- Aggregates are the consistency boundary — they decide if a command is valid
- Early validation prevents unnecessary database round-trips
- A single aggregate per command keeps transactions simple
- Side effects (email, events) should happen after the transaction commits

**Code Example**:

```csharp
public record ApproveOrderCommand(Guid OrderId, string ApprovedBy);

public class ApproveOrderHandler : ICommandHandler<ApproveOrderCommand>
{
public async Task Handle(ApproveOrderCommand cmd)
{
var order = await _repo.GetAsync(cmd.OrderId);
order.Approve(cmd.ApprovedBy);  // Aggregate enforces rules
await _repo.SaveAsync(order);
await _publisher.PublishAsync(new OrderApprovedEvent(order.Id));
}
}
```

**Transition**: "Now for query model design."
:::

---

## Query Model Design

**Queries** — shaped for the consumer use case:

- Avoid joins and complex calculations at query time
- Use projections updated from events or change feeds
- Keep models versioned and rebuildable
- Optimize for latency and throughput

**Types**:
| Query Type | Example | Store |
|-----------|---------|-------|
| List/Search | Product catalog | Elasticsearch |
| Detail | Order details | Relational DB |
| Analytics | Revenue dashboards | OLAP / Data Warehouse |

::: notes
Duration ~00:02

The query model is designed entirely around how data will be consumed.

**Key Points**:

- Query models are "read-only databases" shaped for specific views
- Different query types may use different storage technologies
- Projections are pre-computed at write time, not at query time
- Rebuilding a projection means replaying events through the updater

**Design Tip**: Start by designing the query response first, then work backward to what the projection needs to store.

**Practical Consideration**: Version your projections. When you change a query model, you'll need to rebuild it from the event history.

**Transition**: "Let's talk about consistency — one of the most challenging aspects of CQRS."
:::

---

## Consistency Strategy

**Strong Consistency** — needed for:

- Payments and financial transactions
- Inventory management
- Security and access control

**Eventual Consistency** — acceptable for:

- Activity feeds and notifications
- Analytics dashboards
- Search indexes and recommendations

**Reliable Event Publication** — use the Outbox Pattern:

> Write event to database table atomically with domain change → background process publishes → idempotent consumers

::: notes
Duration ~00:03

Consistency is often the most debated aspect of CQRS implementations.

**Key Points**:

- Not all data requires strong consistency — choosing the right model reduces complexity
- The Outbox Pattern is the industry standard for reliable event publishing
- "Dual writes" (write to DB and publish in the same transaction) are dangerous — use the outbox
- Idempotent consumers handle duplicate event delivery gracefully

**The Outbox Pattern**:

1. Within the same database transaction: write the domain change AND an outbox event record
2. A background process reads unprocessed outbox events and publishes them to the message broker
3. Mark events as processed after successful publication
4. Consumers handle duplicates idempotently

**Transition**: "What common mistakes should we avoid?"
:::

---

## Anti-Patterns to Avoid

| Anti-Pattern                      | Problem                       | Solution                      |
| --------------------------------- | ----------------------------- | ----------------------------- |
| Mixed query in command handler    | Breaks separation of concerns | Query read model separately   |
| Shared ORM model for reads/writes | Couples both models           | Use separate query DTOs       |
| CQRS on simple CRUD               | Unnecessary complexity        | Use simple repository pattern |
| Dual writes without outbox        | Risk of lost events           | Implement outbox pattern      |

::: notes
Duration ~00:02

These anti-patterns are the most common mistakes in CQRS implementations.

**Key Points**:

- The most common mistake is reading from the write store in a query context
- Sharing a single ORM model defeats the purpose of model separation
- Over-engineering is real — CQRS adds complexity that's only worth it in the right domains
- Dual writes (write to database AND directly to message broker) will eventually lose events

**Red Flag**: If your CQRS system has more infrastructure than business logic, you've likely over-applied the pattern.

**Transition**: "Let's look at how to migrate an existing system to CQRS incrementally."
:::

---

<!-- layout: Two Content -->

## Migration Strategy

**Start small, migrate incrementally**

1. **Identify** one bounded context or high-value feature
2. **Split read model** first while keeping the write model intact
3. **Add projections** and the read store incrementally
4. **Introduce event publishing** after the write flow is stable
5. **Expand** to additional contexts over time

::: column

**Quality checklist**

- Command and query models are clearly separated
- Write model enforces all invariants
- Event publication is reliable through outbox or equivalent
- Projection updates are idempotent and monitored

::: notes
Duration ~00:02

Incremental migration reduces risk and allows the team to learn the pattern gradually.

**Key Points**:

- Big-bang migrations almost always fail — start with one context
- Splitting the read model first gives immediate query performance wins without disrupting writes
- Monitoring projection lag is essential once you go to production
- The checklist should be part of every CQRS code review

**Success Story Pattern**: Start with the reporting/analytics use case — these almost always benefit from a separate read model and the risk is lower than transactional paths.

**Transition**: "Let's look at a concrete flow example to tie it all together."
:::

---

## Example: Order Approval Flow

**Command flow (write)**:

1. API receives 'ApproveOrder' command
2. Command handler loads 'Order' aggregate
3. Aggregate validates approval rules
4. Transaction commits to write store
5. 'OrderApproved' event published via outbox

**Query flow (read)**:

1. UI requests order summary dashboard
2. Query API reads 'OrderSummary' projection
3. Read store returns denormalized view
4. Response includes 'lastUpdatedUtc' for freshness indicator

::: notes
Duration ~00:02

Tying the concepts together with a concrete example makes the pattern tangible.

**Key Points**:

- The command and query flows are completely independent paths
- The event bridges the write and read sides asynchronously
- 'lastUpdatedUtc' in the query response lets the UI show freshness information
- The UI can display a "processing" indicator while the projection catches up after a command

**Discussion Question**: "What are the tradeoffs of showing the read model data vs. the command result directly after an approval?"

**Key Takeaway**: CQRS is not magic — it's a deliberate architectural choice that pays off when reads and writes truly have different requirements.
:::

---

<!-- layout: Two Content -->

## Key Takeaways

**Core reminders**

- Separate commands from queries at the architectural level
- Use CQRS when read and write workloads differ materially
- Use the outbox pattern for reliable event publication
- Design for eventual consistency intentionally
- Start small and migrate one context at a time

::: column

**Further reading**

- Martin Fowler: 'martinfowler.com/bliki/CQRS.html'
- Transactional outbox: 'microservices.io/patterns/data/transactional-outbox.html'
- Greg Young's CQRS documents

::: notes
Duration ~00:02

Summarize the key points and provide resources for deeper learning.

**Summary**:

- CQRS separates write models (commands) from read models (queries)
- Use it when the complexity pays off — don't over-apply
- Reliable event publication requires the outbox pattern
- Eventual consistency is the norm — manage client expectations
- Incremental migration is the safe approach

**Call to Action**: Review the 'cqrs-architecture.instructions.md' file in the repository for implementation checklists and code examples.

**Q&A**: Open the floor for architecture questions and real-world implementation challenges.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Specification Driven Software Development
- Architecture Specification
- **▶ Technology Specification**
- Implementation Specification
- Implementation Planning
- Implementation Prompts
- Vertical Slice Implementation
- Code Review with GitHub Copilot

---

<!-- _class: lead -->

# Technology Specification

---

## Technology Specification

- Technology Stack Instruction Files

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "technology-stack-instruction-files-20260321"
prompt: |
  create a marp deck explaining the following content:

  ## Section 5: Technology Stack Instruction Files (Duration: 00:17:00) [x]

  ### Key Topics

  - Creating instruction files for specific technologies
  - HTML5, CSS3, and vanilla JavaScript standards
  - Command-line prompt for instruction file generation
  - Model differences (Claude Sonnet vs. GPT-4)
  - Validation checklists
  - Multi-model evaluation strategy

  ### Subsections

  #### 5.1: Creating Technology Instructions (Duration: 00:08:00)

  - Review requirements document for technology stack
  - Simple prompt: "Create instruction files for the following technologies"
  - HTML5, CSS, vanilla JavaScript (or TypeScript alternative)
  - Comprehensive coverage: semantic markup, accessibility, modern CSS, security, performance

  #### 5.2: Instruction File Review (Duration: 00:05:00)

  - Generated file structure and content review
  - Validation checklist inclusion
  - Target audience: AI assistants (primary), developers (secondary)
  - Comprehensive guidelines for semantic HTML5, CSS3, vanilla JavaScript
  - Security and performance considerations
  - Related documentation references

  #### 5.3: Multi-Model Evaluation (Duration: 00:04:00)

  - Using different models to review instruction files (e.g., Gemini reviewing Claude output)
  - Comparing outputs to identify improvements
  - Building instruction files from multiple sources
  - Model-specific characteristics (Claude Sonnet: comprehensive, GPT-4: variable)
  - Importance during foundation phase
started: "2026-03-21T15:34:00Z"
ended: "2026-03-21T15:49:00Z"
task_durations:
  - task: "slide outline"
    duration: "00:04:00"
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and catalog updates"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/technology-stack-instruction-files-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Technology Stack Instruction Files || Teaching Your AI the House Rules for Every Room

<!-- _class: lead -->

## Technology Stack Instruction Files

- Section focus: turning requirements into tech-specific guidance
- Outcome: show how teams generate, review, and improve instruction files for HTML5, CSS3, and JavaScript work

::: notes
Duration ~00:17

Frame this section as part of the greenfield foundation work rather than a documentation side quest. Explain that instruction files help the AI and the team align on standards before implementation begins, which reduces drift and rework later. Transition by asking what should exist before anyone prompts for technology-specific instructions.
:::

---

## Start with the Requirements

- Review the requirements document before generating any instruction file
- Identify the front-end and implementation technologies explicitly in scope
- Decide whether the stack is HTML5, CSS3, vanilla JavaScript, or a TypeScript variant
- Use the requirements to anchor standards, constraints, accessibility, and security expectations

```mermaid
flowchart LR
    A[Requirements document] --> B[Technology inventory]
    B --> C[Instruction file prompt]
    C --> D[Draft standards and rules]
```

::: notes
Duration ~00:02

Explain that instruction files are most valuable when they reflect the actual technology choices and constraints of the project. If the requirements are vague, the generated guidance will also be vague, so the stack definition has to come first. Transition by showing the simple prompting pattern used to produce the first draft.
:::

---

## Generate the First Draft Quickly

- Use a direct prompt such as: **Create instruction files for the following technologies**
- Name the stack clearly: HTML5, CSS, vanilla JavaScript, or TypeScript
- Ask for guidance on:
  - semantic markup
  - accessibility
  - modern CSS practices
  - security
  - performance
- Treat the first output as a draft, not as final policy

::: notes
Duration ~00:02

Make the point that the initial prompt does not need to be elaborate to be useful. What matters is that it clearly names the technologies and asks for standards that map to real development concerns like semantics, accessibility, and runtime performance. Transition by moving from prompt generation to what a good instruction file should contain.
:::

---

## What a Strong Instruction File Covers

**HTML5**

- semantic structure
- accessible forms and landmarks

**CSS3**

- maintainable selectors
- layout standards and responsive design

**JavaScript or TypeScript**

- safe DOM interaction
- modularity, validation, and performance guardrails

**Cross-cutting concerns**

- security considerations
- performance expectations
- links to related repository guidance

::: notes
Duration ~00:03

Walk through the content categories rather than reading the bullets verbatim. The core idea is that each technology file should move beyond syntax tips and instead define operational expectations for how code should be written in this repository. Transition by describing how the team reviews the generated file before relying on it.
:::

---

## Review the Generated File Critically

- Check the file structure, scope, and clarity
- Ensure a validation checklist is included
- Confirm the primary audience is **AI assistants** and the secondary audience is **developers**
- Verify security and performance guidance is concrete
- Confirm related documentation references are present and accurate

```mermaid
flowchart TB
    A[Generated instruction file] --> B[Structure review]
    A --> C[Checklist review]
    A --> D[Security and performance review]
    A --> E[Reference validation]
```

::: notes
Duration ~00:02

Explain that review is what turns an acceptable draft into a dependable working standard. Teams should inspect whether the file is actionable for the AI, readable for humans, and explicit enough to guide consistent output across sessions. Transition by introducing the role of multiple models in improving quality.
:::

---

## Use Multiple Models to Improve Quality

- Ask a second model to review the first model's output
- Compare tone, completeness, and specificity
- Pull strengths from more than one model into the final file
- Use differences to reveal gaps, ambiguity, or weak examples

| Model tendency                    | Practical takeaway                          |
| --------------------------------- | ------------------------------------------- |
| Claude Sonnet: more comprehensive | Good for broad first drafts                 |
| GPT-4: more variable              | Good candidate for challenge and comparison |

::: notes
Duration ~00:02

Position multi-model review as a quality-control tactic rather than a competition. Different models expose different blind spots, so having one model critique another often surfaces missing examples, incomplete checklists, or weakly stated rules. Transition by tying this evaluation loop back to the broader foundation phase of a new project.
:::

---

## Why This Matters in the Foundation Phase

1. Establish technology standards early
2. Reduce inconsistency before implementation begins
3. Give AI assistants reusable, repo-specific guidance
4. Create artifacts the team can iterate on and version-control
5. Build a stronger base for later slice planning and implementation prompts

**Bottom line**: better instruction files lead to more reliable implementation output.

::: notes
Duration ~00:02

Close by connecting technology instruction files to the larger greenfield workflow. These files are foundational because they shape the quality of later prompts, implementation plans, and generated code, especially when multiple people and multiple models are involved. End by suggesting that every new stack choice should trigger the question, what instruction file do we need before we start building?
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Specification Driven Software Development
- Architecture Specification
- Technology Specification
- **▶ Implementation Specification**
- Implementation Planning
- Implementation Prompts
- Vertical Slice Implementation
- Code Review with GitHub Copilot

---

<!-- _class: lead -->

# Implementation Specification

---

## Implementation Specification

- Vertical Slicing Architecture Introduction

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@2026-03-21"
operator: "johnmillerATcodemag-com"
chat_id: "vertical-slicing-architecture-introduction-20260321"
prompt: |
  create a marp deck explaining the following content:

  ## Section 6: Vertical Slicing Architecture Introduction (Duration: 00:19:00) [x]

  ### Key Topics

  - Vertical slicing architectural pattern
  - Feature-based organization vs. layered approach
  - Self-contained, independent features
  - Maintainability benefits
  - CQRS (Command Query Responsibility Segregation) relationship
  - Developer experience improvements

  ### Subsections

  #### 6.1: Vertical Slicing Concepts (Duration: 00:08:00)

  - **Definition**: Architectural pattern organizing code by features rather than layers
  - **Characteristics**:
    - Spans all technical layers vertically
    - Everything needed for a feature in one place
    - Self-contained and independent
    - Features don't directly reference each other
    - Localized changes improve maintainability

  #### 6.2: File Structure Comparison (Duration: 00:03:00)

  - **Layered Approach**: Controllers, Services, Repositories, Models (separate folders)
  - **Vertical Slices**: Features folder with sub-folders per feature
    - Example: Features/UserRegistration/ contains all user registration code
    - All code for a feature in single location
    - Easy to enhance or modify specific features

  #### 6.3: Benefits (Duration: 00:05:00)

  - **Developer Experience**:
    - Faster feature development
    - All related code in single location
    - No folder jumping
    - New features don't affect existing ones
  - **Maintainability**:
    - Localized changes
    - Clear boundaries reduce bugs
    - Feature-contained refactoring
  - **Team Collaboration**:
    - Parallel feature development
    - Fewer merge conflicts
    - Clear ownership and responsibility
  - **Testing**:
    - Test complete features, not layers
    - Mock at feature boundaries
    - Independent work with mocked dependencies
    - Straightforward integration

  #### 6.4: CQRS Relationship (Duration: 00:03:00)

  - Command Query Responsibility Segregation overview
  - Separate display (read) from data collection (write)
  - Two different stacks joined by messaging
  - Optimize read side for performance (denormalization, caching)
  - Optimize write side for data updates
  - Natural fit with vertical slices: implement read/write portions simultaneously per feature
started: "2026-03-21T17:19:32Z"
ended: "2026-03-21T17:33:30Z"
task_durations:
  - task: "content planning"
    duration: "00:04:00"
  - task: "slide authoring"
    duration: "00:07:00"
  - task: "speaker notes and repo updates"
    duration: "00:03:00"
total_duration: "00:14:00"
ai_log: "ai-logs/2026/03/21/vertical-slicing-architecture-introduction-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Vertical Slicing Architecture Introduction || Features Go Vertical. Layers Go Home.

## Vertical Slicing Architecture Introduction

### Organizing software around features instead of layers

*AI-Assisted Software Development*

::: notes
Duration ~00:01

Welcome to the vertical slicing architecture introduction. This section explains why organizing code by feature can make complex systems easier to understand, extend, and maintain.

Open by asking how many people have had to change a feature by touching controllers, services, repositories, and models in four different folders.

Emphasize that vertical slicing is not just a folder rename. It changes how teams think about boundaries, ownership, and end-to-end feature delivery.

Transition with: "Let's define the pattern first, then compare it to the layered structure most teams already know."
:::

---




## What is a vertical slice?

**A vertical slice organizes code by business feature, not by technical layer.**

- Each feature spans UI, validation, logic, and data access
- Everything needed for the feature lives together
- Slices are self-contained and intentionally independent
- Features avoid direct references to other features
- Changes stay localized, which improves maintainability

> Think in complete user capabilities, not shared technical buckets.

::: notes
This is the core idea for the section, so spend roughly three minutes here. Explain that a slice is a full path through the system for one business capability, such as user registration or order checkout.

Point out that the goal is strong feature boundaries. A developer should be able to open one folder and understand most of what matters for that feature without navigating the whole solution.

Call out the independence rule explicitly: features should not directly reference each other. Shared abstractions can exist, but the feature itself should remain loosely coupled.

Transition with: "That definition becomes clearer when we compare the file structure side by side."
:::

---

## Layered folders vs. feature folders

```mermaid
flowchart LR
    subgraph L["Layered approach"]
        C["Controllers"]
        S["Services"]
        R["Repositories"]
        M["Models"]
    end

    subgraph V["Vertical slices"]
        F1["Features/UserRegistration<br/>Command<br/>Handler<br/>Validator<br/>Result"]
        F2["Features/OrderCheckout<br/>Command<br/>Handler<br/>Validator<br/>Result"]
    end
```

**Layered:** related code is separated by technical type.

**Vertical slices:** all code for a feature is kept in one place.

::: notes
Duration ~00:03

Use about three minutes here and walk the audience through the diagram from left to right. In the layered view, explain that user registration logic is split across multiple folders, which creates navigation overhead and makes changes feel scattered.

Then move to the vertical slice view and show how each feature becomes a mini-application. The 'Features/UserRegistration' folder contains the command, handler, validator, and any related response or data access pieces in one place.

This is a good moment to mention that enhancing one feature becomes easier because the impact area is much more visible. The file structure starts reflecting business capabilities instead of technical plumbing.

Transition with: "Once the structure changes, the day-to-day developer experience changes too."
:::

---

## Why developers like this approach

### Developer experience

- Faster feature development
- All related code in one location
- Less folder jumping during implementation
- New features are less likely to disturb existing ones

### Maintainability

- Localized changes
- Clear boundaries reduce accidental bugs
- Refactoring happens inside the feature more often than across the whole app

::: notes
Duration ~00:03

 Describe the common experience of implementing a new feature in a layered system, where developers bounce between folders just to follow one request from start to finish.

Contrast that with a vertical slice where the work stays mostly inside one feature folder. That reduces cognitive load and makes it easier for a developer to reason about the full behavior before they edit anything.

For maintainability, stress that the architecture makes the blast radius of a change smaller. When the boundary is clear, debugging and refactoring become safer and faster.

Transition with: "Those same boundaries also help teams collaborate and test more effectively."
:::

---




## Collaboration and testing benefits

### Team collaboration

- Teams can build features in parallel
- Clear boundaries mean fewer merge conflicts
- Ownership and responsibility are easier to assign

### Testing approach

- Test complete features, not isolated layers
- Mock at feature boundaries
- Integration becomes more straightforward
- Independent development is easier with mocked dependencies

::: notes
Use about two to three minutes on this slide. Explain that feature folders create natural seams for parallel work, so two developers can often build different slices without changing the same files.

In testing, highlight that the unit of reasoning becomes the feature, not a service class in isolation. That leads to tests that better reflect user behavior and system outcomes.

You can also mention that mocking is still useful, but it tends to happen at boundaries instead of inside every technical layer. That usually produces simpler tests with clearer intent.

Transition with: "Vertical slices also pair naturally with another pattern many teams use: CQRS."
:::

---

## Why CQRS fits well with vertical slices

```mermaid
flowchart LR
    U["User action"] --> C["Command / Write path"]
    U --> Q["Query / Read path"]
    C --> W["Write model<br/>validation + updates"]
    W --> E["Messages / events"]
    E --> R["Read model<br/>denormalized views + cache"]
    Q --> R
```

- CQRS separates reads from writes
- Read side can be optimized for display and performance
- Write side can be optimized for business rules and updates
- Messaging keeps the two stacks coordinated
- A feature slice can implement both read and write concerns together

::: notes
Duration ~00:03

 Explain that Command Query Responsibility Segregation separates the write path from the read path because those two concerns often want different models and optimizations.

On the read side, teams may denormalize data, cache aggressively, or build projections for fast display. On the write side, the focus is enforcing rules, validating intent, and updating authoritative data correctly.

Now connect it back to vertical slices: each feature can own both its command side and its query side. That makes CQRS feel less abstract because the pattern is implemented within a feature boundary rather than as a separate architectural island.

Transition with: "Let's close with the main ideas you want people to remember after this section."
:::

---

## Key takeaways

- Organize by feature when you want stronger business boundaries
- Keep everything needed for a feature in one place
- Prefer independent slices over tightly coupled features
- Use localized changes to improve maintainability
- Consider CQRS when read and write paths have different needs

**Bottom line:** vertical slicing improves focus, flow, and long-term maintainability.

::: notes
Duration ~00:01

Use about one minute to close. Recap that vertical slicing is primarily about improving feature ownership and reducing the cost of change.

Reinforce that the architecture helps both individuals and teams: developers move faster, changes are easier to contain, and the codebase better reflects how the business thinks about work.

If you want an audience prompt, ask which current feature in their codebase would be easiest to convert into a first slice. That question helps bridge the presentation into practical adoption.

End by signaling that the next step is usually implementation guidance, where teams define commands, handlers, validators, and feature-level tests.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Specification Driven Software Development
- Architecture Specification
- Technology Specification
- Implementation Specification
- **▶ Implementation Planning**
- Implementation Prompts
- Vertical Slice Implementation
- Code Review with GitHub Copilot

---

<!-- _class: lead -->

# Implementation Planning

---

## Implementation Planning

- Creating Vertical Slice Implementation Plans
- Dependency Analysis and Planning

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@2026-03-21"
operator: "johnmillerATcodemag-com"
chat_id: "vertical-slice-planning-marp-20260321"
prompt: |
  create a marp deck explaining the following content:

  ## Section 7: Creating Vertical Slice Implementation Plans (Duration: 00:16:00) [x]

  ### Key Topics

  - Vertical slice planning instruction file
  - Slice identification strategies
  - Decomposition principles
  - Using AI to create implementation plans
  - Slice definitions and specifications
  - Implementation roadmap creation

  ### Subsections

  #### 7.1: Slice Planning Instruction File Review (Duration: 00:05:00)

  - Located in '.github/instructions/vertical-slice-planning.instructions.md'
  - **Slice Identification Strategies**:
    - User action decomposition (request-to-response flows)
    - Entity CRUD operations
    - Workflow stage decomposition
    - Business event decomposition
    - CQRS-optimized (separate reads from writes)
  - **Decomposition Principles**:
    - Single responsibility
    - Complete vertical stack
    - No horizontal sharing
    - Minimize external dependencies
  - **Slicing Guidelines**: Not too big, not too small
  - **Decision Tree**: Strategy selection guidance
  - **Analysis**: Data dependencies, service dependencies

  #### 7.2: Generating Implementation Plans (Duration: 00:07:00)

  - Prompt: "Using vertical slice planning instructions and web calculator requirements, create implementation plan using vertical slices"
  - AI generates comprehensive plan with:
    - Summary of requirements
    - Slice identification and decomposition
    - Dependency diagram
    - Proposed implementation sequence
    - Sprint organization
  - Model differences in output detail and approach

  #### 7.3: Multi-Model Evaluation Exercise (Duration: 00:04:00)

  - Using Gemini 2.5 Pro to evaluate Claude Sonnet's vertical slice planning file
  - Identified six improvement areas:
    - Missing task duration metadata
    - Incomplete decomposition examples
    - Need more complete dependency strategy examples
    - Finish implementation sequencing examples
    - Complete roadmap template
    - Finalize slice specification template
  - Demonstrates value of multi-model review strategy
started: "2026-03-21T17:27:41Z"
ended: "2026-03-21T17:36:41Z"
task_durations:
  - task: "requirements review"
    duration: "00:03:00"
  - task: "slide drafting"
    duration: "00:05:00"
  - task: "provenance updates"
    duration: "00:01:00"
total_duration: "00:09:00"
ai_log: "ai-logs/2026/03/21/vertical-slice-planning-marp-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
size: 16:9
title: "Creating Vertical Slice Implementation Plans"
description: "Section 7 deck on slice planning guidance, AI-generated plans, and multi-model review."
---
# Vertical Slice Implementation Plans || The Blueprint Before the Blueprint

## Creating Vertical Slice Implementation Plans

- 16-minute teaching segment
- Focus: how to plan before implementation
- Goal: turn requirements into executable slices

::: notes
Open by framing this section as the bridge between architecture guidance and actual delivery planning.

Explain that vertical slices are not just a coding pattern; they are also a planning tool. The point of the section is to help the audience see how to move from requirements to a buildable roadmap.

Spend a few seconds previewing the three parts of the talk: reviewing the planning instruction file, generating implementation plans with AI, and improving those plans through multi-model evaluation.
:::

---

## What this section covers

- Vertical slice planning instruction file
- Slice identification strategies
- Decomposition principles
- AI-assisted implementation planning
- Slice specifications and roadmaps

::: notes
Use this slide as a table of contents for the section. Keep the pace brisk and make it clear that each bullet corresponds to a practical planning step teams can repeat.

Emphasize that the section is intentionally operational. It is about making slices small enough to implement, complete enough to deliver value, and structured enough that AI can help generate plans instead of vague suggestions.

Transition by saying the first step is understanding the instruction file that defines the planning rules.
:::

---

## 7.1 Review the planning instructions

Reference point:

'.github/instructions/vertical-slice-planning.instructions.md'

What it provides:

- Strategy selection guidance
- Decomposition rules
- Dependency analysis prompts
- Slice definition templates

::: notes
Introduce the instruction file as the planning playbook. It tells both humans and AI how to reason about a feature before code is written.

Call out that a strong instruction file improves consistency. Instead of every plan starting from scratch, the team gets a repeatable way to identify slices, document dependencies, and define an implementation sequence.

Mention that the file is valuable even when AI is not involved because it clarifies how the team wants work decomposed.
:::

---

## Slice identification strategies

| Strategy | Best fit |
| --- | --- |
| User action decomposition | End-to-end user flows |
| Entity CRUD operations | Simple data management |
| Workflow stage decomposition | Multi-step processes |
| Business event decomposition | Event-driven behavior |
| CQRS-optimized slicing | Distinct read/write paths |

::: notes
Walk the audience through the five strategies and explain that no single strategy is always correct. The right one depends on the kind of behavior being modeled.

For user action decomposition, use an example like "submit order" or "reset password." For CRUD, use admin maintenance screens. For workflow stages, mention onboarding or approvals. For business events, use order placed or payment failed. For CQRS, explain separating queries from commands when reads and writes differ significantly.

Stress that the planning file helps choose a strategy rather than forcing one pattern onto every feature.
:::

---

## Decomposition principles

- **Single responsibility** per slice
- **Complete vertical stack** from UI/API to data
- **No horizontal sharing** as the unit of delivery
- **Minimize external dependencies**
- Size slices to be **valuable and manageable**

### Rule of thumb

Avoid slices that are too big to finish or too small to matter.

::: notes
This slide defines the quality bar for a slice. Explain that a slice should deliver one meaningful capability and contain everything needed to implement that capability end to end.

Clarify "no horizontal sharing" by contrasting a real slice with a layer-based task such as "build all repositories first." Horizontal work may still exist, but it should not become the primary planning unit.

Use the phrase "valuable and manageable" more than once. That is the balance teams often miss when they either create giant epics or tiny technical chores that produce no user value.
:::

---

## Analyze before you slice

Ask these questions first:

- What data does this slice read or change?
- What services or APIs does it depend on?
- Can it be deployed independently?
- Does a different strategy fit better?

Decision aid:

'flow -> dependencies -> size check -> sequence'

::: notes
Explain that slicing is not just naming features. It requires examining data dependencies and service dependencies before locking in the plan.

Walk through the decision aid from left to right. Start with the flow, then look at dependency boundaries, then check whether the proposed slice is too large or too fragmented, and finally place it into an execution sequence.

This is a good moment to remind the audience that planning errors often come from ignoring dependencies until implementation begins.
:::

---

## 7.2 Generate plans with AI

Example prompt:

> Using vertical slice planning instructions and web calculator requirements, create implementation plan using vertical slices.

AI can generate:

- Requirements summary
- Slice decomposition
- Dependency diagram
- Implementation order
- Sprint organization

::: notes
Explain that the prompt works because it combines two inputs: the planning instructions and the actual feature requirements. Without both, the output is usually too generic.

Point out that this is where AI becomes a planning accelerator. Instead of starting from a blank page, the team gets a draft plan containing slices, dependencies, sequencing, and potential sprint structure.

Also note that the prompt is intentionally simple. The quality comes from the instruction file and source requirements, not from a complicated prompt.
:::

---

## What a good AI plan should include

1. Clear summary of requirements
2. Identified slices with rationale
3. Dependency relationships
4. Proposed implementation sequence
5. Sprint or milestone grouping

### Watch for model differences

- More detail vs. more concise output
- Different naming and grouping choices
- Different sequencing assumptions

::: notes
Use this slide to define evaluation criteria for AI-generated plans. The audience should leave knowing what "good" looks like, not just that AI can produce something.

Explain that different models may emphasize different aspects. One might provide stronger rationale, another might produce cleaner sequencing, and another might be better at summarizing requirements.

Encourage the audience to compare outputs rather than assuming the first plan is correct. This leads naturally into the multi-model review exercise.
:::

---

## Example planning flow

### Web calculator example

1. Summarize calculator requirements
2. Identify slices such as input, operations, history, validation
3. Map data and service dependencies
4. Sequence foundational slices before enhancements
5. Group slices into sprints

::: notes
Translate the abstract process into a concrete example. Use the calculator scenario because it is simple enough to understand quickly while still showing real decomposition choices.

Mention that one model may group input and validation together, while another may separate them. One may treat history as a later slice because it depends on completed calculations. These are exactly the kinds of planning differences worth discussing.

Reinforce that the output is not just a list of tasks. It is a roadmap with ordering logic.
:::

---

## 7.3 Multi-model evaluation

Gemini 2.5 Pro reviewed Claude Sonnet's planning file and found six gaps:

1. Missing task duration metadata
2. Incomplete decomposition examples
3. Incomplete dependency strategy examples
4. Unfinished implementation sequencing examples
5. Incomplete roadmap template
6. Incomplete slice specification template

::: notes
Present this as a quality-improvement exercise, not a competition between models. The value comes from using one model to review the blind spots of another.

Walk through the six findings quickly and frame them as practical improvements. These are not cosmetic issues; they affect whether teams can actually use the planning artifact consistently.

Highlight that evaluation uncovered missing completeness in examples and templates, which matters because templates are what guide future AI generations.
:::

---

## Key takeaway

### Recommended workflow

'instructions -> AI draft -> review -> refine -> implement'

- Start with a strong planning instruction file
- Generate an initial vertical slice plan
- Compare outputs across models when useful
- Improve templates and examples over time

::: notes
Close with the repeatable workflow. This gives the audience a practical method they can adopt immediately.

Emphasize that the instruction file is the stable asset, AI provides the first draft, and multi-model review improves quality. Over time, the planning assets themselves get better, which improves every future plan.

End by connecting this section to execution: once the slices and roadmap are solid, implementation becomes faster, safer, and easier to parallelize.
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "dependency-analysis-planning-20260321"
prompt: |
  create a marp deck explaining the following content:

  ## 5. Dependency Analysis and Planning
  **Time**: 00:45:00 - 00:48:30
  **Duration**: ~3.5 minutes

  Brief discussion of dependency graphs and how they inform implementation sequencing.

  **Topics Covered**:
  - Reading and interpreting dependency diagrams
  - Understanding which slices must be completed before others
  - Identifying the critical path through implementation
  - Foundational vs. dependent features

  **Key Insights**:
  - Dependency graphs help visualize implementation order
  - Some slices can be parallelized, others are sequential
  - Foundational work must be completed first
started: "2026-03-21T17:28:42Z"
ended: "2026-03-21T17:44:42Z"
task_durations:
  - task: "slide outline"
    duration: "00:03:00"
  - task: "slide authoring"
    duration: "00:10:00"
  - task: "provenance and catalog updates"
    duration: "00:03:00"
total_duration: "00:16:00"
ai_log: "ai-logs/2026/03/21/dependency-analysis-planning-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Dependency Analysis and Planning || Everything Depends on This Slide (Literally)

<!-- _class: lead -->

## Dependency Analysis and Planning

- Section focus: using dependency graphs to sequence vertical slice implementation
- Outcome: show how teams identify prerequisites, parallel work, and the critical path

::: notes
Duration ~00:04

Introduce this section as the point where planning becomes executable rather than aspirational. Explain that dependency analysis helps the team decide what must be built first, what can safely wait, and what can happen in parallel without creating blockers.  Transition by showing a simple dependency graph and explaining how to read it.
:::

---

## Read the Dependency Diagram

- Nodes represent slices, features, or enabling work
- Arrows show that one item depends on another being complete first
- Read from left to right or top to bottom to understand sequencing
- Look for root nodes with no prerequisites

```mermaid
flowchart LR
    A[Foundation setup] --> B[Shared UI shell]
    A --> C[Domain models]
    B --> D[Slice 1]
    C --> D
    D --> E[Slice 2]
    D --> F[Slice 3]
```

::: notes
Duration ~00:01

Explain that a dependency graph is a visual map of implementation order, not just a picture of the system. Root nodes such as foundation setup are important because they unlock other work, while downstream nodes cannot start safely until their prerequisites exist.  Transition by asking which path through the graph will determine overall progress.
:::

---

## Find the Critical Path

- The **critical path** is the longest chain of dependent work
- Delays on that path delay the overall implementation plan
- Independent branches matter, but they do not all block delivery equally
- Focus coordination and risk management on the path that controls completion

```mermaid
flowchart TD
    A[Foundation] --> B[Slice 1]
    B --> C[Slice 2]
    C --> D[Release-ready workflow]
    B --> E[Optional reporting slice]
```

::: notes
Duration ~00:01

Make the point that not every task has the same scheduling weight. The chain from foundation through Slice 1 and Slice 2 to release readiness is the critical path because a delay anywhere in that line affects the final delivery date.  Transition by showing that some branches can still be parallelized once the right prerequisites are in place.
:::

---

## Sequence First, Parallelize Second

- Some slices are strictly sequential because they share prerequisites
- Other slices can run in parallel after the same foundation is done
- Parallel work increases speed only when dependencies are already satisfied
- Planning should prevent teams from starting blocked work too early

```mermaid
flowchart TB
    A[Foundational work complete] --> B[Slice 1]
    A --> C[Slice 2]
    B --> D[Integration slice]
    C --> D
```

::: notes
Duration ~00:01

Explain that parallelization is useful, but only after the common enabling work is complete. In this example, Slice 1 and Slice 2 can move at the same time, yet the integration slice must wait until both are finished, so sequencing still matters.  Transition by separating foundational work from dependent features so the audience can see how to prioritize the backlog.
:::

---

## Distinguish Foundational and Dependent Features

**Foundational work**

- environments, shared components, core models, base services

**Dependent features**

- user-facing slices that rely on those shared capabilities

**Planning rule**

- finish enabling work first when many later slices depend on it

::: notes
Duration ~00:01

Clarify that foundational work is valuable because it unlocks many downstream slices, not because it is glamorous. Dependent features usually deliver visible business value, but they become risky or inefficient if the core infrastructure they need is missing or unstable.  Transition by summarizing a lightweight planning process the team can repeat for every implementation plan.
:::

---

## Use Dependency Analysis to Plan the Roadmap

1. List slices and enabling work
2. Draw the dependency relationships
3. Identify the critical path
4. Mark which branches can run in parallel
5. Schedule foundational work before dependent features

**Bottom line**: dependency graphs turn a feature list into a realistic implementation sequence.

::: notes
Duration ~00:01

Close by turning the concept into a repeatable planning workflow. The audience should leave with the idea that dependency analysis is a small upfront investment that prevents scheduling confusion, blocked development, and unrealistic sequencing later.  End by connecting this back to vertical slices, where smart sequencing makes incremental delivery much easier.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Specification Driven Software Development
- Architecture Specification
- Technology Specification
- Implementation Specification
- Implementation Planning
- **▶ Implementation Prompts**
- Vertical Slice Implementation
- Code Review with GitHub Copilot

---

<!-- _class: lead -->

# Implementation Prompts

---

## Implementation Prompts

- Implementation Prompts and Verification

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "implementation-prompts-verification-20260321"
prompt: |
  create a marp deck explaining the following content:

  ## Section 8: Implementation Prompts and Verification (Duration: 00:22:00) [x]

  ### Key Topics

  - Creating implementation prompts for individual slices
  - Slice-specific prompt files
  - Verification steps inclusion
  - Showcase/demonstration instructions
  - Detailed specifications for HTML, CSS, JavaScript
  - File structure and component organization

  ### Subsections

  #### 8.1: Implementation Prompt Creation (Duration: 00:08:00)

  - Select a slice from implementation plan (e.g., Slice 1: Display Current Value)
  - Prompt: "Using slice X instructions and implementation plan, create prompts file that implements slice 1. Include verification steps and showcase instructions that demonstrate the functionality to stakeholders."
  - Generated prompt file includes:
    - Files to create (index.html, styles.css, main.js)
    - Detailed specifications for each component
    - HTML structure requirements
    - CSS styling (colors, fonts, layout)
    - JavaScript functionality (current value property, display object, update function)

  #### 8.2: Verification Steps (Duration: 00:05:00)

  - **Initial State**: Calculator displays "0" on page load
  - **State Update**: Manual value changes in console update display
  - **Accessibility**: Color contrast ratio ≥ 4.5:1, font size ≥ 2rem
  - Automated testing guidance
  - Manual verification procedures

  #### 8.3: Showcase Instructions (Duration: 00:04:00)

  - Current version: Code snippet for demonstration
  - Improvement suggestion: Target human demonstrators
  - Should list what users see and can do
  - Behavior descriptions
  - Interactive demonstration guidance

  #### 8.4: Creating Multiple Slice Prompts (Duration: 00:05:00)

  - Repeating process for additional slices (Slice 2, etc.)
  - Building complete implementation roadmap
  - Each slice prompt is version-controlled
  - Reusable for future modifications
  - Sequential execution and review approach
  - Systematic implementation verification
started: "2026-03-21T17:28:50Z"
ended: "2026-03-21T17:43:50Z"
task_durations:
  - task: "slide outline"
    duration: "00:03:00"
  - task: "slide authoring"
    duration: "00:10:00"
  - task: "provenance and catalog updates"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/implementation-prompts-verification-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Implementation Prompts and Verification || The Prompt That Does the Implementation (With a Checklist)

<!-- _class: lead -->

## Implementation Prompts and Verification

- Section focus: turning slice plans into actionable build prompts
- Outcome: show how to generate slice-specific prompts, verify behavior, and prepare stakeholder demos

::: notes
Duration ~00:22

Introduce this section as the bridge between planning and actual implementation. The audience should understand that a slice plan becomes much more useful when it is converted into a precise prompt that tells the AI what to build, how to verify it, and how to demonstrate it.  Transition by asking what information a good implementation prompt must capture before any code is generated.
:::

---

## Start from a Single Slice

- Choose one slice from the implementation plan
- Example: **Slice 1 - Display Current Value**
- Use the slice instructions plus the implementation plan as source context
- Write one prompt file per slice so scope stays narrow and testable

```mermaid
flowchart LR
    A[Implementation plan] --> B[Select slice]
    B --> C[Slice-specific prompt]
    C --> D[Targeted implementation]
```

::: notes
Duration ~00:02

Explain that the best implementation prompts are intentionally narrow. Rather than asking for an entire application, the team picks one slice from the plan and turns that into a focused request that can be reviewed and tested independently.  Transition by showing what the actual prompt needs to contain once the slice is chosen.
:::

---

## What the Implementation Prompt Should Say

- Reference the slice instructions and the implementation plan directly
- Ask the model to implement the selected slice
- Require **verification steps** in the output
- Require **showcase instructions** for stakeholder demonstration

**Prompt pattern**

> Using slice X instructions and implementation plan, create a prompt file that implements slice 1. Include verification steps and showcase instructions that demonstrate the functionality to stakeholders.

::: notes
Duration ~00:03

Frame this slide around prompt construction, not just prompt wording. The important move is that the request names the slice, points to the governing instructions, and asks for more than code generation by explicitly requiring verification and demonstration guidance.  Transition by breaking down the expected deliverables inside the generated prompt file.
:::

---

## Expected Deliverables Inside the Prompt File

**Files to create**

- 'index.html'
- 'styles.css'
- 'main.js'

**Specifications to include**

- HTML structure requirements
- CSS colors, fonts, spacing, and layout
- JavaScript behavior for current value, display object, and update function
- File structure and component organization

::: notes
Duration ~00:03

Walk through the prompt output as if you are reviewing a generated file with the class. The goal is not merely to list filenames, but to show that the prompt should describe what each file is responsible for and how the pieces fit together.  Transition by moving from implementation detail to the checks that prove the slice actually works.
:::

---

## Build Verification into the Prompt

- **Initial state**: calculator displays '0' on page load
- **State update**: changing the value in the console updates the display
- **Accessibility**: contrast ratio >= 4.5:1 and font size >= '2rem'
- Include both automated testing guidance and manual verification steps

```mermaid
flowchart TB
    A[Implementation complete] --> B[Initial state check]
    A --> C[Behavior update check]
    A --> D[Accessibility check]
    B --> E[Ready for review]
    C --> E
    D --> E
```

::: notes
Duration ~00:04

Explain that verification should be authored before or alongside implementation, not after the fact. The checks on this slide are strong examples because they cover default state, observable behavior, and accessibility requirements in a way that reviewers and demonstrators can both understand.  Transition by showing how showcase instructions differ from verification even though the two are related.
:::

---

## Showcase Instructions Should Target Humans

- Do more than paste a code snippet
- Describe what users **see** and what they can **do**
- Call out the behavior the demonstrator should point to
- Provide an interactive demo path for stakeholders

**Good showcase guidance includes**

1. starting state on screen
2. action to take
3. visible result
4. why it matters to the audience

::: notes
Duration ~00:03

Make the distinction between proving correctness and presenting value. Verification asks whether the slice works; showcase guidance tells a human demonstrator how to walk stakeholders through what appears on screen, what changes, and why they should care.  Transition by expanding from one slice to the broader roadmap of multiple prompts.
:::

---

## Repeat the Pattern Across All Slices

- Create additional prompt files for Slice 2, Slice 3, and so on
- Version-control each prompt so changes stay traceable
- Reuse prompts later for revisions or follow-on work
- Execute slices sequentially and review each result before moving on
- Build a complete implementation roadmap with systematic verification

**Bottom line**: slice-specific prompts create a repeatable path from plan to implementation to review.

::: notes
Duration ~00:03

Close by connecting the single-slice example to the full delivery workflow. Each prompt becomes a reusable unit of work that can be re-run, refined, and audited over time, which is especially useful when implementation spans multiple sessions or contributors.  End by encouraging the audience to treat prompt files as versioned implementation assets, not disposable chat text.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Specification Driven Software Development
- Architecture Specification
- Technology Specification
- Implementation Specification
- Implementation Planning
- Implementation Prompts
- **▶ Vertical Slice Implementation**
- Code Review with GitHub Copilot

---

<!-- _class: lead -->

# Vertical Slice Implementation

---

## Vertical Slice Implementation

- Basic Vertical Slice Implementation Workflow

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-25"
operator: "johnmillerATcodemag-com"
chat_id: "vertical-slice-basic-workflow-20260325"
prompt: |
  create a marp deck that outlines a basic workflow for implementing an application in vertical slices. According to the implementation plan, some slices can be implemented in parallel.
started: "2026-03-25T00:00:00Z"
ended: "2026-03-25T00:10:00Z"
task_durations:
  - task: "deck authoring"
    duration: "00:07:00"
  - task: "workflow diagram drafting"
    duration: "00:03:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2026/03/25/vertical-slice-basic-workflow-20260325/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
size: 16:9
title: "Basic Vertical Slice Implementation Workflow"
description: "A practical workflow for planning and implementing an application with vertical slices, including parallel slice execution."
---
# Basic Vertical Slice Workflow || Thin Slices, Big Results

## Basic Vertical Slice Implementation Workflow

- Goal: deliver working software in thin, end-to-end slices
- Pattern: plan dependencies first, then parallelize safe slices
- Outcome: faster feedback and lower integration risk

::: notes
Introduce the deck as a practical delivery workflow, not just an architecture concept. Emphasize that each vertical slice includes API, domain logic, persistence, and tests. Mention that parallel work is possible only after dependency analysis confirms slice independence.
:::

---

## Step 1: Define Slice Boundaries

- Start from user-visible use cases
- Split by business capability, not technical layer
- Keep each slice independently testable
- Write a short definition for every slice:
  - Scope
  - Inputs/outputs
  - Done criteria

::: notes
Explain that teams should avoid horizontal tasks like build all repositories first. Reinforce that each slice should produce demonstrable value. Recommend a short template for each slice so implementation and review stay consistent.
:::

---

## Step 2: Build the Implementation Plan

- Identify dependency chain first
- Mark slices as:
  - Foundation (must go first)
  - Parallel-ready (can run together)
  - Integration/cleanup (must go last)
- Sequence by risk and coupling

```mermaid
flowchart LR
    A[Requirements and slice definitions] --> B[Foundation slice]
    B --> C1[Slice A: User Registration]
    B --> C2[Slice B: Product Catalog]
    B --> C3[Slice C: Search]
    C1 --> D[Integration and end-to-end hardening]
    C2 --> D
    C3 --> D
    D --> E[Release candidate]
```

::: notes
Walk left to right. Call out that Foundation might include authentication baseline, shared contracts, and CI setup. Then point to slices A, B, and C as intentionally parallel lanes. Close by explaining that integration hardening is a separate explicit phase.
:::

---

## Step 3: Execute Slices in Parallel

- Assign owners per slice lane
- Use trunk-based integration with short-lived branches
- Keep contracts stable and versioned
- Demo each slice as soon as done

Parallel execution guardrails:

- No hidden cross-slice dependencies
- Shared schema changes reviewed early
- Contract tests required before merge

::: notes
Emphasize team coordination practices. Explain that parallel work fails when contracts are ambiguous. Recommend daily integration checks and a lightweight dependency board to catch collisions early.
:::

---

## Step 4: Integrate, Validate, and Stabilize

- Run full end-to-end and regression tests
- Validate non-functional requirements:
  - Performance
  - Security
  - Observability
- Close documentation and operational runbooks
- Freeze only when release criteria are met

::: notes
Describe this as controlled convergence, not a big bang merge. Point out that each slice already passed its own checks, so this phase focuses on system behavior and production readiness. Encourage using release checklists to avoid late surprises.
:::

---

## Practical Starter Plan (Example)

Week 1

- Foundation slice
- Finalize contracts

Week 2

- Slice A and Slice B in parallel
- Slice C starts mid-week after shared dependency lands

Week 3

- Integration hardening
- UAT and release prep

::: notes
Use this final slide as a reusable planning pattern. Mention that exact durations vary, but the structure remains stable: foundation, parallel execution, then hardening. Invite participants to adapt this pattern to their own project backlog.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Specification Driven Software Development
- Architecture Specification
- Technology Specification
- Implementation Specification
- Implementation Planning
- Implementation Prompts
- Vertical Slice Implementation
- **▶ Code Review with GitHub Copilot**

---

<!-- _class: lead -->

# Code Review with GitHub Copilot

---

## Code Review with GitHub Copilot

- Pull Request and Code Review
- GitHub Code Review with Copilot
- GitHub CLI and PR Management

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "pull-request-code-review-20260321"
prompt: |
  create a marp deck explaining the following content:


  ## 7. Pull Request and Code Review
  **Time**: 01:30:00 - 01:41:24
  **Duration**: ~11.5 minutes

  Creating pull request, initiating code reviews (both human and AI), and addressing feedback.

  **Topics Covered**:
  - **01:30:00 - 01:33:00**: Creating the pull request
    - Branch naming: "slice-1"
    - Git workflow: commit, push, create PR
    - Associating PRs with issues (development section)

  - **01:33:00 - 01:36:00**: Code review process
    - Assigning reviewers (Christopher)
    - Initiating GitHub Copilot code review
    - Waiting for AI-generated review comments
    - Assigning issue to implementer (Dan Blanchard)

  - **01:36:00 - 01:39:00**: Reviewing AI feedback
    - AI identifies missing AI provenance metadata in markdown files
    - Discussion of DOM element access patterns
    - Multiple code quality issues flagged

  - **01:39:00 - 01:41:24**: Addressing review comments
    - How to reference specific review comments
    - Copy-paste vs. direct AI interaction with comments
    - Fixing issues: AI metadata, code patterns
    - Discussion of when to implement vs. ignore certain suggestions

  **Key Issues Identified**:
  - **Markdown files missing AI provenance metadata**: AI reviewer caught missing metadata that should track the generation source
  - **DOM element access patterns**: Suggestions for improved DOM manipulation
  - **Multiple other code quality concerns**: Various improvements suggested by AI reviewer

  **Process Insights**:
  - GitHub Copilot can be added as code reviewer
  - AI review takes a few minutes to complete
  - Review comments can be addressed individually or in batch
  - Some AI suggestions may be contextual and require judgment
  - Manual reviewers work in parallel with AI reviewers
started: "2026-03-21T17:46:47Z"
ended: "2026-03-21T18:01:47Z"
task_durations:
  - task: "slide outline"
    duration: "00:03:00"
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and catalog updates"
    duration: "00:03:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/pull-request-code-review-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Pull Request Code Review || The Code Review That Doesn't Ghost You

<!-- _class: lead -->

## Pull Request and Code Review

- Section focus: moving from implementation into PR creation, review, and comment resolution
- Outcome: show how teams combine human and AI review to improve a slice before merge

::: notes
Duration ~00:12

Introduce this section as the quality gate that turns implementation work into team-reviewed delivery. Explain that the goal is not only to open a pull request, but to create a workflow where human reviewers and AI reviewers can both contribute useful feedback before the slice is merged.  Transition by starting with the mechanics of creating the pull request itself.
:::

---

## Create the Pull Request Cleanly

- Use a focused branch name such as 'slice-1'
- Follow the normal Git flow: commit, push, and create the PR
- Link the pull request to its issue in the development section
- Keep the PR scoped to one slice so review stays clear and actionable

```mermaid
flowchart LR
    A[Local slice work] --> B[Commit changes]
    B --> C[Push branch]
    C --> D[Create pull request]
    D --> E[Link PR to issue]
```

::: notes
Duration ~00:02

Explain that a clean review starts with a clean pull request. Branch naming, a narrow slice-focused scope, and issue linkage all make it easier for both humans and AI to understand what the change is supposed to accomplish and what context it belongs to.  Transition by showing what happens once the PR is open and reviewers are assigned.
:::

---

## Run Human and AI Review in Parallel

- Assign a human reviewer such as Christopher
- Initiate GitHub Copilot code review on the pull request
- Wait a few minutes for AI-generated comments to arrive
- Route implementation work clearly by assigning the issue to the implementer
- Use parallel review to shorten feedback time without sacrificing judgment

```mermaid
flowchart TB
    A[Pull request opened] --> B[Human reviewer assigned]
    A --> C[Copilot review requested]
    B --> D[Human comments]
    C --> E[AI comments]
    D --> F[Implementer triage]
    E --> F
```

::: notes
Duration ~00:02

Make the point that human review and AI review are complementary rather than competitive. The human reviewer brings context, intent, and domain judgment, while Copilot can scan for policy violations, code smells, and other issues that might be easy to miss in a first pass.  Transition by looking at the kinds of issues the AI reviewer surfaced.
:::

---

## What the AI Review Flagged

- Missing AI provenance metadata in Markdown files
- DOM element access patterns that could be improved
- Multiple additional code quality concerns across the change set

**Why this matters**

1. metadata gaps break traceability requirements
2. DOM patterns affect maintainability and clarity
3. mixed quality issues show the value of automated review breadth

::: notes
Duration ~00:02

Use this slide to summarize the review findings before going into comment-handling mechanics. The key takeaway is that the AI review did not focus on one narrow category of defects; it found documentation compliance issues, implementation-pattern concerns, and general quality problems in the same run.  Transition by focusing on how the team should interpret and respond to the comments.
:::

---

## Review Comments Still Require Judgment

- Some comments should be fixed immediately
- Some suggestions may depend on project context
- Not every AI recommendation is automatically correct or worth implementing
- Teams need to decide whether to implement, defer, or ignore each point

**Good reviewer questions**

- Does this comment identify a real defect?
- Does the suggestion fit repository conventions?
- Is the proposed fix worth the churn right now?

::: notes
Duration ~00:02

Stress that AI review produces input, not orders. Review comments can be helpful, but the team still has to evaluate whether a suggestion is accurate, relevant to the slice, and worth making before merge, especially when recommendations touch patterns or style rather than outright defects.  Transition by showing practical ways to handle comments once the team decides to act.
:::

---

## Address Comments One by One or in Batches

- Reference specific review comments when preparing fixes
- Handle comments individually when the issues are distinct or risky
- Batch fixes when several comments point to the same underlying problem
- Use copy-paste or direct AI interaction with comments depending on the workflow
- Typical fixes here included metadata updates and code-pattern adjustments

```mermaid
flowchart LR
    A[Review comment] --> B{Single issue or pattern?}
    B -->|Single| C[Fix individually]
    B -->|Pattern| D[Batch related fixes]
    C --> E[Update PR]
    D --> E
```

::: notes
Duration ~00:02

Explain that comment resolution is partly a coordination problem. If comments are unrelated, it is safer to handle them one at a time so the reasoning stays clear, but if several comments all stem from the same root cause, batching them can reduce churn and speed up the next review pass.  Transition by ending with the broader workflow lessons the team should keep using.
:::

---

## Process Takeaways for Future PRs

- GitHub Copilot can participate as a code reviewer alongside humans
- AI review usually takes a few minutes, so plan for that latency
- Review comments can be handled individually or in grouped passes
- Manual reviewers and AI reviewers are strongest when used together
- Better prompts and instructions can reduce recurring review findings

**Bottom line**: strong PR workflow is not just about opening the review, but about turning feedback into better code and better guidance.

::: notes
Duration ~00:02

Close by tying the mechanics back to team process. The audience should leave with the idea that a pull request is a collaborative checkpoint where both human judgment and AI-assisted review improve quality, and where recurring feedback should eventually drive updates to instructions, prompts, and testing standards.  End by suggesting that every repeated review comment is a candidate for strengthening the guidance upstream.
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "github-code-review-with-copilot-20260321"
prompt: |
  create a marp deck explaining the following content:

  ## Section 4: GitHub Code Review with Copilot (00:22:00 - 00:40:06)

  **Duration**: 18:06

  ### Key Topics

  - GitHub Copilot code review process for PR #4
  - Review identified 8 comments/issues
  - Unicode character usage in comparisons
  - State management issues with error clearing
  - Missing AI provenance metadata
  - Unused constants and functions
  - Commit suggestion feature demonstration

  ### Subsections

  #### Code Review Findings

  - **Unicode issues**: Minus sign character recommendations
  - **State management**: Error state clearing leaves expression tokens intact
  - **Compliance**: AI provenance header missing from previously compliant files
  - **Dead code**: Unused constants and functions identified
  - **Testing gaps**: Subtraction test coverage noted

  #### Review Process Observation

  - Copilot "thinking process" visible during review
  - Manual resolution of comments required
  - Discussion of using review output to improve instruction files
  - Suggestion to tighten instruction files to prevent recurring issues
started: "2026-03-21T17:41:13Z"
ended: "2026-03-21T17:56:13Z"
task_durations:
  - task: "slide outline"
    duration: "00:03:00"
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and catalog updates"
    duration: "00:03:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/github-code-review-with-copilot-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# GitHub Code Review with Copilot || The AI Reviewer Who Never Says "Looks Good to Me"

<!-- _class: lead -->

## GitHub Code Review with Copilot

- Section focus: using Copilot review feedback to improve code, tests, and instructions
- Outcome: show what Copilot found in PR '#4', how humans resolved it, and how review findings feed better standards

::: notes
Duration ~00:18

Introduce this section as a practical demonstration of Copilot acting as a review assistant rather than a code generator. Explain that the value is not just in the comments themselves, but in how the review surfaces patterns such as correctness issues, compliance gaps, and recurring quality risks.  Transition by showing the review workflow from pull request to human action.
:::

---

## How the Review Flow Worked

- Open the pull request and request Copilot review
- Copilot analyzes changed files and leaves review comments
- Review findings are grouped around correctness, maintainability, and compliance
- Humans still decide what to fix, how to fix it, and when to close comments
- Commit suggestions can accelerate straightforward cleanups

```mermaid
flowchart LR
    A[Pull request #4] --> B[Copilot review]
    B --> C[Review comments]
    C --> D[Developer triage]
    D --> E[Manual fixes and commits]
    E --> F[Updated instructions and tests]
```

::: notes
Duration ~00:02

Walk through the process as a collaboration loop rather than an automated approval gate. Copilot can inspect the diff quickly and highlight issues, but the team still has to evaluate the feedback, decide which comments are valid, and implement the actual fixes.  Transition by summarizing the kinds of issues the review identified.
:::

---

## What Copilot Found in PR #4

| Finding area | Example issue | Why it matters |
| --- | --- | --- |
| Unicode usage | non-standard minus sign in comparisons | can cause subtle behavior or readability issues |
| State management | clearing errors leaves expression tokens behind | UI state becomes inconsistent |
| Compliance | AI provenance header missing | repository policy violation |
| Dead code | unused constants and functions | noise, confusion, and maintenance cost |
| Testing gaps | subtraction coverage called out | bugs can slip through |

- Total review volume: **8 comments/issues**

::: notes
Duration ~00:02

Use this slide to give the audience a fast inventory of the feedback categories before you zoom in on individual examples. The important takeaway is that one review surfaced both code-level problems and process-level issues, which shows why review is valuable even when the code appears to work.  Transition by taking the two most concrete implementation findings first.
:::

---

## Code Review Findings: Correctness Problems

**Unicode comparison issue**

- review recommended replacing a Unicode minus character with the standard ASCII '-'
- consistent character usage improves safety and maintainability

**State management issue**

- clearing the error state did not fully reset expression tokens
- partial reset behavior can leave stale calculation state behind

```mermaid
flowchart TB
    A[User hits clear or reset] --> B[Error message removed]
    B --> C{Expression tokens reset?}
    C -->|No| D[Stale state remains]
    C -->|Yes| E[Calculator returns to clean baseline]
```

::: notes
Duration ~00:03

Explain that these two findings are especially useful because they highlight different kinds of correctness risk. The Unicode issue is small but important because unusual characters can be hard to spot and may behave differently across tools, while the state-reset issue is a deeper logic problem because the UI looks reset even when internal state is not.  Transition by moving from correctness to the policy and cleanup findings.
:::

---

## Code Review Findings: Compliance and Cleanup

- Previously compliant files were missing required AI provenance headers
- Unused constants and helper functions were identified as dead code
- Review also noted subtraction test coverage gaps
- Together, these findings show that review should check policy, clarity, and verification, not just functionality

**Review lens**

1. Does the code work?
2. Does it follow repository rules?
3. Is there unnecessary code left behind?
4. Do tests prove the risky behavior?

::: notes
Duration ~00:03

Frame this slide as the broader quality story behind the pull request. Missing provenance metadata is not just a formatting issue in this repository, because it breaks traceability requirements, while dead code and testing gaps both increase the chance of future confusion or regressions.  Transition by describing what the review experience looked like for the humans involved.
:::

---

## What We Observed About the Review Process

- Copilot's visible "thinking process" helped explain why comments were being made
- Review output still required manual interpretation and manual resolution
- The review became a teaching tool, not just a defect list
- Some feedback suggested improvements to instruction files, not only to source files

**Important point**: AI review assists judgment, but it does not replace reviewer accountability.

::: notes
Duration ~00:03

Explain that part of the educational value came from seeing how the review reasoned about the diff. Even when the comments were useful, someone still had to verify the issue, choose the right fix, and decide whether the underlying instructions or prompts should change to prevent the same mistake next time.  Transition by showing how the team can use those findings to strengthen the instruction layer.
:::

---

## Use Review Output to Improve the Instructions

- Tighten instruction files so recurring issues are prevented earlier
- Add explicit rules for ASCII-safe operators and character usage
- Clarify state reset expectations for error handling and token cleanup
- Reinforce provenance requirements where generated files are expected
- Expand tests around risky operations such as subtraction and clear-state behavior

**Bottom line**: the best outcome is not only fixing the PR, but improving the prompts and instructions that shape future PRs.

::: notes
Duration ~00:03

Close by connecting review feedback to process improvement instead of treating comments as isolated repairs. If the same issues can recur, the right move is to update the instruction files, prompt guidance, or test expectations so future generated code starts from a stronger baseline.  End by summarizing that Copilot review is most valuable when it improves both the current change and the next one.
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "github-cli-pr-management-20260321"
prompt: |
  create a marp deck explaining the following content:

  ## Section 6: GitHub CLI & PR Management (00:54:22 - 01:05:34)

  **Duration**: 11:12

  ### Key Topics

  - Discussion of default merge strategy (squash vs. merge commit)
  - GitHub settings navigation for pull request configuration
  - Requesting Copilot code reviews via GitHub web interface
  - GitHub CLI commands for resolving PR comments
  - Personal access token permissions for CLI operations

  ### Subsections

  #### GitHub PR Tools & Extensions

  - GitHub Pull Requests extension for VS Code
  - Viewing PRs directly in IDE for easier context management
  - Lyle Ubben explores resolving comments programmatically via CLI
  - John investigates 'gh pr comment' commands for resolution

  #### Permission & Access Issues

  - Personal access token scope restrictions
  - Classic tokens vs. fine-grained tokens discussion
  - Need for proper permissions to use CLI review features
started: "2026-03-21T17:51:02Z"
ended: "2026-03-21T18:06:02Z"
task_durations:
  - task: "slide outline"
    duration: "00:03:00"
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and catalog updates"
    duration: "00:03:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/github-cli-pr-management-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# GitHub CLI and Pull Request Management || gh pr merge --squash (and Mean It)

<!-- _class: lead -->

## GitHub CLI and PR Management

- Section focus: managing pull requests with GitHub settings, IDE tooling, and the 'gh' CLI
- Outcome: show how merge policy, review tools, and token permissions shape the day-to-day PR workflow

::: notes
Duration ~00:11

Introduce this section as the operational layer around pull requests rather than a pure coding topic. Explain that teams need to understand not only how to create and review PRs, but also how repository settings, IDE integrations, and CLI permissions determine what they can do efficiently.  Transition by starting with the merge strategy decision that affects every PR.
:::

---

## Start with the Merge Strategy

- Decide whether the repository defaults to **squash merge** or **merge commit**
- Squash merge keeps history compact and easier to scan
- Merge commits preserve the exact branch history and commit grouping
- This choice lives in GitHub repository pull request settings

```mermaid
flowchart LR
    A[Feature branch commits] --> B{Merge strategy}
    B -->|Squash| C[One clean commit on main]
    B -->|Merge commit| D[Branch history preserved]
```

::: notes
Duration ~00:02

Explain that merge strategy is a governance decision, not just a button choice at the end of a pull request. Squash merges can make the main branch easier to read, while merge commits retain more detail about how work evolved, so teams should choose based on their review and history preferences.  Transition by moving from repository settings into the tools people use to work with PRs day to day.
:::

---

## Use the Right PR Tools for Context

- The **GitHub Pull Requests** extension for VS Code keeps PR context inside the IDE
- Viewing PRs in the editor reduces browser switching
- Local code, review comments, and changed files are easier to compare side by side
- IDE-based review is especially helpful when debugging comment context

```mermaid
flowchart TB
    A[Pull request opened] --> B[Browser view]
    A --> C[VS Code PR extension]
    C --> D[File diff plus code context]
    C --> E[Lower context switching]
```

::: notes
Duration ~00:02

Make the point that tooling choice affects reviewer efficiency. When developers can see the PR, the code, and their local workspace in one environment, they spend less time reconstructing context and more time evaluating the actual change.  Transition by showing how the CLI fits into that same workflow.
:::

---

## Use the CLI for PR Comment Work

- The 'gh' CLI can support PR comment and review workflows from the terminal
- Team members explored 'gh pr comment' commands for practical resolution workflows
- CLI-based actions are useful when scripting or avoiding extra UI navigation
- Not every review action is equally convenient or permitted through the CLI

**Typical CLI goal**

- inspect PR status
- add comments
- help coordinate comment resolution

::: notes
Duration ~00:02

Frame this slide around exploration and experimentation rather than a promise that every review action is frictionless. The CLI is powerful because it lets developers stay in terminal-first workflows and script repeated actions, but there are still limits depending on permissions, command support, and token setup.  Transition by showing that Copilot review itself still often starts in the GitHub web interface.
:::

---

## Request Copilot Review and Then Triage the Output

- Copilot code review can be requested from the GitHub web interface
- After review arrives, teams can use browser, IDE, or CLI tools to manage follow-up work
- Good workflow means choosing the best tool for each step, not forcing one interface for everything
- Review handling still depends on repository settings and auth permissions

```mermaid
flowchart LR
    A[GitHub web UI] --> B[Request Copilot review]
    B --> C[Review comments appear]
    C --> D[Browser triage]
    C --> E[IDE context]
    C --> F[CLI follow-up]
```

::: notes
Duration ~00:02

Explain that PR management is often multi-surface by nature. A team may request the Copilot review in the web UI, inspect the comments in the IDE for better context, and then use the CLI for quick status checks or scripted follow-up actions, so the workflow is hybrid rather than exclusive.  Transition by focusing on why permissions often become the limiting factor.
:::

---

## Permissions Can Block the Best Workflow

- Personal access token scopes determine what CLI operations are allowed
- Insufficient permissions can prevent review-related commands from working
- Teams discussed **classic tokens** versus **fine-grained tokens**
- Proper permissions are required before CLI review features become reliable

**Common friction points**

1. token lacks needed repo or review scope
2. command works in theory but fails in practice
3. workflow changes depending on auth model

::: notes
Duration ~00:02

Stress that many workflow frustrations are really authentication problems in disguise. Developers may assume a CLI command is broken when the actual issue is that the token does not have permission to read, comment on, or manage the review workflow the way they expect.  Transition by ending with the operational lessons teams should carry forward.
:::

---

## Practical Takeaways for PR Management

- Choose a merge strategy intentionally and document it
- Use the VS Code PR extension when local code context matters
- Use 'gh' where it reduces repetitive PR management work
- Expect some Copilot review steps to begin in the web interface
- Verify token permissions early when CLI features do not behave as expected

**Bottom line**: strong PR management is a combination of repository settings, tool selection, and the right access model.

::: notes
Duration ~00:02

Close by summarizing that effective PR management is never just about knowing commands. Teams need a clear merge policy, the right interface for the task at hand, and authentication that supports the workflow they want to use, or else the process becomes slower and more confusing than it needs to be.  End by encouraging the audience to audit both their tools and their permissions before they need them under pressure.
:::