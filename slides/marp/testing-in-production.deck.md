---
marp: true
theme: default
paginate: true
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "testing-in-production-20260317"
prompt: |
  create a marp deck titled "Testing in Production" explaining the following content:

  ### Key Topics

  - Safe production testing strategies
  - Shadow traffic and canary releases
  - Observability and automated rollback
  - Beta testing groups

  ### Subsection 5.1: Engineered Production Testing

  #### Core Principle

  - Hide features behind flags until ready
  - Test in real environment with real loads

  #### Techniques

  - **Shadow traffic**: Test with production-like traffic without user impact
  - **Canary releases**: Gradual rollout to subset of users
  - **Observability dashboards**: Real-time monitoring of issues
  - **Automated rollback**: Auto-disable features exceeding error budgets

  ### Subsection 5.2: Error Budget Management

  #### Automatic Feature Disabling

  - Set error threshold for features
  - Monitor error rate over time window
  - Auto-disable if threshold exceeded
  - Notify team for investigation

  **Example**: "If more than X errors in Y minutes for this feature, disable and alert"

  ### Subsection 5.3: Beta Testing Strategy

  #### Implementation

  - Create pool of internal users or beta testers
  - Enable features for specific user groups
  - Test in production environment with real data
  - Gather feedback before wider rollout

  #### Benefits

  - Real-world validation with actual loads
  - Early detection of edge cases
  - User behavior often unexpected
  - Reduces risk of full-scale failure
started: "2026-03-17T15:30:00Z"
ended: "2026-03-17T15:42:00Z"
task_durations:
  - task: "draft structure and content"
    duration: "00:08:00"
  - task: "formatting and refinement"
    duration: "00:04:00"
total_duration: "00:12:00"
ai_log: "ai-logs/2026/03/17/testing-in-production-20260317/conversation.md"
source: "johnmillerATcodemag-com"
---
# Testing in Production || Testing in Production: Bravery or Strategy?

## Testing in Production

Safe production testing strategies
Shadow traffic and canary releases
Observability and automated rollback
Beta testing groups

::: notes
Testing in production is not reckless—it's engineered risk management. Traditional staging environments can never fully replicate production conditions, traffic patterns, or edge cases. This module teaches you how to validate changes safely in the real environment where they'll ultimately run. We'll cover feature flags, shadow traffic, canary releases, error budgets, and beta testing strategies.
:::

---

## Why Test in Production?

<!-- layout: Two Content -->

**The Reality Gap**

- Staging can't replicate production scale
- Real user behavior is unpredictable
- Production data reveals edge cases
- Load patterns differ between environments

::: column

**The Risk Without It**

- Mass failures on release day
- No rollback strategy
- Customer-facing incidents
- Extended downtime

::: notes
The gap between staging and production is inevitable. No matter how sophisticated your pre-production environments are, they lack real users, real data volumes, and real integration complexity. Testing in production bridges this gap—but only if you do it safely. Without production testing, your first exposure to production conditions is a full rollout, when the blast radius is maximum. Ask the class: How many have experienced a "worked fine in staging" failure? What was the cost?
:::

---

## Engineered Production Testing

Core principles and safe techniques

::: notes
This section introduces the fundamental techniques for safe production testing. Everything here is built on one core idea: separate deployment from exposure. You can ship code to production without turning it on for users. This decoupling is what makes production testing safe.
:::

---

<!-- layout: Two Content -->

## Core Principle

**Hide features behind flags until ready**

- Deploy code without activating behavior
- Control exposure programmatically
- Enable instant rollback
- Test incrementally with real infrastructure

::: column

**Test in real environment with real loads**

- Production data and integration points
- Actual traffic patterns and volumes
- Real-world latency and failure modes
- Genuine user behavior

::: notes
Feature flags are the foundation of safe production testing. They allow you to deploy new code without exposing users to it. This means you can validate functionality in production infrastructure before risking customer impact. Emphasize that "real loads" includes not just volume, but also the complexity of production integrations—third-party APIs, legacy systems, database constraints, and network conditions that staging can't replicate.
:::

