# AI Conversation Log

- Chat ID: exercise-creating-prompt-files-20260319
- Operator: johnmillerATcodemag-com
- Model: openai/gpt-5.4@unknown
- Started: 2026-03-19T16:10:00Z
- Ended: 2026-03-19T16:18:00Z
- Total Duration: 00:08:00

## Context

- Inputs: past-class-recordings/2026-02/AI-Assisted Software Development with GitHub Copilot (Tue Morning)-summary.md, Slides/individual-slides/exercise-template.md, existing exercise slides
- Targets: Slides/individual-slides/exercise-creating-prompt-files.md
- Constraints/Policies: .github/instructions/ai-assisted-output.instructions.md, .github/instructions/copilot-instructions.md, .github/instructions/create-marp-slides.instructions.md, .github/instructions/marp-slides.instructions.md, .github/instructions/slide-pipeline.instructions.md

## Exchanges

### Exchange 1

[2026-03-19T16:10:00Z] johnmillerATcodemag-com

```text
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
```

[2026-03-19T16:18:00Z] openai/gpt-5.4@unknown

```text
Created a standalone Marp exercise slide based on the repository's exercise template pattern. The slide captures the three-phase workflow, success criteria, and facilitator notes focused on consistency, context isolation, and instruction-file impact.

Also created matching provenance files under ai-logs/2026/03/19/exercise-creating-prompt-files-20260319/ and added the artifact to the README's Notable Artifacts section.
```

## Work Burst Closure

**Artifacts Produced**:

- `Slides/individual-slides/exercise-creating-prompt-files.md` - Marp exercise slide for the prompt-file comparison workshop
- `ai-logs/2026/03/19/exercise-creating-prompt-files-20260319/conversation.md` - Conversation log for slide creation
- `ai-logs/2026/03/19/exercise-creating-prompt-files-20260319/summary.md` - Session summary with resumability context

**Next Steps**:

- [ ] Preview the slide in Marp or deck generation flow
- [ ] Add the slide to a section manifest if it should appear in a compiled session deck
- [ ] Reuse the exercise structure for other prompt-vs-instruction comparison exercises

**Duration Summary**:

- Template mapping: 00:02:00
- Exercise authoring: 00:04:00
- Provenance and catalog updates: 00:02:00
- Total: 00:08:00
