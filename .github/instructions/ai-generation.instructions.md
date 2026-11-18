---
applyTo: "**/*"
---

# AI-Assisted Output Instructions

## Overview

This repository requires provenance and chat linkage for AI-assisted artifacts. Keep metadata complete, logs traceable, and instructions concise for both humans and AI agents.

## Audience

Contributors generating or curating AI-assisted content (code, docs, diagrams, tests, data).

## Scope

- Require README updates for durable artifacts.
- Prefer concise, AI-readable outputs that minimize token use (except files in `docs/`, all README files, and files in the project root, which target human technical readers).

## Terminology

- Do not output `U+2011`; use `-` instead.
- Do not output `U+2019`; use `'` instead.

### Required post-creation steps

1. Update `README.md` for durable artifacts with a short description and link.

## Placement and naming

- Place this file at `.github/instructions/ai-generation.instructions.md`.
- Prefer lowercase descriptive artifact filenames using kebab case.
- README entries are required for durable artifacts; optional for temporary drafts.
- For human-facing writing standards, follow [Human-Facing Writing Instructions](human-facing-writing.instructions.md).
- Files in `docs/`, all README files (e.g., `README.md`, `docs/README.md`), and files in the project root are exempt from token optimization requirements and should target human technical readers with full detail and explanation.
- In those human-facing files, avoid AI slop: no generic filler, repetition, vague claims, inflated introductions, canned conclusions, or polished text without concrete information.

## Quality checklist

- [ ] README updated for durable artifacts
- [ ] No secrets/credentials in logs or prompts
- [ ] Content is concise and token-optimized (except `docs/` files, README files, and project root files, which prioritize human readability)

## PR checklist

- [ ] README updates included where required

