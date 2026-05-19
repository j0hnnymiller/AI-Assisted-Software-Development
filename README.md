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
- [`.github/instructions/business-rules-to-slices.instructions.md`](.github/instructions/business-rules-to-slices.instructions.md) — **AI Assistants**: Explicit procedures for analyzing business rules, extracting use cases, and designing vertical slices ([chat log](ai-logs/2025/10/22/business-rules-vertical-slices-20251022/conversation.md))
- [`.github/instructions/vertical-slice.instructions.md`](.github/instructions/vertical-slice.instructions.md) — **AI Assistants**: Comprehensive guide for generating vertical slice code with rules, templates, and validation checklists ([chat log](ai-logs/2025/10/22/ai-vertical-slice-implementation-20251022/conversation.md))
- [`.github/instructions/business-rules-to-vertical-slices.instructions.md`](.github/instructions/business-rules-to-vertical-slices.instructions.md) — **Developers**: Guide for analyzing business requirements, extracting rules, and designing implementable vertical slices ([chat log](ai-logs/2025/10/22/business-rules-vertical-slices-20251022/conversation.md))
- [`.github/instructions/copilot-instructions.md`](.github/instructions/copilot-instructions.md) — **GitHub Copilot Users Start Here** - Comprehensive Copilot-specific guidance for model format, conversation logging, and quality standards ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))
- [`.github/instructions/github-cli.instructions.md`](.github/instructions/github-cli.instructions.md) — Comprehensive guidance for using GitHub CLI effectively in development workflows, including authentication, repository operations, PR management, and automation ([chat log](ai-logs/2026/02/06/github-cli-instructions-20260206/conversation.md))
- [`.github/instructions/cqrs-architecture.instructions.md`](.github/instructions/cqrs-architecture.instructions.md) — CQRS architecture guidance for command/query separation, consistency, and implementation checklists ([chat log](ai-logs/2026/02/07/cqrs-architecture-instructions-20260207/conversation.md))
- [`.github/instructions/chatmode-file.instructions.md`](.github/instructions/chatmode-file.instructions.md) — Comprehensive authoring guidelines for creating custom GitHub Copilot chat modes ([chat log](ai-logs/2025/10/21/create-chatmode-instructions-20251021/conversation.md))
- [`.github/instructions/create-prompt.instructions.md`](.github/instructions/create-prompt.instructions.md) — Comprehensive guidelines for authoring effective repository prompts ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))
- [`.github/instructions/instruction-prompt-files.instructions.md`](.github/instructions/instruction-prompt-files.instructions.md) — Requirements for creating prompts that generate instruction files ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))
- [`.github/instructions/vertical-slice-architecture.instructions.md`](.github/instructions/vertical-slice-architecture.instructions.md) — Comprehensive guide for implementing vertical slice architecture with feature-centric code organization ([chat log](ai-logs/2025/10/22/vertical-slice-instructions-20251022/conversation.md))

### Custom GitHub Copilot Chat Modes

Custom chat modes are specialized AI assistants that extend GitHub Copilot's capabilities for specific domains and workflows. Activate with `@<modename>` in GitHub Copilot chat.

#### Role-Based Chat Modes (Generated from Personas)

- [`.github/chatmodes/product-manager.chatmode.md`](.github/chatmodes/product-manager.chatmode.md) — Requirements translation, stakeholder communication, and business alignment for product management workflows
- [`.github/chatmodes/solution-architect.chatmode.md`](.github/chatmodes/solution-architect.chatmode.md) — System design, architecture patterns, and technology evaluation for enterprise solutions
- [`.github/chatmodes/senior-developer.chatmode.md`](.github/chatmodes/senior-developer.chatmode.md) — Advanced code generation, debugging expertise, performance optimization, and technical mentorship
- [`.github/chatmodes/technical-writer.chatmode.md`](.github/chatmodes/technical-writer.chatmode.md) — Documentation creation, content organization, and multi-format publishing for user-focused technical content
- [`.github/chatmodes/security-reviewer.chatmode.md`](.github/chatmodes/security-reviewer.chatmode.md) — Comprehensive security analysis, vulnerability detection, and compliance validation for secure systems
- [`.github/chatmodes/devops-engineer.chatmode.md`](.github/chatmodes/devops-engineer.chatmode.md) — Infrastructure automation, CI/CD pipeline optimization, and cloud resource management
- [`.github/chatmodes/devtest-engineer.chatmode.md`](.github/chatmodes/devtest-engineer.chatmode.md) — Test automation, quality assurance, and comprehensive performance testing strategies
- [`.github/chatmodes/site-reliability-engineer.chatmode.md`](.github/chatmodes/site-reliability-engineer.chatmode.md) — System reliability, incident response, performance monitoring, and service level management

