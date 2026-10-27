---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "92373087-9b97-420d-a3ac-53f20e65be8a"
prompt: |
  TypeScript
  JavaScript
  @types/node
  typescript
  Node.js

  Create instruction files for these technologies
started: "2026-10-27T14:59:23-07:00"
ended: "2026-10-27T15:14:23-07:00"
task_durations:
  - task: "Node.js release-status verification"
    duration: "00:04:00"
  - task: "Node.js and @types/node instruction authoring"
    duration: "00:11:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/10/27/92373087-9b97-420d-a3ac-53f20e65be8a/conversation.md"
source: "User request; generate-instructions skill; evidence from !here-be-dragons/Labs/lab1-3-typescript and nodejs.org release schedule"
name: nodejs
description: "Use when writing, reviewing, or configuring Node.js applications, scripts, or packages; covers runtime version selection, @types/node alignment, package.json scripts, built-in modules, async I/O, errors, configuration, and testing."
applyTo: "**/package.json,**/.nvmrc,**/.node-version"
version: "1.0.0"
author: "johnmillerATcodemag-com"
tags: ["nodejs", "runtime", "types-node", "npm"]
owner: "johnmillerATcodemag-com"
reviewedDate: "2026-10-27"
nextReview: "2027-01-27"
---

# Node.js Instructions

## Overview

Rules for code that runs on Node.js and for its runtime and type configuration,
including the `@types/node` package.

- **Audience**: AI assistants (primary), developers
- **Scope**: runtime version, `@types/node`, `package.json` scripts, built-in
  APIs, async I/O, process behavior, configuration, testing
- **Loading**: `applyTo` matches runtime manifests only, because a file pattern
  cannot distinguish Node code from browser code. Load this file by task
  relevance or attach it when editing Node `.ts`/`.js` source.
- **Out of scope**: language rules (see [TypeScript](typescript.instructions.md)
  and [JavaScript](javascript.instructions.md)); dependency selection, approval,
  and licensing (see [Dependency Management](dependency-management-policy.instructions.md))
- **Repository evidence**: `!here-be-dragons/Labs/lab1-3-typescript` declares
  `@types/node ^20.0.0`, compiles to CommonJS, and runs `node dist/main.js`. It
  declares no `engines` field or version file. Local tooling during authoring
  was Node v22.

## Table of Contents

