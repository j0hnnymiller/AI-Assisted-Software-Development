---
name: app-hosting-decision-tree
description: Guide a citizen developer (cdev) with little or no  production experience to choose a hosting platform for a new app. Ask only questions that can change the platform recommendation, verify relevant product facts, and return a concise recommendation with reasons and sources.
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "app-hosting-cost-decision-20261015"
prompt: |
  Cost should be a factor. For example a Azure Data Bricks app is significantly more expensive than an Azure Web Service app.
  How do you propose that we factor cost into the decision tree?
  go ahead
started: "2026-10-15T13:59:14-07:00"
ended: "2026-10-15T14:01:25-07:00"
task_durations:
  - task: "decision flow and cost guidance"
    duration: "00:02:11"
total_duration: "00:02:11"
ai_log: "ai-logs/2026/10/15/app-hosting-cost-decision-20261015/conversation.md"
source: "johnmillerATcodemag-com"
revisions:
  - chat_id: "cost-estimate-defaults-20261015"
    model: "github-copilot-sdk/model-not-exposed@not-exposed"
    date: "2026-10-15"
    change: "Set East US 2 as the default pricing region and require user-context-based hosting size estimates."
    ai_log: "ai-logs/2026/10/15/cost-estimate-defaults-20261015/conversation.md"
---

# Choose a Platform for Your New App

**For citizen developers (cdevs):** Use this skill when you know the business problem your app should solve but are unsure where it should run. You may have little or no experience with app hosting or production operations.

This skill asks only about facts that can change the hosting-platform recommendation. It returns a concise recommendation, the reasons it fits, and relevant official sources. It does not build or deploy the app, create a decision-record file, or provide a production-readiness checklist or post-recommendation follow-up.

## Scope

Consider only these Azure and Azure Databricks hosting options:

- **Azure Databricks App**
- **Azure Databricks Micro App**
- **Azure App Service**
- **Azure Container Apps**
- **Azure Functions**
- **Azure Static Web Apps**
- **Hybrid**: an Azure-hosted app that uses Azure Databricks for data or AI

Do not recommend low-code platforms, generic Databricks Apps, or generic Databricks Micro Apps. If no listed option is a reasonable fit for a cdev to operate, recommend getting help from the cloud platform team rather than escalating to a platform such as AKS.

## Principles

1. **Use plain language.** Ask about the app and its users, not Azure service names. Define technical terms briefly when they are needed.
2. **Ask only decision-relevant questions.** Every question must map to a branch in the decision tree and be capable of changing the platform recommendation. Do not ask about implementation technology, access to subscriptions or workspaces, support ownership, app lifecycle stage, data sensitivity, or operational readiness unless that fact directly changes which platform fits.
3. **Ask one question at a time.** Offer multiple-choice answers, include "I'm not sure", and explain in one sentence why the answer affects the recommendation. Allow te user to go back to a previous question.
4. **Handle uncertainty honestly.** If a relevant answer is unknown, ask a concise clarification only when it could distinguish platform choices. Otherwise make the recommendation conditional and state the uncertainty; do not add a checklist or follow-up task.
5. **Prefer the least to operate.** Recommend the simplest suitable platform. Do not choose containers unless the app's workload requires them.
6. **Verify product facts.** Do not guess current capabilities, availability, prerequisites, or pricing behavior.
7. **Factor cost after functional fit.** First identify hosts that meet the app's requirements; then use comparable cost estimates, the user's budget, and cost priority to choose among them. Do not recommend an unsuitable host just because it is cheaper.

## Running this skill

