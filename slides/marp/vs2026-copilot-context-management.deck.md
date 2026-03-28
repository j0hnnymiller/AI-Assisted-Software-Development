---
ai_generated: true
model: "anthropic/claude-sonnet-4-5@2025-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "vs2026-copilot-context-management-20260327"
prompt: |
  Using "docs/research-GitHub Copilot in Visual Studio Code vs Visual Studio 2026 Community Edition.docx"
  as a source, create a marp deck that describes the GitHub Copilot features in Visual Studio 2026
  for managing context. Include equivalents to the files that reside in the .github folder in
  Visual Studio Code.
started: "2026-03-27T00:00:00Z"
ended: "2026-03-27T00:15:00Z"
task_durations:
  - task: "research and outline"
    duration: "00:05:00"
  - task: "slide authoring"
    duration: "00:08:00"
  - task: "provenance and notes"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/27/vs2026-copilot-context-management-20260327/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Managing Context with GitHub Copilot || Your AI Has a Memory - Use It Wisely

## Visual Studio 2026

Equivalents to the VS Code `.github` Folder

::: notes
Duration ~00:01

Welcome participants to this session on context management with GitHub Copilot in Visual Studio 2026. The central question driving this deck is: how do developers who are familiar with the .github folder conventions in VS Code replicate that same level of context control inside Visual Studio 2026? By the end of this session, participants will understand which files work the same way, which features replace them, and where gaps still exist.
:::

---

## Why Context Management Matters

- Copilot responses are only as good as the context it receives
- Poor context = generic, off-target suggestions
- Good context = consistent, project-aware, standard-aligned output
- Context management lets you **steer** Copilot instead of just accepting what it gives

**Three context layers:**

1. **Implicit** — open files, solution structure, symbols
2. **Explicit** — #mentions, attached files, chat selections
3. **Persistent** — instructions files, memories, prompt files

::: notes
Duration ~00:01

Establish why this matters before diving into mechanics. AI models are stateless by nature; every prompt starts fresh unless the developer or the tooling actively provides context. In a team setting, inconsistent context leads to code that ignores conventions, naming standards, or architecture patterns. The three-layer framing sets up the rest of the deck nicely: implicit context the IDE provides automatically, explicit context the developer adds per-prompt, and persistent context that carries standards across every session and every team member.
:::

---

## The `.github` Folder in VS Code (Recap)

VS Code uses the `.github` folder as the primary location for persistent Copilot context files:

| File / Pattern                   | Purpose                                       |
| -------------------------------- | --------------------------------------------- |
| `copilot-instructions.md`        | Global instructions for all Copilot responses |
| `instructions/*.instructions.md` | Scoped instructions with `applyTo` patterns   |
| `prompts/*.prompt.md`            | Reusable prompt templates                     |
| `.mcp.json`                      | MCP server configuration                      |
| `agents/*.chatmode.md`           | Custom agents and chat modes                  |
| `agents/*.agent.md`              | Declarative agent definitions                 |

::: notes
Duration ~00:02

Provide a quick recap for participants who are already familiar with VS Code conventions. The goal is to set up the comparison that follows. Emphasize that this folder is the "control panel" for Copilot behavior in VS Code: it tells the model how to behave, what standards to follow, what tools to call, and which personas to adopt. For participants who are less familiar, encourage them to treat this table as the benchmark they will use to evaluate Visual Studio 2026 support. Transition by asking: which of these files does Visual Studio 2026 also understand?
:::

---

## VS 2026 Compatibility Matrix

Which `.github` files does Visual Studio 2026 recognize?

| VS Code File              | VS 2026 Support | Notes                              |
| ------------------------- | :-------------: | ---------------------------------- |
| `copilot-instructions.md` |     ✅ Full     | Same path, auto-discovered         |
| `*.instructions.md`       |     ✅ Full     | Auto-discovered, `applyTo` honored |
| `prompts/*.prompt.md`     |     ✅ Full     | Managed via Tools > Options        |
| `.mcp.json`               |     ✅ Full     | Workspace + user profile level     |
| `agents/*.chatmode.md`    |     ❌ None     | Custom agents not yet supported    |
| `agents/*.agent.md`       |     ❌ None     | Custom agents not yet supported    |
| Tool sets                 |     ❌ None     | No equivalent in VS 2026           |

::: notes
Duration ~00:01

