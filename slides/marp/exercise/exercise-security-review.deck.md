---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "calculator-project-exercise-deck-20260317"
prompt: |
  create an exercise slide deck, using the #file:exercise-template.md, for the provided calculator project exercise content.
started: "2026-03-17T03:28:00Z"
ended: "2026-03-17T03:36:00Z"
task_durations:
  - task: "content normalization"
    duration: "00:03:00"
  - task: "deck authoring"
    duration: "00:05:00"
total_duration: "00:08:00"
ai_log: "ai-logs/2026/03/17/calculator-project-exercise-deck-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
<!-- layout: Two Content -->

## Exercise: Security Review

Objectives

- Systematically review code for security issues
- Address discovered vulnerabilities
- Strengthen input validation and safe patterns

Activities

1. Security Review:
   - Prompt: "Review this code for security vulnerabilities"
   - Address identified issues
   - Add input validation where missing

::: column

2. Validate Fixes:
   - Write tests for fixed vulnerabilities
   - Review fixes with peers
   - Document rationale for security decisions

Success Criteria

- No obvious security issues remain
- AI recommendations are critically evaluated and validated

::: notes
Duration ~00:40

## Security Review Exercise Instructions

**Prerequisites:** Functional calculator project

### Objectives

- Apply practical security checks to working code.

### Activities

- Validate fixes with tests and review, not assumptions.

### Success Criteria

- Security posture improves with documented rationale.
  :::