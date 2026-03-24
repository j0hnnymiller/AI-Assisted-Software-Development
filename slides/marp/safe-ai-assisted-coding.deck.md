---
marp: true
theme: default
paginate: true
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "safe-ai-assisted-coding-20260314"
prompt: |
  merge these marp decks: "_Safe Brownfield Coding.pptx";
  "_Essential Safety Measures.pptx"; "_Building Safety Nets.pptx"
started: "2026-03-14T20:05:00Z"
ended: "2026-03-14T20:12:00Z"
task_durations:
  - task: "PPTX extraction and Marp authoring"
    duration: "00:07:00"
total_duration: "00:07:00"
ai_log: "ai-logs/2026/03/14/safe-ai-assisted-coding-20260314/conversation.md"
source: "johnmillerATcodemag-com"
---

## Safe AI-Assisted Coding

Using feature flags to minimize risk
As-Is and To-Be test suites
Essential safety measures
Building safety nets
Exercises throughout

::: notes
Welcome to this combined module on safe AI-assisted coding in brownfield codebases. Stress at the outset that AI acceleration without safety discipline creates new categories of risk. The three sections — Safe Brownfield Coding, Essential Safety Measures, and Building Safety Nets — form a coherent strategy: introduce change safely, validate it rigorously, and protect the systems that run the business.
:::

---




<!-- Part 1 -->

## Safe Brownfield Coding

Using feature flags to minimize risk
As-Is and To-Be test suites
Testing in production
Retiring feature flags
Exercise: Implementing a feature flag

::: notes
Part 1 focuses on the mechanics of introducing change safely into a living codebase. Feature flags are the primary technique: they decouple deployment from release, allowing you to ship code to production before exposing users to new behavior. As-Is and To-Be test suites capture the contract between old and new. Production testing completes the picture by giving you real-world feedback before full rollout.
:::

---




## Using Feature Flags

**Why feature flags matter**

- Enable incremental rollout
- Allow instant rollback
- Reduce blast radius
- Support A/B testing and shadow traffic
- Decouple deployment from release

**Best practices**

- Keep flags short-lived
- Name flags clearly
- Document intent and retirement criteria

::: notes
Feature flags are the safest mechanism for introducing AI-generated changes into a brownfield system. A flag makes every change reversible without a code deployment. Emphasize the blast-radius point: if the new behavior is wrong, only flagged users are affected. The best-practices list is non-negotiable in a brownfield context — flag sprawl is a real problem and AI can accelerate it if teams are not disciplined. Name flags with enough context that a reader six months from now understands what the flag does and when it was intended to retire.
:::

---




## Retiring Feature Flags

**Why retirement matters**

- Prevents flag bloat
- Reduces cognitive load
- Simplifies code paths
- Ensures long-term maintainability

**Retirement workflow**

- Validate stability
- Remove old code paths
- Update documentation
- Add provenance to the change

::: notes
Feature flags that are never retired become permanent complexity. This is especially dangerous with AI-generated code because AI can produce large volumes of flagged changes in a short time. Walk through the retirement workflow: confirm the new behavior is stable in production, delete the old branch, update tests to reflect the new reality, and document the change with provenance metadata so the audit trail is clear. Ask students: what is the cost of a flag that is never retired? The answer is both cognitive and operational — it affects every developer who reads the code and every test that branches on it.
:::

---




## As-Is and To-Be Test Suites

**As-Is tests**

- Capture current behavior
- Protect against regressions
- Document legacy expectations

**To-Be tests**

- Define desired future behavior
- Guide modernization
- Validate new patterns and architecture

::: notes
The As-Is / To-Be pairing is a foundational technique for brownfield modernization. Before changing anything, write tests that describe what the system currently does — even if that behavior seems wrong. These tests are your insurance policy. To-Be tests describe what you want to be true after the change. Running both suites simultaneously is how you know whether the transition is complete and safe. AI is excellent at generating To-Be tests from a description of desired behavior; it is less reliable at generating As-Is tests because it cannot observe production behavior directly. Always pair AI-generated As-Is tests with manual review.
:::

---




## Testing in Production

**Safe production testing techniques**

- Feature-flag-controlled exposure
- Shadow traffic
- Canary releases
- Observability dashboards
- Error-budget-based rollout

**Benefits**

- Real-world validation
- Early detection of edge cases
- Reduced risk of full-scale failures

::: notes
No test suite in development can fully replicate production conditions. Shadow traffic — routing a copy of real requests to the new code path without affecting users — is the gold standard for validating AI-generated changes. Canary releases expose a small percentage of users to new behavior while monitoring error budgets. Emphasize that these techniques are layered: feature flags enable canaries; observability dashboards tell you when to stop. Ask: what does your current observability stack capture, and is it sufficient to detect a regression introduced by AI-generated code?
:::

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

