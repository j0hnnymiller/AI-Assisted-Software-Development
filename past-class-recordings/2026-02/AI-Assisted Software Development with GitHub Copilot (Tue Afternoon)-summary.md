# AI-Assisted Software Development with GitHub Copilot (Tue Afternoon)

## Overview

- **Total Duration**: ~01:47:45 (1 hour 47 minutes)
- **Sections**: 11
- **Format**: VTT (WebVTT)
- **Speaker**: John Miller (primary instructor)
- **Participants**: Buddy Toups, Dan Blanchard, Tom Bui, Christopher Rockwell, Stephen Childs, Boris Giterman

---

## Section 1: Introduction and Setup (Duration: 00:00:26 - 00:11:21, ~11 minutes) [ ]

### Key Topics

- Welcome and opening discussion
- AI logging practices and conversation tracking
- Discussion of organizational vs repository instruction files
- Path-scoped instruction files introduction

### Subsection 1.1: AI Logging Discussion (00:00:39 - 00:01:30)

- Buddy Toups comments on AI logging trick being "pretty neat"
- Discussion of "programming with language" concept
- John Miller emphasizes AI enables tasks previously too time-consuming

### Subsection 1.2: Organizational Instruction Files (00:07:05 - 00:11:21)

- Explanation of organizational instruction files for Business/Enterprise tiers
- Path-scoped instruction files capability discovered
- Ability to define instructions at folder level for technology-specific rules
- Example: ASP.NET project-specific instructions in subfolder
- Discussion of using sub-repos for common instruction files

---

## Section 2: Exercise Introduction - Creating Project-Specific Instruction Files (Duration: 00:11:21 - 00:18:20, ~7 minutes) [ ]

### Key Topics

- Goal: Generate project/application-specific instruction files
- Using meta prompts to scale instruction file creation
- Benefits: common structure, module-specific rules, architectural constraints

### Subsection 2.1: Creating Technology Inventory (00:13:05 - 00:15:07)

- Prompt: "Create an inventory of the technologies used in this project"
- Purpose: Identify tech stack for creating technology-specific instruction files
- Resulting inventory includes: .NET 9, C# 11+, Razor Pages, Kestrel, Bootstrap

### Subsection 2.2: Background Sessions (00:17:01 - 00:18:20)

- Demonstration of creating new chat sessions to run in background
- Allows delegation of prompt execution to background tasks
- Multiple concurrent sessions for creating different instruction files

---

## Section 3: Creating Instruction Files with Sessions (Duration: 00:18:20 - 00:26:15, ~8 minutes) [x]

### Key Topics

- Using background sessions to create multiple instruction files concurrently
- Session management interface
- Reviewing generated instruction files

### Subsection 3.1: Concurrent File Generation (00:18:40 - 00:23:40)

- Created instruction file for .NET standards and practices
- Created instruction file for Kestrel/Razor Pages
- Created instruction file for DI service layer
- Sessions shown with "in progress" status
- Approval workflow for file creation

### Subsection 3.2: Session Management (00:23:40 - 00:26:15)

- Viewing session status in sidebar
- Multiple sessions running concurrently
- Reviewing completed session outputs
- Applying or rejecting generated changes

---

## Section 4: Session vs Conversation Clarification (Duration: 00:26:15 - 00:32:00, ~6 minutes) [ ]

### Key Topics

- Distinction between sessions and conversations
- Troubleshooting session output variations

### Subsection 4.1: Sessions Explained (00:30:06 - 00:31:40)

- Same chat mode, instruction files, repo, model settings
- Session resets model's short-term memory
- Like "rebooting the assistant" vs clearing chat window
- Dan Blanchard experiences different output quality - resolved by creating new session

### Subsection 4.2: Workflow Demonstration (00:32:00 - 00:35:00)

- Copy technology inventory section
- Create new background session
- Paste prompt to generate instruction file
- Switch between sessions to review outputs

---

## Section 5: VS Code Configuration Tips (Duration: 00:35:00 - 00:40:30, ~5.5 minutes) [ ]

### Key Topics

- Keyboard shortcut configuration
- Multi-command extension for Marp slides

### Subsection 5.1: Custom Keyboard Shortcuts (00:38:00 - 00:40:30)

- Sharing custom keybinding for Marp preview
- Control+Shift+Alt+X triggers two commands sequentially
- Requires multi-command extension
- Demonstrates markdown.showPreviewToSide + workbench.action.moveEditorToNewWindow
- Language condition for markdown files

---

## Section 6: Metadata and README Updates (Duration: 00:40:30 - 00:47:15, ~7 minutes) [ ]

### Key Topics

- AI-generated files automatically update README
- Metadata requirements and provenance tracking
- Context window management with instruction files

### Subsection 6.1: Automatic README Updates (00:40:30 - 00:42:05)

- Generated instruction files trigger README updates
- AI-assisted output instructions require README entry for new files
- Shows example of instruction file entries in README

### Subsection 6.2: Context Management (00:42:05 - 00:44:00)

- Diagnostics view shows all instruction files included in context
- Discussion of context window consumption
- Introduction to agents for selective instruction file usage
- Path-scoped instruction files and "applies to" clauses

---

## Section 7: Context Analysis and Validation (Duration: 00:47:15 - 00:58:00, ~11 minutes) [ ]

