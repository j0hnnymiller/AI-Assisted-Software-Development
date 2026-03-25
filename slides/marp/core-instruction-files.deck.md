---
marp: true
theme: default
paginate: true
---

<!-- layout: Two Content -->

## Core Instructions

**Artifact and workflow rules**

- `ai-assisted-output.instructions.md`
  Guidance for AI-generated artifacts
- `chatmode-file.instructions.md`
  Guidance for generating chat modes
- `instruction-files.instructions.md`
  Guidance for generating instruction files

::: column

**Prompt-related rules**

- `prompt-file.instructions.md`
  Guidance for generating prompt files
- `instruction-prompt-files.instructions.md`
  Guidance for prompts that generate instruction files

::: notes
Duration ~00:03

Present the core instruction files that govern AI-assisted development in this repository. These files are the foundation of the guardrails system.

Explain each file's purpose:

- ai-assisted-output.instructions.md: The master policy for ALL AI-generated content, covering provenance, logging, and compliance
- chatmode-file.instructions.md: Defines how to create custom chat modes for specific development workflows
- instruction-files.instructions.md: Meta-instructions for creating new instruction files
- prompt-file.instructions.md: Guidelines for creating reusable prompt files
- instruction-prompt-files.instructions.md: Meta-prompts that generate instruction files

Emphasize the hierarchical nature: ai-assisted-output is the root policy that all others reference.

Transition: "Let's dive into how to use these..."
:::
