# GitHub Copilot Instruction Stack

### How `appliesTo`, chat modes, and promptfiles shape the final instructions

------------------------------------------------------------------------

# Overview

### What this deck covers

-   How Copilot assembles the instruction stack
-   How `appliesTo` filters instruction files
-   Where instruction files should live
-   How chat modes and promptfiles influence the stack
-   A diagram of the full hierarchy
-   Guidance for designing maintainable guardrails

------------------------------------------------------------------------

# The Instruction Stack

### The layers Copilot merges for every prompt

1.  **Organization-level instruction files**
2.  **Repository-level instruction files**
3.  **Chat mode instructions**
4.  **Promptfile instructions**
5.  **User message**

**Speaker Notes:** Copilot merges these layers deterministically. Higher
layers constrain or override lower ones. Promptfiles never override
guardrails---they only add task-specific instructions.

------------------------------------------------------------------------

# Where `appliesTo` Fits

### The filtering mechanism for instruction files

`appliesTo` is a **selector** that determines *when* an instruction file
is included in the stack.

Common selectors include:

-   **repositories** -- include only for specific repos
-   **languages** -- include only for certain languages
-   **filePatterns** -- include only when editing certain files
-   **tools** -- include only when using specific Copilot features
-   **scopes** -- include only in chat, only in editor, etc.

**Speaker Notes:** `appliesTo` is not a guardrail itself. It's a routing
rule. It prevents irrelevant instructions from polluting the stack and
keeps the assistant focused.

------------------------------------------------------------------------

# How `appliesTo` Interacts with the Stack

### Filtering happens *before* merging

1.  Copilot discovers all instruction files in scope
2.  Copilot filters them using `appliesTo`
3.  Copilot merges the remaining files into the stack

**Speaker Notes:** This means you can have many instruction files in
`.github/instructions/`, but only the ones whose `appliesTo` match the
current context will be included.

------------------------------------------------------------------------

# Example: appliesTo in Action

\`\`\`yaml appliesTo: languages: \["python"\] scopes: \["editor"\]
