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

### What you need to know for your organization

::: notes
Duration ~00:01

Introduce the topic by framing it as a decision teams need to make. Most developers have heard of Copilot, but licensing details are often misunderstood. This session clarifies the tiers and what each unlocks.

Transition: "Let's start with an overview of what's available."
:::

---

<!-- layout: Two Content -->

## Copilot Plan Overview

**Individual**

- `$10/mo`
- Code completions
- Copilot Chat
- No policy management
- No org instruction files

**Business**

- **`$19/user/mo`**
- Code completions and chat
- Policy management
- Org instruction files

::: column

**Enterprise**

- `$39/user/mo`
- Includes Business capabilities
- Adds enterprise-only features

**Quick comparison**

- Individual is for solo usage
- Business is the main team starting point
- Enterprise adds knowledge, analytics, and deeper controls

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

## Business License — $19/user/month

- 🏢 **Centralized management** via GitHub organization settings
- 🔒 **Policy controls** — enable/disable features per org or team
- 📋 **Audit logs** — track Copilot usage across the organization
- 🚫 **Content exclusions** — block Copilot from specific files or repos
- 🌐 **Works with GitHub.com** and GitHub Enterprise Server
- ✅ No seat minimum — pay only for active users

::: notes
Duration ~00:02

This is the most common license tier for companies. Focus on the operational benefits for managers and security teams, not just developers.

Key talking points:

- $19/user/month billed monthly, or discounted annually
- Admins can assign/unassign seats at any time
- Content exclusions are critical for IP-sensitive codebases (e.g., exclude `/src/proprietary/`)
- Audit logs satisfy many compliance requirements without needing Enterprise

Common question: "What counts as an active user?" — A user who has Copilot enabled in their IDE at least once in the billing cycle.

Transition: "Now let's look at what Business adds that Individual doesn't..."
:::

---

## Business vs. Enterprise

### Business ($19/user/mo)

- Organization-wide policy management
- Org-level instruction files (`.github/instructions/`)
- Content exclusions & audit logs
- Standard model access

### Enterprise ($39/user/mo) — adds:

- 🧠 **Copilot Knowledge Bases** — index your internal docs & repos
- 🎯 **Fine-tuned models** on your private codebase
- 📊 **Advanced audit & usage analytics**
- 💬 **Copilot in GitHub.com** (PR summaries, issue chat)
- 🔐 Enhanced compliance & data residency options

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

<!-- layout: Two Content -->

## Organization-Level Instruction Files

### Business & Enterprise unlock `.github/instructions/`

```
your-org/
└── .github/
  └── instructions/
    ├── coding-standards.instructions.md
    ├── security-policy.instructions.md
    └── api-guidelines.instructions.md
```

::: column

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

## Getting Started

1. **Assign seats** in GitHub Org Settings → Copilot → Access
2. **Set policies** — choose which features to enable org-wide
3. **Add content exclusions** for sensitive paths
4. **Create org instruction files** in `.github/instructions/`
5. **Developers install** the Copilot extension in their IDE
6. **Monitor usage** via Audit Log or Copilot usage dashboard

> 💡 **Tip**: Start with a pilot group, gather feedback, then roll out broadly.

::: notes
Duration ~00:02

Give attendees a concrete action plan to leave with.

Key talking points:

- Seat assignment is instant; developers can start using Copilot within minutes
- Recommend starting with 5-10 power users as a pilot cohort
- The usage dashboard (Enterprise) or audit log (Business) helps justify ROI
- Instruction files should be a collaborative effort — involve senior devs and architects

Common concern: "What about IP and training data?" — Reassure that Business/Enterprise plans opt out of using your code to train GitHub's models by default.

Transition: "Any questions on licensing, pricing, or rollout?"
:::

---

## Key Takeaways

- 💰 **Business** = $19/user/month — right for most organizations
- 🏢 **Enterprise** = $39/user/month — adds Knowledge Bases & fine-tuning
- 📋 **Org instruction files** available on Business & above
- 🔒 Both plans offer policy controls and content exclusions
- 🚀 You can start small and scale — no minimum seat count

### ❓ Questions?

::: notes
Summarize the session and open the floor for questions.

Key points to reinforce:

- Business tier is the most common starting point
- Org instruction files are a high-value, low-effort win on day one
- Enterprise is worth evaluating once the team is comfortable with Business features

For questions, be ready to address:

- Billing and seat management specifics
- How instruction files interact with repo-level settings
- Data privacy and training opt-out policies
- GitHub Enterprise Server (on-prem) compatibility

Use the remaining session time for Q&A. Don't rush this slide.
:::
