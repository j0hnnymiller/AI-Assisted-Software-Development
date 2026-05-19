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
## Exercise: Clone the AI-Assisted-Software-Development Repository

**Setup and Objectives**

Prerequisites

- Git
- GitHub account

Objectives

- Fork the AI-Assisted-Software-Development repository
- Clone your fork to your local machine
- Switch to the brownfield branch to confirm branch navigation

**Activities and Success Criteria**

Activities

1. Search GitHub for AI-Assisted-Software-Development.
2. Fork the repository into your GitHub account.
3. Clone your fork locally with SSH or HTTPS.
4. Open a terminal in the cloned repository.
5. Switch to the brownfield branch.

::: column

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