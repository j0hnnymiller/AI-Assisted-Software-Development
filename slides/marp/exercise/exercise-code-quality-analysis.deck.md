---
marp: true
theme: default
paginate: true
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
