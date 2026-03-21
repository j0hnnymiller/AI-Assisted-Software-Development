---
ai_generated: true
model: "anthropic/claude-sonnet-4-5@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "mcp-model-context-protocol-servers-20260321"
prompt: |
  Merge three MCP slide decks (mcp-model-context-protocol-servers.md,
  mcp-servers-vscode-copilot.md, mcp-servers.md) into one authoritative deck.
  Use mcp-model-context-protocol-servers.md as the base, inject the hands-on
  install, Copilot integration sequence diagram, secure config, and exercise
  slides from the PPTX-extracted sources, and enhance the architecture slide
  with the Mermaid diagram from mcp-servers-vscode-copilot.md.
started: "2026-03-21T22:30:00Z"
ended: "2026-03-21T22:45:00Z"
task_durations:
  - task: "comparison and merge planning"
    duration: "00:05:00"
  - task: "slide authoring"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/mcp-model-context-protocol-servers-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

<!-- _class: lead -->

# MCP: Model Context Protocol Servers

## Extending GitHub Copilot with External Tools and Data

- Connect Copilot to databases, APIs, infrastructure tools, and custom systems
- Built on a standardized protocol so any tool can speak to Copilot
- Duration target: about 15 minutes

::: notes
Open by framing MCP as Copilot's extensibility layer beyond the repository. Copilot is already powerful for code in a repo, but many real workflows require reaching outside that boundary: querying a database, checking infrastructure state, or pulling from an internal API. MCP is the standard that makes all of those integrations possible.

Timing: 1 minute

Transition: "Let's start with what MCP actually is."
:::

---

## What Is MCP?

- **Model Context Protocol** is a standardized communication layer between Copilot and external services
- Adds capabilities and data sources that Copilot cannot access on its own
- Any tool or service that speaks MCP can be connected to Copilot
- A large and growing library of community-built servers already exists
- Key mindset: **configure and consume** — not build from scratch

```mermaid
flowchart LR
    A[GitHub Copilot\nClient] -- MCP Protocol --> B[MCP Server]
    B -- Resources --> A
    B -- Tools --> A
```

::: notes
Explain MCP as an open protocol rather than a proprietary plugin system. The key idea is standardization: any team can build a server that exposes data or capabilities to Copilot using the same protocol, which means the ecosystem grows without waiting for first-party integrations.

MCP servers are like npm packages — install and use. Configuration is simple JSON — no coding required.

Examples:

- GitHub MCP Server: Access repos and issues
- Postgres MCP Server: Query your database
- Filesystem MCP Server: Safe file access for Copilot
- Slack MCP Server: Read channels and messages

Timing: 1-2 minutes

Transition: "Let's look at the architecture in detail."
:::

---

## Architecture: Five Components

```mermaid
graph LR
    A[VS Code<br/>Copilot<br/>Client] <-->|JSON-RPC| B[MCP Server<br/>Transport Layer]
    B <-->|Protocol| C[Resources<br/>Files, APIs,<br/>Databases]
    style A fill:#0078d4,color:#fff
    style B fill:#68217a,color:#fff
    style C fill:#107c10,color:#fff
```

| Component     | Role                                                  |
| ------------- | ----------------------------------------------------- |
| **Client**    | VS Code / GitHub Copilot — sends requests             |
| **Server**    | MCP server — provides capabilities and data           |
| **Protocol**  | Standardized message format connecting both sides     |
| **Resources** | Data the server exposes (files, records, state)       |
| **Tools**     | Functions the server gives Copilot permission to call |

::: notes
Walk through each component methodically. The client is already familiar — VS Code with Copilot enabled. The server is what you install. The protocol is what makes them interoperable. Resources are data that can be read into context; tools are actions that Copilot can invoke on behalf of the user.

Consumer focus: think "install and configure" not "build and deploy" — like VS Code extensions from the marketplace.

Timing: 2-3 minutes

Transition: "Let's see why you'd want MCP in your workflow."
:::

---

## Use Cases

**External Data Access**

- Query live databases and include results in Copilot's context
- Pull from internal APIs or documentation systems

