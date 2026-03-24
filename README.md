# AI-Assisted-Software-Development-Course

Files suppoting the CODE Training AI Assisted Software Development not included in the public repos.-Course
This repo was created for the AIASD CODE Training Course

## Guidance & Instructions

- [`.github/instructions/marp-slides.instructions.md`](.github/instructions/marp-slides.instructions.md) — Instructions and templates for creating Marp slide files. Slides created using these instructions must be placed in `slides/marp/` and include AI provenance metadata linking to an `ai-logs/` conversation (see `.github/instructions/ai-assisted-output.instructions.md` and `.github/instructions/copilot-instructions.md`).

## Useful Keybinding

This keybinding opens markdown files in a side-by-side preview and copies the editor to a new window for easier review:

```json
{
  "key": "ctrl+shift+alt+x",
  "command": "extension.multiCommand.execute",
  "args": {
    "sequence": [
      "markdown.showPreviewToSide",
      "workbench.action.copyEditorToNewWindow"
    ]
  },
  "when": "editorLangId == mdc"
}
```

This requires the `multiCommand` extension and is configured to trigger when editing Marp markdown files (`.mdc`).

## Prompts

[x] #file:check-context.prompt.md apply this prompt to files in the .github/instructions folder

[x] Update the readme.md file with current state of the application. Include mermaid C4 diagrams.

[x] #codebase analyze the code and report any deviations from the instructions in the .github/instructions folder

[x] Looking at the current #codebase, what tests are need and missing?

[x] Looking at the current #codebase, what tests are need and missing in order to verify a successful migration to Vue 3.4?

[x] Looking at the current #codebase, what needs refactoring?

[x] Looking at the current #codebase, what are security concerns? Create issues from your findings.

[x] Analyze the #codebase and create github issues for any dead code you find

[x] Analyze the files in the .github/instructions folder and report where they no longer represent best practices

[ ] #codebase analyze the code and report any deviations from the instructions in the .github/instructions folder

[ ] Create tests for #file:validatorsCustom.js

[ ] Look at the current #codebase and find the bugs?

[ ] Add comprehensive error logging architecture

[ ] The two branches sonnet4 and gpt5 contain implementations of the comprehensive error logging architecture. The gpt5 implementation is in commit aafed869e3c243b758d7a89cf29f19fa70c41f8a. The sonnet4 implementation is in commit fed7e9e927e458fa95f30ef91a3bbfcb201e20ea. Review each implementation and report the pros and cons of each.

## AI-Assisted Artifacts & Provenance

This repository enforces provenance and logging for any AI-assisted outputs (code, docs, diagrams, tests, data).

### Guidance & Instructions

- [`.github/instructions/ai-assisted-output.instructions.md`](.github/instructions/ai-assisted-output.instructions.md) — How to generate AI-assisted outputs with required metadata, logging, and CI enforcement
- [`.github/instructions/ai-business-rules-to-slices.instructions.md`](.github/instructions/ai-business-rules-to-slices.instructions.md) — **AI Assistants**: Explicit procedures for analyzing business rules, extracting use cases, and designing vertical slices ([chat log](ai-logs/2025/10/22/business-rules-vertical-slices-20251022/conversation.md))
- [`.github/instructions/ai-vertical-slice-implementation.instructions.md`](.github/instructions/ai-vertical-slice-implementation.instructions.md) — **AI Assistants**: Comprehensive guide for generating vertical slice code with rules, templates, and validation checklists ([chat log](ai-logs/2025/10/22/ai-vertical-slice-implementation-20251022/conversation.md))
- [`.github/instructions/business-rules-to-vertical-slices.instructions.md`](.github/instructions/business-rules-to-vertical-slices.instructions.md) — **Developers**: Guide for analyzing business requirements, extracting rules, and designing implementable vertical slices ([chat log](ai-logs/2025/10/22/business-rules-vertical-slices-20251022/conversation.md))
- [`.github/instructions/copilot-instructions.md`](.github/instructions/copilot-instructions.md) — **GitHub Copilot Users Start Here** - Comprehensive Copilot-specific guidance for model format, conversation logging, and quality standards ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))
- [`.github/instructions/create-chatmode.instructions.md`](.github/instructions/create-chatmode.instructions.md) — Comprehensive authoring guidelines for creating custom GitHub Copilot chat modes ([chat log](ai-logs/2025/10/21/create-chatmode-instructions-20251021/conversation.md))
- [`.github/instructions/create-prompt.instructions.md`](.github/instructions/create-prompt.instructions.md) — Comprehensive guidelines for authoring effective repository prompts ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))
- [`.github/instructions/instruction-prompt.instructions.md`](.github/instructions/instruction-prompt.instructions.md) — Requirements for prompts that generate instruction files ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))
- [`.github/instructions/vertical-slice-architecture.instructions.md`](.github/instructions/vertical-slice-architecture.instructions.md) — Comprehensive guide for implementing vertical slice architecture with feature-centric code organization ([chat log](ai-logs/2025/10/22/vertical-slice-instructions-20251022/conversation.md))

