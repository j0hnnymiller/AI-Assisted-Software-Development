<#
.SYNOPSIS
Copies selected GitHub Copilot instruction/agent files from a source repo to a destination.

.PARAMETER SourceRoot
Root of the source repository (defaults to the path you provided).

.PARAMETER DestinationRoot
Root where files will be copied (defaults to current directory).

.PARAMETER WhatIf
If specified, runs as a dry-run.

.PARAMETER Force
If specified, allows replacement of read-only files. Normal files follow Copy-Item overwrite behavior.
#>

[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$SourceRoot = 'C:\git\AIASD\AI-Assisted-Software-Development',
    [string]$DestinationRoot = (Get-Location).Path,
    [switch]$Force
)

$patterns = @(
    '.github\agents\*.agent.md',
    '.github\instructions\ai-assisted-output.instructions.md',
    '.github\instructions\custom-agents.instructions.md',
    '.github\instructions\prompt-file.instructions.md',
    '.github\instructions\instruction-files.instructions.md',
    '.github\instructions\marp-slides.instructions.md'
)

if (-not (Test-Path -LiteralPath $SourceRoot -PathType Container)) {
    Write-Error "SourceRoot not found: $SourceRoot"
    exit 1
}

$SourceRoot = (Get-Item -LiteralPath $SourceRoot).FullName
$copied = @()
$planned = 0
$failed = 0
foreach ($pattern in $patterns) {
    $fullPattern = Join-Path -Path $SourceRoot -ChildPath $pattern
    try {
        if (-not (Test-Path -LiteralPath (Split-Path $fullPattern -Parent) -PathType Container -ErrorAction Stop)) {
            Write-Verbose "No source directory for $fullPattern"
            continue
        }
        $files = Get-ChildItem -LiteralPath (Split-Path $fullPattern -Parent) -Filter (Split-Path $fullPattern -Leaf) -File -ErrorAction Stop
    }
    catch {
        $failed++
        Write-Warning "Failed to enumerate $fullPattern`: $($_.Exception.Message)"
        continue
    }
    if (-not $files) {
        Write-Verbose "No matches for $fullPattern"
        continue
    }
    foreach ($item in $files) {
        $relative = $item.FullName.Substring($SourceRoot.Length).TrimStart('\', '/')
        $destPath = Join-Path $DestinationRoot $relative
        $destDir = Split-Path $destPath -Parent
        if (-not $PSCmdlet.ShouldProcess($destPath, "Copy $($item.FullName)")) {
            if ($WhatIfPreference) {
                $planned++
                Write-Output "Planned: $($item.FullName) -> $destPath"
            }
            continue
        }

        $copyParams = @{
            LiteralPath = $item.FullName
            Destination = $destPath
            ErrorAction = 'Stop'
        }
        if ($Force) { $copyParams['Force'] = $true }
        try {
            if (-not (Test-Path -LiteralPath $destDir -PathType Container -ErrorAction Stop)) {
                New-Item -ItemType Directory -Path $destDir -Force -ErrorAction Stop | Out-Null
            }
            Copy-Item @copyParams
            $copied += $destPath
            Write-Output "Copied: $($item.FullName) -> $destPath"
        }
        catch {
            $failed++
            Write-Warning "Failed to copy $($item.FullName): $($_.Exception.Message)"
        }
    }
}

if ($WhatIfPreference) {
    Write-Output "Total files planned: $planned"
}
elseif ($copied.Count -eq 0) {
    Write-Warning "No files copied. Use `-Verbose` or run with `-WhatIf` to verify patterns and paths."
}
else {
    Write-Output "Total files copied: $($copied.Count)"
}

if ($failed -gt 0) {
    Write-Warning "Total operations failed: $failed"
    exit 1
}

exit 0
