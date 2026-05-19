---
marp: true
theme: default
paginate: true
---

# AIASD Exercises

::: notes
This is the title slide for the exercises section. It should use the default title slide layout with the title "Exercises" and no subtitle or body content. The notes should indicate that this slide serves
as a section header for the exercises portion of the presentation.
**Expected PPTX Rendering:**
- Layout: Title Slide
- Title Placeholder: "Exercises"
- Subtitle Placeholder: (empty)
- Content Placeholder: (empty)
:::

---

<!-- _class: lead -->

## Course Modules

- Exercises
- **▶ Brownfield Software Development Exercises**
- Building a Backlog Exercises
- Addressing Technical Debt Exercises
- Multi-Implementation Comparison Exercises

---

<!-- layout: Two Content -->

## Exercise: Implementing a Feature Flag

**Objectives**
  - Learn how to introduce a safe, reversible change
  - Practice designing a feature flag workflow
  - Understand As-Is and To-Be test implications
  - Document rollout and retirement criteria

**Activities**
  1. Select a small brownfield function or module
  2. Identify a safe, incremental change to introduce
  3. Design a feature flag with name, description, rollout plan, rollback plan, and retirement criteria

::: column

  4. Write As-Is and To-Be test cases
  5. Document the change with provenance metadata

**Success Criteria**:
  - Feature flag is scoped
  - Rollout/rollback plans are explicit
  - Tests are correct
  - Retirement criteria are documented

::: notes
Duration ~00:20

Give students 20 minutes. Encourage them to select something real from their own codebases if possible -- the exercise is more meaningful with familiar code. The feature flag design is more important than the implementation: students should be able to articulate why the flag exists, who can see the new behavior, and what evidence will trigger retirement. Circulate and ask teams to describe their rollback plan. Debrief: what made the boundary hard to define? What surprised you about writing As-Is tests?
:::

---

<!-- Layout: Two Content -->

## Exercise: Building the Safety Nets

**Objectives**
  - Identify missing safety nets in a brownfield system
  - Strengthen protection using AI and human review practices
  - Apply test automation principles
  - Produce actionable improvements

**Activities**
  1. Select a brownfield module or file
  2. Identify existing safety nets (tests, reviews, documentation)
  3. Ask AI to identify missing or weak safety nets

::: column

  4. Strengthen by adding tests, drafting review checklists, documenting architectural constraints
  5. Share findings with a partner for validation

**Success Criteria**:
  - Missing nets identified
  - Improvements are safe and incremental
  - Coverage or clarity improved
  - Review and documentation guardrails are strengthened

::: notes
Duration ~00:20

This exercise is the capstone of the combined module. Students apply all three sections simultaneously: they audit a real codebase, use AI to find gaps, and produce a concrete list of improvements. The partner validation step is important -- it simulates the human-in-the-loop review process and often surfaces things one person missed. Debrief questions: what was missing that surprised you? How did AI's assessment of the safety nets compare to your own? What would you prioritize first? Encourage students to bring their findings back to their teams.
:::

---

<!-- _class: lead -->

## Course Modules

- Exercises
- Brownfield Software Development Exercises
- **▶ Building a Backlog Exercises**
- Addressing Technical Debt Exercises
- Multi-Implementation Comparison Exercises

---

<!-- layout: Two Content -->

## Exercise: Create Project Requirement

Objective:
  - Create project requirement instructions, some project-specific, some generic, using both manual and Copilot-assisted methods.

Activities:
  1. Create a project-requirements.md file that includes:
    - Business rules
    - Workflows
    - Purpose
    - Tech stack
    - Architecture

::: column

  2. Use Copilot to generate instruction files using the project-requirements.md file and the codebase for context.

Success Criteria:
  - Instructions are clear and actionable
  - Both manual and AI-assisted methods are used
  - Instruction files are generated successfully

::: notes
Author requirement docs, then use Copilot to generate scaffolding and validate alignment.
:::

---

<!-- layout: Two Content -->

## Exercise: Create an Implementation Plan

Objectives
- Translate issues into a structured remediation plan
- Ensure changes are incremental and reversible
- Align modernization with evergreen principles
- Incorporate testing and rollback strategies
Activities
1. Select 2-3 issues from the previous exercise.
2. For each issue, create a remediation plan including:
  - Problem definition
  - Root cause
  - Proposed solution
  - Step-by-step implementation
  - Rollback plan
  - Required test updates
  - Documentation updates

::: column

3. Review plan.

Success Criteria
- Plans are incremental, safe, and reversible
- Include clear steps and rollback strategies
- Align with evergreen development principles
- Include test and documentation updates

::: notes
Duration ~00:20

