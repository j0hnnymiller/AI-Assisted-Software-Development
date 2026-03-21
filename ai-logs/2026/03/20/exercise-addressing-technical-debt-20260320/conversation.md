# AI Conversation Log

- Chat ID: exercise-addressing-technical-debt-20260320
- Operator: johnmillerATcodemag-com
- Model: openai/gpt-5.4@unknown
- Started: 2026-03-20T17:18:30.8705200-07:00
- Ended: 2026-03-20T17:24:30.8705200-07:00
- Total Duration: 00:06:00

## Context

- Inputs: Slides/individual-slides/exercise-template.md, Slides/individual-slides/exercise-template.pptx, CODE/Evergreen/AIASD-Addressing-Tech-Debt.md, user-provided exercise content
- Targets: Slides/individual-slides/exercise-addressing-technical-debt.md, README.md
- Constraints/Policies: .github/instructions/ai-assisted-output.instructions.md, .github/instructions/copilot-instructions.md, .github/instructions/create-marp-slides.instructions.md, .github/instructions/slide-pipeline.instructions.md

## Exchanges

### Exchange 1

[2026-03-20T17:18:30.8705200-07:00] johnmillerATcodemag-com

```text
create an exercise marp slide using the Slides\individual-slides\exercise-template.pptx template for the following:


# **Exercise: Prompt Copilot to Address Technical Debt**

### Duration

10 minutes

### Objectives

- Practice writing high-signal prompts
- Apply architectural constraints
- Produce safe, incremental remediation requests

### Activities

1. Select a small piece of technical debt.
2. Write a prompt that includes:
   - Description of the debt
   - Constraints and rules
   - Expected behavior
   - Required tests and documentation
3. Ask Copilot to propose a remediation.
4. Review the output for correctness.

### Success Criteria

- Prompt is clear, scoped, and actionable
- Copilot produces a safe, incremental change
- Output aligns with architectural rules
- Provenance metadata is included

::: notes
Encourage participants to choose a real example from their brownfield system. The goal is clarity and safety, not complexity.
:::

---

# **Exercise: Assigning an Issue to Copilot**

### Duration

10 minutes

### Objectives

- Convert technical debt into a structured issue
- Provide Copilot with actionable context
- Practice writing acceptance criteria

### Activities

1. Select a technical debt item.
2. Create a GitHub-style issue with:
   - Title
   - Description
   - Impact and risk
   - Acceptance criteria
   - Provenance metadata
3. Assign the issue to Copilot.
4. Review Copilot's proposed remediation.

### Success Criteria

- Issue is clear and well-structured
- Acceptance criteria are testable
- Copilot produces a relevant draft
- Provenance metadata is present

::: notes
This exercise reinforces the workflow of treating Copilot as a junior developer who receives tasks and produces drafts.
:::

---

# **Exercise: Delegating Work to Copilot**

### Duration

15 minutes

### Objectives

- Practice delegating multi-step tasks
- Ensure Copilot follows architectural rules
- Validate AI-generated remediation plans

### Activities

1. Select a multi-step technical debt item.
2. Ask Copilot to:
   - Analyze the problem
   - Propose a remediation plan
   - Generate code changes
   - Update tests
   - Update documentation
3. Review Copilot's output.
4. Identify missing context or risks.

### Success Criteria

- Delegation prompt is complete and structured
- Copilot produces a multi-step plan
- Output is safe, incremental, and reversible
- Human review identifies any gaps

::: notes
This exercise builds confidence in delegating larger tasks while maintaining safety and architectural alignment. Emphasize that humans remain the final reviewers.
:::
```

[2026-03-20T17:24:30.8705200-07:00] openai/gpt-5.4@unknown

```text
Created a three-slide Marp exercise deck at Slides/individual-slides/exercise-addressing-technical-debt.md following the exercise template structure used in this repository.

The deck preserves the three requested exercises, adds complete AI provenance front matter, expands the speaker notes for facilitator delivery, and uses the same Markdown-to-PPTX workflow that existing exercise slides use when they reference exercise-template.pptx.

I also added the matching ai-log conversation and summary files and registered the new exercise deck in README.md under Notable Artifacts for traceability.
```

## Work Burst Closure

**Artifacts Produced**:

- `Slides/individual-slides/exercise-addressing-technical-debt.md` - Three-slide Marp exercise deck for technical debt workflows with Copilot
- `ai-logs/2026/03/20/exercise-addressing-technical-debt-20260320/conversation.md` - Conversation transcript and provenance record
- `ai-logs/2026/03/20/exercise-addressing-technical-debt-20260320/summary.md` - Session summary for resumability

**Next Steps**:

- [ ] Preview the deck in Marp or merge it into a course manifest if it should be included in a scheduled day deck
- [ ] Generate PPTX output through the existing slide pipeline if a compiled artifact is needed

**Duration Summary**:

- Template mapping: 00:02:00
- Exercise authoring: 00:03:00
- Provenance and catalog updates: 00:01:00
- Total: 00:06:00