### Custom GitHub Copilot Chat Modes

Custom chat modes are specialized AI assistants that extend GitHub Copilot's capabilities for specific domains and workflows. Activate with `@<modename>` in GitHub Copilot chat.

- [`.github/chatmodes/DocumentationUpdater.chatmode.md`](.github/chatmodes/DocumentationUpdater.chatmode.md) — Documentation maintenance, accuracy verification, and continuous improvement ([chat log](ai-logs/2025/10/22/create-documentation-updater-chatmode-20251022/conversation.md))
- [`.github/chatmodes/DocDesignArchitect.chatmode.md`](.github/chatmodes/DocDesignArchitect.chatmode.md) — Technical documentation, diagramming with Mermaid, and readability improvements
- [`.github/chatmodes/SecurityAnalyzer.chatmode.md`](.github/chatmodes/SecurityAnalyzer.chatmode.md) — Code security analysis, vulnerability detection, and automated issue creation
- [`.github/chatmodes/codebase-explorer.chatmode.md`](.github/chatmodes/codebase-explorer.chatmode.md) — Rapid codebase understanding and evaluation
- [`.github/chatmodes/GitFlowStrategist.chatmode.md`](.github/chatmodes/GitFlowStrategist.chatmode.md) — Branching policies, merge style enforcement, and CI/CD hygiene

### Meta-Prompts (Prompt Generators)

- [`.github/copilot/Promptfiles/meta/create-instruction-prompt.prompt.md`](.github/copilot/Promptfiles/meta/create-instruction-prompt.prompt.md) — Generates new instruction-generating prompts with AI provenance built-in ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))

### Instruction-Generating Prompts

- [`.github/copilot/Promptfiles/create-chatmode-instructions.prompt.md`](.github/copilot/Promptfiles/create-chatmode-instructions.prompt.md) — Generates comprehensive authoring guidelines for creating custom GitHub Copilot chat modes

### Notable Artifacts

- **Commit Workspace Changes in Logical Groups Prompt** ([`.github/prompts/commit-workspace-changes-logical-groups.prompt.md`](.github/prompts/commit-workspace-changes-logical-groups.prompt.md))
  - Reusable operational prompt that inspects workspace diffs, creates intent-based commit groupings, stages each group safely, and emits focused commit messages
  - Includes guardrails for non-destructive Git usage, staged-file validation steps, and a standardized completion report format
  - Provenance: [Chat log](ai-logs/2026/03/24/commit-workspace-changes-logical-groups-20260324/conversation.md) | [Summary](ai-logs/2026/03/24/commit-workspace-changes-logical-groups-20260324/summary.md)

- **Managing Instruction Files & Context Windows** ([`slides/marp/managing-instruction-files-context-windows.deck.md`](slides/marp/managing-instruction-files-context-windows.deck.md))
  - 7-slide Marp deck covering instruction sharing strategy, scoped application patterns, context monitoring, and token tracking
  - Includes an operational workflow blueprint and implementation checklist
  - Provenance: [Chat log](ai-logs/2026/03/17/managing-instruction-files-context-windows-20260317/conversation.md) | [Summary](ai-logs/2026/03/17/managing-instruction-files-context-windows-20260317/summary.md)

- **Exercise: Technology Inventory & Instruction Generation** ([`slides/marp/exercise-technology-inventory-instruction-generation.deck.md`](slides/marp/exercise-technology-inventory-instruction-generation.deck.md))
  - Exercise slide covering technology inventory creation, concurrent background sessions, simultaneous instruction generation, and session management workflows
  - Template-aligned with objectives, activities, success criteria, and facilitator notes
  - Provenance: [Chat log](ai-logs/2026/03/17/exercise-technology-inventory-instruction-generation-20260317/conversation.md) | [Summary](ai-logs/2026/03/17/exercise-technology-inventory-instruction-generation-20260317/summary.md)

