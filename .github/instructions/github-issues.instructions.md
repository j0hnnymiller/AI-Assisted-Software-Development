---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "github-issues-instructions-20261112-1120"
prompt: |
  create an instruction file for creating github issues
started: "2026-11-12T11:19:51.616-08:00"
ended: "2026-11-12T11:25:41.088-08:00"
task_durations:
  - task: "Issue guidance research and authoring"
    duration: "00:05:49"
total_duration: "00:05:49"
ai_log: "ai-logs/2026/11/12/github-issues-instructions-20261112-1120/conversation.md"
source: "user request"
description: "Use when drafting or creating GitHub issues, defining titles, descriptions, acceptance criteria, checking duplicates, or deciding whether to publish; covers evidence, scope, privacy, and authorization."
---

# GitHub Issue Authoring

## Overview

Use this guide to draft clear, actionable GitHub issues and to decide what evidence,
repository context, and authorization are needed before publishing them. Apply it
to bugs, feature requests, maintenance, documentation, and other work items.

This guide covers issue content and safe creation. For issue discovery and
publication commands, follow [GitHub CLI Instructions](github-cli.instructions.md).
For bug or dead-code analysis, use the focused
[create-bug-issues skill](../skills/create-bug-issues/SKILL.md) or
[create-dead-code-issues skill](../skills/create-dead-code-issues/SKILL.md).
These skills may produce drafts; their use does not authorize publishing.

## Table of Contents

- [Workflow](#workflow)
- [Issue Content](#issue-content)
- [Issue Body Template](#issue-body-template)
- [Evidence and Safety](#evidence-and-safety)
- [Publishing Issues](#publishing-issues)
- [Validation Checklist](#validation-checklist)

## Workflow

1. **Confirm the destination and requested action.**
   - Resolve the repository when it is not clear from the request or active
     workspace. Ask when multiple repositories are plausible.
   - Distinguish between researching, drafting, and publishing. Drafting does not
     authorize creating or editing an issue on GitHub.
   - Determine the issue type and intended audience. Ask about missing decisions
     that materially affect the proposed work.

2. **Check existing context.**
   - Review relevant repository code, documentation, requirements, and existing
     issues before drafting.
   - Search open and closed issues for duplicates or issues that already cover
     the same outcome. If a likely duplicate exists, cite it and recommend
     commenting on or updating it instead of creating another.
   - Check the repository's issue templates and existing conventions when
     available. Follow a relevant template; do not invent required labels,
     milestones, assignees, or title prefixes.

3. **Define one actionable outcome.**
   - Describe the problem or requested change, who or what it affects, and why
     the work matters.
   - Keep an issue small enough to discuss, estimate, implement, and verify.
     Split work only when outcomes can be acted on and accepted independently.
   - State verified dependencies and sequencing constraints. Do not promise
     parallel implementation unless the relevant boundaries and dependencies
     have been checked.

4. **Draft and verify.**
   - Use a concise, specific title that names the problem or outcome.
   - Include only sections that are relevant to the issue type; remove unused
     template headings.
   - Verify links, file paths, line references, reproduction steps, and claims
     against available evidence. Mark uncertainty rather than presenting it as
     fact.

## Issue Content

### Titles

- Make the title understandable without requiring the reader to open the body.
- Describe the affected behavior or desired outcome, not only a proposed
  implementation.
- Do not add a severity, priority, component prefix, or issue number unless the
  repository's documented convention requires it.

### Type-specific details

| Issue type | Include |
| --- | --- |
| Bug | Observed behavior, expected behavior, concise reproduction steps, affected environment or version when relevant, impact, and supporting evidence. |
| Feature | User or system need, desired outcome, constraints, and testable acceptance criteria. Separate optional implementation ideas from requirements. |
| Maintenance or refactoring | Specific target, reason, behavior that must remain unchanged, and verification needed to establish completion. |
| Documentation | Intended readers, information that is missing or incorrect, and the expected documentation outcome. |

Use priority, severity, estimates, or ownership only when supplied by the user
or grounded in a documented repository process. Otherwise omit them or identify
them as undecided.

## Issue Body Template

Adapt this template to the issue type and the repository's issue form. Remove
sections that do not apply.

```markdown
## Summary
<Problem or desired outcome>

## Context
<Who or what is affected, and why this matters>

## Expected outcome
<Observable result when the work is complete>

## Acceptance criteria
- [ ] <Specific, verifiable condition>
- [ ] <Relevant tests, documentation, or compatibility condition>

## Evidence
<Reproduction steps, verified file and line references, logs, screenshots, or links>

## Dependencies and scope
<Known prerequisites, related issues, constraints, and exclusions>
```

For bugs, state actual and expected behavior and provide reproducible steps when
possible. For feature requests, focus on the need and outcome. For maintenance
and documentation, define the deliverable and how it will be verified.

## Evidence and Safety

- Support findings with the smallest useful evidence. For code findings, verify
  the referenced path and line range; do not infer runtime behavior from a
  pattern alone.
- Include versions, logs, screenshots, or examples only when they help someone
  reproduce or evaluate the issue. Sanitize them first.
- Never include credentials, tokens, private personal data, or unrelated
  confidential information. Use synthetic examples when possible.
- Do not publish details of an exploitable security vulnerability in a public
  issue. Use the repository's private vulnerability-reporting process or ask
  the user which approved channel to use.
- Link related issues with a short explanation of whether they are duplicates,
  prerequisites, or merely related. Do not create speculative issue
  dependencies.

## Publishing Issues

- Create, edit, assign, label, close, or otherwise publish an issue only when
  the user explicitly requests that external action. A request to find issues,
  prepare drafts, or write this guide is not authorization to publish.
- Before creation, confirm the repository and review the final title, body, and
  any requested metadata. If the repository or intended change is ambiguous,
  ask before publishing.
- Use the applicable repository issue form and documented labels. Verify that
  labels, milestones, and assignees exist; do not silently create or guess
  metadata.
- Follow [GitHub CLI Instructions](github-cli.instructions.md) for CLI usage and
  authentication. Never expose credentials in commands, issue content, or
  logs.
- After successful creation, report the issue link and any metadata applied.
  If creation fails, report the error; do not imply that an issue was created.

## Validation Checklist

- [ ] The destination repository and requested action are clear.
- [ ] Relevant existing issues and repository templates were checked.
- [ ] The title is specific, concise, and free of unsupported classification.
- [ ] The body states a concrete problem or outcome and useful acceptance criteria.
- [ ] Claims, references, and reproduction details are verified or marked uncertain.
- [ ] Scope, dependencies, and exclusions are realistic and evidence-based.
- [ ] Sensitive information and public vulnerability details are excluded.
- [ ] No issue was published without explicit user authorization.
- [ ] The result clearly distinguishes a draft from a published issue.

## Summary

Make each issue distinct, evidence-based, scoped, and verifiable. Check for
duplicates and repository conventions, protect sensitive information, and treat
publishing as a separate action that requires explicit authorization.