This is the anchor slide participants will refer back to throughout the session. The key insight is that the file-based, persistent context files work the same way in Visual Studio 2026 because the underlying Copilot platform reads these files regardless of IDE. The gap is in agent customization and tool sets, which remain VS Code-only as of early 2026. Surface the implication: teams with existing .github folders will get consistent context in both IDEs for instructions and prompts, but cannot yet share custom agent definitions. Transition into a deeper look at each supported file type.
:::

---

## `copilot-instructions.md` — Same File, Both IDEs

**Path:** `.github/copilot-instructions.md`

- Auto-discovered by both VS Code and Visual Studio 2026
- Applies to **all Copilot interactions** in the repository
- No configuration required — just create the file
- Use it to encode:
  - Coding standards and naming conventions
  - Architecture patterns and off-limits patterns
  - Language/framework preferences
  - Team-specific context or domain vocabulary

```markdown
# Managing Context with GitHub Copilot || Your AI Has a Memory - Use It Wisely

Always use the Result<T> pattern for error handling.
Prefer record types over classes for DTOs.
Follow the CQRS patterns defined in .github/instructions/.
```

::: notes
Duration ~00:02

This is the highest-impact slide for teams migrating from VS Code. The file path is identical, the behavior is identical, and no additional setup is required in Visual Studio 2026. If a team already has this file, every developer opening the solution in VS 2026 immediately benefits from it. Walk through the example content and explain the three categories of instruction it demonstrates: a coding pattern rule, a language idiom preference, and a cross-reference to more detailed instruction files. Emphasize that this file is checked in to source control and therefore enforced for the whole team automatically.
:::

---

## `*.instructions.md` — Scoped Instructions

**Path:** `.github/instructions/*.instructions.md`

- Visual Studio 2026 auto-discovers these files
- The `applyTo` front matter header scopes instructions to matching file patterns

