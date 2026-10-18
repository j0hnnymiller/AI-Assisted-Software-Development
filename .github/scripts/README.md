---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
prompt: |
  go ahead
started: "2026-10-18T12:55:34.864-07:00"
ended: "2026-10-18T12:57:39.092-07:00"
task_durations:
  - task: "Copy helper remediation and focused Pester validation"
    duration: "00:02:04"
total_duration: "00:02:04"
ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
source: "User approval of the copy-helper remediation recommendations"
---

# AI Instruction Copy and Synchronization Scripts

This directory contains the PowerShell script that synchronizes copies of `ai-assisted-output.instructions.md` across repositories under `C:\git`.

## `sync-ai-instructions.ps1`

Run from the repository root:

```powershell
# Preview what would change
.\.github\scripts\sync-ai-instructions.ps1 -WhatIf

# Synchronize outdated copies
.\.github\scripts\sync-ai-instructions.ps1
```

| Parameter | Description |
| --- | --- |
| `-WhatIf` | Show planned updates without changing files |
| `-Force` | Update all discovered copies regardless of their age |
| `-Backup` | Create backups before updating files |
| `-Detailed` | Show detailed progress |

The script's search root and canonical source path are configured in the script. Review those values before running it in a different environment.

## `copy-copilot-files.ps1`

Copies selected agent and instruction files from a source repository. Deprecated prompt
files are excluded. This is a simple copy helper, not the cross-repository configuration
sync workflow: it does not compare lineage, create branches, or update the sync manifest.

```powershell
.\.github\scripts\copy-copilot-files.ps1 -DestinationRoot C:\path\to\target -WhatIf
.\.github\scripts\copy-copilot-files.ps1 -DestinationRoot C:\path\to\target
```

- `-SourceRoot` defaults to `C:\git\AIASD\AI-Assisted-Software-Development`.
- `-DestinationRoot` defaults to the current directory.
- `-WhatIf` reports planned copies without creating directories or changing files.
- `-Force` passes PowerShell's force option to copying, including read-only file replacement.
- Existing files follow `Copy-Item` overwrite behavior even without `-Force`.
- Completed copies are counted only after success. Enumeration, directory creation, and
  copy failures are reported and return exit code 1; successful operations return 0.
- Missing optional source directories or unmatched patterns are skipped; no matches produce
  a warning (or a zero planned count in preview), not a copy failure.

Run the focused regression tests with the existing Pester installation:

```powershell
Invoke-Pester -Path .\.github\scripts\tests\copy-copilot-files.Tests.ps1 -Output Detailed
```