---

<!-- layout: Two Content -->

## Technique 1: Shadow Traffic

**Concept**

Route a copy of production traffic to new code path
Original code serves the actual response
No user impact—shadow results are discarded

**Benefits**

- Zero risk to users
- Production-scale load testing
- Compare old vs. new behavior
- Identify performance regressions

::: column

**Implementation**

Incoming Request
  ├─> Old Code (serves response)
  └─> New Code (logged/monitored, discarded)

::: notes
Shadow traffic is the safest production testing technique. Every production request is duplicated: one copy goes to the existing code (which serves the user), and one copy goes to the new code (which is monitored but discarded). You get full production validation with zero customer risk. Shadow traffic is ideal for testing performance, correctness, and edge-case handling. It's especially valuable for AI-generated code because you can compare outputs between human-written and AI-generated implementations at production scale.
:::

---

<!-- layout: Two Content -->

## Technique 2: Canary Releases

**Concept**

Gradual rollout to increasing percentage of users
Monitor health metrics at each stage
Expand exposure only if metrics are healthy

**Rollout Stages**

- **1%**: Internal employees, beta users
- **5%**: Expand to low-risk segments
- **25%**: Quarter of production traffic
- **100%**: Full rollout after validation

::: column

**Health Checks**

- Error rate within budget
- Latency acceptable
- No spike in support tickets

::: notes
Canary releases incrementally expand feature exposure. Start with 1% of users—often your internal team or a beta cohort—and monitor error rates, latency, and user reports. If metrics remain healthy, expand to 5%, then 25%, and finally 100%. If any stage shows degradation, halt the rollout and investigate. The key: define "healthy" before you start. What error rate is acceptable? What latency threshold? What volume of support tickets? Canary releases turn deployment into a data-driven decision rather than a leap of faith.
:::

---

<!-- layout: Two Content -->

## Technique 3: Observability Dashboards

**Real-time monitoring**

- Feature-specific error rates
- Latency percentiles such as p50, p95, p99
- Resource utilization including CPU and memory
- User impact metrics such as conversion and engagement

**Essential alerts**

- Threshold violations
- Anomaly detection
- Baseline comparisons
- Correlated multi-signal alerts

::: column

**Dashboard example**

```
Feature: Payment Processing v2
├─ Error Rate: 0.8% (baseline: 0.5%) ⚠️
├─ p95 Latency: 320ms (baseline: 280ms) ⚠️
├─ Canary Coverage: 5%
└─ Auto-rollback: ARMED
```

::: notes
Observability is your feedback loop. Without real-time dashboards, production testing is blind guessing. You need visibility into error rates, latency, resource consumption, and business metrics. Crucially, you need these metrics scoped to the feature under test—not just global application health. If your payment processing feature is in canary mode, you need a dashboard that shows error rates specifically for that feature across both the canary and control groups. Modern observability platforms support feature-flag-aware telemetry. This is non-negotiable for safe AI-assisted development.
:::

---

<!-- layout: Two Content -->

## Technique 4: Automated Rollback

**Automated response to failures**

- Define error budgets per feature
- Monitor continuously in real time
- Auto-disable a feature if the budget is exceeded
- Alert the team for investigation

**Why automation matters**

- Humans are too slow
- Response stays consistent
- Blast radius stays smaller
- MTTR drops quickly

::: column

**Rollback conditions**

```yaml
feature: payment_processing_v2
error_budget:
  threshold: 1.0% # max allowed error rate
  window: 5min # measurement period
  action: disable # auto-disable if exceeded
  notify: [oncall-team, slack-alerts]
```

::: notes
Automated rollback is the safety net. If error rates or latency exceed predefined thresholds, the system disables the feature automatically—no human in the loop. This is critical because production incidents escalate rapidly. The time between "something's wrong" and "customers are affected" is measured in seconds. Automated rollback limits the blast radius and ensures a consistent response. Define your thresholds ahead of time based on historical baselines and capacity planning. The example shows a YAML config: if payment processing v2 exceeds 1% error rate in any 5-minute window, disable it and alert the team. Ask: What's the cost of a two-minute delay in rollback?
:::

