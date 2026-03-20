---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "feature-flags-test-suites-20260319"
prompt: |
  create a marp deck titled "Feature Flags and Test Suites" explaining the following content:

  ## Section 4: Feature Flags and Test Suites (Duration: ~00:07:00) [x]

  **Time Range**: 00:45:12 - 00:52:12

  ### Key Topics

  - Feature flags for managing work-in-progress
  - As-Is vs. To-Be test suites
  - Safe deployment strategies

  ### Subsection 4.1: As-Is Test Suites

  #### Purpose

  - Capture current behavior in tests
  - Protect against regressions
  - Document expectations for production

  #### Core Strategy

  - Go to production anytime As-Is tests pass
  - New implementations hidden behind feature flags
  - High confidence with compiled code + passing As-Is tests

  #### Growing the As-Is Suite

  - Add tests before making code modifications
  - Increase coverage as changes are identified
  - Build trust in test suite incrementally

  #### Critical Rule

  - **Feature flag discipline**: Ensure new code wrapped by feature flags
  - **Watch for bleed**: Any unwrapped code will hit production
  - **As-Is tests as gate**: These define production readiness

  ### Subsection 4.2: To-Be Test Suites

  #### Purpose

  - Define future behavior
  - Validate work-in-progress features
  - Track implementation progress

  #### Workflow

  1. Implement feature flag around code to modify
  2. When flag ON: Execute new behavior
  3. Write tests that only run when feature flag ON
  4. Separate test execution strategy in pipeline

  #### Automation Strategy

  **Phase 1**: As-Is Tests

  - Set flags to match production state
  - Run current behavior tests
  - Look for regressions

  **Phase 2**: To-Be Tests

  - Turn on appropriate flags
  - Execute To-Be testing
  - Assess progress toward completion

  #### Benefits

  - Smaller To-Be suite for check-in procedures
  - Guide modernization efforts
  - Validate new practices and architectures

  #### Maintenance Requirement

  **After Production Release**:

  - Move To-Be tests into As-Is suite
  - Tests become part of regression suite
  - Maintain consistency with production state

  ### Subsection 4.3: Feature Flag Retirement

  **AI-Assisted Approach**:

  - Before AI: Create pull request to implement flag, merge, retire later
  - With AI: Ask to "identify changes needed to remove this feature flag"
  - AI effectively removes feature flags from codebase
started: "2026-03-19T19:45:09-07:00"
ended: "2026-03-19T20:05:00-07:00"
task_durations:
  - task: "structure content"
    duration: "00:06:00"
  - task: "draft slide deck"
    duration: "00:09:00"
  - task: "add provenance files"
    duration: "00:04:00"
  - task: "update README"
    duration: "00:01:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2026/03/19/feature-flags-test-suites-20260319/conversation.md"
source: "johnmillerATcodemag-com"
---

marp: true
theme: default
paginate: true
backgroundColor: #ffffff

---

# Feature Flags and Test Suites

## Safe Delivery for Work in Progress

Section 4 · 00:45:12 - 00:52:12

::: notes
Open by framing this section as a practical deployment safety pattern for brownfield work.

Key message: feature flags are not only a release mechanism. They are also a testing and change-management boundary.

Emphasize the three ideas that tie the section together:

- protect current production behavior with As-Is tests
- validate future behavior with To-Be tests
- use flags to keep work-in-progress isolated until ready

Suggested timing: 45 seconds.
Transition: move from the title into why these patterns matter operationally.
:::

---

## Section Overview

### Key Topics

- **Feature flags** for managing work-in-progress safely
- **As-Is test suites** for protecting current production behavior
- **To-Be test suites** for validating future behavior under flags
- **Deployment discipline** that keeps incomplete work out of production
- **Feature flag retirement** once the new path is proven

### Working Principle

**Production readiness = compiled code + production-aligned flags + passing As-Is tests**

::: notes
Use this slide to establish vocabulary early.

Define As-Is as the current production contract. Define To-Be as the desired future contract. Explain that flags let both contracts coexist temporarily without confusing deployment readiness.