### Key Topics

- Running context analysis prompt
- Identifying issues in instruction files
- Implementing recommendations

### Subsection 7.1: Identifying Issues (00:48:15 - 00:50:45)

- Unresolved git merge conflict detected
- Model-specific contradictions found
- Inconsistent operator fields identified
- Critical, high, and medium priority issues categorized

### Subsection 7.2: Addressing Issues (00:50:45 - 00:58:00)

- Prompt: "Implement the recommendation for issue #2"
- Discussing enforcement for AI-generated content only
- Modifying instruction files to check for `ai_generated: true` field
- GitHub Action implementation discussion deferred

---

## Section 8: Documentation Generation (Duration: 00:58:00 - 01:20:00, ~22 minutes) [x]

### Key Topics

- Automatic README updates
- Module-level documentation
- Maintaining documentation aligned with code

### Subsection 8.1: Update README Files (01:08:40 - 01:11:20)

- Prompt: "@workspace update the readme files with current state of the projects"
- Scans entire codebase
- Updates multiple README files with current information
- Adds references, building instructions, development workflow

### Subsection 8.2: Module Documentation (01:16:17 - 01:19:22)

- Session completes with multiple file changes
- Three README files updated
- Significant information added to documentation
- Discussion of creating documentation instruction file for standards

### Subsection 8.3: API Documentation (01:19:22 - 01:20:00)

- Can generate API references with usage samples
- Strategies for keeping documentation synchronized:
  - Run prompts regularly
  - Create documentation instruction file requiring updates with PRs
  - Delegate documentation responsibility to AI

---

## Section 9: Architecture Diagrams with Mermaid (Duration: 01:20:00 - 01:27:05, ~7 minutes) [x]

### Key Topics

- Generating architecture diagrams from code
- Mermaid diagram syntax and rendering
- Component and container diagrams

### Subsection 9.1: Diagram Generation (01:23:00 - 01:26:00)

- Generates C4 component diagrams
- Container diagrams showing web app and browser
- System context diagrams
- Mermaid syntax used for diagram-as-code

### Subsection 9.2: Diagram Types and Rendering (01:26:00 - 01:27:05)

- Supports dependency graphs, data flow diagrams, deployment topologies
- Most UML diagram types supported
- Can define custom diagram types in Mermaid
- Warning: Review diagrams carefully for errors
- Mermaid rendering issues can occur

---

## Section 10: Code Explanation and Analysis (Duration: 01:27:05 - 01:36:00, ~9 minutes) [x]

### Key Topics

- Explaining unfamiliar code
- Mapping call chains and dependencies
- Identifying hidden coupling
- Test coverage analysis

### Subsection 10.1: Code Explanation (01:28:20 - 01:30:05)

- Select code and use Control+I for inline chat
- Right-click "Explain" option available
- Focus on test code understanding
- Helps identify gaps in test coverage

### Subsection 10.2: Coverage Gap Analysis (01:30:05 - 01:36:00)

- Analyzing test files for completeness
- Prompt: Explains test suite structure and coverage
- Generates coverage report: 95% for calculator service
- Identifies missing coverage areas
- Provides recommended test implementation plan
- Can implement additional tests based on recommendations

---

## Section 11: Code Translation and Technical Hotspot Analysis (Duration: 01:36:00 - 01:47:45, ~12 minutes)

### Key Topics

- Translating code between languages
- Reviewing code compliance with instruction files
- Creating GitHub issues from findings

### Subsection 11.1: Code Translation (01:37:00 - 01:38:20)

- Select code and ask to rewrite in different language
- Example: C# to Go translation
- Useful for understanding cross-language patterns

### Subsection 11.2: Instruction Compliance Review (01:38:20 - 01:44:00)

- Question from Tom Bui about targeting specific files with instructions
- Demonstration of scoped review: "review calculator service and report any differences from meeting instruction files"
- Finds minor issues: invalid expressions should return result type failures vs exceptions
- Shows how to scope analysis to specific projects/files vs entire workspace

### Subsection 11.3: Creating GitHub Issues (01:44:00 - 01:47:45)

- Prompt: "Take your findings and create GitHub issues"
- Requires GitHub CLI installed and configured
- Automatically pushes issues to repository
- Example of identifying non-Evergreen patterns
- Generates issue with description, acceptance criteria
- Discussion of applying checks to AI-generated vs human-created content

---

## Summary Statistics

- **Total sections**: 11
- **Average section length**: ~09:46
- **Longest section**: Section 8 (Documentation Generation) - ~22 minutes
- **Shortest section**: Section 5 (VS Code Configuration) - ~5.5 minutes
- **Primary focus areas**:
  - Instruction file creation and management (Sections 2-7)
  - Documentation automation (Section 8)
  - Code analysis and quality (Sections 10-11)
- **Key participants**: John Miller (instructor), Dan Blanchard, Tom Bui, Buddy Toups
- **Technical tools demonstrated**: GitHub Copilot, VS Code, Mermaid, GitHub CLI

---

**Document Version**: 1.0.0
**Last Updated**: 2026-02-17
**Generated By**: AI Assistant
**Source**: AI-Assisted Software Development with GitHub Copilot (Tue Afternoon).vtt
