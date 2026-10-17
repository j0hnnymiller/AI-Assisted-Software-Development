# AI Instruction Synchronization Script

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