---

## Error Budget Management

Automatic feature disabling based on thresholds

::: notes
Error budgets formalize reliability targets. Instead of saying "minimize errors," you say "this feature can tolerate X errors per Y minutes." This makes reliability measurable and enforceable through automation.
:::

---

## Error Budget Fundamentals

**Defining the Budget**

- **Threshold**: Maximum allowable error rate or count
- **Window**: Time period for measurement (e.g., 5 min, 1 hour)
- **Action**: What happens when exceeded (disable, alert, throttle)
- **Notify**: Who gets alerted and how

**Example**

> "If more than 10 errors occur in 5 minutes for the 'checkout redesign' feature, automatically disable it and alert the on-call engineer."

::: notes
An error budget is a contract between reliability and velocity. It says: we can afford this many errors before the feature becomes unacceptable. Budgets are set based on historical data, business impact, and user tolerance. A critical payment flow has a tighter budget than an experimental dashboard widget. The example is prescriptive: 10 errors in 5 minutes triggers automatic disabling. This specificity is essential—vague thresholds lead to delayed responses or false positives. Set budgets collaboratively with product, engineering, and SRE.
:::

---

## Automatic Feature Disabling

**Workflow**

1. **Monitor**: Track errors by feature flag
2. **Evaluate**: Check against budget every N seconds
3. **Trigger**: Budget exceeded? Execute action
4. **Disable**: Turn off feature flag
5. **Notify**: Alert team via PagerDuty, Slack, email
6. **Investigate**: Team analyzes root cause

**Implementation Pseudocode**

```python
if feature_errors(window=5min) > 10:
    disable_feature_flag("checkout_redesign")
    alert(oncall_team, "Error budget exceeded")
    log_incident(feature="checkout_redesign",
                 errors=feature_errors(window=5min))
```

::: notes
The workflow is simple: continuous monitoring feeds into a real-time evaluation loop. If the feature's error count exceeds the budget, the system disables the feature and notifies the team. The pseudocode shows the logic: count errors in a rolling window, compare against threshold, disable if exceeded, and log the incident for post-mortem. This automation reduces Mean Time To Detection (MTTD) and Mean Time To Recovery (MTTR). Without it, you rely on humans checking dashboards or responding to customer complaints—both are too slow for modern production systems.
:::

---

<!-- layout: Two Content -->

## Setting the Right Budget

**Factors to Consider**

- **Business Criticality**: Payment > Analytics > Cosmetic UI
- **User Tolerance**: Users tolerate less error in checkout than search
- **Historical Baseline**: What's your current error rate?
- **Feature Maturity**: New features get tighter budgets

::: column

**Budget examples**

- **Payment Processing**
  Critical, budget `5 errors / 5 min`, baseline `2`.
  Zero tolerance for revenue-impacting failure.
- **Search Results**
  High, budget `50 errors / 5 min`, baseline `30`.
  Affects UX, but not direct revenue.
- **Recommendation Widget**
  Medium, budget `200 errors / 5 min`, baseline `150`.
  Non-blocking and experimental.

::: notes
Not all features deserve the same budget. Payment processing is revenue-critical, so its budget is tight: 5 errors in 5 minutes is the limit. Search is important but not as critical, so it gets a higher budget. Recommendations are experimental and non-blocking, so their budget is loose. The "Baseline" column shows current production error rates; budgets are set relative to baseline with some safety margin. The "Justification" column documents why the budget is what it is—this is crucial for audit trails and future adjustments. Ask the class: What features in your system are truly critical? How would you set their budgets?
:::

---

## Beta Testing Strategy

Testing in production with real users, limited exposure

::: notes
Beta testing is production testing with a human feedback loop. You enable features for a curated group of users—internal employees, power users, or external beta testers—and solicit feedback before wider rollout. This combines the realism of production with the safety of controlled exposure.
:::

---

<!-- layout: Two Content -->

## Beta Testing Implementation

**Build the beta pool**