Call out that the deck is about safe modernization, not just feature toggles.

Suggested timing: 45 seconds.
Transition: explain why feature flags are the enabling mechanism.
:::

---

## Feature Flags for Managing Work in Progress

### Why They Matter

- Hide incomplete implementations from production traffic
- Let teams merge incrementally without exposing unfinished behavior
- Support safe rollout, rollback, and staged validation
- Create a clean switch between current and future paths

### The Discipline Requirement

- **Every changed path must be wrapped** when the new behavior is not ready
- **Any unwrapped code can bleed into production**
- Flags are only safe when the test strategy matches the flag strategy

::: notes
Stress that flags are not magic. The safety comes from disciplined usage.

Good phrasing for delivery: “A feature flag is a boundary. If you leave holes in the boundary, production traffic finds them.”

This is the setup for why As-Is tests are the deployment gate.

Suggested timing: 45 seconds.
Transition: shift into As-Is suites as the primary production gate.
:::

---

## As-Is Test Suites

### Purpose

- Capture **current behavior** in executable tests
- Protect against regressions while modernization is underway
- Document what production is expected to do today

### Core Strategy

- Go to production anytime **As-Is tests pass**
- Keep new implementations hidden behind feature flags
- Build confidence from **compiling code + passing As-Is tests**

::: notes
This is one of the most important slides in the deck.

Frame As-Is tests as the answer to: “Can I ship right now without harming current users?” If the answer is yes, the current production contract is intact.

Clarify that As-Is does not mean ideal or modern. It means the current supported behavior.

Suggested timing: 1 minute.
Transition: explain how the As-Is suite grows over time instead of being complete on day one.
:::

---

## Growing the As-Is Suite Incrementally

### Practical Expansion Pattern

1. Identify code you need to change
2. Add tests that capture existing behavior first
3. Confirm those tests pass before modifying code
4. Use the tests as the baseline safety net for future edits

### Why This Works

- Coverage grows where change risk is highest
- Trust in the test suite builds incrementally
- The suite becomes more valuable with each change

::: notes
Make the point that teams do not need perfect coverage before they start. They need strategic coverage around the change surface.

This is a useful brownfield message: add tests where you are about to operate, not everywhere at once.

Suggested timing: 45 seconds.
Transition: reinforce the critical rule that keeps this safe.
:::

---

## Critical Rule: As-Is Tests Define Production Readiness

### Non-Negotiables

- **Feature flag discipline**: wrap all new behavior that is not production-ready
- **Watch for bleed**: unwrapped code paths can reach production users
- **As-Is tests are the gate**: they define whether the app is safe to ship now

### Operational Meaning

If production flags are set to current behavior and As-Is tests pass, the build is deployable.

::: notes
Deliver this as the governing rule of the section.

This is where you tie testing, flags, and deployment together. The audience should leave with the idea that production readiness is evaluated against the current contract, not the aspirational one.

Suggested timing: 40 seconds.
Transition: now introduce To-Be suites as the way to validate future behavior without weakening the As-Is gate.
:::

---

## To-Be Test Suites

### Purpose

- Define the **future behavior** of the system
- Validate work-in-progress features safely
- Measure implementation progress against the target state

### Core Workflow

1. Implement a feature flag around the code being changed
2. When the flag is **ON**, execute the new behavior
3. Write tests that only run when the flag is **ON**
4. Execute these tests separately from the As-Is deployment gate

::: notes
Explain that To-Be tests are forward-looking. They are not the production gate while the feature is still in progress.

Useful phrasing: “As-Is tells us whether we can ship now. To-Be tells us whether we’re getting closer to what we want to ship later.”

Suggested timing: 1 minute.
Transition: show how the pipeline should execute both suites without mixing their purpose.
:::

---

## Two-Phase Pipeline Strategy

### Phase 1: As-Is Tests

- Set flags to match **production state**
- Run tests for current behavior
- Look for regressions and deployment blockers

### Phase 2: To-Be Tests

- Turn on the appropriate feature flags
- Run tests for new behavior only
- Assess progress toward the completed implementation