#### Utility Chat Modes

- [`.github/chatmodes/technical-writer.chatmode.md`](.github/chatmodes/technical-writer.chatmode.md) — Documentation maintenance, accuracy verification, and continuous improvement ([chat log](ai-logs/2025/10/22/create-documentation-updater-chatmode-20251022/conversation.md))
- [`.github/chatmodes/documentation-visualizer.chatmode.md`](.github/chatmodes/documentation-visualizer.chatmode.md) — Technical documentation, diagramming with Mermaid, and readability improvements
- [`.github/chatmodes/security-expert.chatmode.md`](.github/chatmodes/security-expert.chatmode.md) — Code security analysis, vulnerability detection, and automated issue creation
- [`.github/chatmodes/codebase-explorer.chatmode.md`](.github/chatmodes/codebase-explorer.chatmode.md) — Rapid codebase understanding and evaluation
- [`.github/chatmodes/git-expert.chatmode.md`](.github/chatmodes/git-expert.chatmode.md) — Branching policies, merge style enforcement, and CI/CD hygiene

### Custom GitHub Copilot Agents

- [`.github/agents/product-manager.agent.md`](.github/agents/product-manager.agent.md) — Product strategy, requirements analysis, and stakeholder alignment ([chat log](ai-logs/2026/02/12/create-custom-agents-20260212/conversation.md))
- [`.github/agents/solution-architect.agent.md`](.github/agents/solution-architect.agent.md) — System design, architecture patterns, and decision support ([chat log](ai-logs/2026/02/12/create-custom-agents-20260212/conversation.md))
- [`.github/agents/senior-developer.agent.md`](.github/agents/senior-developer.agent.md) — Code quality, best practices, and implementation guidance ([chat log](ai-logs/2026/02/12/create-custom-agents-20260212/conversation.md))
- [`.github/agents/technical-writer.agent.md`](.github/agents/technical-writer.agent.md) — Documentation, API references, and user guidance ([chat log](ai-logs/2026/02/12/create-custom-agents-20260212/conversation.md))
- [`.github/agents/security-reviewer.agent.md`](.github/agents/security-reviewer.agent.md) — Security analysis, vulnerability detection, and compliance review ([chat log](ai-logs/2026/02/12/create-custom-agents-20260212/conversation.md))
- [`.github/agents/devops-engineer.agent.md`](.github/agents/devops-engineer.agent.md) — CI/CD, infrastructure automation, and deployment strategy ([chat log](ai-logs/2026/02/12/create-custom-agents-20260212/conversation.md))
- [`.github/agents/devtest-engineer.agent.md`](.github/agents/devtest-engineer.agent.md) — Test automation, QA strategy, and coverage guidance ([chat log](ai-logs/2026/02/12/create-custom-agents-20260212/conversation.md))
- [`.github/agents/sre-engineer.agent.md`](.github/agents/sre-engineer.agent.md) — Site reliability, monitoring, and incident response ([chat log](ai-logs/2026/02/12/create-custom-agents-20260212/conversation.md))

### Meta-Prompts (Prompt Generators)

- [`.github/prompts/meta/create-instruction-files-prompt-file.prompt.md`](.github/prompts/meta/create-instruction-files-prompt-file.prompt.md) — Generates new instruction-generating prompts with AI provenance built-in ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))

### Instruction-Generating Prompts

- [`.github/prompts/create-chatmode-instructions-file.prompt.md`](.github/prompts/create-chatmode-instructions-file.prompt.md) — Generates comprehensive authoring guidelines for creating custom GitHub Copilot chat modes
- [`.github/prompts/merge-marp-decks.prompt.md`](.github/prompts/merge-marp-decks.prompt.md) — Merges individual Marp slide decks from `slides/marp/` into a single combined presentation ([chat log](ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md))

### Notable Artifacts

