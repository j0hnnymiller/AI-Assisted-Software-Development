---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-21"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-mcp-server-create-test-use-20260321"
prompt: |
  create a marp exercise deck that guides student in creating, testing, and using this mcp server
started: "2026-03-21T23:10:00Z"
ended: "2026-03-21T23:30:00Z"
task_durations:
  - task: "exercise design"
    duration: "00:08:00"
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and README updates"
    duration: "00:03:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2026/03/21/exercise-mcp-server-create-test-use-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Create, Test, and Use an MCP Server || Exercise: Build the Bridge Between Copilot and Everything Else

---

## Exercise: Create, Test, and Use a Local MCP Server

**Objectives**
  - Create a minimal PowerShell MCP server that supports `initialize`, `tools/list`, and `tools/call`
  - Validate protocol behavior with an end-to-end smoke test script
  - Connect the server to VS Code and use the `echo` tool from Copilot

**Activities**
  1. **Create**: Build `scripts/mcp/simple-mcp-server.ps1` with JSON-RPC framing and MCP method routing
  2. **Test**: Run `scripts/mcp/test-simple-mcp-server.ps1` and verify initialize/tools/list/tools/call responses
  3. **Use**: Confirm `.mcp.json` points to the local server, then prompt Copilot to call the `echo` tool

**Success Criteria**
  - Server starts without errors and responds with valid MCP JSON-RPC envelopes
  - Test output reports `MCP test passed.` and confirms all three checkpoints
  - Copilot can discover the `echo` tool and return the expected echoed text

::: notes
Duration ~00:30

Facilitate this as a lab where students progress from implementation to verification to real usage. Start by framing MCP as a local integration pattern: the server reads JSON-RPC over stdio, advertises tools, and returns structured results.

For Phase 1, have students create `scripts/mcp/simple-mcp-server.ps1` with helper functions for `Content-Length` framing, plus handlers for `initialize`, `tools/list`, and `tools/call`. Emphasize that `tools/list` should return the `echo` tool schema and `tools/call` should validate `name == "echo"` and required `arguments.text`.

For Phase 2, run `pwsh -NoLogo -NoProfile -File .\scripts\mcp\test-simple-mcp-server.ps1` from repo root. Students should verify three checks in output: initialize success, echo tool listing, and echo text round-trip. If test fails, inspect malformed headers, missing `id` correlation, or invalid response shape.

For Phase 3, confirm `.mcp.json` includes command `pwsh` and args `-NoProfile -File scripts/mcp/simple-mcp-server.ps1`. In Copilot Chat, ask for a tool call using text like: "Use the echo MCP tool and send the text 'MCP lab check'." Debrief by asking students where they would replace echo with a real internal API or automation tool.

Timing guidance: 10 minutes create, 10 minutes test/debug, 8 minutes use and discuss, 2 minutes recap. During recap, connect this lab to production hardening topics: auth, input validation, audit logs, and tool least-privilege design.
:::