### Result

One pipeline answers two different questions without confusing them.

::: notes
This slide is about automation clarity.

Explain that mixing current-state and future-state expectations in one suite creates noise. Separating them makes check-ins cleaner and makes release decisions more defensible.

If helpful, mention that teams may run As-Is on every merge and To-Be on branches, PRs, or targeted CI jobs depending on maturity.

Suggested timing: 50 seconds.
Transition: summarize the delivery and modernization advantages of this pattern.
:::

---

## Benefits of the Split-Suite Model

### Delivery Benefits

- Safe check-ins even when a feature is incomplete
- Smaller, more focused To-Be suites for in-progress work
- Faster regression confidence from a stable As-Is gate

### Modernization Benefits

- Guides refactoring and architectural change deliberately
- Validates new practices before full cutover
- Makes progress visible without exposing partial work

::: notes
Frame this as a way to increase both safety and velocity.

This is not additional ceremony for its own sake. It reduces ambiguity in team workflows and gives engineering leaders clearer answers about what is safe to deploy versus what is still being built.

Suggested timing: 40 seconds.
Transition: next, explain the maintenance obligation once the feature goes live.
:::

---

## After Release: Move To-Be into As-Is

### Maintenance Requirement

Once the new behavior becomes production behavior:

- Move the relevant **To-Be tests** into the **As-Is suite**
- Let them become part of the main regression safety net
- Keep the test suite aligned with actual production state

### Why It Matters

- Prevents obsolete expectations from lingering
- Keeps the deployment gate honest
- Avoids maintaining two competing truths indefinitely

::: notes
This is the cleanup step teams often skip.

Explain that the split-suites model is temporary by design. If the new path is now the real path, the regression suite must reflect that reality. Otherwise the safety model drifts.

Suggested timing: 40 seconds.
Transition: use that cleanup idea to introduce feature flag retirement itself.
:::

---

## Feature Flag Retirement

### Traditional Pattern

- Create PR to add the flag
- Merge and ship safely behind the flag
- Return later to remove the flag manually

### AI-Assisted Pattern

- Ask AI to **identify changes needed to remove this feature flag**
- Use the response to remove obsolete branches, conditions, and tests
- Simplify the codebase after the rollout is complete

### Goal

Treat flag retirement as a planned cleanup task, not optional future work.

::: notes
Emphasize that flags are useful only when temporary. Permanent flags accumulate complexity, duplicate branches, and test overhead.

AI is especially strong here because flag cleanup is often mechanical: find conditionals, collapse branches, remove dead tests, and simplify configuration.

Suggested timing: 45 seconds.
Transition: show the full end-to-end flow as one lifecycle.
:::

---

## End-to-End Workflow

### Recommended Sequence

1. Add As-Is tests around the code you will change
2. Introduce the feature flag around the new implementation
3. Keep the As-Is suite aligned with production behavior
4. Build To-Be tests for the new path under the flag
5. Run both phases in CI for different decisions
6. Release the feature to production when ready
7. Promote To-Be tests into As-Is
8. Retire the feature flag and dead code

::: notes
This slide ties the whole system together into one repeatable pattern.

Encourage the audience to think of this as a modernization playbook. It works especially well in brownfield systems where big-bang rewrites are too risky.

Suggested timing: 45 seconds.
Transition: finish with the concise operational takeaways.
:::

---

## Key Takeaways

- **As-Is tests** protect what production does today
- **To-Be tests** validate what production should do tomorrow
- **Feature flags** isolate unfinished behavior safely
- **Separate pipeline phases** prevent deployment confusion
- **Retirement matters**: after release, move tests and remove the flag

### Final Principle

**Use feature flags to manage change, and use test suites to define when that change is safe.**

::: notes
Close with the operating model, not the mechanics.

If there is time, ask the audience which part their current workflow is missing: As-Is coverage, To-Be validation, pipeline separation, or flag retirement discipline.

Suggested timing: 30 seconds.
Transition: hand off to the next section or open for questions.
:::
