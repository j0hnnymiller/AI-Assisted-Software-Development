---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "create"]
description: "Update application documentation with current-state details and Mermaid C4 diagrams"
title: "Docs: Update application overview with Mermaid C4 diagrams"
labels: [documentation, architecture, diagram]
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Deprecated this prompt and linked its skill replacement."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

> **Deprecated:** Do not use or distribute this prompt. Its maintained workflow is [`update-application-c4-diagrams`](../skills/update-application-c4-diagrams/SKILL.md). This file remains only as a migration record.

Update application documentation to include current-state details and Mermaid C4 diagrams.

## Scope

- Audit repo for current state (features, services, workflows)
- Update README.md or create /docs/overview.md with:
  - Executive summary of system
  - Technology stack and high-level architecture
  - Build/run instructions if missing
- Add Mermaid C4 diagrams (at minimum):
  - C4 Context (C1)
  - C4 Container (C2)
  - Optional: C4 Component (C3) for critical service

## Acceptance Criteria

- README.md/docs/overview.md contains:
  - Accurate current app state description
  - At least one Mermaid C1 and C2 diagram
  - Links to deeper docs/diagrams
- Diagrams render correctly (GitHub Mermaid support)
- Assumptions/unknowns called out with TODOs

## Example Stubs

```mermaid
%% C4 Context (C1)
C4Context
    title System Context
    Person(user, "End User")
    System(system, "Target System", "Purpose")
    System_Ext(dep, "External Dependency", "Function")
    Rel(user, system, "Uses")
    Rel(system, dep, "Calls")
```

```mermaid
%% C4 Container (C2)
C4Container
    title System Container Diagram
    Person(user, "End User")
    System_Boundary(system, "Target System") {
      Container(web, "Web App", "Framework", "UI")
      Container(api, "API", "Runtime", "Logic")
      ContainerDb(db, "Database", "DB Type", "Store")
    }
    Rel(user, web, "Browses")
    Rel(web, api, "REST/GraphQL")
    Rel(api, db, "Queries")
```

## Notes

- Multiple services: include per-service sections, repeat C2 as needed
- Keep diagrams small, focused; link to deeper C3/C4 as architecture evolves
