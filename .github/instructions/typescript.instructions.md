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
  - task: "Repository evidence and release-status verification"
    duration: "00:05:00"
  - task: "TypeScript instruction authoring"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/10/27/92373087-9b97-420d-a3ac-53f20e65be8a/conversation.md"
source: "User request; generate-instructions skill; evidence from !here-be-dragons/Labs/lab1-3-typescript and TypeScript 6.0/7.0 release notes"
name: typescript
description: "Use when writing, reviewing, or configuring TypeScript source, declaration files, or tsconfig; covers strict typing, module settings, the typescript compiler package, and TS 6/7 migration checks."
applyTo: "**/*.ts,**/*.tsx,**/*.mts,**/*.cts,**/tsconfig*.json"
version: "1.0.0"
author: "johnmillerATcodemag-com"
tags: ["typescript", "tsconfig", "compiler", "types"]
owner: "johnmillerATcodemag-com"
reviewedDate: "2026-10-27"
nextReview: "2027-01-27"
---

# TypeScript Instructions

## Overview

Rules for TypeScript source (`.ts`, `.tsx`, `.mts`, `.cts`, `.d.ts`) and
`tsconfig*.json`, including the `typescript` compiler package.

- **Audience**: AI assistants (primary), developers
- **Scope**: language usage, compiler configuration, compiler version handling
- **Out of scope**: runtime APIs and `@types/node` (see
  [Node.js](nodejs.instructions.md)); plain JavaScript (see
  [JavaScript](javascript.instructions.md))
- **Repository evidence**: the only TypeScript project is
  `!here-be-dragons/Labs/lab1-3-typescript` (training lab, `typescript ^5.0.0`,
  `strict: true`, `module: commonjs`, no linter, formatter, or test runner).
  Treat its settings as a lab baseline, not a repository-wide standard.

## Table of Contents

