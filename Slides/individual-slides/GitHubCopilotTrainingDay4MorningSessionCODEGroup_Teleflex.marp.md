---
marp: true
theme: default
paginate: true
---

# GitHub Copilot Training Day 4 Morning Session

---

# Greenfield Development Overview

- Introduction to Greenfield development
- Update on previous exercise: running prompts and GitHub workflows

::: notes
Key points:

- Greenfield development as a focus for the session.
- Recap of previous exercise involving prompts and GitHub workflows.
:::

---

# PR Hook Prompt Execution

- Running prompts in PR hooks
- Automated evaluation of code changes
- Style check failures and categorization

::: notes
Key points:

- Demonstrated running prompts in PR hooks for automated code review.
- Style check failures are detected and categorized.
- The workflow updates PR comments with findings.
:::

---

# Debugging Workflow Issues

- Local evaluation of files against instruction files
- Identifying issues in pipeline/workflow vs. files
- Importance of prompt structure

::: notes
Key points:

- Local evaluation helps isolate issues between files and workflow.
- Prompt structure is critical for successful automation.
:::

---

# Prompt Example & Workflow Modification

- Example prompt: "This commit introduced an intentional style violation."
- Workflow modification to use OpenAI or Copilot CLI
- Handling API keys and secrets

::: notes
Key points:

- Example prompt used to trigger style violation detection.
- Workflow can be modified to use different AI providers (OpenAI, Copilot CLI, Azure OpenAI).
- Managing API keys and secrets is necessary for workflow execution.
  Prompt: This commit introduced an intentional style violation.
:::

---

# Troubleshooting and Iteration

- Errors with CLI extensions and API keys
- Switching between OpenAI and Copilot CLI
- Importance of reviewing output and making decisions

::: notes
Key points:

- Troubleshooting involved switching between AI providers and resolving CLI extension issues.
- Reviewing output is essential to ensure correct workflow behavior.
:::

---

# Azure DevOps Integration Discussion

- Equivalent use of OpenAI keys in Azure DevOps
- Azure OpenAI as an alternative
- Token management and project setup

::: notes
Key points:

- Azure DevOps can integrate with OpenAI or Azure OpenAI for similar workflows.
- Token management and project setup are required for integration.
:::

---

# Effort and Debugging Reflection

- Time spent debugging: 30-60 minutes
- Importance of following advice and having API keys ready
- Emphasis on reviewing workflow output

::: notes
Key points:

- Debugging and setup took between half an hour and an hour.
- Having API keys ready and following advice speeds up the process.
- Always review workflow output for correctness.
:::

---

# Exercise: Implement PR Hook Prompt Evaluation

**Duration:** 15 minutes

**Objectives:**

- Practice setting up PR hook prompt evaluation
- Learn to automate code review with AI
- Understand workflow modification and troubleshooting

**Activities:**

1. Set up a PR hook to run a prompt for code review.
2. Modify the workflow to use OpenAI or Copilot CLI.
3. Manage API keys and secrets for workflow execution.
4. Debug and resolve any issues encountered.

**Success Criteria:**

- PR hook successfully runs prompt and updates PR comments
- Workflow detects and categorizes style violations
- API keys and secrets are managed securely
- Troubleshooting steps are documented

::: notes
Prompt: Set up a PR hook to run a prompt for code review.
Prompt: Modify the workflow to use OpenAI or Copilot CLI.
Prompt: Manage API keys and secrets for workflow execution.
Prompt: Debug and resolve any issues encountered.
:::

---

# Exercise: Integrate AI Review in Azure DevOps

**Duration:** 15 minutes

**Objectives:**

- Practice integrating OpenAI/Azure OpenAI in Azure DevOps
- Learn token management and project setup
- Automate PR comment updates with AI findings

**Activities:**

1. Set up Azure DevOps project for AI-powered code review.
2. Integrate OpenAI or Azure OpenAI using tokens.
3. Configure workflow to update PR comments with AI findings.
4. Test and validate the integration.

**Success Criteria:**

- Azure DevOps project is set up for AI review
- Tokens are managed securely
- Workflow updates PR comments with AI findings
- Integration is tested and validated

::: notes
Prompt: Set up Azure DevOps project for AI-powered code review.
Prompt: Integrate OpenAI or Azure OpenAI using tokens.
Prompt: Configure workflow to update PR comments with AI findings.
Prompt: Test and validate the integration.
:::

---

# Q&A and Wrap-up

- Open discussion on Greenfield development and workflow automation
- Review of key takeaways
- Next steps for participants

::: notes
Key points:

- Encourage questions and discussion on session topics.
- Summarize key takeaways and next steps.
:::