---




<!-- Part 2 -->

## Essential Safety Measures

AI accelerates development — but also accelerates mistakes
Strong safety nets must be in place before introducing AI into a brownfield codebase
These practices reduce risk, increase confidence, and protect production systems

::: notes
Part 2 elevates from individual techniques to organizational practices. The opening statement is deliberate: AI is a force multiplier, and a force multiplier amplifies both good and bad decisions. Teams that introduce AI without safety measures in place will move fast and break things — in production, with real users. Frame these practices not as bureaucracy but as the infrastructure that makes AI-assisted development sustainable.
:::

---




## Backup & Rollback Strategies

- Use branching strategies that isolate AI-generated changes
- Commit early and often to create natural rollback points
- Archive snapshots of critical modules before modernization
- Ensure you can revert any AI-assisted change without drama
- Use feature flags to separate release from deployment

::: notes
Branching strategy is the first line of defense. AI-generated changes should live in short-lived feature branches that are easy to squash and revert. "Commit early and often" creates fine-grained rollback points — if the AI-generated refactor breaks something on step 7, you can revert to step 6 rather than the beginning. Archiving snapshots of critical modules is especially important for systems without test coverage: the snapshot becomes the implicit specification. Ask students: how long would it take you to roll back an AI-generated change that has been merged to main and deployed? If the answer is "hours," that is a gap.
:::

---




## Confidence Frameworks

- Strong tests are the backbone of safe AI-assisted refactoring
- Unit, integration, and behavioral tests validate AI output
- Coverage matters less than signal quality
- Tests should detect regressions, not just assert happy paths
- _If all of the test automation passes, how confident are you to deploy to production?_

::: notes
The closing question is the most important slide on this topic. A high coverage number is meaningless if the tests only assert happy paths and never detect regressions. Signal quality — the ability of a test failure to indicate a real problem — is what matters. AI can generate high-coverage tests quickly, but those tests may be shallow. Require that AI-generated tests include negative cases, boundary conditions, and realistic edge cases. The confidence question should be asked regularly during sprint reviews.
:::

---




## Change Review Processes

- Treat AI as a junior developer: everything gets reviewed
- Use human-in-the-loop validation for correctness and intent
- Require architectural review for structural changes
- Enforce standards through linters, static analysis, and policy checks
- Leverage AI to reduce the review burden

::: notes
The "junior developer" framing is intentional and useful: junior developers produce valuable code, but it requires mentorship and review. AI is similar — capable but not infallible. Human-in-the-loop validation is not optional in a brownfield context where the cost of a production defect is high. Architectural review for structural changes protects against pattern drift: AI may refactor toward patterns that are locally reasonable but globally inconsistent. The last bullet is the payoff: AI can pre-screen diffs, flag risky patterns, and generate review checklists, reducing the cognitive load on human reviewers.
:::

---




## Incremental Change Methodology

- Break modernization into small, safe, reversible steps
- Avoid "big bang" refactors — they're brittle and risky
- Use iterative loops: propose → validate → refine → commit
- Let AI assist with each step rather than entire subsystems at once

::: notes
Big-bang refactors are the most common failure mode in brownfield modernization. They produce large diffs that are hard to review, create many merge conflicts, and are catastrophic when they fail. The propose → validate → refine → commit loop is the antidote. AI is excellent at the "propose" step; humans and automated tests cover the "validate" step; AI assists with "refine"; the team decides when to commit. Emphasize "each step rather than entire subsystems at once" — this requires discipline because AI will happily refactor an entire subsystem in one shot if you ask it to.
:::

---




## Keeping Change Sets Small

- Small diffs are easier to review and validate
- Small changes reduce merge conflicts and regression risk
- AI should be instructed to limit scope intentionally
- Small changes accumulate into large improvements over time
- **Beware: AI can produce huge amounts of code quickly**

::: notes
The final bullet is the warning: AI's ability to generate large volumes of code quickly is both its strength and its danger in a brownfield context. A developer asking "refactor this entire module" may receive a thousand-line diff that is technically correct but impossible to review safely. Instruct students to scope their AI prompts explicitly: "refactor only this function," "add error handling to only these two lines," "do not change the function signature." Small, scoped prompts produce small, reviewable diffs that accumulate into substantial progress.
:::

---




## Respecting Brownfield Code

- Brownfield systems are valuable — they run the business
- Avoid assumptions that "old" means "wrong"
- Understand the constraints that shaped the existing design
- Modernize with empathy, not aggression

::: notes
Close Part 2 with a values statement. Brownfield codebases have history — decisions that seem wrong today were often correct given the constraints of their time. Approaching legacy code with contempt ("this is terrible, let's rewrite it") is a recipe for breaking things that were not broken. Modernize with empathy: ask why a pattern was chosen, not just what it does. AI can help decode legacy patterns — ask it to explain a confusing piece of code before asking it to change it. This builds understanding and reduces the risk of breaking implicit contracts.
:::