- **Exercise: Creating Prompt Files** ([`slides/marp/exercise-creating-prompt-files.deck.md`](slides/marp/exercise-creating-prompt-files.deck.md))
  - Exercise slide covering baseline prompt execution, guided rerun with instruction files, and structured comparison of the resulting outputs
  - Emphasizes prompt structure, context isolation, reproducibility, and the impact of instruction files on output quality
  - Provenance: [Chat log](ai-logs/2026/03/19/exercise-creating-prompt-files-20260319/conversation.md) | [Summary](ai-logs/2026/03/19/exercise-creating-prompt-files-20260319/summary.md)

- **Exercise: Create, Test, and Use a Local MCP Server** ([`slides/marp/exercise-mcp-server-create-test-use.deck.md`](slides/marp/exercise-mcp-server-create-test-use.deck.md))
  - Hands-on exercise slide guiding students through building a PowerShell MCP server, validating it with an end-to-end test script, and invoking it through Copilot
  - Covers MCP JSON-RPC method flow (`initialize`, `tools/list`, `tools/call`), smoke-test validation, and local `.mcp.json` integration
  - Provenance: [Chat log](ai-logs/2026/03/21/exercise-mcp-server-create-test-use-20260321/conversation.md) | [Summary](ai-logs/2026/03/21/exercise-mcp-server-create-test-use-20260321/summary.md)

- **Exercise: Create and Use a Custom Agent** ([`slides/marp/exercise-create-and-use-custom-agent.deck.md`](slides/marp/exercise-create-and-use-custom-agent.deck.md))
  - Hands-on exercise slide guiding students through creating a repository-scoped custom agent, refining role boundaries, and running it in Copilot Chat
  - Covers agent file structure, tool-scope decisions, and practical output validation through a targeted prompt
  - Provenance: [Chat log](ai-logs/2026/03/21/exercise-create-and-use-custom-agent-20260321/conversation.md) | [Summary](ai-logs/2026/03/21/exercise-create-and-use-custom-agent-20260321/summary.md)

- **VS Code Copilot Agents Overview** ([`slides/marp/_vscode-copilot-agents-overview.deck.md`](slides/marp/_vscode-copilot-agents-overview.deck.md))
  - Multi-slide Marp deck covering the agent model in VS Code, agent types, local versus cloud workflows, and practical task selection guidance
  - Explains how Copilot agents differ from inline suggestions and when to use interactive, background, cloud, or third-party agent flows
  - Provenance: [Chat log](ai-logs/2026/02/06/vscode-agents-slides-20260206/conversation.md) | [Summary](ai-logs/2026/02/06/vscode-agents-slides-20260206/summary.md)

- **Exercise: Create and Use a Custom Skill** ([`slides/marp/exercise-create-and-use-custom-skill.deck.md`](slides/marp/exercise-create-and-use-custom-skill.deck.md))
  - Hands-on exercise slide guiding students through creating a repository skill, refining trigger phrases, and using it with a matching Copilot prompt
  - Covers `.github/skills/<name>/SKILL.md`, description-driven relevance matching, and procedural output design for repeatable slide review workflows
  - Provenance: [Chat log](ai-logs/2026/03/21/exercise-create-and-use-custom-skill-20260321/conversation.md) | [Summary](ai-logs/2026/03/21/exercise-create-and-use-custom-skill-20260321/summary.md)

- **Creating Instruction Files from Prompts** ([`slides/marp/creating-instruction-files-from-prompts.deck.md`](slides/marp/creating-instruction-files-from-prompts.deck.md))
  - 7-slide Marp deck covering prompt execution, generated instruction review, inference as a drafting accelerator, and prompt-first refinement strategy
  - Emphasizes regenerating from the prompt to preserve source control history, reproducibility, and provenance quality
  - Provenance: [Chat log](ai-logs/2026/03/20/creating-instruction-files-from-prompts-20260320/conversation.md) | [Summary](ai-logs/2026/03/20/creating-instruction-files-from-prompts-20260320/summary.md)

