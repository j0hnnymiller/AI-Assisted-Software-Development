# AI Conversation Log

- Chat ID: exercise-creating-prompt-files-2026-03-17
- Operator: johnmillerATcodemag-com
- Model: anthropic/claude-3.5-sonnet@2024-10-22
- Started: 2026-03-17T22:25:00Z
- Ended: 2026-03-17T22:35:00Z
- Total Duration: 00:10:00

## Context

- Inputs: AI-Assisted Software Development with GitHub Copilot (Tue Morning)-summary.md (lines 191-258), course recording summary
- Targets: Slides/individual-slides/exercise-creating-prompt-files.md
- Constraints/Policies: .github/instructions/create-marp-slides.instructions.md, .github/instructions/ai-assisted-output.instructions.md, .github/instructions/copilot-instructions.md

## Exchanges

### Exchange 1

[2026-03-17T22:25:00Z] johnmillerATcodemag-com

```text
create a marp deck titled "Exercise: Creating Prompt Files" explaining the following content:

### 6. Hands-On Exercise: Creating Prompt Files [x]

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

**Exercise Findings**:

- **Chris Bishop's Results**: AI recommended merging core principles from original document with new document, suggested including conceptual foundation, provided comparison table
- **Rockwell Christopher's Results**: Extensive differences including mode declaration, model specification, log creation requirements, interesting distinction between AI-generated vs. manual checklists
- **General Observations**:
  - Non-deterministic nature of AI output without guidance
  - Significant improvement in consistency with instruction files
  - More complete metadata and provenance with instructions
  - Better adherence to repository standards

**Key Discussion Points**:

- Reproducibility and dependability of AI output
- Reducing scrutiny burden through better guidance
- Making AI-generated code more predictable
- Trade-offs between verbose human-readable vs. terse AI-optimized instruction files

**Token Optimization Discussion**:

- John's experience with context window limitations
- Evolution from verbose human-targeted to terse AI-targeted instructions
- Requirement to "minimize token consumption while maintaining clarity"
- Creating separate human-readable documentation vs. AI instruction files

**Clarifications During Exercise**:

- Boris Giterman asked about sequence of instruction files (which to use first)
- John clarified the exercise is about creating a prompt that creates a prompt that creates an instruction
- Dan Blanchard asked about file location (.github/copilot/Promptfiles vs .github/instructions)
- Confusion resolved: prompt files go in /prompts, instruction files in /instructions
```

[2026-03-17T22:28:00Z] anthropic/claude-3.5-sonnet@2024-10-22

```text
I'll create a comprehensive Marp deck for the "Exercise: Creating Prompt Files" hands-on exercise. This slide deck will walk through all three phases of the exercise, explain the findings from participants, and cover the key discussion points about reproducibility, token optimization, and instruction file benefits.

The deck will be structured as:
1. Exercise overview and objectives
2. Phase 1: Baseline without instructions
3. Phase 2: Enhanced with instructions
4. Phase 3: Comparison analysis
5. Participant findings (Chris Bishop, Rockwell Christopher, general observations)
6. Key discussion points (reproducibility, token optimization, trade-offs)
7. Q&A and clarifications
8. Lessons learned
9. Practical applications
10. Wrap-up and action items

Creating file: Slides/individual-slides/exercise-creating-prompt-files.md
```

## Work Burst Closure

**Artifacts Produced**:

- `Slides/individual-slides/exercise-creating-prompt-files.md` - Comprehensive 60+ slide Marp deck for hands-on exercise workshop

**Next Steps**:

- [ ] Generate PowerPoint output if needed
- [ ] Review slide content for accuracy
- [ ] Consider adding to course agenda YAML file
- [ ] Update README.md if deemed notable artifact

**Duration Summary**:

- Content structuring and slide creation: 00:10:00
- Total: 00:10:00