---




<!-- Part 3 -->

## Building Safety Nets

Protecting brownfield codebases
Leveraging AI code reviews
Effective human code reviews
The role of test automation
Exercise: Building safety nets in practice

::: notes
Part 3 synthesizes the previous sections into a practical framework for building safety nets. A safety net is anything that catches a problem before it reaches users: tests, code reviews, AI-assisted analysis, observability, and documentation. Building safety nets before modernizing is not overhead — it is the prerequisite that makes modernization safe. Introduce this section as the backbone of safe AI-assisted development.
:::

---




## Protecting Brownfield Codebases

**Key Practices**

- Preserve existing behavior unless intentionally changed
- Avoid large, risky refactors
- Use incremental modernization
- Maintain architectural boundaries
- Document every AI-assisted change

**Why it matters**

- Brownfield systems run the business
- Stability is more important than novelty
- Safety nets reduce fear and increase confidence

::: notes
Behavioral preservation is the prime directive: every change must be intentional and documented. "Incremental modernization" and "maintain architectural boundaries" work together — incremental changes are easier to contain within boundaries. Documenting AI-assisted changes is both an audit trail and a learning record. Ask students: how would you know, six months from now, which parts of the codebase were modified by AI? If the answer is "we wouldn't," that is a risk. Provenance metadata and conventional commit messages that tag AI-assisted changes solve this problem.
:::

---




## Leveraging AI Code Reviews

**AI can assist by:**

- Highlighting risky changes
- Detecting missing tests
- Identifying architectural violations
- Suggesting safer alternatives
- Surfacing potential regressions

**Benefits**

- Faster feedback loops
- More consistent review quality
- Early detection of drift

::: notes
AI code review is most valuable as a pre-screen before human review. It catches the obvious problems — missing error handling, missing tests, obvious anti-patterns — so human reviewers can focus on intent, correctness, and architectural alignment. Demo opportunity: paste a simple diff into Copilot Chat and ask "what risks do you see in this change?" Show that the AI identifies missing edge cases or documentation gaps. Consistent review quality is a significant benefit in teams where code review load is high and reviewer attention varies.
:::

---




## Effective Human Code Reviews

**Human reviewers focus on:**

- Intent and correctness
- Architectural alignment
- Business logic validation
- Risk assessment
- Ensuring changes are incremental and reversible

**Best practices**

- Review small change sets
- Ask for context when missing
- Validate AI-generated code with skepticism and curiosity

::: notes
Human reviewers bring judgment that AI cannot: they know the business domain, the team's architectural decisions, and the history of the codebase. The final best practice — "skepticism and curiosity" — is the right posture for AI-generated code. Skepticism means not trusting output because it looks correct; curiosity means asking why the AI made a particular choice. This posture produces better reviews and better understanding. Encourage students to treat AI-generated code the same way they treat code from a talented but new team member: capable but worth verifying.
:::

---




## The Role of Test Automation

**Test automation provides:**

- Behavioral guarantees
- Regression detection
- Confidence for modernization
- Guardrails for AI-assisted refactoring

**Types of tests**

- Unit tests
- Integration tests
- End-to-end tests
- Snapshot and contract tests

::: notes
Snapshot and contract tests deserve emphasis in brownfield contexts: snapshot tests capture the exact output of a function and fail if it changes; contract tests capture the API contract between services. Both are powerful as As-Is safety nets. AI is very good at generating unit and integration tests from existing code — but always verify that AI-generated tests actually detect the regressions they claim to detect by intentionally breaking the code and confirming the tests fail. A test that never fails provides false confidence.
:::

---

## Exercise: Building the Safety Nets

**Objectives**

- Identify missing safety nets in a brownfield system
- Strengthen protection using AI and human review practices
- Apply test automation principles
- Produce actionable improvements

**Activities**

1. Select a brownfield module or file
2. Identify existing safety nets (tests, reviews, documentation)
3. Ask AI to identify missing or weak safety nets
4. Strengthen by adding tests, drafting review checklists, documenting architectural constraints
5. Share findings with a partner for validation

**Success Criteria**: missing nets identified, improvements are safe and incremental, coverage or clarity improved, review and documentation guardrails are strengthened

::: notes
Duration ~00:20

This exercise is the capstone of the combined module. Students apply all three sections simultaneously: they audit a real codebase, use AI to find gaps, and produce a concrete list of improvements. The partner validation step is important — it simulates the human-in-the-loop review process and often surfaces things one person missed. Debrief questions: what was missing that surprised you? How did AI's assessment of the safety nets compare to your own? What would you prioritize first? Encourage students to bring their findings back to their teams.
:::
