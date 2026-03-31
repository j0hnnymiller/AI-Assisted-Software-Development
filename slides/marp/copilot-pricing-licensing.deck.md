---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "copilot-pricing-licensing-20260314"
prompt: |
  create a marp deck describing GitHub Copilot Pricing & Licensing. Include Business vs. Enterprise
  license comparison; $19/month per user for business license; Organization-level instruction files access
started: "2026-03-14T15:53:12Z"
ended: "2026-03-14T15:53:30Z"
task_durations:
  - task: "draft"
    duration: "00:00:18"
total_duration: "00:00:18"
ai_log: "ai-logs/2026/03/14/copilot-pricing-licensing-20260314/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# GitHub Copilot Pricing and Licensing || How Much Does an AI Pair Programmer Cost?

---

### What you need to know for your organization

::: notes
Duration ~00:01

Introduce the topic by framing it as a decision teams need to make. Most developers have heard of Copilot, but licensing details are often misunderstood. This session clarifies the tiers and what each unlocks.

Transition: "Let's start with an overview of what's available."
:::

---

<!-- layout: Two Content -->

## Copilot Plan Overview

| Feature                        | Individual | Business          | Enterprise    |
| ------------------------------ | ---------- | ----------------- | ------------- |
| **Price**                      | `$10/mo`   | **`$19/user/mo`** | `$39/user/mo` |
| Code completions               | ✅         | ✅                | ✅            |
| Copilot Chat                   | ✅         | ✅                | ✅            |
| Policy management              | ❌         | ✅                | ✅            |
| Org instruction files          | ❌         | ✅                | ✅            |
| Includes Business capabilities | —          | —                 | ✅            |
| Enterprise-only features       | —          | —                 | ✅            |

::: notes
Duration ~00:02

Walk through the table column by column, not row by row — it helps the audience track each tier's value proposition.

Key talking points:

- Individual is for solo developers; no organizational control
- Business at $19/user/month is the sweet spot for most teams
- Enterprise adds Copilot Knowledge Bases, fine-tuning, and advanced audit logs
- All paid plans include unlimited completions and chat

Emphasize: Business tier is where most organizations should start. Enterprise is for large orgs with compliance or custom knowledge needs.
:::

---

<!-- layout: Two Content -->

## Business vs. Enterprise

Business ($19/user/mo)
- Organization-wide policy management
- Org-level instruction files (`.github/instructions/`)
- Content exclusions & audit logs
- Standard model access

::: column

Enterprise ($39/user/mo) — adds:

- **Copilot Knowledge Bases** — index your internal docs & repos
- **Fine-tuned models** on your private codebase
- **Advanced audit & usage analytics**
- **Copilot in GitHub.com** (PR summaries, issue chat)
- Enhanced compliance & data residency options

::: notes
Duration ~00:03

Frame this as "Business is the foundation; Enterprise is the multiplier."

Key talking points:

- Most teams won't need Knowledge Bases until they have significant internal documentation
- Fine-tuned models are a game-changer for teams with large proprietary codebases
- PR summaries (Enterprise) save meaningful time in code review workflows
- Data residency matters for EU/regulated industries

Help the audience self-select: "If you have a team under 500 and no compliance requirements, Business is probably right for you today."
:::

---

## Organization-Level Instruction Files

Business & Enterprise unlock `.github/instructions/`

```
your-org/
└── .github/
  └── instructions/
    ├── coding-standards.instructions.md
    ├── security-policy.instructions.md
    └── api-guidelines.instructions.md
```

**What this gives you**
  - Instructions apply automatically across org repositories
  - Copilot follows them in chat and code suggestions
  - Repo-level instructions can extend the org defaults
  - Updates propagate without developer action

::: notes
Duration ~00:03

This feature is one of the biggest unlocks of the Business tier and often underappreciated.

Key talking points:

- Org-level instructions are like a style guide that Copilot reads before every suggestion
- Examples: "Always use our internal logger, never console.log", "Follow OWASP guidelines", "Use our DTO pattern"
- Repo-level instructions inherit from org-level; they don't replace them
- This is how you scale coding standards without code reviews catching every deviation

Demo opportunity: Show a `.github/instructions/` file with a coding standard rule, then show Copilot following it in the IDE.

Transition: "Let's talk about how to get started..."
:::

---

