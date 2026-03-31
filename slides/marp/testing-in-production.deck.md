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

---

## Testing in Production

- Safe production testing strategies
- Shadow traffic and canary releases
- Observability and automated rollback
- Beta testing groups

::: notes
Testing in production is not reckless—it's engineered risk management. Traditional staging environments can never fully replicate production conditions, traffic patterns, or edge cases. This module teaches you how to validate changes safely in the real environment where they'll ultimately run. We'll cover feature flags, shadow traffic, canary releases, error budgets, and beta testing strategies.
:::

---

<!-- layout: Two Content -->

## Why Test in Production?

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
  - Route a copy of production traffic to new code path
  - Original code serves the actual response
  - No user impact—shadow results are discarded

**Benefits**
  - Zero risk to users
  - Production-scale load testing
  - Compare old vs. new behavior
  - Identify performance regressions

::: column

**Implementation**

```
Incoming Request
  ├─> Old Code (serves response)
  └─> New Code (logged/monitored, discarded)
```

::: notes
Shadow traffic is the safest production testing technique. Every production request is duplicated: one copy goes to the existing code (which serves the user), and one copy goes to the new code (which is monitored but discarded). You get full production validation with zero customer risk. Shadow traffic is ideal for testing performance, correctness, and edge-case handling. It's especially valuable for AI-generated code because you can compare outputs between human-written and AI-generated implementations at production scale.
:::

---

<!-- layout: Two Content -->

## Technique 2: Canary Releases

**Concept**
  - Gradual rollout to increasing percentage of users
  - Monitor health metrics at each stage
  - Expand exposure only if metrics are healthy

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

