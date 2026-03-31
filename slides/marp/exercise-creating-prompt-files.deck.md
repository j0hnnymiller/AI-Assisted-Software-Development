---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-creating-prompt-files-refactor-2026-03-17"
prompt: |
  Refactor the exercise-creating-prompt-files.md file to follow the exercise-template.md structure,
  condensing the multi-slide deck into a single exercise slide with comprehensive speaker notes
started: "2026-03-17T23:00:00Z"
ended: "2026-03-17T23:10:00Z"
task_durations:
  - task: "refactoring and condensing"
    duration: "00:10:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2026/03/17/exercise-creating-prompt-files-refactor-2026-03-17/conversation.md"
source: "johnmillerATcodemag-com"
---

# Exercise: Creating Prompt Files || Exercise: The Prompt Engineering Gauntlet

---

## Exercise: Creating Prompt Files

**Objectives**

- Understand prompt structure and best practices for AI instruction file generation
- Practice prompt engineering by creating reusable prompt files
- Observe measurable impact of instruction files on AI output quality
- Compare outputs with and without instruction file guidance

**Activities**

- **Phase 1 - Baseline**: Create prompt to generate Evergreen instruction file without repository instruction files; save output for comparison
- **Phase 2 - Enhanced**: Pull repository updates with instruction files; clear chat context; re-run identical prompt with new guidance
- **Phase 3 - Analysis**: Compare both outputs using AI-assisted analysis; quantify differences in structure, metadata completeness, and quality
- **Discussion & Review**: Analyze findings on reproducibility, token optimization, non-determinism, and real participant results

::: column

**Success Criteria**

- Generated complete instruction file for Evergreen software development in both phases
- Completed comparison analysis identifying 3+ significant structural/metadata differences
- Understand how instruction files reduce output variance from ±40% to ±10%
- Recognize token optimization strategies achieving 60-70% reduction in context usage
- Explain reproducibility benefits and non-determinism management strategies

:::

::: notes

## Creating Prompt Files Exercise Instructions

Duration ~00:22

**Prerequisites:** Git access to repository, GitHub Copilot enabled, ability to open multiple chat windows

**Goal**: Experience the difference instruction files make in AI output quality through a three-phase controlled experiment measuring consistency, completeness, and reproducibility.

### Objectives

1. **Understand prompt structure**: Learn to recognize components of effective prompts, identify required vs. optional elements, and apply best practices for clarity and specificity when generating instruction files.

2. **Practice prompt engineering**: Write a prompt that generates a complete instruction file for Evergreen software development, iterate on quality based on output, and refine prompts to achieve desired results.

3. **Observe instruction file impact**: Compare outputs generated with and without instruction files, quantify measurable quality improvements in structure and metadata, and understand how instruction files enable reproducibility across team members and time.

:::
