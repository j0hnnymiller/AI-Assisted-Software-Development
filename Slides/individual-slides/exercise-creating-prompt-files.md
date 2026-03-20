---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-creating-prompt-files-20260319"
prompt: |
  create an exercise marp slide using the Slides\individual-slides\exercise-template.pptx template for the following:

  ### 6. Hands-On Exercise: Creating Prompt Files

  **Duration**: 01:35:07 - 01:57:29 (22:22)

  **Content**:

  - Exercise introduction: Create prompt file that creates instruction file
  - First attempt without instruction files (baseline)
  - Adding instruction files to repository
  - Second attempt with instruction files (comparison)
  - Comparing results from both iterations
  - Discussion of non-deterministic behavior and consistency

  **Exercise Objectives**:

  - Understand prompt structure
  - Practice defining intent, constraints, and success criteria
  - Create reusable, clear, scoped prompts
  - Observe the impact of instruction files on output quality

  **Exercise Steps**:

  1. **Phase 1 - Without Instructions**:
     - Create prompt to generate Evergreen software development instruction file
     - No guidance from existing instruction files
     - Save output for comparison
  2. **Phase 2 - With Instructions**:
     - John pushed instruction files to repository
     - Participants pulled updates
     - Cleared chat context (new chat window)
     - Re-ran same prompt with instruction files available
     - Compared differences
  3. **Phase 3 - Comparison**:
     - Use AI to compare the two generated files
     - Identify significant differences
     - Report findings
started: "2026-03-19T16:10:00Z"
ended: "2026-03-19T16:18:00Z"
task_durations:
  - task: "template mapping"
    duration: "00:02:00"
  - task: "exercise authoring"
    duration: "00:04:00"
  - task: "provenance and catalog updates"
    duration: "00:02:00"
total_duration: "00:08:00"
ai_log: "ai-logs/2026/03/19/exercise-creating-prompt-files-20260319/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

## Exercise: Creating Prompt Files

Duration: 22:22

Objectives

- Understand prompt structure
- Practice defining intent, constraints, and success criteria
- Create reusable, clear, scoped prompts
- Observe the impact of instruction files on output quality

Activities

1. Phase 1 - Without Instructions:
   - Create a prompt that generates an Evergreen software development instruction file
   - Work without repository instruction guidance
   - Save the generated result as the baseline output
2. Phase 2 - With Instructions:
   - Pull the newly added instruction files into the repository
   - Clear chat context and start a fresh conversation
   - Re-run the same prompt with instruction files now available
   - Capture the second output for comparison
3. Phase 3 - Comparison:
   - Ask AI to compare the baseline and guided outputs
   - Identify significant structural, metadata, and quality differences
   - Report findings on consistency and non-deterministic behavior

Success Criteria

- Prompt includes clear intent, constraints, and success criteria
- Baseline and guided outputs are both captured for side-by-side review
- Comparison identifies meaningful differences in completeness and consistency
- Participants can explain how instruction files changed the resulting output

::: notes

## Creating Prompt Files Exercise Instructions

**Duration:** 22:22
**Prerequisites:** Access to the repository before and after instruction-file updates, ability to start a fresh Copilot chat, and a place to save both generated outputs.

### Objectives

- Help participants understand that prompt files should define the task, constraints, and expected deliverable clearly.
- Show that reusable prompts are easier to review and rerun when they are tightly scoped.
- Demonstrate how repository instruction files improve consistency, completeness, and standards compliance.
- Reinforce that AI output remains non-deterministic, but better guidance reduces variance.

### Facilitation Guidance

Start by framing this as a controlled experiment: same task, two different context conditions. In Phase 1, let participants experience the ambiguity of running without repository guidance so they can see what the model invents or omits. In Phase 2, emphasize the importance of clearing chat context before rerunning, because lingering context would invalidate the comparison. Reserve the final segment for a group debrief on what changed, why it changed, and which improvements matter most for production use.

### Key Teaching Points

Call out differences in provenance metadata, structure, and adherence to repository conventions rather than treating any wording difference as equally important. Ask participants to notice whether the guided version is easier to review, safer to reuse, and more likely to pass team standards. Use the discussion to connect prompt files, instruction files, and reproducibility as part of the same operational discipline.

### Transition

Close by linking this exercise to the next step in the workflow: once a strong prompt exists, the team can version it, refine it, and regenerate instruction files more reliably than starting from scratch each time.
:::