**Tool Integration**

- Control infrastructure tools like Terraform or Kubernetes directly from the editor
- Interact with cloud provider APIs without leaving VS Code

**Custom Solutions**

- Build a server for proprietary internal systems
- Expose institutional data that no public server covers

::: notes
Use this slide to show why MCP matters in practice. The most compelling cases are often ones where the developer needs real state that lives outside the repo: the current schema of a production database, the live status of a Kubernetes deployment, or data from an internal system.

Encourage the audience to think about what data sources or tools they access repeatedly that could be connected to Copilot through an MCP server.

Timing: 1 minute

Transition: "Let's look at what servers are available today."
:::

---

## Available Pre-Built Servers

- **GitHub Repos** — repository metadata, issues, pull requests
- **Database Systems** — Postgres, MySQL, SQLite, MongoDB
- **Terraform** — infrastructure state and plan output
- **Kubernetes** — cluster status and resource inspection
- **Cloud Provider APIs** — AWS, Azure, GCP integrations
- **Web & APIs** — REST, GraphQL, browser automation (Puppeteer)

> Community-maintained libraries add new servers regularly

::: notes
Emphasize that you do not need to build a server to benefit from MCP. Most common integration points already have a server available.

Specific package names to mention:

- @modelcontextprotocol/server-github — Full GitHub integration
- @modelcontextprotocol/server-postgres — Direct database queries
- @modelcontextprotocol/server-filesystem — Workspace file access
- @modelcontextprotocol/server-brave-search — Web search integration
- @modelcontextprotocol/server-puppeteer — Browser automation

The infrastructure-focused servers — Terraform and Kubernetes — tend to generate the most interest in DevOps or platform engineering teams.

Timing: 45-60 seconds

Transition: "Now let's find the right server for your needs."
:::

---

## Finding MCP Servers

**VS Code Extension Gallery**

- Search `MCP` in the extensions panel
- Read the description to confirm what resources and tools are exposed

**Model Context Protocol Website**

- `modelcontextprotocol.io` — canonical registry and documentation

**GitHub Community Repository**

- `github.com/modelcontextprotocol/servers` — community-maintained collection with usage examples

::: notes
Make this actionable. The VS Code extension gallery is the fastest entry point because it is already open. The MCP website is the authoritative source for documentation and the full server registry.

Suggest that attendees check the extension gallery for the tool they care most about as a next-step exercise.

Timing: 30-45 seconds

Transition: "Let's install your first MCP server."
:::

---

## Installing Your First MCP Server

**Example: GitHub MCP Server**

1. Install the server package:

```bash
npm install -g @modelcontextprotocol/server-github
```

2. Configure in VS Code `settings.json`:

```json
{
  "mcp.servers": {
    "github": {
      "command": "mcp-server-github",
      "env": { "GITHUB_TOKEN": "${env:GITHUB_TOKEN}" }
    }
  }
}
```

3. Reload VS Code — the MCP server starts automatically

> **Token budget**: each enabled server uses ~128 tokens of context window — enable only what you need

::: notes
Walk through the real example — emphasize it's just package installation. Install like any npm/pip package, configure with credentials and options, and servers start automatically with VS Code.

Common issues:

- Missing credentials: Set environment variables before starting VS Code
- Package not found: Check npm registry or install from GitHub directly
- Permission errors: Verify token scopes match what the server requires

Available servers to mention: @modelcontextprotocol/server-filesystem, @modelcontextprotocol/server-postgres, @modelcontextprotocol/server-sqlite

Token budget note: This is often overlooked. Each enabled MCP server occupies a slice of Copilot's context window even when not actively used — treat them like browser tabs: useful when open for a reason, wasteful if left open by default.

Timing: 4-5 minutes (show live demo if possible)

Transition: "Now let's see Copilot use this context."
:::

---

## Copilot + MCP Integration

**Enhanced capabilities with MCP context:**