- **AI-Assisted MFC to WPF Conversions Slides** ([`slides/marp/ai-assisted-mfc-to-wpf-conversions.deck.md`](slides/marp/ai-assisted-mfc-to-wpf-conversions.deck.md))
  - Marp slide deck for planning and executing MFC-to-WPF migration using AI-assisted workflows
  - Covers both whole-application conversion and module-by-module migration patterns
  - Includes architecture mapping, quality gates, estimation heuristics, and presenter notes on every slide
  - Provenance: [Chat log](ai-logs/2026/05/04/mfc-to-wpf-conversion-deck-20260504/conversation.md) | [Summary](ai-logs/2026/05/04/mfc-to-wpf-conversion-deck-20260504/summary.md)

- **Thursday GE Merged Course Deck** ([`slides/merged/ge/aiasd-311-thursday.ge-draft.md`](slides/merged/ge/aiasd-311-thursday.ge-draft.md))
  - Manifest-driven combined Marp deck assembled from `slides/manifests/ge/aiasd-311-thursday.ge.manifest.md`
  - Includes section divider slides, module progression context, and speaker notes coverage across all slide blocks
  - Provenance: [Chat log](ai-logs/2026/05/04/merge-marp-thursday-ge-20260504/conversation.md) | [Summary](ai-logs/2026/05/04/merge-marp-thursday-ge-20260504/summary.md)

- **VTT Content Summarizer Promptfile** ([`.github/prompts/summarize-vti-content.prompt.md`](.github/prompts/summarize-vti-content.prompt.md))
  - Analyzes VTT (Video Text Track) files from class recordings and generates structured summaries
  - Extracts timing information, section breakdowns, key topics, and action items
  - Includes sample files: [VTT input](past-class-recordings/2026-02/AI-Assisted%20Software%20Development%20with%20GitHub%20Copilot%20(Mon%20Afternoon).vtt) | [Generated summary](past-class-recordings/2026-02/AI-Assisted%20Software%20Development%20with%20GitHub%20Copilot%20(Mon%20Afternoon)-summary.md)
  - Documentation: [Usage Guide](past-class-recordings/USAGE.md) | [Live Demo](past-class-recordings/DEMO.md)
  - Provenance: [Chat log](ai-logs/2026/02/17/create-vtt-summarizer-20260217/conversation.md)

- **VS Code Copilot Agents Overview Slides** ([`slides/marp/vscode-copilot-agents-overview.deck.md`](slides/marp/vscode-copilot-agents-overview.deck.md))
  - Comprehensive Marp slide deck covering VS Code Copilot Agents ecosystem with interactive workflows
  - 12 slides with detailed speaker notes covering local, background, cloud, and third-party agents
  - Includes decision matrices, hand-off workflows, and practical implementation guidance
  - Provenance: [Chat log](ai-logs/2026/02/06/vscode-agents-slides-20260206/conversation.md) | [Summary](ai-logs/2026/02/06/vscode-agents-slides-20260206/summary.md)

- **GitHub Worktrees Guide Slides** ([`slides/marp/github-worktrees-guide.deck.md`](slides/marp/github-worktrees-guide.deck.md))
  - Comprehensive Marp slide deck teaching parallel development with Git worktrees
  - 12 slides covering introduction, essential commands, practical workflows, hands-on exercises, and best practices
  - Includes detailed speaker notes, troubleshooting guidance, and resources for continued learning
  - Provenance: [Chat log](ai-logs/2026/02/06/github-worktrees-slides-20260206/conversation.md) | [Summary](ai-logs/2026/02/06/github-worktrees-slides-20260206/summary.md)

- **Creating Custom Agents Slides** ([`slides/marp/creating-custom-agents.deck.md`](slides/marp/creating-custom-agents.deck.md))
  - Comprehensive Marp slide deck teaching how to create specialized GitHub Copilot custom agents
  - 12 slides covering overview, creation workflows across platforms (GitHub, VS Code, JetBrains, Eclipse, Xcode), configuration, examples, usage, and best practices
  - Includes extensive speaker notes with timing guidance, delivery instructions, audience interaction points, and Q&A preparation
  - Provenance: [Chat log](ai-logs/2026/02/12/create-custom-agents-marp-20260212/conversation.md) | [Summary](ai-logs/2026/02/12/create-custom-agents-marp-20260212/summary.md)

