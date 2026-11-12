---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "ae2e29d6-183f-4dde-8453-6726cf6c42cd"
prompt: |
  save this as a new instruction file
started: "2026-11-12T07:21:02.7169371-08:00"
ended: "2026-11-12T07:25:08.0048048-08:00"
task_durations:
  - task: "Instruction drafting and repository indexing"
    duration: "00:03:10"
  - task: "Provenance logs and validation"
    duration: "00:00:55"
total_duration: "00:04:05"
ai_log: "ai-logs/2026/11/12/ae2e29d6-183f-4dde-8453-6726cf6c42cd/conversation.md"
source: "user request"
name: human-facing-writing
description: "Guidance for clear, useful human-facing communications and documentation."
applyTo: "**/*"
version: "1.0.0"
author: "johnmillerATcodemag-com"
tags: ["writing", "documentation", "communications", "readability"]
owner: "Development Team"
reviewedDate: "2026-11-12"
nextReview: "2027-02-12"
---

# Human-Facing Writing Instructions

## Overview

Apply this guidance when drafting or editing communications and documentation for people. Apply it to code comments and API documentation only where relevant. Do not apply it to source logic or machine-readable content.

## Table of Contents

- [Writing Rules](#writing-rules)
- [Code Documentation](#code-documentation)
- [Editing Existing Content](#editing-existing-content)
- [Validation Checklist](#validation-checklist)
- [Summary](#summary)

## Writing Rules

- Identify the intended audience and purpose.
- Organize content around what readers need to know or do.
- Lead with the main point, status, recommendation, or request.
- Put supporting context after the main point.
- Prefer familiar words and direct sentences.
- Write one thought per sentence.
- Use active voice when it makes the meaning clearer.
- Strive for clarity in the spirit of ASD-STE100.
- Avoid metaphors and aphorisms.
- Avoid jargon. Define technical terms when readers need them.
- Keep paragraphs focused on one topic.
- Use headings and lists to help readers find information.
- Use tables for structured comparisons or reference data. Do not put ordinary narrative in tables.
- Be concise without omitting relevant evidence, caveats, assumptions, owners, dates, or next steps.
- Distinguish verified facts from assumptions, recommendations, and uncertainty.
- State actions, owners, and deadlines clearly when they are known.
- Present procedure steps in order. State relevant prerequisites and expected results.
- Use descriptive link text that tells readers what they will find.

## Code Documentation

- Add code comments, docstrings, or API documentation only to explain behavior, intent, constraints, or rationale that readers cannot derive from the code itself.
- Do not restate names, signatures, or straightforward implementation steps.

## Editing Existing Content

- Remove historical derivation and obsolete facts during edits.
- Retain historical material only when the document's purpose or an audit, compliance, or provenance requirement needs it.
- Remove filler, repetition, and claims that the available evidence does not support.
- Review the result from the intended reader's perspective. Make the purpose, key information, and requested action easy to identify.

## Validation Checklist

- [ ] The intended audience and purpose are clear.
- [ ] Each sentence expresses one thought.
- [ ] Necessary technical terms are explained.
- [ ] Facts, assumptions, and recommendations are distinguishable.
- [ ] Actions, owners, dates, and next steps are clear when relevant.
- [ ] Code documentation explains only information that cannot be derived from code.
- [ ] Unneeded historical derivation and obsolete facts have been removed.
- [ ] Required audit, compliance, and provenance records remain intact.

## Summary

Write for the reader's purpose. Prefer clear, direct prose. Keep only the context readers need and the history the document must preserve.

---

**Document Version**: 1.0.0
**Last Updated**: 2026-11-12
**Maintainer**: Development Team
**Next Review**: 2027-02-12
**Related Instructions**: [AI-Assisted Output Instructions](ai-assisted-output.instructions.md)
