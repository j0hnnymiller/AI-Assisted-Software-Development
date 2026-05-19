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

  Objectives
    - Explore an unfamiliar codebase
  Activities
    - Fork this repo https://github.com/j0hnnymiller/AIASD-20260209-BF.git
    - Clone the forked repo
    - Create a GitHub PAT https://github.com/settings/tokens
    - Store the PAT in the GITHUB_TOKEN environment variable

  ::: column

  Success Criteria
    - Repo is available locally

  ::: notes
  Duration ~00:20

  Guide participants through creating a fork of the brownfield exercise repository, cloning it locally, and creating a GitHub PAT for authenticated access. Emphasize that this setup work enables the later brownfield labs.
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