- **Technology Stack Instruction Files** ([`slides/marp/technology-stack-instruction-files.deck.md`](slides/marp/technology-stack-instruction-files.deck.md))
  - 7-slide Marp deck covering requirements-based instruction generation, review checklists, and multi-model evaluation for HTML5, CSS3, and JavaScript guidance
  - Explains how teams draft standards quickly, critique them systematically, and use multiple models to improve quality during the foundation phase
  - Provenance: [Chat log](ai-logs/2026/03/21/technology-stack-instruction-files-20260321/conversation.md) | [Summary](ai-logs/2026/03/21/technology-stack-instruction-files-20260321/summary.md)

- **Organizational vs. Repository Instruction Files Deck** ([`slides/marp/organizational-vs-repository-instruction-files.deck.md`](slides/marp/organizational-vs-repository-instruction-files.deck.md))
  - 7-slide Marp deck covering enterprise-tier capabilities, path-scoped instruction files, and folder-level technology-specific rules
  - Includes layering and precedence guidance for multi-level instruction governance
  - Provenance: [Chat log](ai-logs/2026/03/17/organizational-vs-repository-instruction-files-20260317/conversation.md) | [Summary](ai-logs/2026/03/17/organizational-vs-repository-instruction-files-20260317/summary.md)

- **Feature Flags and Test Suites** ([`slides/marp/feature-flags-and-test-suites.deck.md`](slides/marp/feature-flags-and-test-suites.deck.md))
  - Marp deck covering feature flags for work-in-progress, As-Is vs. To-Be test suites, safe deployment gates, and AI-assisted flag retirement
  - Includes speaker notes for delivery and operational guidance for CI pipeline separation
  - Provenance: [Chat log](ai-logs/2026/03/19/feature-flags-test-suites-20260319/conversation.md) | [Summary](ai-logs/2026/03/19/feature-flags-test-suites-20260319/summary.md)

- **Safety Measures & Best Practices** ([`slides/marp/safety-measures-best-practices.deck.md`](slides/marp/safety-measures-best-practices.deck.md))
  - 7-slide Marp deck covering safety nets, review discipline for AI-generated code, signal-vs-coverage testing guidance, safe feature-flag removal, small change sets, and Azure DevOps MCP-assisted PR review support
  - Frames AI as an eager knowledgeable junior developer and closes with an actionable safety checklist for teams
  - Provenance: [Chat log](ai-logs/2026/03/22/safety-measures-best-practices-20260322/conversation.md) | [Summary](ai-logs/2026/03/22/safety-measures-best-practices-20260322/summary.md)

- **Effective Prompts for Technical Debt** ([`slides/marp/effective-prompts-for-technical-debt.deck.md`](slides/marp/effective-prompts-for-technical-debt.deck.md))
  - Marp deck covering structured technical debt prompts, GitHub issue workflow, Copilot-assisted issue handling, and prompt components for safe remediation
  - Includes speaker notes and a reusable prompt template covering constraints, tests, docs, and provenance expectations
  - Provenance: [Chat log](ai-logs/2026/03/22/effective-prompts-technical-debt-20260322/conversation.md) | [Summary](ai-logs/2026/03/22/effective-prompts-technical-debt-20260322/summary.md)

- **Technical Debt Copilot Exercise Sequence** ([`slides/marp/exercise-addressing-technical-debt-with-copilot.deck.md`](slides/marp/exercise-addressing-technical-debt-with-copilot.deck.md))
  - Three-slide exercise set covering prompt authoring, GitHub issue assignment, and multi-step delegation for technical debt remediation with Copilot
  - Uses the exercise template structure with duration, objectives, activities, success criteria, and facilitator notes on every slide
  - Provenance: [Chat log](ai-logs/2026/03/22/exercise-technical-debt-copilot-workflows-20260322/conversation.md) | [Summary](ai-logs/2026/03/22/exercise-technical-debt-copilot-workflows-20260322/summary.md)

- **Repository Fork and Clone Exercise Deck** ([`slides/marp/exercise-fork-and-clone-repositories.deck.md`](slides/marp/exercise-fork-and-clone-repositories.deck.md))
  - Three-slide exercise deck covering course repository forking, brownfield branch setup, PAT configuration, and multi-repo fork validation
  - Uses the exercise template structure with objectives, activities, success criteria, command examples, and facilitator notes for each exercise
  - Provenance: [Chat log](ai-logs/2026/03/22/exercise-repository-fork-clone-deck-20260322/conversation.md) | [Summary](ai-logs/2026/03/22/exercise-repository-fork-clone-deck-20260322/summary.md)