- **Code Explanation and Analysis Slides** ([`slides/marp/code-explanation-and-analysis.deck.md`](slides/marp/code-explanation-and-analysis.deck.md))
  - Marp slide deck for Section 10 of the AI-Assisted Software Development course covering code explanation and test coverage gap analysis
  - 11 slides covering inline chat (Ctrl+I), right-click explain, test code understanding, coverage report generation (calculator service example), gap identification, prioritized implementation plans, and hands-on exercises
  - Includes comprehensive speaker notes with timing guidance, live demo instructions, audience interaction points, and exercise facilitation tips
  - Provenance: [Chat log](ai-logs/2026/03/18/code-explanation-analysis-marp-20260318/conversation.md)
- **Merge Marp Decks Promptfile** ([`.github/prompts/merge-marp-decks.prompt.md`](.github/prompts/merge-marp-decks.prompt.md))
  - Defines the discover→strip→assemble workflow for merging `slides/marp/*.deck.md` into a combined presentation
  - Includes acceptance criteria: all decks represented, section dividers, speaker notes on every slide, valid front matter
  - Provenance: [Chat log](ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md) | [Summary](ai-logs/2026/03/18/merge-marp-decks-20260318/summary.md)

- **AI-Assisted Output Slides** ([`slides/marp/ai-assisted-output.deck.md`](slides/marp/ai-assisted-output.deck.md))
  - 10-slide Marp deck on provenance metadata, placement policy, logging workflow, quality gates, and CI enforcement
  - Sourced from `.github/instructions/ai-assisted-output.instructions.md`
  - Provenance: [Chat log](ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md)

- **CQRS Architecture Slides** ([`slides/marp/cqrs-architecture.deck.md`](slides/marp/cqrs-architecture.deck.md))
  - 12-slide Marp deck on when to use CQRS, core principles, architecture components, consistency strategies, anti-patterns, and migration
  - Sourced from `.github/instructions/cqrs-architecture.instructions.md`
  - Provenance: [Chat log](ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md)

- **Dependency Management Policy Slides** ([`slides/marp/dependency-management-policy.deck.md`](slides/marp/dependency-management-policy.deck.md))
  - 12-slide Marp deck on risk classification, selection criteria, approval workflow, vulnerability SLAs, license compliance, and supply chain security
  - Sourced from `.github/instructions/dependency-management-policy.instructions.md`
  - Provenance: [Chat log](ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md)

- **GitHub CLI Slides** ([`slides/marp/github-cli.deck.md`](slides/marp/github-cli.deck.md))
  - 10-slide Marp deck on issue management, PR workflows, Actions monitoring, code review, and CI/CD integration
  - Sourced from `.github/instructions/github-cli.instructions.md`
  - Provenance: [Chat log](ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md)

- **Business Rules to Vertical Slices** ([`slides/marp/business-rules-to-slices.deck.md`](slides/marp/business-rules-to-slices.deck.md))
  - 10-slide Marp deck on analysis workflow, rule types, use case identification, feature boundary tests, and vertical slice design
  - Sourced from `.github/instructions/business-rules-to-slices.instructions.md`
  - Provenance: [Chat log](ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md)

- **AI-Assisted Dev Overview** ([`slides/marp/ai-assisted-dev-overview.deck.md`](slides/marp/ai-assisted-dev-overview.deck.md))
  - 62-slide combined Marp deck merging all 6 individual module presentations with section divider slides
  - Modules: AI Output · CQRS · Dependency Management · GitHub CLI · Business Rules to Slices · Custom Agents
  - Usable as a full-day course or per-module standalone; every slide has comprehensive speaker notes
  - Provenance: [Chat log](ai-logs/2026/03/18/merge-marp-decks-20260318/conversation.md) | [Summary](ai-logs/2026/03/18/merge-marp-decks-20260318/summary.md)

- **AIASD Class 311 Monday** ([`slides/marp/aiasd-311-monday.deck.md`](slides/marp/aiasd-311-monday.deck.md))
  - Combined Marp deck for the Monday session of Class 311; ~30 slides across 5 modules with section dividers
  - Modules: AI Output · Vertical Slice Architecture · Creating Prompt Files · Dependency Management · Custom Chat Modes
  - Every slide has comprehensive speaker notes; section dividers allow standalone per-module delivery
  - Manifest: [`slides/aiasd-311-monday.yaml`](slides/aiasd-311-monday.yaml)
  - Provenance: [Chat log](ai-logs/2026/03/20/merge-marp-decks-monday-20260320/conversation.md) | [Summary](ai-logs/2026/03/20/merge-marp-decks-monday-20260320/summary.md)
