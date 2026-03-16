---
marp: true
theme: default
paginate: true
---

## Advanced Context Techniques

Modern AI tools rely heavily on context quality
Developers can shape context intentionally
Reduces hallucinations, drift, and rework
Strong context discipline is a core AI‑era skill

::: notes
This slide frames the idea that AI quality is directly tied to context quality.

Models don’t “understand” your repo – they interpret whatever you give them.

Advanced context techniques let you control what the model sees and how reliably it stays aligned with your architecture.
:::

---

## File & Folder Mentions (# Syntax)

How it helps
Explicitly pull files into context
Ensures the model references real code, not guesses
Supports cross‑file refactoring and API consistency
Reduces drift in large repos
Examples
#src/utils/date.ts
#services/

::: notes
The # syntax is one of the most powerful ways to anchor Copilot.

It forces the model to load specific files or directories into its working memory.

This is essential when you want the model to follow existing patterns or avoid hallucinating APIs.
:::

---

## Spaces & Knowledge Bases Integration

Why they matter
Persistent, structured context containers
Store architectural rules, domain models, coding standards
Provide long‑term memory beyond a single prompt
Ideal for instruction files and evergreen boundaries
Use cases
Architecture constraints
Domain terminology
API contracts
Coding conventions

::: notes
Spaces and knowledge bases give you a stable context layer that doesn’t depend on prompt length.

Instead of repeating instructions every session, you store them once and let Copilot reference them automatically.

This is especially valuable for brownfield systems with scattered tribal knowledge.
:::

---

## Premium Usage Monitoring

High‑end models = high reasoning cost
Monitor usage patterns to avoid unnecessary calls
Use a tiered strategy:
  - Premium for architecture & refactoring
  - Mid‑tier for implementation
  - Lightweight for boilerplate
Optimize prompts to reduce token consumption

::: notes
Premium models are incredible, but they’re not free.

Monitoring usage helps teams understand where they’re over‑relying on heavyweight models.

A tiered strategy ensures the right model is used for the right task, keeping costs predictable and output quality high.
:::

---

## Token Estimation & Overflow Detection

Models have strict token limits
Overflow causes silent failures:
  - Missing requirements
  - Contradictions
  - Forgotten rules
Techniques to stay within limits:
  - Summaries
  - Chunking
  - Scoped prompts
  - Instruction files

::: notes
Open by explaining that token limits are one of the most important but least visible constraints in AI-assisted development.

When a model exceeds its context window, it silently drops earlier content.

This leads to missing requirements, contradictions, or forgotten rules.

The goal of this section is to help developers recognize overflow symptoms and apply techniques to prevent them.
:::

---

## Why Token Limits Matter

Every model has a maximum context window
Prompts, code, examples, and instructions all consume tokens
Exceeding the limit forces the model to discard earlier content
The model never alerts you when this happens

::: notes
Token limits are a hard boundary.

Everything the model reads – your prompt, code snippets, examples, and even its own reasoning – counts toward the limit.

When the limit is exceeded, the model truncates the earliest content, which often contains critical instructions or architectural rules.
:::

---

## Silent Failure Modes

What Overflow Looks Like
Missing requirements
Contradictions
Forgotten rules
Inconsistent reasoning
Loss of architectural constraints

::: notes
Overflow is subtle.

The model behaves as if you never gave it the missing information.

Developers often misinterpret this as stubbornness or randomness, but it’s simply the model losing context due to token pressure.

These symptoms are your early warning signs.
:::

---

## Technique: Summaries

How Summaries Help
Compress large files into short, high‑signal descriptions
Preserve intent without overwhelming the context window
Reuse summaries across prompts
Reduce noise and improve model alignment

::: notes
Summaries are your first line of defense.

Instead of pasting entire files, summarize their purpose, interfaces, and constraints.

Summaries dramatically reduce token usage while keeping the model aligned with the system’s intent.

They also become reusable context anchors for future prompts.
:::

---

## Technique: Chunking

How Chunking Works
Break large tasks into smaller, self‑contained steps
Provide only the relevant portion of the code
Validate each chunk before moving on
Prevents the model from being overloaded

::: notes
Chunking keeps prompts small and manageable.

Instead of asking the model to refactor a huge file, break the task into sections.

This keeps each prompt within safe token limits and makes the output easier to review, test, and roll back if needed.
:::

---

## Technique: Scoped Prompts

Benefits
Limit the model’s focus to a single module or function
Reduce irrelevant context
Improve accuracy and reduce hallucinations
Keep token usage predictable

::: notes
Scoped prompts are about intentionality.

Tell the model exactly what part of the system to focus on.

This reduces token usage and improves reliability because the model isn’t trying to reason about the entire codebase at once.

It also reduces hallucinations by narrowing the reasoning space.
:::

---

## Technique: Instruction Files

Why They Matter
Move stable rules out of the active prompt
Provide persistent architectural and style guidance
Reduce repeated tokens across sessions
Keep prompts short and high‑signal

::: notes
Instruction files are a powerful way to reduce token load.

Instead of repeating architectural rules or coding standards in every prompt, store them in a persistent instruction file.

This frees up space for task‑specific context and keeps the model aligned with your evergreen architecture.
:::

---
