---
marp: true
theme: default
paginate: true
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "understanding-legacy-code-20260322"
prompt: |
  create a marp deck explaining the following content:
  What is legacy code, what is not legacy code, how codebases degrade over time,
  what is evergreen code, and legacy code needs respect not fear.
started: "2026-03-22T02:31:38Z"
ended: "2026-03-22T02:34:00Z"
task_durations:
  - task: "slide creation"
    duration: "00:02:30"
total_duration: "00:02:30"
ai_log: "ai-logs/2026/03/22/understanding-legacy-code-20260322/conversation.md"
source: "johnmillerATcodemag-com"
---
# Understanding Legacy Code || Legacy Code Deserves Respect

## What is Legacy Code

- No universally accepted definition
- Easier to define what is _not_ legacy code

::: notes
Try this in quick chat:

- "what are three definitions of legacy code?"
- "what are 10 definitions of legacy code?"
- "what are 25 definitions of legacy code?"

Ask the audience: "Who recognizes these definitions in their work?"

Encourage discussion about their experiences with legacy code. This primes the audience to think critically about the term rather than accepting a single definition. The variety of answers from AI prompts demonstrates that the concept is genuinely contested. (~2 minutes)
:::

---

## What is Not Legacy Code

- All codebases start as greenfield
- Few codebases are evergreen

::: notes
Explain greenfield characteristics: new code, clear patterns, modern tooling, no accumulated debt. The key insight is that greenfield is the starting point, not a permanent state. Ask: how many in the room are working on a truly greenfield project right now? The answer is usually "very few." Evergreen is the rare exception — code that has been actively maintained to resist decay. Most production code falls somewhere on the spectrum between "recently greenfield" and "deeply legacy." (~1.5 minutes)
:::

---

## Codebases Degrade Over Time

Due to changes in:

- Technology
- Practices
- People
- Business rules
- Workflows
- Architecture

::: notes
Discuss each driver of decay with a brief example. Technology: the framework you chose in 2015 is now unmaintained. Practices: the team that wrote this used a different style guide. People: the original authors left and took context with them. Business rules: the logic was correct for the old pricing model, not the new one. Workflows: the CI/CD pipeline changed but the code assumptions didn't. Architecture: microservices replaced the monolith but some code was never migrated. The point: code doesn't degrade because developers did something wrong — it degrades because the world around it changed. (~2 minutes)
:::

---

## What is Evergreen Code

- Evergreen code actively resists technical debt
- Evergreen ≠ Legacy; everything else is
- Evergreen is the goal
  - _"If we were to write it all over again, it would turn out just like it is"_

::: notes
Describe evergreen goals: maintainability, minimal debt, and consistent patterns that still align with modern practices. The defining characteristic is that evergreen code is intentional — it doesn't happen by accident. Teams invest in keeping it current. The quote on the slide is the ultimate test: if you'd make the same decisions today, the code is evergreen. If you'd do it differently, it has started to decay. Use this as a reflective question for the audience: can they point to any part of their codebase that passes this test? (~2 minutes)
:::

