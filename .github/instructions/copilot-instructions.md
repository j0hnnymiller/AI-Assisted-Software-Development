---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "prompt-file.instructions-2025-10-15"
prompt: |
  Consolidate all Copilot-specific instructions into a single copilot-instructions.md file
  that can be referenced from other meta-prompts, prompts, and instruction files.
started: "2025-10-15T16:00:00Z"
ended: "2025-10-15T16:15:00Z"
task_durations:
  - task: "requirements consolidation"
    duration: "00:10:00"
  - task: "file creation"
    duration: "00:05:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*"
---

# GitHub Copilot Instructions for AI-Assisted Development

## Overview

This document provides comprehensive instructions for GitHub Copilot when working in this repository. These instructions ensure consistent, compliant, and high-quality AI-assisted outputs with proper provenance tracking.

**Scope**: All AI-assisted work in this repository must follow these instructions.

## Core Principles

### Excluded Context

- Never read, search, quote, summarize, attach, or otherwise include files or content from `!here-be-dragons/` in any request, prompt, tool call, or response. Apply this exclusion to every task. If relevant material is needed, ask the user to provide it outside that folder.

