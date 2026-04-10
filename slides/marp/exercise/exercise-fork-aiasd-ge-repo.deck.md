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
## Exercise: Fork the 20260330-aiasd-ge Repo

**Objectives**

- Explore an unfamiliar codebase with a safe personal fork
- Clone and validate local access to the brownfield exercise repository
- Configure PAT-based authentication for GitHub operations

::: column

**Activities and Success Criteria**

Activities

1. Open https://github.com/j0hnnymiller/20260330-aiasd-ge.git.
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