- **Context-Aware Completions** — access to project-specific patterns
- **Tool Use** — Copilot can invoke server tools on your behalf
- **Security Boundaries** — controlled, audited access to resources

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Copilot as GitHub Copilot
    participant MCP as MCP Server
    participant Res as Resources

    Dev->>Copilot: "Create user auth"
    Copilot->>MCP: Request context
    MCP->>Res: Fetch schema, patterns
    Res-->>MCP: Return context
    MCP-->>Copilot: Structured context
    Copilot-->>Dev: Code matching your patterns
```

::: notes
Emphasize the "before and after" — without MCP, completions are based only on training data. With MCP, completions match YOUR codebase patterns.

Examples:

- Database connection: MCP provides your actual schema and connection pattern
- API calls: MCP shares your error handling approach
- Testing: MCP provides your test framework and fixture patterns

Security note: MCP servers can implement rate limiting. Audit logs track what context was provided. The permission model prevents unauthorized access.

Timing: 3-4 minutes

Transition: "Let's talk about configuring these safely."
:::

---

## Configuring Servers Securely

**Security checklist:**

- ✅ Use environment variables for credentials (never hardcode tokens)
- ✅ Grant minimum necessary permissions
- ✅ Review server source code on GitHub before installing
- ✅ Configure allowed paths/resources explicitly
- ❌ Never use full admin credentials when a reader role is sufficient

**Best practices:**

- Start with read-only servers
- Use scoped tokens (e.g., `repo:read` only for GitHub)
- Enable only needed capabilities
- Test in non-production first
- Keep servers updated

::: notes
Security from the consumer perspective — this is all about what YOU control in configuration.

Good config examples:

// Good: Scoped GitHub token
"env": { "GITHUB_TOKEN": "${env:GH_READ_TOKEN}" }

// Good: Limited database access
"env": { "DATABASE_URL": "postgresql://readonly-user@host/db" }

// Bad: Full access token hardcoded
"env": { "TOKEN": "ghp_admintoken123456" }

Common mistakes:

- Using admin credentials when a reader role is sufficient
- Granting access to the entire filesystem instead of the workspace folder
- Not checking what data the server actually sends to AI

Timing: 3-4 minutes

Transition: "Let's put this into practice."
:::

---

## Exercise: Using MCP Servers

**Quick Start (30 minutes)**

1. Install the MCP extension in VS Code (search "MCP" in marketplace)
2. Pick **one** server to start: **GitHub** or **Filesystem**
3. Set credentials in your environment variables
4. Add server config to `settings.json`
5. Reload VS Code and test with Copilot

```bash
# Filesystem server quick start
npm install -g @modelcontextprotocol/server-filesystem
```

```json
{
  "mcp.servers": {
    "filesystem": {
      "command": "mcp-server-filesystem",
      "args": ["${workspaceFolder}"]
    }
  }
}
```

Ask Copilot: _"What files are in this project?"_

**Resources:** `github.com/modelcontextprotocol/servers` | `modelcontextprotocol.io`

::: notes
Make it feel achievable — "you can do this today."

Don't try to install all servers at once. Pick ONE that solves a current pain point. Test thoroughly before adding more.

Recommended first server by use case:

- Filesystem: if you want Copilot to understand your project structure
- GitHub: if you want context from issues and PRs
- Postgres: if you want schema-aware SQL generation

Active community: Discord and GitHub Discussions are helpful for issues.

Timing: 2-3 minutes for intro, 20-30 minutes hands-on

Transition: "Questions about getting started?"
:::

---

## Summary

- MCP gives Copilot a standardized way to reach **external data and tools**
- Architecture: client ↔ protocol ↔ server exposing **resources** and **tools**
- Pre-built servers cover most common integrations; custom servers handle the rest
- Find servers via VS Code gallery, `modelcontextprotocol.io`, or GitHub
- Install as extensions, **enable selectively** to manage token cost (~128 per server)

::: notes
Recap the key takeaways. The audience should leave with three things:

1. An understanding of what MCP is and why it exists
2. Knowledge of where to find servers for their specific tools
3. Awareness of the token overhead so they configure their environment deliberately

Invite questions or suggest exploring the VS Code gallery as a hands-on follow-up.

Timing: 30 seconds recap + Q&A
:::
