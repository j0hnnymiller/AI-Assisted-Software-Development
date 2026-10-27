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
  - task: "Repository evidence review"
    duration: "00:03:00"
  - task: "JavaScript instruction authoring"
    duration: "00:12:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/10/27/92373087-9b97-420d-a3ac-53f20e65be8a/conversation.md"
source: "User request; generate-instructions skill; repository scan found no first-party JavaScript source"
name: javascript
description: "Use when writing or reviewing plain JavaScript (.js, .jsx, .mjs, .cjs) or jsconfig files; covers module format, modern syntax, JSDoc type checking, async error handling, and validation."
applyTo: "**/*.js,**/*.jsx,**/*.mjs,**/*.cjs,**/jsconfig*.json"
version: "1.0.0"
author: "johnmillerATcodemag-com"
tags: ["javascript", "ecmascript", "jsdoc", "modules"]
owner: "johnmillerATcodemag-com"
reviewedDate: "2026-10-27"
nextReview: "2027-01-27"
---

# JavaScript Instructions

## Overview

Rules for hand-written JavaScript source and `jsconfig*.json`.

- **Audience**: AI assistants (primary), developers
- **Scope**: syntax, modules, typing through JSDoc, error handling, validation
- **Out of scope**: TypeScript source and compiler settings (see
  [TypeScript](typescript.instructions.md)); runtime APIs, packages, and
  `@types/node` (see [Node.js](nodejs.instructions.md))
- **Repository evidence**: no first-party `.js`, `.mjs`, or `.cjs` source exists.
  The TypeScript lab emits JavaScript to `dist/`, which is git-ignored. These
  rules are recommendations until a JavaScript project defines its own.

## Table of Contents

- [AI Assistant Guidelines](#ai-assistant-guidelines)
- [Module Format](#module-format)
- [Language Conventions](#language-conventions)
- [Type Checking with JSDoc](#type-checking-with-jsdoc)
- [Patterns and Anti-Patterns](#patterns-and-anti-patterns)
- [Testing and Validation](#testing-and-validation)
- [Validation Checklist](#validation-checklist)
- [Summary](#summary)

## AI Assistant Guidelines

1. NEVER edit generated JavaScript (`dist/`, `build/`, `*.min.js`); change the
   source and rebuild.
2. Determine the module format before editing (see below); do not mix `require`
   and `import` in one file.
3. Match the project's existing linter and formatter; do not add tools without
   approval.
4. Handle every promise: `await` it, return it, or attach a rejection handler.
5. Report the validation command run and its result.

## Module Format

| Signal | Format | Syntax |
| ------ | ------ | ------ |
| `.mjs` | ES module | `import` / `export` |
| `.cjs` | CommonJS | `require` / `module.exports` |
| `.js` + nearest `package.json` has `"type": "module"` | ES module | `import` / `export` |
| `.js` + no `"type"` or `"type": "commonjs"` | CommonJS (Node) | `require` / `module.exports` |
| `.js` loaded by `<script type="module">` or a bundler | ES module | `import` / `export` |

- Prefer ES modules for new projects.
- In Node ES modules, include file extensions in relative imports
  (`./book.js`), and use `import.meta.dirname` / `import.meta.filename`
  instead of `__dirname` / `__filename` where the runtime supports them.

## Language Conventions

- Use `const` by default, `let` when reassigned; NEVER `var`.
- Use strict equality (`===`, `!==`).
- Use template literals, optional chaining (`?.`), and nullish coalescing (`??`).
  Use `??` rather than `||` when `0`, `""`, or `false` are valid values.
- Use `class` syntax and `#private` fields for encapsulated state.
- Use named exports; avoid default exports unless a framework requires them.
- Naming: PascalCase for classes, camelCase for functions and variables.
- Throw `Error` subclasses, never strings; preserve causes with
  `new Error(message, { cause })`.
- Do not modify built-in prototypes or rely on implicit globals.

## Type Checking with JSDoc

Use JSDoc types when a JavaScript project needs type safety without a build step.

```javascript
// @ts-check

/**
 * @param {readonly { title: string, author: string }[]} books
 * @param {string} term
 * @returns {{ title: string, author: string }[]}
 */
export function searchBooks(books, term) {
  const needle = term.toLowerCase();
  return books.filter(
    (b) => b.title.toLowerCase().includes(needle) || b.author.toLowerCase().includes(needle)
  );
}
```

- Enable project-wide checking with `jsconfig.json` (`"checkJs": true`) or
  per file with `// @ts-check`.
- Apply the [TypeScript](typescript.instructions.md) compiler-option rules to
  `jsconfig.json`.

## Patterns and Anti-Patterns

✅ Await and propagate with context:

```javascript
export async function loadCatalog(readFile, path) {
  try {
    return JSON.parse(await readFile(path, "utf8"));
  } catch (error) {
    throw new Error(`Failed to load catalog from ${path}`, { cause: error });
  }
}
```

❌ Floating promise and swallowed error:

```javascript
function loadCatalog(path) {
  readFile(path).then((text) => JSON.parse(text)).catch(() => {});
}
```

| ❌ Avoid | ✅ Use instead |
| -------- | -------------- |
| `var`, `==` | `const`/`let`, `===` |
| `eval`, `new Function`, string `setTimeout` | Direct function calls |
| Callback pyramids | `async`/`await` |
| `array.forEach(async ...)` expecting sequencing | `for...of` with `await`, or `Promise.all` |
| Mutating function arguments | Return new values |
| Editing compiled output | Edit source and rebuild |

## Testing and Validation

- No JavaScript test runner or linter is configured in this repository. Use the
  project's runner if present; otherwise propose one before adding it. For
  Node-only code, `node:test` and `node:assert/strict` need no dependencies.
- Syntax-check a single file without running it: `node --check <file>`.
- Follow [Test-Driven Development](test-driven-development.instructions.md).

## Validation Checklist

- [ ] Module format matches file extension and `package.json` `"type"`.
- [ ] No `var`, `==`, `eval`, or floating promises introduced.
- [ ] Errors are `Error` instances with context and preserved `cause`.
- [ ] Generated output was not edited.
- [ ] Existing lint, type-check (`checkJs`), and tests pass, or failures are reported.

## Summary

- Determine module format first; never mix CommonJS and ES module syntax.
- Write modern, strict-equality, `const`-first JavaScript.
- Use JSDoc with `checkJs` for type safety without a build step.
- Handle every promise and preserve error causes.

---

**Document Version**: 1.0.0
**Last Updated**: 2026-10-27
**Maintainer**: johnmillerATcodemag-com
**Related Instructions**: [TypeScript](typescript.instructions.md),
[Node.js](nodejs.instructions.md),
[Test-Driven Development](test-driven-development.instructions.md)