- **Internal users** — employees, QA, product managers
- **External beta testers** — volunteers from the customer base
- **Power users** — high-engagement users who tolerate some risk
- **Segmentation** — role, region, or usage pattern

**Instrumentation**

- Track feature usage
- Log errors and edge cases
- Collect feedback from surveys and support tickets

::: column

**Enable features by cohort**

```python
if user.in_beta_pool("checkout_redesign"):
  show_new_checkout()
else:
  show_old_checkout()
```

::: notes
Beta testing requires a curated pool of users who are willing to experience new features before general availability. Internal users are the safest starting point—they understand the risks and can report issues effectively. External beta testers add diversity and real-world use cases. The code snippet shows feature-flag logic: if a user is in the beta pool for "checkout_redesign," they see the new version; otherwise, they see the old version. Instrumentation is critical: log everything that happens in the beta path so you can diagnose issues and understand user behavior.
:::

---

<!-- layout: Two Content -->

## Benefits of Beta Testing

**Real-world validation**

- Actual users, actual data, actual workflows
- Validates assumptions under production conditions
- Exposes edge cases missed in testing

**Early detection of issues**

- Catch bugs before wide release
- Identify UX problems from real feedback
- Discover integration failures at scale

::: column

**User behavior is often unexpected**

- Users interact in ways you did not anticipate
- Workflows span multiple sessions or devices
- Real usage patterns differ from test scenarios

**Reduces full-scale failure risk**

- Limit blast radius to the beta pool
- Iterate before expanding exposure
- Build confidence incrementally

::: notes
Beta testing is insurance. You get real-world validation with limited blast radius. Users behave unpredictably—they'll click things you didn't expect, enter data in formats you didn't anticipate, and combine features in novel ways. Beta testing surfaces these edge cases before they affect your entire user base. It's also a feedback mechanism: beta users can tell you if the feature makes sense, if the UX is confusing, or if it solves their problem. This qualitative feedback is as valuable as the quantitative metrics from observability. The goal: by the time you release to 100% of users, the feature is proven in production and you have high confidence it will work.
:::

---

<!-- layout: Two Content -->

## Beta Testing Workflow

**Phase 1: Internal Beta**

- 10-50 internal users
- High-touch feedback (Slack, stand-ups)
- Rapid iteration on critical bugs

**Phase 2: External Beta**

- 100-1,000 external testers
- Survey-based feedback
- Monitor error rates and support tickets

::: column

**Phase 3: Gradual Rollout**

- 5% → 25% → 50% → 100%
- Each tier validated before expansion
- Continuous monitoring throughout

::: notes
The workflow is staged. Start with internal users for rapid feedback and iteration—these are your friendliest critics. Expand to external beta testers for scale and diversity. Finally, roll out incrementally to the full user base using canary releases. Each phase has different goals: internal beta catches critical bugs, external beta validates UX and edge cases, gradual rollout ensures production stability at scale. Specify durations and cohort sizes ahead of time so the team knows what success looks like. Document the criteria for moving between phases (e.g., "proceed to external beta if error rate < 0.5% in internal beta").
:::

---

<!-- layout: Two Content -->

## Testing in Production: Key Takeaways

**Core techniques**

- Shadow traffic for zero-risk validation
- Canary releases for incremental exposure
- Observability for monitoring and alerting
- Automated rollback for fast response
- Error budgets for explicit reliability limits
- Beta testing for real-user feedback

::: column

**Mindset shift**

- Production is the ultimate test environment
- Risk is managed, not eliminated
- Deploy does not equal release
- Automation and observability are non-negotiable

::: notes
Testing in production is a disciplined practice, not a gamble. The techniques we've covered—shadow traffic, canaries, observability, automated rollback, error budgets, and beta testing—work together as a system. Feature flags decouple deployment from release. Observability tells you when something goes wrong. Automated rollback limits damage. Error budgets encode acceptable risk. Beta testing gives you qualitative feedback. The mindset shift: production is not scary if you have the right tools and processes. In fact, production is the only environment that truly matters. Everything else is a rehearsal. AI accelerates development velocity, and these techniques ensure you can accelerate safely.
:::