- [AI Assistant Guidelines](#ai-assistant-guidelines)
- [Runtime Versions](#runtime-versions)
- [@types/node](#typesnode)
- [package.json and Scripts](#packagejson-and-scripts)
- [Runtime Conventions](#runtime-conventions)
- [Patterns and Anti-Patterns](#patterns-and-anti-patterns)
- [Testing and Validation](#testing-and-validation)
- [Validation Checklist](#validation-checklist)
- [Summary](#summary)

## AI Assistant Guidelines

1. Identify the target Node major from `engines`, `.nvmrc`, `.node-version`, CI,
   or container images before using a runtime API. If none exists, ask.
2. Use only APIs available in the lowest supported Node major.
3. Keep `@types/node` aligned with that major (see below).
4. Use `node:`-prefixed built-in imports and promise-based APIs.
5. NEVER log, commit, or echo secrets from `process.env` or `.env` files.

## Runtime Versions

**Status (verified 2026-10-27 at [Node.js Releases](https://nodejs.org/en/about/previous-releases)):**

| Major | Status |
| ----- | ------ |
| 26 | Current |
| 24 (Krypton) | LTS |
| 22 (Jod) | LTS |
| 20 and earlier | End of life |

- Target an Active or Maintenance LTS major for production; do not target
  Current or EOL releases.
- Starting with Node.js 27, every major becomes LTS after its Current phase.
  Re-check the schedule instead of assuming the even/odd rule.
- Declare the supported range in `package.json` `engines.node` (for example,
  `">=22"`) and keep CI and container images consistent with it.
- **Repository note**: the lab's `@types/node ^20` targets an EOL runtime.
  Upgrading it is a separate, approved change; do not upgrade it incidentally.

## @types/node

| Rule | Requirement |
| ---- | ----------- |
| TN-001 | Install `@types/node` as a `devDependency` only in projects that run on Node. Do not add it to browser-only code. |
| TN-002 | Match its major version to the lowest supported Node major (Node 22 → `@types/node` 22.x). A newer major exposes APIs the runtime lacks. |
| TN-003 | Under TypeScript 6.0+, list it explicitly: `"types": ["node"]`. The default `types` is `[]`, so globals such as `process` and built-in modules fail to resolve without it. |
| TN-004 | Update `@types/node` with the runtime upgrade, not independently. |
| TN-005 | Do not declare ad hoc `declare const process: any` or duplicate Node types. |

## package.json and Scripts

- Define the entry point and standard scripts; follow the lab's existing names:
  `build`, `start`, `dev`, `type-check`. Add `test` when tests exist.
- Set `"type"` explicitly (`"module"` or `"commonjs"`) for new packages.
- Use `npm ci` in CI and automated validation; use `npm install` only when
  intentionally changing dependencies.
- Use `npm ci --omit=dev` for production installs.
- Keep tool versions local (`devDependencies`) and invoke them through scripts.
- Apply version-range and approval rules from
  [Dependency Management](dependency-management-policy.instructions.md).

## Runtime Conventions

- Import built-ins with the `node:` prefix: `import { readFile } from "node:fs/promises";`
- Prefer `node:fs/promises`; avoid synchronous I/O except in startup code or
  short CLI scripts.
- Use the global `fetch`, `AbortController`, and `AbortSignal.timeout()` for
  HTTP calls with timeouts.
- Build file paths with `node:path` or `URL`, never string concatenation.
- Read configuration once at startup, validate it, and fail fast with a clear
  message. Use `node --env-file=.env` or the project's existing loader; keep
  `.env` out of source control.
- Set `process.exitCode` and let the event loop drain; call `process.exit()`
  only after output is flushed and cleanup is done.
- Handle `SIGINT`/`SIGTERM` in long-running services to close servers and
  connections.
- Treat `unhandledRejection` and `uncaughtException` handlers as last-resort
  logging, then exit; never use them for normal control flow.
- Native TypeScript execution: recent Node releases run TypeScript that uses
  only erasable syntax. Confirm support for the pinned version in the
  [Node.js TypeScript docs](https://nodejs.org/api/typescript.html) before
  relying on it; it does not type-check.

## Patterns and Anti-Patterns

✅ Async I/O with timeout and context:

```typescript
import { readFile } from "node:fs/promises";

export async function loadJson<T>(path: string): Promise<T> {
  const text = await readFile(path, "utf8");
  return JSON.parse(text) as T;
}

export async function getJson(url: string): Promise<unknown> {
  const response = await fetch(url, { signal: AbortSignal.timeout(5_000) });
  if (!response.ok) {
    throw new Error(`GET ${url} failed: ${response.status}`);
  }
  return response.json();
}
```

❌ Blocking I/O in a request path, unprefixed import, abrupt exit:

```typescript
import fs from "fs";

export function handler(): string {
  const data = fs.readFileSync("./data.json", "utf8");
  if (!data) process.exit(1);
  return data;
}
```

| ❌ Avoid | ✅ Use instead |
| -------- | -------------- |
| `fs.*Sync` in servers or hot paths | `node:fs/promises` |
| `process.exit()` inside library code | Throw; let the entry point set `process.exitCode` |
| `child_process.exec` with interpolated input | `execFile`/`spawn` with an argument array |
| Hard-coded secrets or ports | Validated environment configuration |
| Deprecated `new Buffer()` | `Buffer.from()` / `Buffer.alloc()` |
| `npm ci --only=production` | `npm ci --omit=dev` |

## Testing and Validation

- No test runner is configured in this repository. Prefer the project's existing
  runner; for new Node-only tests without dependencies, use `node:test` with
  `node:assert/strict` and ask before adding a framework.
- Confirm the runtime used: `node --version`.
- Lab validation (from the lab folder): `npm ci` or `npm install`, then
  `npm run type-check`, `npm run build`, and `npm start`.
- Follow [Test-Driven Development](test-driven-development.instructions.md).

## Validation Checklist

- [ ] Target Node major identified; it is an LTS release, or the exception is stated.
- [ ] Used APIs exist in the lowest supported major.
- [ ] `@types/node` major matches the runtime and is listed in `types` for TS 6.0+.
- [ ] Built-ins use the `node:` prefix; no new sync I/O in request paths.
- [ ] Configuration is validated; no secrets in code, logs, or commits.
- [ ] Build, type-check, and tests run, or failures are reported.

## Summary

- Target an LTS Node major and declare it in `engines`.
- Keep `@types/node` aligned with that major and list it in `types`.
- Use `node:` built-ins, promise APIs, timeouts, and validated configuration.
- Exit via `process.exitCode`; handle shutdown signals in services.

---

**Document Version**: 1.0.0
**Last Updated**: 2026-10-27
**Maintainer**: johnmillerATcodemag-com
**Related Instructions**: [TypeScript](typescript.instructions.md),
[JavaScript](javascript.instructions.md),
[Dependency Management](dependency-management-policy.instructions.md),
[Test-Driven Development](test-driven-development.instructions.md)