```yaml
---
applyTo: "**/*.cs"
---
# Managing Context with GitHub Copilot || Your AI Has a Memory - Use It Wisely
- Use nullable reference types (`#nullable enable`)
- Prefer `ILogger<T>` injection over static logging
- Async methods must use the `Async` suffix
```

**How VS 2026 uses them:**

- Automatically included when the current file matches the `applyTo` glob
- No slash command needed — context is injected silently
- Multiple instruction files can apply simultaneously

::: notes
Duration ~00:02

Explain the benefit of scoped instructions over a single global file: a C# developer gets C# standards, a TypeScript developer gets TypeScript standards, and a SQL developer gets SQL standards-all from the same repository. Visual Studio 2026 implements the same glob-matching logic that VS Code uses for `applyTo`. One important nuance: the files must be under `.github/instructions/` for auto-discovery, though the exact subfolder scheme is flexible. Encourage participants to treat these files as living documentation that Copilot actively enforces rather than static references no one reads.
:::

---

## Prompt Files — Reusable Prompt Templates

**Path:** `.github/prompts/*.prompt.md` (or configured in Tools > Options)

- Define reusable prompts for common tasks
- Invoked via slash commands in the Copilot Chat window
- Stored in source control — shared across the team
- Can reference instruction files and carry their own context

**Example:** `.github/prompts/add-unit-tests.prompt.md`

```yaml
---
description: Generate xUnit tests for the selected class
---
Generate comprehensive xUnit tests for the selected class.
Follow the Arrange-Act-Assert pattern.
Ensure each public method has at least one happy-path and one error-path test.
Mock all dependencies using NSubstitute.
```

::: notes
Duration ~00:02

Prompt files solve the "I have to retype the same 200-word prompt every day" problem. In Visual Studio 2026 these files are managed via Tools > Options > GitHub > Copilot, where the discovery path can be set. The key value proposition is that the team encodes expertise into prompt files: a senior developer writes the ideal test generation prompt once, and everyone on the team benefits from it instantly. Contrast this with VS Code, where the same file is invoked by a slash command in chat. The experience is slightly different in VS 2026 but the file format and storage location are compatible.
:::

---

## `.mcp.json` — MCP Tool Configuration

**Path:** `.mcp.json` (workspace) or `%USERPROFILE%\.mcp.json` (user)

Visual Studio 2026 includes a **full MCP client** supporting tools, prompts, resources, and sampling.

```json
{
  "servers": {
    "azure-devops": {
      "type": "http",
      "url": "https://my-mcp-server/ado",
      "tools": ["get-work-items", "create-branch", "link-commit"]
    },
    "company-docs": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@company/docs-mcp-server"]
    }
  }
}
```

**Tools are disabled by default** — approve each tool via chat pane or settings

::: notes
Duration ~00:02

MCP is the context management feature with the most immediate operational impact. By connecting Copilot to internal tools, the developer no longer has to paste work item IDs, look up API specifications manually, or switch tabs to find documentation. Visual Studio 2026 adds a CodeLens-based authentication flow for managed MCP servers. Highlight the two-level configuration: workspace-level `.mcp.json` (checked into source control, shared with the team) and user-level `%USERPROFILE%\.mcp.json` (personal tools like calendar, notes, or private databases). The tools-disabled-by-default security posture is important for enterprise environments-demonstrate where approvals are granted in the chat pane.
:::

---

## VS 2026 Exclusive: Memories

A feature with no direct VS Code counterpart

- Copilot **learns and stores** coding preferences across sessions
- Memories persist across solutions and repositories
- Automatically applied to future interactions
- Can be explicitly managed (viewed, edited, deleted)

**What gets stored:**

- Preferred patterns and idioms you consistently accept
- Naming conventions inferred from accepted suggestions
- Architecture preferences observed across sessions
- Personal tools workflow patterns

**Where:** Tools > Options > GitHub > Copilot > Memories

::: notes
Duration ~00:02

Memories represent a fundamentally different approach to context management than files: instead of the developer writing instructions, the model observes behavior and writes its own. For experienced developers, this means Copilot adapts over time-after a week of consistently accepting Record types over classes, accepting async/await patterns, and using a particular error-handling style, those preferences become part of the implicit context for every session. Make the distinction clear: instruction files are for team standards (checked in, version-controlled, explicit), while memories are for personal workflow preferences (private, inferred, adaptive). Emphasize that memories are managed and not invisible-developers can review and delete entries they do not want.
:::

---

## VS 2026 Exclusive: Output Window as Context

A powerful context source with no VS Code equivalent

- Build errors, debug output, and test results can be **attached to a chat prompt**
- Right-click any output window entry → "Ask Copilot"
- Or manually reference output in the chat pane

**Use cases:**

| Output Source       | Context Value                                   |
| ------------------- | ----------------------------------------------- |
| Build errors        | "Fix this compilation error in context"         |
| Test failure output | "Explain why this test failed"                  |
| Debug call stack    | "Analyze this exception and suggest a fix"      |
| Profiler results    | "What is causing this memory allocation spike?" |

::: notes
Duration ~00:02

The Output Window integration is one of the most underappreciated context features in Visual Studio 2026. In VS Code, developers must copy-paste error messages into the chat window or rely on #codebase references. In VS 2026, the output pane is a first-class context source: clicking "Ask Copilot" on a build error automatically attaches the full error message, the file, the line number, and the surrounding code to the prompt. Walk through the four use cases and ask participants which one they would use most. The profiler + Copilot integration is particularly powerful-the Profiler Agent uses this context to generate benchmarks, suggest optimizations, and validate improvements in a guided loop.
:::

---

## VS 2026 Exclusive: Solution-Wide Context

Visual Studio 2026 leverages full solution awareness automatically

- **Solution indexing** provides repository-wide symbol resolution
- **Project dependencies and references** inform multi-file reasoning
- **Source control state** (uncommitted changes, branch) is included
- **Architectural patterns** inferred from the solution structure

**Practical impact:**

- Ask "where is the authentication handler registered?" across 50 projects
- Refactoring spans the correct files automatically
- "How is this interface implemented?" works solution-wide

**No file needed** — VS 2026 provides this context automatically

::: notes
Duration ~00:02

This slide addresses a common question: "if VS 2026 has all this automatic context, why do I need instruction files at all?" The answer is that automatic context covers structural and factual questions (where is X, what calls Y) but not behavioral standards (how should X be written, which patterns to avoid). Solution-wide context and instruction files are complementary, not competing. Emphasize that in large enterprise solutions with hundreds of projects, this automatic context is a significant advantage over VS Code, which relies on workspace indexing that can be slower and less complete for very large repositories.
:::

---

## What Is NOT in Visual Studio 2026 (Yet)

VS Code features with no current equivalent:

| VS Code Feature                | Why It Matters                                            |
| ------------------------------ | --------------------------------------------------------- |
| Custom agents / chat modes     | Persona-based AI workflows for planning, review, security |
| `.github/agents/*.chatmode.md` | Encode specialized agent behavior in source control       |
| Tool sets                      | Group tools for specific workflow contexts                |
| Skills folders                 | Reusable instruction sets with examples                   |
| Third-party agent support      | Claude, Codex, and other provider agents                  |
| Agent handoff orchestration    | Chaining agents across complex workflows                  |

**Current workarounds in VS 2026:**

- Use detailed prompt files to approximate agent personas
- Use `.mcp.json` to surface tools in specific contexts
- Use instruction files with narrow `applyTo` scopes as pseudo-skills

::: notes
Duration ~00:02

This is an important slide for managing expectations. Participants who rely heavily on custom agents in VS Code will find this gap significant. The current status (as of early 2026) is that agent skills are explicitly listed as a known limitation in the Visual Studio developer community. Frame this as "not yet" rather than "never" - the roadmap shows clear investment in this area. The workarounds section is practical: prompt files can encode much of the persona behavior that a chatmode.md file provides, even if they cannot fully replace the interactive, stateful agent experience. Transition by noting that despite these gaps, the supported context features cover the majority of day-to-day context management needs.
:::

---

## Managing Context via Tools > Options

Visual Studio 2026 provides a centralized context management UI

**Tools > Options > GitHub > Copilot:**

```
├── General
│   ├── Enable/disable inline completions
│   └── Model selection
├── Chat
│   ├── Custom instructions path
│   ├── Prompt files discovery path
│   └── MCP server management
├── Memories
│   ├── View and edit stored memories
│   └── Enable/disable memory learning
└── Agent Mode
    ├── Tool approval settings
    └── Default model for agent tasks
```

All file-based context (instruction files, prompt files) can also be **checked in** to source control for team sharing.

::: notes
Duration ~00:01

Walk participants through the UI location so they can find it immediately after the session. The key distinction from VS Code (where settings are in settings.json or the GUI settings editor) is that Visual Studio 2026 exposes these in the traditional Tools > Options tree that Visual Studio developers already know. Emphasize the hybrid nature: UI-managed settings for the individual, file-based settings for the team. A team lead can define the instruction and prompt files, check them into the repo, and every developer on the team benefits without any personal configuration. Individual developers then layer personal memories and model preferences on top.
:::

---

## Side-by-Side: Context Management Summary

| Context Mechanism                  | VS Code | Visual Studio 2026 |
| ---------------------------------- | :-----: | :----------------: |
| `copilot-instructions.md`          |   ✅    |         ✅         |
| `*.instructions.md` with `applyTo` |   ✅    |         ✅         |
| Prompt files (`.github/prompts/`)  |   ✅    |         ✅         |
| `.mcp.json` (workspace)            |   ✅    |         ✅         |
| `%USERPROFILE%\.mcp.json`          |   ✅    |         ✅         |
| Custom agents / chat modes         |   ✅    |         ❌         |
| Tool sets                          |   ✅    |         ❌         |
| Memories (persistent learning)     |   ❌    |         ✅         |
| Output window as context           |   ❌    |         ✅         |
| Solution-wide automatic context    | Partial |         ✅         |
| Microsoft Learn integration        |   ❌    |         ✅         |

::: notes
Duration ~00:01

Use this table as a reference for the Q&A discussion. The headline message: there is strong parity in the file-based context mechanisms, meaningful gaps in agent customization that favor VS Code, and meaningful exclusive features in VS 2026 for solution context and adaptive learning. Organizations with teams using both IDEs can maintain a single set of .github files and get consistent behavior from instructions, prompts, and MCP tools across both environments - which is a strong argument for investing in these files even if a team is primarily VS Code today. Transition to key takeaways.
:::

---

## Key Takeaways

1. **Most .github files just work** in Visual Studio 2026 — no conversion needed
2. **`copilot-instructions.md` and `*.instructions.md`** are your highest-impact investment — they work in both IDEs
3. **Prompt files** bridge the gap where custom agents are not yet available in VS 2026
4. **`.mcp.json`** unlocks tool-augmented context at both workspace and user levels
5. **Memories** in VS 2026 provide adaptive, personal context that files cannot
6. **Output window context** is a VS 2026 superpower for debugging and profiling workflows
7. **Custom agents are not yet supported** — use detailed prompt files as a workaround

> Start with `copilot-instructions.md`. Check it in. Share it with the team. Everything else builds from there.

::: notes
Duration ~00:01

Close with an action the participants can take immediately: create or update the copilot-instructions.md file in their repository today. The key insight to leave participants with is that context management in Visual Studio 2026 is not a different system that requires learning new conventions - it is the same file-based system they already know from VS Code, with additional capabilities layered on top. The investment in .github folder conventions pays dividends in both IDEs simultaneously. For teams considering migrating from VS Code to Visual Studio 2026, the context management story is good news: they keep everything they have and gain new features.
:::