- **GitHub Copilot VS Code Workflows Exercise Deck** ([`slides/marp/exercise-github-copilot-vscode-workflows.deck.md`](slides/marp/exercise-github-copilot-vscode-workflows.deck.md))
  - Four-slide exercise deck covering Copilot onboarding, context management, chat workflow organization, and Ask/Edit/Agent mode selection
  - Uses the exercise template structure with objectives, activities, success criteria, and facilitator notes for each lab sequence
  - Provenance: [Chat log](ai-logs/2026/03/22/exercise-github-copilot-vscode-workflows-20260322/conversation.md) | [Summary](ai-logs/2026/03/22/exercise-github-copilot-vscode-workflows-20260322/summary.md)

- **Evergreen Software Development Exercise Deck** ([`slides/marp/evergreen-software-development-exercise-deck.deck.md`](slides/marp/evergreen-software-development-exercise-deck.deck.md))
  - Two exercise slides covering evergreen core principles and common failure modes
  - Template-aligned structure with duration, objectives, activities, success criteria, and speaker notes
  - Provenance: [Chat log](ai-logs/2026/03/16/evergreen-exercise-deck-20260316/conversation.md) | [Summary](ai-logs/2026/03/16/evergreen-exercise-deck-20260316/summary.md)

- **GitHub Copilot Skills: A Practical Introduction** ([`slides/marp/github-copilot-skills-practical-introduction.deck.md`](slides/marp/github-copilot-skills-practical-introduction.deck.md))
  - 12-slide Marp deck covering skill structure, `SKILL.md` anatomy, loading behavior, authoring practices, and common enterprise use cases
  - Explains how Copilot Skills differ from promptfiles, custom instructions, and chat modes while positioning them as procedural workflow modules
  - Provenance: [Chat log](ai-logs/2026/03/21/github-copilot-skills-practical-introduction-20260321/conversation.md) | [Summary](ai-logs/2026/03/21/github-copilot-skills-practical-introduction-20260321/summary.md)

- **Best Practices and Q&A: Custom Agents** ([`slides/marp/best-practices-and-qa-custom-agents.deck.md`](slides/marp/best-practices-and-qa-custom-agents.deck.md))
  - 7-slide Marp deck covering agent design best practices, least-privilege tool strategy, team sharing, examples, and rollout validation
  - Explains how to keep agents narrowly scoped, iteratively improved, and safe to share across teams or organizations
  - Provenance: [Chat log](ai-logs/2026/03/21/best-practices-and-qa-custom-agents-20260321/conversation.md) | [Summary](ai-logs/2026/03/21/best-practices-and-qa-custom-agents-20260321/summary.md)

- **Implementation Plan Prioritization** ([`slides/marp/implementation-plan-prioritization.deck.md`](slides/marp/implementation-plan-prioritization.deck.md))
  - Marp deck covering security audit findings, impact/effort prioritization, visible technical-debt tracking, and Phase Zero security planning
  - Frames prioritization as the bridge between backlog generation and safe implementation sequencing for brownfield work
  - Provenance: [Chat log](ai-logs/2026/03/21/ai-prioritization-brownfield-protection-20260321/conversation.md) | [Summary](ai-logs/2026/03/21/ai-prioritization-brownfield-protection-20260321/summary.md)

- **Vertical Slice Implementation** ([`slides/marp/vertical-slice-implementation-webcat.deck.md`](slides/marp/vertical-slice-implementation-webcat.deck.md))
  - Marp deck covering first-slice setup, prompt-versus-issue scope checks, Copilot-assisted live coding, and verification strategy for the "Implement Foundational WebCat" slice
  - Highlights `webcat-frontend` organization decisions and the shift from manual verification toward automated testing
  - Provenance: [Chat log](ai-logs/2026/03/22/vertical-slice-implementation-webcat-20260322/conversation.md) | [Summary](ai-logs/2026/03/22/vertical-slice-implementation-webcat-20260322/summary.md)

- **Prompt Authoring Instructions** ([`.github/instructions/create-prompt.instructions.md`](.github/instructions/create-prompt.instructions.md))
  - Comprehensive guidelines for creating effective, well-structured repository prompts
  - Generated from: [`.github/copilot/Promptfiles/prompt-file.instructions.prompt.md`](.github/copilot/Promptfiles/prompt-file.instructions.prompt.md)
  - Provenance: [Chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md)

