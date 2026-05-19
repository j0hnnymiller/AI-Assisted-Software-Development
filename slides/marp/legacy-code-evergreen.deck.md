---
marp: true
theme: default
paginate: true
ai_generated: true
model: "openai/gpt-5.4@2026-03-22"
operator: "johnmillerATcodemag-com"
chat_id: "legacy-code-evergreen-20260322"
prompt: |
  create a marp deck explaining the following content:


  ## What is legacy code

  - No universally accepted definition
  - Easier to define what is _not_ legacy code

  ::: notes
  Try this in quick chat:

  - "what are three definitions of legacy code?"
  - "what are 10 definitions of legacy code?"
  - "what are 25 definitions of legacy code?"

  Ask the audience: "Who recognizes these definitions in their work?"

  Encourage discussion about their experiences with legacy code.
  :::

  ---

  ## What is not legacy code

  - All codebases start as greenfield
  - Few codebases are evergreen

  <!--
  Try this in quick chat:
  what are three definitions of code that is not legacy?
  -->

  ::: notes
  Explain greenfield characteristics and why "not legacy" is rare at scale.
  :::

---
# Legacy Code and Evergreen Development || The Code That Time Forgot (But Production Didn't)

  ## Codebases degrade over time

  Due to changes in:

  - Technology
  - Practices
  - People
  - Business rules
  - Workflows
  - Architecture

  ::: notes
  Discuss drivers of decay (tech, people, rules) and give a brief example.
  :::

---




  ## What is Evergreen Code

  - Evergreen code actively resists technical debt
  - Evergreen ≠ Legacy; everything else is
  - Evergreen is the goal
    - If we were to write all over again, it would turn out just like it is

  ::: notes
  Describe evergreen goals: maintainability, minimal debt, and consistent patterns.
  :::

---




  ## Legacy code needs respect not fear

  - It works - Don't break it!
  - It works - Well-tested (by users)
  - It works - It is, what it is
    - "You get what you get and you don't throw a fit"

  ::: notes
  Emphasize safety-first approach: back up, test, and validate before large changes.
  :::
started: "2026-03-22T02:36:51Z"
ended: "2026-03-22T02:41:30Z"
task_durations:
  - task: "slide authoring"
    duration: "00:04:39"
total_duration: "00:04:39"
ai_log: "ai-logs/2026/03/22/legacy-code-evergreen-20260322/conversation.md"
source: "johnmillerATcodemag-com"

---

<!-- _class: lead -->

# Legacy Code and Evergreen Development || The Code That Time Forgot (But Production Didn't)

## Understanding how code ages and how teams respond

::: notes
Duration ~00:01

Open by telling the audience this section is about mindset as much as mechanics. Explain that "legacy code" is often treated like a criticism, but in practice it is a normal state that most long-lived systems eventually reach. Set the expectation that the goal is not to shame existing systems, but to understand how they evolve and how to improve them safely.
:::

---

## What is Legacy Code

- No universally accepted definition
- Easier to define what is _not_ legacy code

::: notes
Duration ~00:02

Start by acknowledging that legacy code means different things to different teams, authors, and organizations. Try this in quick chat: "what are three definitions of legacy code?", then "what are 10 definitions of legacy code?", and finally "what are 25 definitions of legacy code?" to show how many valid viewpoints exist. Ask the audience, "Who recognizes these definitions in their work?" and encourage a short discussion about their own experiences. The key takeaway is that legacy code is a fuzzy label, which is why defining the opposite can sometimes be more useful.
:::

---

## What is Not Legacy Code

- All codebases start as greenfield
- Few codebases are evergreen

::: notes
Duration ~00:02

Explain that every codebase begins as greenfield because, at the beginning, there is no accumulated history, constraint, or drift. Then contrast that with evergreen code, which is code that has been intentionally maintained so well that it still feels current and appropriate. If you want an audience prompt, ask quick chat for "three definitions of code that is not legacy" and compare the results to the previous slide. Emphasize that truly non-legacy code is rare at scale because most systems accumulate compromises over time.
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
Duration ~00:02

Walk down the list and connect each item to a real-world example. Technology changes when a framework, platform, or dependency becomes outdated; practices change when teams adopt new standards; people change when context leaves with staff turnover. Business rules and workflows evolve because organizations evolve, and architecture changes because systems are restructured around new priorities. Reinforce that code decay is often less about bad developers and more about a changing environment around otherwise useful software.
:::

---




## What is Evergreen Code

- Evergreen code actively resists technical debt
- Evergreen != Legacy; everything else is
- Evergreen is the goal
  - If we were to write all over again, it would turn out just like it is

::: notes
Describe evergreen code as intentionally maintained, consistently refactored, and aligned with current needs rather than frozen in time. Stress that evergreen does not mean perfect; it means the code still reflects good choices for today's context and can absorb change without excessive friction. The quote on the slide is a useful test: if you rebuilt the system now and would make essentially the same decisions, the code is probably evergreen. Ask the audience to think of any area in their codebase that passes that test, then transition to how we should approach code that does not.
:::

---

## Legacy Code Needs Respect, Not Fear

- It works - Don't break it!
- It works - Well-tested (by users)
- It works - It is what it is
  - "You get what you get and you don't throw a fit"

::: notes
Duration ~00:02

Close by reframing legacy code as something that has already proven it can deliver value. Explain that production use is a form of testing, even if that testing is informal and hard-won, so careless rewrites are risky. Emphasize a safety-first approach: back up the code, add characterization tests where possible, make small changes, and validate behavior before expanding the scope of refactoring. End with the reminder that respect leads to careful improvement, while fear often leads to avoidance or reckless rewrites.
:::