1. In the first response, explain that the skill will choose a hosting platform only, then ask Q1 and stop. Do not research products, inspect files, or ask multiple questions before the user responds.
2. Use any app description or requirements the user already provided to answer relevant questions. Do not ask for information that cannot change the recommendation.
3. Ask the relevant questions in [Questions for the user](#questions-for-the-user), one per turn. Skip conditional questions that do not apply.
4. Track answers by question ID and preserve unknowns; do not turn unknowns into assumptions without saying so.
5. Apply the functional branches in the [Decision tree](#decision-tree) to identify viable host candidates. If an answer changes which branch fits, clarify it before recommending; do not require a playback-confirmation step.
6. Ask Q9 after identifying candidates unless the user already stated a budget or cost priority. Ask one question at a time; do not ask Q9 again if already answered.
7. Apply the cost screen in D7. Use East US 2 unless the user names another region. Estimate hosting size from the user's stated usage and workload; do not ask the user to choose an instance size. If critical usage data is missing and could change the choice, ask one plain-language question about that usage; otherwise show a conditional range and state the assumption.
8. Verify material platform and pricing claims against current official Microsoft, Azure, or Databricks sources and cite them in the recommendation.
9. Return the recommendation in chat and stop. Do not create files, checklists, next steps, or post-recommendation questions.

## Questions for the user

Ask only questions relevant to the app. "I'm not sure" is always an acceptable answer; use it to make the recommendation conditional if the uncertainty affects the result.

| ID | Ask the user | Answer choices | Why this affects the recommendation | Maps to |
| --- | --- | --- | --- | --- |
| Q1 | What will the app mainly do? | A website people read; a screen or dashboard people use; a service other apps call; work that runs on a schedule or when something happens; work that must keep running; a mix | Different kinds of work fit different hosting platforms. | Workload shape |
| Q2 | Who needs to use the app? | People in my company who sign in; invited partners who sign in; customers who sign in; anyone on the internet without signing in; not sure | Some hosting options do not support customer or anonymous access. | Audience and sign-in |
| Q3 | Where does the app's data live, or where does it need to go? | Azure Databricks; another business system, database, or file location; more than one of these; the app has no data connection; not sure | Hosting near governed data can affect which platform fits. | Data location |
| Q4 | Does the app need to honor different users' existing data permissions in Azure Databricks? | Yes; no; not sure | Using the existing Databricks permissions can favor hosting the app alongside that data. | Data authorization |
| Q5 | If the app uses AI, does it need to use data or models in Azure Databricks? | Yes; no; not sure | An AI dependency on Databricks can favor hosting the app near that data or model. | Data and AI placement |
| Q6 | If the app runs work in the background, how must that work run? | It does not; on a schedule or when an event happens; continuously; not sure | Scheduled work and continuously running services fit different platforms. | Background workload |
| Q7 | About how many people might use the app at its busiest, and how often or how long will they use it? | A few people occasionally; a team during work hours; many people at once or frequent/extended use; not sure | Peak use and active hours help estimate a suitable hosting size and comparable monthly cost. | Usage pattern, hosting size, and cost |
| Q8 | For occasional use, is a slower first response after idle acceptable? | Yes; no, it needs to respond consistently; there is no occasional-use requirement; not sure | Some options pause when idle and may take longer to respond when used again. | Idle behavior |
| Q9 | How should monthly hosting cost affect the choice? | Stay within a hard monthly budget of [amount]; prefer the lowest-cost option that meets the app's needs; balance cost with fit; no budget or preference yet | A budget cap or cost priority can change which of the viable hosts is recommended. | Cost priority and budget |

When the user has already answered a question, record that answer without asking it again. Ask Q2 only for a user-facing app. Ask Q3 when a data connection could make the result Hybrid. Ask Q4 only when the app uses Azure Databricks data, and Q5 only when the app uses AI. Ask Q6 when the app includes background work. Ask Q7 when needed to distinguish idle behavior or estimate cost; ask Q8 only if an Azure Databricks Micro App remains a candidate. Ask Q9 after identifying viable candidates unless cost preference or budget is already known. Do not ask the user to select a technical hosting size. Estimate a plausible starting size, instance count, and scaling assumption from the usage and workload information the user has supplied. If a missing usage detail could materially change the cost comparison, ask one targeted, plain-language question about the app's expected demand; otherwise present a conditional range and state the sizing assumption.

## Platforms in plain language

Verify current details in official documentation before making a recommendation.

| Platform | Plain-language description | Usually fits |
| --- | --- | --- |
| **Azure Databricks App** | Runs an interactive Python or Node.js app in an Azure Databricks workspace, near its data. Users sign in; anonymous access is not supported. | Internal, signed-in users; app data or per-user governed access is in Azure Databricks; no continuous background worker. |
| **Azure Databricks Micro App** | A smaller-footprint Azure Databricks app that can pause when idle. | Internal, signed-in use that is occasional and can tolerate a slower first response. Verify availability and limitations before recommending. |
| **Azure App Service** | A managed platform for websites and web APIs. | Typical interactive apps and APIs, including customer-facing apps with sign-in or protection configured. |
| **Azure Container Apps** | Runs apps packaged as containers and can host services or background workers. | Continuous background work, multiple app components, or a workload that specifically requires containers. |
| **Azure Functions** | Runs code in response to a schedule or event. | Background tasks without a full interactive app. |
| **Azure Static Web Apps** | Hosts website pages and scripts, optionally with a small API. | Informational websites or simple front ends with light data needs. |
| **Hybrid** | Runs the app on an Azure hosting platform while using Azure Databricks for data or AI. | Azure Databricks data or AI is needed, but the audience or workload rules out a Databricks App. |

## Decision tree

Use these steps to select the host. If an app has distinct interactive and background parts, recommend the fitting combination only when that changes the hosting decision.

| Step | Decision | Rule |
| --- | --- | --- |
| D1 | What workload must be hosted? | Scheduled or event-triggered background work without an interactive app points to Azure Functions; continuous background work points to Azure Container Apps. Add Hybrid when the work must use Databricks data or AI. User-facing apps and websites continue to D2. For a mix, evaluate each part. |
| D2 | Does the app depend on Azure Databricks data, per-user data permissions, or AI placement near governed Databricks data? | If yes, continue to D3. Otherwise continue to D4. |
| D3 | Can the audience use a signed-in internal app? | For employees or signed-in partners, continue to D5. For customers or anonymous users, use an Azure host and recommend Hybrid if the app still depends on Databricks data or AI. |
| D4 | What kind of Azure-hosted app is needed? | A standalone informational website points to Azure Static Web Apps. A website or API that needs live Databricks data or AI points to a Hybrid using Azure App Service. A typical interactive app or API without a Databricks dependency points to Azure App Service. An interactive app with scheduled or event-triggered work may use Azure App Service with Azure Functions. Use Azure Container Apps when continuous workers are required. |
| D5 | Is the Databricks-dependent app an interactive app, dashboard, or assistant? | If yes, continue to D6. For a website, API, or mixed workload, use D4 and retain the Databricks dependency in the recommendation. |
| D6 | Is use small and occasional, with a slower first response acceptable? | If yes, Azure Databricks Micro App may fit, subject to verified availability and limitations. Otherwise, Azure Databricks App. |
| D7 | Which viable host best fits the user's cost constraint or priority? | Compare only functionally viable candidates using the same region, usage period, and expected activity assumptions. Default to East US 2 unless the user specifies another region. Estimate each candidate's hosting plan or service tier, instance count, and scaling behavior from the user's stated demand and workload; do not ask the user to pick technical infrastructure sizes. If there is a hard budget, prefer a viable estimate within it; if none fits, say so rather than recommend an unsuitable host. If lowest cost is preferred, choose the lowest defensible estimate. If cost is balanced with fit, explain the cost tradeoff and retain the better functional fit. With one viable candidate, check it against any budget and state the estimate. |

```mermaid
flowchart TD
  Q1["Q1: What will the app do?"] --> D1{"D1: Choose workload host; add Hybrid if needed"}
  Q6["Q6: How must background work run?"] --> D1
  Q3["Q3: Where is the data?"] --> D1
  Q5["Q5: Does AI need Databricks data or models?"] --> D1
  D1 -->|"Scheduled or event-triggered only"| D7
  D1 -->|"Continuous background work"| D7
  D1 -->|"User-facing app or website"| D2{"D2: Does Databricks data or AI affect the host choice?"}

  Q4["Q4: Must Databricks permissions be honored?"] --> D2
  Q3 --> D2
  Q5 --> D2
  D2 -->|"No"| D4{"D4: What kind of user-facing app?"}
  D2 -->|"Yes"| D3{"D3: Can users sign in as internal users or partners?"}

  Q2["Q2: Who will use the app?"] --> D3
  D3 -->|"No: customers or anonymous users"| D4
  D3 -->|"Yes: employees or invited partners"| D5{"D5: Is it an interactive app, dashboard, or assistant?"}

  D5 -->|"Yes"| D6{"D6: Is use occasional and a slow first response acceptable?"}
  D5 -->|"No: website, API, or mixed workload"| D4
  Q6 --> D4
  Q7["Q7: Peak users and usage pattern?"] --> D6
  Q7 --> D7
  Q8["Q8: Is a slower first response acceptable?"] --> D6
  D6 -->|"Yes, subject to verified availability"| D7
  D6 -->|"No or not occasional"| D7

  D4 -->|"Informational website, no Databricks dependency"| D7
  D4 -->|"Website or API with Databricks dependency"| D7
  D4 -->|"Interactive app or API, no Databricks dependency"| D7
  D4 -->|"App plus scheduled or event-triggered work"| D7
  D4 -->|"Continuous worker required"| D7
  Q9["Q9: What budget or cost priority applies?"] --> D7{"D7: Compare cost among functionally viable hosts"}

  D7 -->|"Scheduled or event-triggered work"| R1["R1: Azure Functions; Hybrid if Databricks is needed"]
  D7 -->|"Continuous background work"| R2["R2: Azure Container Apps; Hybrid if Databricks is needed"]
  D7 -->|"Occasional Databricks interactive app; cost and fit checked"| R3["R3: Azure Databricks Micro App"]
  D7 -->|"Databricks interactive app; cost and fit checked"| R4["R4: Azure Databricks App"]
  D7 -->|"Informational website"| R5["R5: Azure Static Web Apps"]
  D7 -->|"Website or API with Databricks dependency"| R6["R6: Hybrid using Azure App Service"]
  D7 -->|"Interactive app or API, no Databricks dependency"| R7["R7: Azure App Service"]
  D7 -->|"App plus scheduled or event-triggered work"| R8["R8: Azure App Service plus Azure Functions; Hybrid if needed"]
  D7 -->|"No viable host fits the hard budget"| R9["R9: No suitable listed option within budget; do not force a recommendation"]
```

All diagram nodes are labeled by type: intake questions (`Q*`), decision steps (`D*`), or terminal recommendations (`R*`).

## Research rules

- Use current official Microsoft, Azure, and Databricks documentation. Cite sources for material claims about supported workloads, sign-in, prerequisites, availability, idle behavior, and pricing.
- Distinguish verified product capabilities from organization-specific availability. If a prerequisite cannot be confirmed, make the recommendation conditional rather than asking unrelated readiness questions.
- Compare only functionally viable candidates. Use official pricing pages or calculators for estimated monthly costs; do not rely on remembered prices or unsupported claims that one platform is always cheaper.
- Use **East US 2** as the default region unless the user specifies another region. Verify that each candidate is available in that region; if not, identify the nearest reasonable region and disclose the difference rather than silently changing regions.
- Estimate hosting size from the information the user provided about peak simultaneous users, usage frequency and duration, workload shape, performance or availability needs, and data/compute intensity. Translate this into a plausible starting service tier, instance count, and scaling assumption using current official guidance and the pricing calculator. Do not ask the citizen developer to choose a SKU, plan, VM size, or instance count.
- Use the same region, time period, usage/activity assumptions, and included cost scope for every candidate. Use a consistent monthly period (normally 730 hours) and comparable availability/scaling assumptions. Include required hosting and billed compute; identify shared or existing resources separately and state material exclusions.
- If the user's demand description does not support a confident size, do not invent precision. Give a clearly labeled low-to-likely estimate range with explicit assumptions. Ask one plain-language usage question only when the missing input could materially change which viable option is least expensive or whether a hard budget is met; otherwise preserve the uncertainty in the recommendation.
- State the estimate date, region, derived sizing assumptions, included/excluded charges, and source. Do not imply a quote or false precision. If a defensible comparison is not possible, say which cost is unverified and make the recommendation conditional if that could change the choice.
- Cost estimates support platform selection only; do not expand into implementation, deployment, operations, security-review, or production-readiness guidance.
- Do not provide implementation, deployment, operations, security-review, or production-readiness guidance.

## Recommendation response

Return a concise response in chat containing:

1. The recommended platform (or the smallest fitting combination for a mixed workload) and confidence: confirmed or conditional.
2. Two or three reasons directly tied to the user's answers.
3. A concise estimated monthly cost or range for the recommendation and the most relevant viable alternative when cost could affect the choice; name the region (East US 2 by default), the user-context-derived hosting size/scale assumptions, and any unverified costs. If the user gave a hard budget, say whether the estimate appears within it.
4. The most relevant alternative and why it fits less well, if comparison helps explain the choice.
5. Official sources supporting material product and pricing claims.

Do not create a decision-record file, checklist, action plan, support handoff, glossary, or follow-up question after the recommendation. Define any necessary technical term inline and keep the response focused on platform choice.