This exercise helps participants move from analysis to execution. The goal is to build modernization plans that are safe, thoughtful, and aligned with evergreen principles.
:::

---

<!-- layout: Two Content -->

## Exercise: Building the Backlog

Objectives
  - Practice identifying technical debt
  - Convert findings into actionable GitHub issues
  - Apply consistent structure
  - Prioritize issues based on risk and impact

Activities
  1. Select a brownfield module or file.
  2. Use AI to identify:
    - Technical debt
    - Risks
    - Test confidence
    - Architectural issues

::: column

  3. Convert each finding into a GitHub issue with:
    - Title
    - Description
    - Acceptance criteria
    - Labels
  4. Prioritize the issues using impact vs. effort.

Success Criteria
  - Issues are clear, actionable, and well-structured
  - Prioritization reflects real risk and effort
  - Backlog is ready for implementation

::: notes
Duration ~00:20

Encourage participants to treat this as a real backlog-building session. The goal is not volume -- it's clarity and actionability. Reinforce that a well-structured backlog is the foundation for safe, incremental modernization.
:::

---

<!-- _class: lead -->

## Course Modules

- Exercises
- Brownfield Software Development Exercises
- Building a Backlog Exercises
- **▶ Addressing Technical Debt Exercises**
- Multi-Implementation Comparison Exercises

---

<!-- layout: Two Content -->

## Exercise: Generate Instruction Files

Objectives
  - Use meta prompts to scale instruction-file creation
  - Capture module-specific rules
  - Encode domain and architectural constraints

Activities
  1. Prompt Copilot to create instruction files for the standards and conventions of the tech stack
  2. Review instructions

::: column

Success Criteria
  - Instruction files reflect real system constraints
  - Meta prompts produce consistent structure
  - Files are ready for team use

::: notes
Duration ~00:20

Participants experience the leverage of meta prompts and see how AI can accelerate documentation.

Prompts:

Create instruction files for the backend technologies

Create instruction files for the front-end technologies

Create instruction files for the front-end technologies
:::

---

<!-- Layout: Two Content -->

## Exercise: Generate Issues to Make the Codebase Evergreen

Objectives
  - Identify conformance gaps
  - Convert gaps into actionable issues
  - Apply consistent structure and provenance
  - Prioritize issues based on risk and impact

Activities
  1. Select a brownfield module or file.
  2. Compare it against the project's instruction file.
  3. Ask AI to identify conformance gaps.

::: column

  4. Convert each gap into a GitHub issue with:
    - Title
    - Description
    - Violated rule
    - Suggested remediation
    - Acceptance criteria
    - Provenance metadata
  5. Prioritize the issues.

Success Criteria
- Issues are clear, actionable, and aligned with instruction files
- Provenance metadata is included
- Prioritization reflects real risk and effort
- Backlog is ready for team review

::: notes
Duration ~00:15

Encourage participants to treat this as a real backlog-building session. The goal is clarity and actionability, not volume.
:::

---

<!-- Layout: Two Content -->

## Exercise: Identifying Code Outside the Guardrails

Objectives
  - Detect code that violates architectural rules
  - Identify patterns that contradict instruction files
  - Practice safe analysis workflows
  - Make a plan for remediation

Activities
  1. Review the code
  2. Compare it against the instruction files
  3. Identify violations or risky patterns

::: column

  4. Propose safe remediation steps
  5. Document findings with provenance

Success Criteria
  - Deviations are correctly identified
  - Remediation steps are safe and incremental
  - Documentation includes provenance

::: notes
Duration ~00:10

This exercise reinforces the importance of guardrails and helps participants practice applying them to real code.
:::

---

<!-- Layout: Two Content -->

## Exercise: Code Quality Analysis

Objectives
  - Use AI to detect non-evergreen code patterns in the workspace.
  - Distinguish temporary artifacts from long-lived maintainable assets.
  - Propose practical evergreen refactors with clear priority.

Activities
  1. AI Baseline Scan
    - Run an AI prompt to identify files that look date-bound, draft-only, or placeholder-heavy.
    - Collect at least 8 candidate findings across docs, prompts, and slides.
  2. Evidence and Classification
    - Classify each finding as one type: date-bound metadata, draft artifact, stale placeholder, duplicated policy, or legacy process text.
    - Validate each candidate with one concrete file location.

::: column

  3. Evergreen Refactor Plan
    - Select top 3 high-impact findings.
    - Write a before/after recommendation focused on longevity, clarity, and reduced maintenance.
  4. Share and Defend
    - Present one finding and explain why it is not evergreen.
    - Defend your proposed fix with expected impact.