- [AI Assistant Guidelines](#ai-assistant-guidelines)
- [Compiler Package and Versions](#compiler-package-and-versions)
- [tsconfig Rules](#tsconfig-rules)
- [Language Conventions](#language-conventions)
- [Patterns and Anti-Patterns](#patterns-and-anti-patterns)
- [Testing and Validation](#testing-and-validation)
- [Validation Checklist](#validation-checklist)
- [Summary](#summary)

## AI Assistant Guidelines

1. Read the nearest `package.json` and `tsconfig*.json` before editing; follow the
   project's installed TypeScript version, module system, and style.
2. Keep `strict` enabled. NEVER weaken compiler options to silence an error.
3. Prefer precise types over `any`; use `unknown` at untrusted boundaries and
   narrow before use.
4. Run the project's type-check script after changes and report the result.
5. Do not upgrade `typescript` or change `module`, `moduleResolution`, or
   `target` unless the task requires it; state the impact when you do.

## Compiler Package and Versions

| Rule | Requirement |
| ---- | ----------- |
| TS-001 | Install `typescript` as a project `devDependency`; do not rely on a global `tsc`. |
| TS-002 | Run the compiler through npm scripts (`npm run build`, `npm run type-check`) or `npx tsc` **only after** dependencies are installed. Without a local install, `npx tsc` resolves the unrelated npm package `tsc`. |
| TS-003 | Commit the lockfile so the resolved compiler version is reproducible. |
| TS-004 | Treat a TypeScript major-version change as a migration: read the release notes, run the type-check, and record config changes. |

**Version facts (verified 2026-10-27; re-check release notes before relying on them):**

- TypeScript 6.0 is the bridge release to the native (Go) 7.x compiler. It
  deprecates options that 7.x no longer supports.
- TypeScript 6.0 changes defaults: `strict` → `true`, `module` → `esnext`,
  `target` → latest ES version, and `types` → `[]` (no automatic `@types/*`
  inclusion).
- Deprecated in 6.0: `moduleResolution node`/`node10` and `classic`,
  `target es5`, `downlevelIteration`, `baseUrl`, and setting `esModuleInterop`
  or `allowSyntheticDefaultImports` to `false`.
- TypeScript 7.0 is released. Verify package name, editor integration, and
  supported options in the [TypeScript releases](https://github.com/microsoft/TypeScript/releases)
  before upgrading.

## tsconfig Rules

- Set options explicitly instead of relying on defaults that changed in 6.0:
  `strict`, `module`, `moduleResolution` (when not implied), `target`,
  `rootDir`, and `types`.
- Choose module settings by runtime:

  | Project type | `module` | `moduleResolution` |
  | ------------ | -------- | ------------------ |
  | Node.js app or library | `nodenext` | (implied `nodenext`) |
  | Bundled web app | `preserve` or `esnext` | `bundler` |
  | Legacy CommonJS (migrating) | `commonjs` | `bundler` (TS 6.0+) or plan `nodenext` |

- List ambient type packages explicitly, for example `"types": ["node"]`.
- Keep `skipLibCheck: true` only as a build-speed choice; do not use it to hide
  errors in your own `.d.ts` files.
- Keep `outDir` and `rootDir` explicit when emitting, so output paths do not move.

✅ Explicit, upgrade-safe Node configuration:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "nodenext",
    "rootDir": "./src",
    "outDir": "./dist",
    "strict": true,
    "types": ["node"],
    "declaration": true,
    "sourceMap": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"]
}
```

❌ Relies on deprecated and changed defaults (lab baseline; fails or changes
behavior under TS 6.0+):

```json
{
  "compilerOptions": {
    "module": "commonjs",
    "outDir": "./dist"
  }
}
```

Through TypeScript 5.x, `module: commonjs` without `moduleResolution` implies
the now-deprecated `node10` resolution; under TS 6.0+, the missing `types`
array also drops `@types/node` globals such as `console` and `process`.

## Language Conventions

### Naming

| Element | Convention | Example |
| ------- | ---------- | ------- |
| Classes, interfaces, types, enums | PascalCase | `Library`, `BookSummary` |
| Functions, methods, variables | camelCase | `searchBooks`, `isAvailable` |
| Module-level constants | camelCase or UPPER_SNAKE_CASE; match the file | `maxResults` |
| Files | match project convention (lab uses lowercase: `book.ts`) | `library.ts` |

Do not prefix interfaces with `I`.

### Organization

- One primary export per module; keep helpers in a separate module (lab:
  `utils.ts`).
- Use named exports; avoid default exports unless a framework requires them.
- Use `import type` for type-only imports.
- Document exported APIs with JSDoc summaries (lab pattern: `/** Represents a book... */`).

### Typing

- Annotate exported function parameters and return types; let locals infer.
- Use `readonly` and `ReadonlyArray<T>` for data that callers must not mutate.
- Return copies of internal collections (lab: `return [...this.books]`).
- Model alternatives with discriminated unions, not optional-flag combinations.
- Use `satisfies` to check object literals without widening.
- Prefer `undefined` for absence; do not mix `null` and `undefined` without reason.

## Patterns and Anti-Patterns

✅ Narrow `unknown` at boundaries:

```typescript
export function parseYear(input: unknown): number {
  const year = typeof input === "string" ? Number.parseInt(input, 10) : NaN;
  if (!Number.isInteger(year)) {
    throw new RangeError(`Invalid year: ${String(input)}`);
  }
  return year;
}
```

❌ Silence the checker:

```typescript
export function parseYear(input: any) {
  return input as number; // no validation; unsafe cast
}
```

| ❌ Avoid | ✅ Use instead |
| -------- | -------------- |
| `any`, `as any`, `// @ts-ignore` | `unknown` + narrowing; `// @ts-expect-error` with a reason only when unavoidable |
| Non-null assertion `value!` on unchecked data | Explicit check or optional chaining |
| `enum` in code run by Node type stripping | `as const` objects or union literals |
| `namespace` for module organization | ES modules |
| Logging inside domain classes (lab simplification) | Return results; log at the application edge |
| Turning off `strict` or a strict sub-flag | Fix the type error |

## Testing and Validation

- No test framework is configured in this repository. Follow
  [Test-Driven Development](test-driven-development.instructions.md) and use the
  project's existing runner; ask before adding one. For Node-only code,
  `node:test` avoids new dependencies.
- Confirmed lab commands (run from the lab folder after `npm install`):
  - `npm run type-check` (`tsc --noEmit`)
  - `npm run build` (`tsc`)
- Report the compiler version used (`npx tsc --version` after install).

## Validation Checklist

- [ ] `strict` remains enabled; no new `any`, `@ts-ignore`, or unchecked `!`.
- [ ] Exported functions have explicit parameter and return types.
- [ ] `module`, `moduleResolution`, `target`, `rootDir`, and `types` are explicit
      in changed `tsconfig` files.
- [ ] No option deprecated in TypeScript 6.0 is added.
- [ ] `typescript` is a local `devDependency`; lockfile updated with any change.
- [ ] Type-check passes, or the failure is reported with its output.

## Summary

- Keep strict typing; narrow `unknown` instead of using `any`.
- Make compiler options explicit; TypeScript 6.0 changed defaults and 7.x drops
  deprecated options.
- Use the project-local `typescript` package through npm scripts.
- Validate with the project's type-check command.

---

**Document Version**: 1.0.0
**Last Updated**: 2026-10-27
**Maintainer**: johnmillerATcodemag-com
**Related Instructions**: [JavaScript](javascript.instructions.md),
[Node.js](nodejs.instructions.md),
[Dependency Management](dependency-management-policy.instructions.md),
[Test-Driven Development](test-driven-development.instructions.md)
