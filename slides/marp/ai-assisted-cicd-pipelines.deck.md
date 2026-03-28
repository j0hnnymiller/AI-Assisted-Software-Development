---
marp: true
theme: default
paginate: true
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "ai-cicd-pipelines-20260314"
prompt: |
  create a marp deck describing AI assistance in creating and maintaining GitHub CI/CD pipelines.
  GitHub Actions YAML generation, build automation, coverage thresholds
started: "2026-03-14T19:57:13Z"
ended: "2026-03-14T20:05:00Z"
task_durations:
  - task: "slide content creation"
    duration: "00:08:00"
total_duration: "00:08:00"
ai_log: "ai-logs/2026/03/14/ai-cicd-pipelines-20260314/conversation.md"
source: "johnmillerATcodemag-com"
---
# AI-Assisted CI/CD Pipelines || YAML: Now With 50% Less Soul-Crushing Manual Edits

## AI-Assisted CI/CD Pipelines

GitHub Actions YAML generation
Build automation with AI
Coverage thresholds
Pipeline maintenance and evolution
Exercise: Generate a pipeline from scratch

::: notes
Introduce this module as a practical guide to using AI — specifically GitHub Copilot — to design, generate, and maintain CI/CD pipelines on GitHub Actions. Emphasize that the goal is not to automate humans out of the loop but to reduce the friction between "intent" and "working YAML". Many teams struggle to get a pipeline right on the first try; AI dramatically shortens that feedback cycle.
:::

---




## Why Pipelines Are Hard

YAML syntax is unforgiving
Action versions change constantly
Environment variables, secrets, and caching rules interact unexpectedly
Coverage gates, linting, and deployment steps differ per project
Copy-paste drift between projects accumulates silently

::: notes
Open with empathy. Most developers have lost an afternoon to a mis-indented YAML block or an unexpected breaking change in a third-party action. These are not skill failures — they are complexity failures. AI closes the gap between "I know what I want" and "here is the correct YAML to achieve it."
:::

---




## What AI Brings to CI/CD

```text
You → intent           AI → working YAML
   "run tests on PR"        on: [pull_request]
                            jobs: test: ...
```

Generate pipelines from plain English
Explain unfamiliar pipeline syntax
Diagnose failing workflow runs from logs
Suggest caching, matrix, and concurrency improvements
Keep actions pinned and up to date

::: notes
Walk through the mental model: the developer provides intent, the AI provides syntactically correct, contextually appropriate YAML. This is not magic — the AI has seen thousands of pipelines. Stress that the developer still reviews and owns every line. AI accelerates the first draft and the debugging loop, not the decision-making.
:::

---




## GitHub Actions YAML Generation

Ask Copilot in chat or inline:

```text
Prompt: "Create a GitHub Actions workflow that runs
dotnet test on every pull request targeting main,
uploads a code coverage report, and fails if
coverage drops below 80%."
```

Copilot generates:

- Trigger block (`on:`)
- Job matrix
- Step sequence
- Coverage upload + threshold enforcement

::: notes
Live demo opportunity: open a blank `.github/workflows/ci.yml` and type the prompt as a comment. Show how Copilot completes the file. Point out that the model understands dotnet CLI, the Coverlet report format, and the `codecov/codecov-action` convention. Then ask it to explain each step — students can use this to build mental models, not just cargo-cult YAML.
:::

---




## Anatomy of an AI-Generated Workflow

```yaml
name: CI

on:
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: "8.x"
      - run: dotnet restore
      - run: dotnet build --no-restore
      - run: dotnet test --no-build
          --collect:"XPlat Code Coverage"
```

::: notes
Walk through each section: triggers, runner, checkout, SDK setup, restore, build, test. Point out `actions/checkout@v4` — a pinned major version. Ask students: what happens if you omit the `--no-restore` flag on build? What if `ubuntu-latest` changes? These are exactly the questions AI can help answer in context. Normalize asking the AI "why is this step here?" as a learning technique.
:::

---




## Coverage Thresholds

Coverage gates enforce quality — AI helps configure them correctly

```yaml
- name: Test with coverage
  run: |
    dotnet test --collect:"XPlat Code Coverage" \
      -- DataCollectionRunSettings.DataCollectors \
         .DataCollector.Configuration.Threshold=80

- name: Upload coverage
  uses: codecov/codecov-action@v4
  with:
    fail_ci_if_error: true
    threshold: 80
```

Ask Copilot: _"How do I fail the build if branch coverage drops below 80%?"_

::: notes
Coverage thresholds are one of the most common sources of confusion: where does the threshold live? In the test runner config? In the upload action? In a separate tool? AI answers this correctly for the specific framework in use. Demo: ask Copilot the same question for Jest, pytest, and dotnet — show that the answer differs and the AI knows the difference. Emphasize that a threshold without enforcement is just aspirational documentation.
:::

---




## Build Automation Patterns

AI can generate: matrix builds, dependency caching, artifact upload

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    dotnet: ["7.x", "8.x"]

steps:
  - uses: actions/cache@v4
    with:
      path: ~/.nuget/packages
      key: ${{ runner.os }}-nuget-
        ${{ hashFiles('**/*.csproj') }}

  - uses: actions/upload-artifact@v4
    with:
      name: test-results
      path: TestResults/