- **Instruction Validation Report** ([`validation-report-20251015-212137.md`](validation-report-20251015-212137.md))
  - Comprehensive analysis of instruction file conflicts and inconsistencies
  - Identifies 7 issues (1 high, 4 medium, 3 low severity) with fixes applied to critical issues
  - Generated from: [`.github/copilot/Promptfiles/meta/validate-and-improve-instructions.prompt.md`](.github/copilot/Promptfiles/meta/validate-and-improve-instructions.prompt.md)
  - Status: Critical fixes applied (Option C executed - 4 issues resolved, 3 deferred for refactoring)
  - Provenance: [Chat log](ai-logs/2025/10/15/validate-improve-instructions-20251015-212137/conversation.md) | [Summary](ai-logs/2025/10/15/validate-improve-instructions-20251015-212137/summary.md)
  - Verification: [Fixes verified 2025-10-16](validation-fixes-verified-20251016.md) ([chat log](ai-logs/2025/10/16/resume-validation-fixes-20251016/conversation.md))

- **CQRS Architecture Slides** ([`slides/marp/cqrs-architecture.deck.md`](slides/marp/cqrs-architecture.deck.md))
  - Comprehensive presentation explaining Command Query Responsibility Segregation (CQRS) pattern
  - Covers when to use CQRS, core principles, implementation examples, and migration strategies
  - Includes detailed speaker notes for effective delivery
  - Provenance: [Chat log](ai-logs/2026/02/07/cqrs-architecture-slides-20260207/conversation.md)

- **Vertical Slicing Architecture Introduction** ([`slides/marp/vertical-slicing-architecture-introduction.deck.md`](slides/marp/vertical-slicing-architecture-introduction.deck.md))
  - 7-slide Marp deck introducing feature-based architecture, layered versus slice-oriented structure, and the maintainability benefits of localized change
  - Covers developer experience improvements, team collaboration, testing strategy, and the introductory CQRS relationship
  - Includes Mermaid visuals and detailed speaker notes for classroom delivery
  - Provenance: [Chat log](ai-logs/2026/03/21/vertical-slicing-architecture-introduction-20260321/conversation.md) | [Summary](ai-logs/2026/03/21/vertical-slicing-architecture-introduction-20260321/summary.md)

- **Instruction File ApplyTo Patterns Slides** ([`slides/marp/instruction-file-applyto-patterns.deck.md`](slides/marp/instruction-file-applyto-patterns.deck.md))
  - 13-slide Marp presentation explaining glob pattern matching for instruction file applyTo fields
  - Covers universal patterns, file extension matching, directory-specific patterns, and best practices
  - Includes comprehensive speaker notes (1-3 minutes per slide) with timing, examples, and audience interaction cues
  - Features real-world examples from this repository, common pitfalls, testing strategies, and decision frameworks
  - Provenance: [Chat log](ai-logs/2026/03/03/applyto-patterns-marp-deck-20260303/conversation.md) | [Summary](ai-logs/2026/03/03/applyto-patterns-marp-deck-20260303/summary.md)

## Utility Scripts

This repository includes utility scripts for repository management and maintenance:

### Branch Change Tracking

Identify branches with changes that haven't been merged to main:

- **Bash:** [`scripts/check_unmerged_branches.sh`](scripts/check_unmerged_branches.sh) - For Linux/Mac/WSL
- **PowerShell:** [`scripts/check_unmerged_branches.ps1`](scripts/check_unmerged_branches.ps1) - For Windows/PowerShell Core

**Usage:**

```bash
# Bash
./scripts/check_unmerged_branches.sh

# PowerShell
.\scripts\check_unmerged_branches.ps1
```

See [`scripts/README.md`](scripts/README.md) for detailed documentation and configuration options.

### Security Issue Management

Scripts for managing GitHub security issues:

- `close_duplicate_security_issues.ps1` - Close duplicate security issues
- `close_latest_security_issues.ps1` - Close latest security issues
- `close_new_security_issues.ps1` - Close new security issues
- `close_resolved_security_issues.ps1` - Close resolved security issues
- `emergency_security_cleanup.ps1` - Emergency security cleanup

### Local MCP Server (PowerShell)

- `scripts/mcp/simple-mcp-server.ps1` - Simple local MCP server exposing an `echo` tool over stdio
- `scripts/mcp/test-simple-mcp-server.ps1` - End-to-end test script that validates initialize, tools/list, and tools/call
- `.mcp.json` - Workspace MCP configuration that launches the PowerShell MCP server

For run and test commands, see [`scripts/README.md`](scripts/README.md).