- **AIASD Class 311 — Tuesday Session** ([`slides/marp/aiasd-311-tuesday.deck.md`](slides/marp/aiasd-311-tuesday.deck.md))
  - Combined Marp deck for Class 311 Tuesday, generated from manifest `slides/aiasd-311-tuesday.yaml`
  - Modules: AI Output Standards · CQRS Architecture · GitHub CLI · Business Rules to Vertical Slices · Custom Agents
  - ~35 slides with section dividers and comprehensive speaker notes on every slide
  - Provenance: [Chat log](ai-logs/2026/03/20/merge-marp-decks-aiasd-311-tuesday-20260320/conversation.md) | [Summary](ai-logs/2026/03/20/merge-marp-decks-aiasd-311-tuesday-20260320/summary.md)

- **Code Explanation and Analysis Slides** ([`slides/marp/code-explanation-and-analysis.deck.md`](slides/marp/code-explanation-and-analysis.deck.md))
  - Marp slide deck for Section 10 of the AI-Assisted Software Development course covering code explanation and test coverage gap analysis
  - 11 slides covering inline chat (Ctrl+I), right-click explain, test code understanding, coverage report generation (calculator service example), gap identification, prioritized implementation plans, and hands-on exercises
  - Includes comprehensive speaker notes with timing guidance, live demo instructions, audience interaction points, and exercise facilitation tips
  - Provenance: [Chat log](ai-logs/2026/03/18/code-explanation-analysis-marp-20260318/conversation.md)

- **Prompt Authoring Instructions** ([`.github/instructions/prompt-file.instructions.md`](.github/instructions/prompt-file.instructions.md))
  - Comprehensive guidelines for creating effective, well-structured repository prompts
  - Generated from: [`.github/prompts/create-prompt-file-instructions-file.prompt.md`](.github/prompts/create-prompt-file-instructions-file.prompt.md)
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

- **Getting Started Checklist** ([`slides/marp/getting-started-checklist.deck.md`](slides/marp/getting-started-checklist.deck.md))
  - Converted 3-slide Marp deck covering phased AI adoption steps and a high-level AI-assisted workflow from requirements to implementation
  - Preserves the extracted workflow visual and adds speaker notes for presentation use in the course slide pipeline
  - Provenance: [Chat log](ai-logs/2026/03/26/convert-getting-started-checklist-20260326/conversation.md) | [Summary](ai-logs/2026/03/26/convert-getting-started-checklist-20260326/summary.md)

- **GitHub Copilot Memory Feature** ([`slides/marp/copilot-memory-feature.deck.md`](slides/marp/copilot-memory-feature.deck.md))
  - Marp deck explaining the Copilot memory feature, including user, session, and repository memory scopes
  - Covers memory workflow, memory hygiene, and a slide-authoring example for practical application
  - Provenance: [Chat log](ai-logs/2026/04/10/copilot-memory-feature-deck-20260410/conversation.md) | [Summary](ai-logs/2026/04/10/copilot-memory-feature-deck-20260410/summary.md)

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

## Document Conversion

### Pandoc Configuration Files

Standardized document conversion configurations for slides, documentation, and presentations:

- **[`slides-to-pptx.yaml`](slides-to-pptx.yaml)** - Optimized for converting Marp slides to PowerPoint presentations
- **[`to-pdf.yaml`](to-pdf.yaml)** - Professional PDF output for slides and documentation
- **[`pandoc-defaults.yaml`](pandoc-defaults.yaml)** - Comprehensive multi-format configuration
- **[`PANDOC.md`](PANDOC.md)** - Complete usage guide with examples and customization options
- **[`templates/`](templates/)** - PowerPoint reference templates for professional formatting

**Quick Examples:**

```bash
# Convert slide deck to PowerPoint with template support
pandoc --defaults=slides-to-pptx slides/marp/github-worktrees-guide.deck.md -o github-worktrees.pptx

# Convert documentation to PDF
pandoc --defaults=to-pdf README.md -o project-overview.pdf
```

**Note**: For professional PowerPoint formatting, create a reference template in the `templates/` directory. See [`templates/README.md`](templates/README.md) for instructions.
