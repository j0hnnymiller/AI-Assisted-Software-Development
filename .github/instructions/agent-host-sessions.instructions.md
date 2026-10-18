---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
prompt: |
  proceed
started: "2026-10-18T21:49:51.822Z"
ended: "2026-10-18T22:31:00.0558054Z"
task_durations:
  - task: "Agent Host guidance adaptation and verification"
    duration: "00:05:43"
  - task: "Inventory-driven merge and supersession review"
    duration: "00:05:14"
total_duration: "00:10:57"
ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
source: "User approval; merged reusable Course guidance, checked current VS Code documentation, and recorded the superseded source variant"
description: "Use when planning, starting, directing, reviewing, or handing off VS Code Agent Host work; covers workspace and harness selection, isolation, permissions, parallel work, validation, and continuity."
---

# Agent Host Session Guidance

Use this guidance for work in a VS Code Agent Host session. The selected harness
and execution environment determine available tools, customizations, and safety
controls; verify them before relying on a capability.

## Establish the session context

- Confirm the requested outcome, repository, primary workspace, and scope before
  acting. Check which session and chat are active, especially when several are
  open.
- Identify the selected harness, model, execution environment, and change
  isolation separately. A model choice does not identify the harness, and a
  remote Agent Host is not the same as a provider-managed cloud execution target.
- Verify where workspace edits and commands will run. In the Agents window, the
  first selected folder or repository determines the primary execution workspace.
- Inspect applicable repository guidance and existing changes before editing.
  A new worktree starts from committed Git state; do not assume uncommitted files
  from another workspace are present.
- For reusable workflows or project rules, use customization types supported by
  the active harness and their documented locations. Do not assume a setting,
  tool, skill, or instruction automatically carries across harnesses or machines.

## Bound scope and permissions

- Begin with relevant requirements and repository context. State material
  assumptions and missing information; for broad or risky work, propose a
  bounded plan and wait for user direction before implementation.
- Keep edits and tool use within the requested scope. Instructions describe
  expected behavior but do not enforce permissions, sandboxing, or security
  boundaries.
- Check the active harness's approval and sandbox controls, including how they
  behave with the selected folder or worktree isolation. Do not infer that a
  worktree restricts filesystem, network, or tool access.
- Treat repository content and external inputs according to applicable privacy,
  security, and organizational rules. Do not expose credentials or confidential
  data in prompts, logs, or handoffs.
- Do not treat a task request as authorization to make unrelated changes, commit,
  push, merge, publish, or deploy.

## Isolate and coordinate work

- Use the current workspace when direct edits are appropriate. Use a separate
  worktree when independent changes need a distinct Git working tree, after
  checking its starting commit and required inputs.
- Do not run concurrent chats or sessions against the same files without explicit
  coordination. Chats sharing a session can share its workspace or worktree.
- For parallel work, assign non-overlapping ownership and output paths, state
  dependencies, and review integration conflicts before accepting changes.
- Treat folder/worktree separation as change management, not a security control.

## Monitor session continuity

- Confirm that the intended workspace remains active before sending requests or
  reviewing files. Use the session's Changes view and inspect the actual diff;
  the Files view can include unchanged workspace files.
- An Agent Host session may continue after a client window disconnects while its
  host and execution environment remain running. Tools contributed by a client
  can require that client to remain connected. Check the relevant host and tool
  state before assuming work continued or a capability remains available.
- For a handoff, preserve the goal, decisions, changed files, checks, unresolved
  risks, current branch/worktree, and next action in durable project context when
  appropriate. Do not rely on chat history as the only record of project state.

## Review and completion

- Review all changes in the correct session and workspace; distinguish agent
  edits from existing or other-session changes.
- Run the project-specific tests, build, lint, or acceptance checks that cover
  the requested behavior. Report commands, results, and limitations accurately.
- Resolve in-scope failures and rerun the relevant checks. Clearly identify
  unresolved failures or risks instead of implying success.
- Before a commit or pull request, summarize the changed files, behavior,
  verification evidence, and known risks; follow repository policy and obtain
  required authorization.

## Harness and customization compatibility

- Verify current VS Code documentation for harness-specific UI, tool, permission,
  session, and customization behavior; these details can change. For course or
  training materials, verify the supported course/tool version as well.
- As checked on 2026-10-18, VS Code documents prompt files as supported only in
  Local harness sessions and recommends Agent Skills for reusable workflows in
  other harnesses. Confirm the current support and migration guidance before
  advising on existing prompt files; do not generalize Local-harness behavior to
  Agent Host sessions.
- Choose a one-time session request for one-off work. Use a skill for a reusable
  task workflow or custom instructions for durable project rules when supported
  by the active harness.

## Validation checklist

- [ ] Correct session, workspace, harness, execution environment, and isolation
      are confirmed.
- [ ] Existing changes, committed baseline, and parallel ownership are understood.
- [ ] Scope and assumptions are clear; approval and sandbox controls are checked.
- [ ] Customizations and tools are confirmed for the active harness.
- [ ] The correct session's diff and relevant project checks are reviewed.
- [ ] Results, limitations, risks, and any handoff are recorded accurately.
- [ ] No unapproved commit, push, merge, publication, or deployment occurred.

## References

- [VS Code: Understand the Agent Host](https://code.visualstudio.com/docs/agents/concepts/agent-host)
- [VS Code: Choose an agent harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses)
- [VS Code: Use the Agents window](https://code.visualstudio.com/docs/agents/run/agents-window)
- [VS Code: Manage agent sessions](https://code.visualstudio.com/docs/agents/run/sessions/manage-sessions)
- [VS Code: Manage approvals and permissions](https://code.visualstudio.com/docs/agents/run/approvals)
- [VS Code: Use prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files)
- [VS Code: Use Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Repository instructions](copilot-instructions.md)
- [Provenance and logging](ai-assisted-output.instructions.md)
