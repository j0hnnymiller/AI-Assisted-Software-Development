---
ai_generated: true
model: "openai/gpt-5.3-codex@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-repository-fork-clone-deck-20260322"
prompt: |
  create an exercise marp slide deck using the slides\exercise-template.pptx template for the following:


  ## Exercise: Clone the AI-Assisted-Software-Development Repository

  Prerequisites: Git, GitHub account
  Objectives
  Fork the AI-Assisted-Software-Development repo
  Activities
  Clone the git@github.com:johnmillerATcodemag-com/AI-Assisted-Software-Development.gitrepository
  Switch to the brownfield branch
  Success Criteria
  Cloned repository exists locally

  ::: notes
  Duration ~00:10

  Objective: Fork the course repos Tasks
  Search GitHub for
  AI-Assisted-Software-Development
  Fork this repo
  This will create a personal copy under your GitHub account
  You can make changes without affecting the original repo
  :::

  ---

  ## Exercise: Fork the AIASD-20260209-BF Repo

  Objectives: Explore an unfamiliar codebase
  Activities
  Fork this repo https://github.com/j0hnnymiller/AIASD-20260209-BF.git
  Clone the forked repo
  Create a GitHub PAT https://github.com/settings/tokens
  Store the PAT in the GITHUB_TOKEN environment variable
  Success Criteria
  Repo is available locally

  ::: notes
  Duration ~00:20

  Guide participants through creating a fork of the brownfield exercise repository, cloning it locally, and creating a GitHub PAT for authenticated access. Emphasize that this setup work enables the later brownfield labs.
  :::

  ---

  ## Exercise: Fork the repos

  Objective: Fork the course repos
  Search GitHub for

  - AI-Assisted-Software-Development
  - zeus.academia.3b
    Fork the repos
  - This will create a personal copy under your GitHub account
  - You can make changes without affecting the original repo
started: "2026-03-22T00:00:00Z"
ended: "2026-03-22T00:10:00Z"
task_durations:
  - task: "exercise deck authoring"
    duration: "00:06:00"
  - task: "provenance logging"
    duration: "00:02:00"
  - task: "readme update"
    duration: "00:02:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2026/03/22/exercise-repository-fork-clone-deck-20260322/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Fork and Clone Repositories || Exercise: Your First git clone of Many

## Exercise: Clone the AI-Assisted-Software-Development Repository

**Setup and Objectives**

Prerequisites

- Git
- GitHub account

Objectives

- Fork the AI-Assisted-Software-Development repository
- Clone your fork to your local machine
- Switch to the brownfield branch to confirm branch navigation

::: column

**Activities and Success Criteria**

Activities

1. Search GitHub for AI-Assisted-Software-Development.
2. Fork the repository into your GitHub account.
3. Clone your fork locally with SSH or HTTPS.
4. Open a terminal in the cloned repository.
5. Switch to the brownfield branch.

```bash
git clone git@github.com:<your-username>/AI-Assisted-Software-Development.git
cd AI-Assisted-Software-Development
git checkout brownfield
```

Success Criteria

- Repository is forked under your GitHub account
- Cloned repository exists locally
- Brownfield branch is checked out successfully

::: notes
Duration ~00:10

Set the context by explaining that this is foundational setup for all later course tasks. Guide participants to fork first, then clone their own fork, so they have push access and can safely make changes without affecting the original repository. If students hit authentication issues, pause briefly to confirm whether they are using SSH keys or HTTPS credentials and help them choose one method consistently. Close by asking everyone to run `git branch --show-current` so they can verify they are on the brownfield branch before moving forward.
:::

---

## Exercise: Fork the AIASD-20260209-BF Repo

**Objectives**

- Explore an unfamiliar codebase with a safe personal fork
- Clone and validate local access to the brownfield exercise repository
- Configure PAT-based authentication for GitHub operations

::: column

**Activities and Success Criteria**

Activities

1. Open https://github.com/j0hnnymiller/AIASD-20260209-BF.git.
2. Fork the repository to your personal GitHub account.
3. Clone the forked repository locally.
4. Create a GitHub PAT at https://github.com/settings/tokens.
5. Store the token in the `GITHUB_TOKEN` environment variable.

```bash
$env:GITHUB_TOKEN = "<your-pat>"

export GITHUB_TOKEN="<your-pat>"
```

Success Criteria

- Forked repository exists in your GitHub account
- Repository is available locally and can be opened in VS Code
- `GITHUB_TOKEN` is set in the current shell session

::: notes
Duration ~00:20

Frame this as brownfield readiness work and explain that a clean setup now prevents workflow friction later. Walk students through forking and cloning first, then move to PAT creation with a reminder to use least-privilege token scopes and never commit tokens to source control. During the hands-on period, check that everyone can authenticate successfully before they continue into subsequent labs. Transition by emphasizing that local clone plus PAT setup is the baseline for future repository analysis and change workflows.
:::

---

## Exercise: Fork the Repos

**Objective**

- Fork the course repositories needed for independent practice

::: column

**Activities and Success Criteria**

Activities

1. Search GitHub for the following repositories:
   - AI-Assisted-Software-Development
   - zeus.academia.3b
2. Fork both repositories into your GitHub account.
3. Confirm each fork appears under your account.
4. Optional: clone each fork locally for offline work.

Success Criteria

- Both repositories are forked to your GitHub account
- You can identify the original upstream repositories
- You can explain why forking protects the source repositories

::: notes
Duration ~00:10

Use this slide as a consolidation exercise to reinforce the fork-first workflow pattern across multiple repositories. Encourage participants to describe the difference between upstream and origin in their own words, because that understanding reduces merge and push mistakes later in the course. If time permits, have learners quickly clone one of the forks and verify remotes using `git remote -v` as a confidence check. End with a short recap that forking gives each participant a safe workspace while preserving the integrity of the course-owned repositories.
:::