```

::: notes
Matrix builds and caching are two patterns that dramatically improve pipeline performance but are tedious to hand-write. Show how asking Copilot "add a matrix build for Windows and Ubuntu across .NET 7 and 8" produces the correct strategy block. Ask it to explain the cache key hash — students often do not realize that changing a .csproj file correctly invalidates the cache. Artifact upload is another common gap; AI fills it without needing to hunt through documentation.
:::

---




## Maintaining Pipelines with AI

Pipelines rot — actions deprecate, runners change, dependencies drift

Ask Copilot to:

- Explain a failing run from pasted log output
- Upgrade pinned action versions safely
- Refactor a 300-line workflow into reusable workflows
- Add a deployment stage to an existing CI workflow

_"This workflow is failing with exit code 128 — here is the log. What is wrong?"_

::: notes
Maintenance is where AI pays long-term dividends. Demo: paste a failing workflow log into Copilot Chat and ask what is wrong. The model can identify common error patterns — missing permissions, wrong branch reference, deprecated node version warnings. Also show the refactoring use case: large workflows become hard to read; AI can extract shared steps into reusable workflows with `workflow_call` triggers without breaking existing runs.
:::

---




## Reusable Workflows

AI generates caller and callee in one prompt

```yaml
# AI-Assisted CI/CD Pipelines || YAML: Now With 50% Less Soul-Crushing Manual Edits
on:
  workflow_call:
    inputs:
      dotnet-version:
        required: true
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: ${{ inputs.dotnet-version }}
      - run: dotnet test
```

::: notes
Reusable workflows (`workflow_call`) are a powerful but often underused GitHub Actions feature. Teams that copy-paste CI logic across repos accumulate drift. AI can audit an existing set of workflows, identify duplicated patterns, and generate a reusable workflow plus updated callers in a single conversation. Show the prompt: "Here are our five workflow files. Extract the test steps into a reusable workflow and update each caller." This is a real time-saver in large organizations.
:::

---




## Secrets, Permissions, and Security

AI assists but YOU own security decisions

```yaml
permissions:
  contents: read
  checks: write # required for test reporters
  pull-requests: write # required for PR comments

env:
  SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

Ask AI: _"What is the minimum permissions block for uploading coverage?"_
Review AI output — it cannot know your org's secret names
Never commit secrets; use `${{ secrets.NAME }}`

::: notes
Stress that AI can suggest correct permission scopes but cannot see your repository's secret store or org policies. The developer must verify secret names and confirm that the minimum-privilege principle is applied. This is a great moment to discuss GITHUB_TOKEN permissions — defaulting to read-all is a common mistake that AI will flag if prompted. The key habit: ask AI "what permissions does this step need?" rather than granting write-all and moving on.
:::

---




## From Zero to Pipeline: Live Workflow

```text
1. Describe your stack to Copilot
   "Node 20, Vitest, Playwright e2e, deploys to Azure"

2. Ask for a complete CI workflow
   → Copilot generates trigger, jobs, steps

3. Ask for coverage enforcement
   → Copilot adds threshold + upload steps

4. Ask "what caching should I add?"
   → Copilot adds node_modules cache with correct key

5. Paste a failure log and ask "why?"
   → Copilot diagnoses in seconds
```

::: notes
Walk through this five-step workflow live or in a recorded demo. The goal is to show the conversation as a dialogue, not a one-shot prompt. Each ask builds on the previous output. Encourage students to try this with their own stack immediately after the session. The pipeline does not need to be perfect on step 2 — that is the point. Iteration with AI is fast.
:::

---

## Hands-On Exercise

**Goal**: Generate a complete CI pipeline for a provided sample repo

1. Open GitHub Copilot Chat in VS Code
2. Ask: _"Create a GitHub Actions CI workflow for this project"_
3. Review and commit the generated YAML
4. Add a coverage threshold at 70%
5. Ask Copilot to explain one step you do not understand
6. **Bonus**: Add a matrix build for two Node versions

_Sample repo link provided by instructor_

::: notes
Duration ~00:20

 Circulate and watch for students who try to use Copilot as a black box without reading the output. Prompt them: "Can you explain line 12 to me?" That question forces engagement. Common issues: students forget to create the `.github/workflows/` directory, or they use the wrong indentation. AI usually catches these if students paste the file back and ask "is this correct YAML?" Debrief: what surprised you? What did the AI get wrong?
:::

---




## Key Takeaways

AI dramatically shortens the pipeline feedback loop
Generated YAML is a starting point — review every line
Coverage thresholds belong in both the test runner _and_ the upload action
Reusable workflows reduce drift across repositories
Maintenance conversations are as valuable as generation
You own the pipeline; AI is your co-pilot

::: notes
Close by reinforcing ownership. Students may be tempted to treat AI-generated pipelines as authoritative. Remind them that the AI has no knowledge of their org's compliance requirements, runner quotas, or secret naming conventions. The value is in speed and correctness of syntax — the developer still provides judgment. Leave time for questions; common ones are about self-hosted runners, environments and approval gates, and how to handle monorepos.
:::