Success Criteria
  - 8 or more non-evergreen findings identified with evidence.
  - Findings are correctly categorized by non-evergreen pattern.
  - Top 3 recommendations are specific, actionable, and evergreen-focused.
  - Team can explain why each proposed change improves long-term maintainability.

::: notes
Duration ~00:20

## Code Quality Analysis Exercise Instructions

**Prerequisites:** Access to the full workspace, AI chat enabled, and search tools available.

### Objectives

- Find and document non-evergreen code and content patterns.
- Use AI plus direct file evidence to avoid false positives.
- Convert findings into evergreen improvement actions.

### Suggested Prompt

Analyze the workspace for code or content that is not evergreen. Focus on date-coupled content, draft artifacts, placeholders like <auto> or <timestamp>, duplicated instructions, and unstable naming. Return findings as: file, reason, risk, and evergreen fix.

### Suggested Hunt Areas

- Slides with draft naming patterns and temporary outputs.
- Prompt and instruction files containing placeholder metadata.
- Repeated policy content that can drift over time.

### Activities

- Step 1: Run your AI scan and collect raw findings.
- Step 2: Verify each result against an actual file and exact snippet.
- Step 3: Prioritize top 3 findings by impact and effort.
- Step 4: Draft evergreen replacements and share with the group.

### Success Criteria

- At least 8 validated findings.
- At least 3 high-impact evergreen refactors proposed.
- Clear justification connecting each fix to maintainability and future reuse.
:::

---

<!-- Layout: Two Content -->

## Exercise: Prompt Copilot to Address Technical Debt

Objectives
  - Practice writing high-signal prompts
  - Apply architectural constraints
  - Produce safe, incremental remediation requests

Activities
  1. Select a small piece of technical debt.
  2. Write a prompt that includes:
    - Description of the debt
    - Constraints and rules
    - Expected behavior
    - Required tests and documentation

::: column

  3. Ask Copilot to propose a remediation.
  4. Review the output for correctness.

Success Criteria
  - Prompt is clear, scoped, and actionable
  - Copilot produces a safe, incremental change
  - Output aligns with architectural rules
  - Provenance metadata is included

::: notes
Duration ~00:10

Encourage participants to choose a real example from their brownfield system. The goal is clarity and safety, not complexity.
:::

---

## Exercise: Assigning an Issue to Copilot

Objectives
Convert technical debt into a structured issue
Provide Copilot with actionable context
Practice writing acceptance criteria
Activities
Select a technical debt item.
Create a GitHub-style issue with:
  - Title
  - Description
  - Impact and risk
  - Acceptance criteria
  - Provenance metadata
Assign the issue to Copilot.
Review Copilot's proposed remediation.
Success Criteria
Issue is clear and well-structured
Acceptance criteria are testable
Copilot produces a relevant draft
Provenance metadata is present

::: notes
Duration ~00:10

This exercise reinforces the workflow of treating Copilot as a junior developer who receives tasks and produces drafts.
:::

---

## Exercise: Delegating Work to Copilot

Objectives
Practice delegating multi-step tasks
Ensure Copilot follows architectural rules
Validate AI-generated remediation plans
Activities
Select a multi-step technical debt item.
Ask Copilot to:
  - Analyze the problem
  - Propose a remediation plan
  - Generate code changes
  - Update tests
  - Update documentation
Review Copilot's output.
Identify missing context or risks.
Success Criteria
Delegation prompt is complete and structured
Copilot produces a multi-step plan
Output is safe, incremental, and reversible
Human review identifies any gaps

::: notes
Duration ~00:15

This exercise builds confidence in delegating larger tasks while maintaining safety and architectural alignment. Emphasize that humans remain the final reviewers.
:::

---

<!-- _class: lead -->

## Course Modules

- Exercises
- Brownfield Software Development Exercises
- Building a Backlog Exercises
- Addressing Technical Debt Exercises
- **▶ Multi-Implementation Comparison Exercises**

---

<!-- layout: Two Content -->

## Exercise: Prompt Multiple Models to Address Technical Debt

Objectives
  - Compare outputs from different models
  - Identify strengths and weaknesses
  - Evaluate risk and quality

Activities
  1. Select a small technical debt item.
  2. Prompt two or more models to propose a fix.

::: column

  3. Compare outputs for:
    - Safety
    - Clarity
    - Test coverage
    - Architectural alignment
  4. Synthesize the best elements into a final solution.

Success Criteria
  - Differences between models are clearly identified
  - Risks and strengths are evaluated
  - Final synthesized solution is safe and incremental
  - Provenance metadata is included

::: notes
Duration ~00:15

Encourage participants to think like reviewers comparing multiple PRs. The goal is to understand model behavior, not to pick a favorite.
:::