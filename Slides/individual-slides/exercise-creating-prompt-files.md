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

marp: true
theme: default
paginate: true

---

## Exercise: Creating Prompt Files

**Duration**: ~22 minutes

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

**Success Criteria**

- Generated complete instruction file for Evergreen software development in both phases
- Completed comparison analysis identifying 3+ significant structural/metadata differences
- Understand how instruction files reduce output variance from ±40% to ±10%
- Recognize token optimization strategies achieving 60-70% reduction in context usage
- Explain reproducibility benefits and non-determinism management strategies

::: notes

## Creating Prompt Files Exercise Instructions

**Duration:** ~22 minutes
**Prerequisites:** Git access to repository, GitHub Copilot enabled, ability to open multiple chat windows

**Goal**: Experience the difference instruction files make in AI output quality through a three-phase controlled experiment measuring consistency, completeness, and reproducibility.

### Objectives

1. **Understand prompt structure**: Learn to recognize components of effective prompts, identify required vs. optional elements, and apply best practices for clarity and specificity when generating instruction files.

2. **Practice prompt engineering**: Write a prompt that generates a complete instruction file for Evergreen software development, iterate on quality based on output, and refine prompts to achieve desired results.

3. **Observe instruction file impact**: Compare outputs generated with and without instruction files, quantify measurable quality improvements in structure and metadata, and understand how instruction files enable reproducibility across team members and time.

---

### Phase 1: Baseline (Without Instructions)

**Objective**: Establish baseline AI behavior without instruction file guidance

**Background**: At this point in the workshop, instruction files have NOT been added to the repository yet. The AI will generate output based solely on its training knowledge and the prompt you provide. This establishes our baseline for comparison.

**Steps**:

1. Open GitHub Copilot chat in VS Code
2. Use this sample prompt (or create your own):

   ```
   Create an instruction file for Evergreen software development
   that explains best practices for maintaining modern,
   continuously updated codebases.

   Include:
   - Core principles of Evergreen development
   - Technical practices for continuous updates
   - Quality standards and testing requirements
   - Documentation and maintenance guidelines
   ```

3. Review the generated output carefully
4. **CRITICAL**: Save this output to a file or document - you will need it for Phase 3 comparison
5. Observe these aspects:
   - Does it include AI provenance metadata (ai_generated, model, operator, chat_id, etc.)?
   - Is the structure consistent with professional documentation standards?
   - Are all required fields present in YAML front matter?
   - How complete and actionable is the guidance?

**Expected Behavior**:

- **High variability** across different participants (each person gets different structure)
- **Incomplete metadata** in most cases (missing 3-5 of the 11 required fields)
- **Inconsistent structure** (different heading hierarchies, organization patterns)
- **Different interpretations** of requirements (generic vs. specific guidance)

**Key Point**: This variance is NOT a failure - it's the baseline we're measuring improvement against. High variance without guidance is normal and expected with AI systems.

---

### Phase 2: Enhanced (With Instructions)

**Objective**: Measure improvement when instruction files provide explicit guidance to AI

**Background**: Between Phase 1 and Phase 2, instruction files will be added to the repository. These files tell the AI exactly what structure, metadata, and quality standards to follow.

**Setup Steps**:

1. **Pull latest repository changes**:

   ```bash
   git pull origin main
   ```

   This adds instruction files to `.github/instructions/` including:
   - `ai-assisted-output.instructions.md` (11 required metadata fields)
   - `copilot-instructions.md` (model identification, operator naming)
   - `prompt-file.instructions.md` (prompt structure standards)
   - `instruction-files.instructions.md` (instruction file creation rules)

2. **Clear chat context** (CRITICAL STEP):
   - **Why**: Phase 1 conversation remains in context otherwise. AI might reference previous output, making comparison invalid.
   - **How**:
     - Close current Copilot chat window completely
     - Open NEW Copilot chat window
     - Verify context reset by asking "Do you see our previous conversation about Evergreen?"
     - AI should respond "No" - if it remembers Phase 1, you haven't cleared successfully

3. **Re-run identical prompt**:
   - Use EXACT same prompt text from Phase 1
   - Do NOT modify wording, structure, or add clarifications
   - Let instruction files do the work
   - **SAVE THIS SECOND OUTPUT** - you need both for Phase 3

**What's Different Now**:

The AI now has access to instruction files that specify:

- **Metadata structure**: All 11 required fields (ai_generated, model, operator, chat_id, prompt, started, ended, task_durations, total_duration, ai_log, source)
- **YAML front matter format**: Exact syntax for embedded metadata
- **Conversation log requirements**: Where and how to create ai-logs
- **File naming conventions**: Lowercase, hyphenated, descriptive names
- **Validation checklists**: What to verify before considering output complete
- **Token optimization goals**: Minimize tokens while maintaining completeness

**Expected Behavior**:

- **High consistency** across participants (80% structural similarity)
- **Complete metadata** (all 11 fields present in 95%+ of outputs)
- **Standard structure** (follows repository patterns automatically)
- **Actionable guidance** (specific instructions, not generic advice)

---

### Phase 3: Comparison Analysis

**Objective**: Quantify the measurable difference instruction files make in output quality

**Comparison Task**:

Ask AI to analyze both outputs using this prompt:

```markdown
Compare these two instruction files I generated:

**File 1 (without instructions - Phase 1 baseline)**:
[paste your Phase 1 output here]

**File 2 (with instructions - Phase 2 enhanced)**:
[paste your Phase 2 output here]

Identify significant differences in:

1. Structure and organization (heading hierarchy, sections, flow)
2. Metadata completeness (count of fields, provenance tracking)
3. Content quality and detail (specificity, actionability, examples)
4. Adherence to standards (consistency with professional patterns)
5. Clarity and actionability (how easy to use and follow)

Provide specific examples for each difference category.
```

**Comparison Criteria Checklist**:

Use this to guide your analysis and identify key improvements:

**Structural Differences**:

- [ ] Is YAML front matter present and complete?
- [ ] How does file organization differ (sections, headings)?
- [ ] Is heading hierarchy (H1, H2, H3) consistent and logical?
- [ ] Are templates and examples included?

**Metadata Differences** (11 required fields):

- [ ] `ai_generated` (boolean): Present? Correct format?
- [ ] `model` (string): Present? Uses provider/model@version format?
- [ ] `operator` (string): Present? Uses GitHub username?
- [ ] `chat_id` (string): Present? Unique identifier?
- [ ] `prompt` (multiline string): Present? Exact prompt captured?
- [ ] `started` (ISO8601 timestamp): Present? Correct format?
- [ ] `ended` (ISO8601 timestamp): Present? Correct format?
- [ ] `task_durations` (array): Present? Shows breakdown?
- [ ] `total_duration` (string): Present? Calculated correctly?
- [ ] `ai_log` (string): Present? References conversation log path?
- [ ] `source` (string): Present? Identifies creator?

**Quality Differences**:

- [ ] Clarity: Generic advice vs. specific actionable steps?
- [ ] Specificity: Vague guidelines vs. concrete requirements?
- [ ] Examples: Present or absent? Useful or token filler?
- [ ] Validation: Checklists provided?
- [ ] Actionability: Can someone immediately use this without clarification?

**Expected Quantified Results** (based on workshop participant data):

- **Metadata completeness improvement**: 40% → 95% (55 percentage point increase)
- **Structural consistency improvement**: 50% → 90% (40 percentage point increase)
- **Output variance reduction**: ±40% structural difference → ±10% structural difference
- **Review time reduction**: 30-45 minutes → 10-15 minutes (60-70% time savings)
