---
marp: true
theme: default
paginate: true
---

## Prompt Files

::: notes
Introduce prompt files as a key guardrail mechanism for AI-assisted development. This slide sets the stage for understanding how prompt files differ from instruction files and chat modes.

Key points:

- Prompt files are task-specific templates
- They're executable and reusable
- Different from instruction files (which provide continuous guidance)
- Part of the "prompt-first" development approach

Timing: 1 minute brief intro.
Transition: "Let's define what we mean by executable task templates..."
:::

---

## Executable Task Templates

::: notes
Define prompt files as "executable task templates." This framing helps participants understand their purpose and usage.

Key concept: Prompt files are like functions—they take inputs (context, requirements) and produce outputs (code, docs, artifacts).

Draw parallels to:

- Shell scripts (automation)
- GitHub Actions workflows (CI/CD)
- Makefiles (build automation)

Prompt files bring the same benefits: repeatability, standardization, knowledge capture.

Timing: 1-2 minutes.
Transition: "So what exactly makes a prompt file?"
:::

---

## What Are Prompt Files?

Definition
Structured templates for specific, repeatable tasks
Contain detailed instructions for particular objectives
Designed for execution in AI chat interfaces
Key Characteristics
Scope: Single, focused task or workflow
Execution: Run on-demand when needed
Purpose: Define “what” to accomplish with specific steps
::: notes
Provide a formal definition and key characteristics of prompt files.

Definition breakdown:

- Structured templates: Follow a consistent format with metadata
- Specific, repeatable tasks: Not general guidance—concrete objectives
- Designed for execution: Meant to be run, not just read

Key characteristics:

1. Scope: Single task focus (generate tests, create docs, refactor module)
2. Execution: On-demand—you invoke them when needed
3. Purpose: Define deliverables clearly

Contrast with instruction files:

- Instruction files: Continuous guidance (always active)
- Prompt files: One-time execution (run and done)

Timing: 2-3 minutes.
Transition: "Let's look at the structure..."
:::

---

## Prompt File Structure

- -- mode: agent model: "anthropic/claude-3.5-sonnet@2024-10-22" tools: ["create", "edit", "read"] description: Generate comprehensive API documentation prompt_metadata: id: generate-api-docs title: API Documentation Generator category: documentation output_format: markdown --- # Generate API Documentation ## Context Create comprehensive API documentation from code analysis... ## Requirements 1. Analyze existing API endpoints 2. Generate OpenAPI specifications 3. Create developer-friendly guides 4. Include example requests/responses ## Deliverable Generate `docs/api/` folder with complete documentation...

---

## Prompt Files: Use Cases

Perfect For:
Code Generation → Create specific components/features
Documentation → Generate standardized docs
Analysis Tasks → Code reviews, security audits
Refactoring → Structured code improvements
Examples:
implement-user-authentication.prompt.md
generate-test-suite.prompt.md
create-deployment-pipeline.prompt.md

---

## Prompt Files Best Practices

✅ Do This:
Include comprehensive metadata
Provide clear context and requirements
Specify expected deliverables
Include verification steps
❌ Avoid This:
Vague or ambiguous instructions
Missing prerequisite information
No success criteria defined
Overly complex single prompts (break them down)
