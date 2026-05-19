<#
.SYNOPSIS
Generate PPTX slide decks from course Markdown files using pandoc.

.DESCRIPTION
This script looks for slide Markdown files in the `Slides` folder for the
provided courses and runs pandoc to create .pptx slide decks.

By default it will process: Fundementals, Evergreen, Greenfield.
It will skip any course where the expected Markdown file is not found and
will report a summary at the end.

.EXAMPLE
# Generate the three default decks
.
\scripts\generate-slides.ps1

# Generate only Evergreen and Greenfield with slide level 3
.
\scripts\generate-slides.ps1 -Courses Evergreen,Greenfield -SlideLevel 3
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string[]]
    $Courses = @("Fundementals", "Evergreen", "Greenfield"),

    [int]
    $SlideLevel = 2
)

function Write-Info($msg) { Write-Host "[INFO]  $msg" -ForegroundColor Cyan }
function Write-Warn($msg) { Write-Host "[WARN]  $msg" -ForegroundColor Yellow }
function Write-Err($msg) { Write-Host "[ERROR] $msg" -ForegroundColor Red }

# Determine repository root (assumes this script lives in <repo>/scripts)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir "..")
$slidesDir = Join-Path $repoRoot "Slides"

Write-Info "Repository root: $repoRoot"
Write-Info "Slides directory: $slidesDir"

# Check for pandoc
$pandocCmd = Get-Command pandoc -ErrorAction SilentlyContinue
if (-not $pandocCmd) {
    Write-Err "pandoc not found in PATH. Please install pandoc and ensure it's on PATH."
    exit 2
}

$results = @()

foreach ($course in $Courses) {
    Write-Info "Processing course: $course"

    # Search for candidate markdown files that include the course token and end with -slides.md
    $candidates = Get-ChildItem -Path $slidesDir -Filter "*-slides.md" -File -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -match [regex]::Escape($course) -or $_.Name -match ($course -replace '\s', '') }

    if (-not $candidates -or $candidates.Count -eq 0) {
        Write-Warn "No slide Markdown found in '$slidesDir' for course token '$course'. Skipping."
        $results += [pscustomobject]@{ Course = $course; Status = 'Missing'; Source = $null; Output = $null }
        continue
    }

    if ($candidates.Count -gt 1) {
        Write-Warn "Multiple candidates found for '$course'. Using the first match: $($candidates[0].Name)"
    }

    $src = $candidates[0].FullName
    $out = [System.IO.Path]::ChangeExtension($src, '.pptx')

    Write-Info "Source: $src"
    Write-Info "Output: $out"

    try {
        # Run pandoc; include Slides directory in resource path so embedded images are resolved
        $resourcePath = $slidesDir
        & pandoc $src -o $out --slide-level=$SlideLevel --resource-path=$resourcePath
        if ($LASTEXITCODE -ne 0) {
            Write-Err "pandoc exited with code $LASTEXITCODE for course '$course'."
            $results += [pscustomobject]@{ Course = $course; Status = 'Failed'; Source = $src; Output = $out; ExitCode = $LASTEXITCODE }
        }
        else {
            Write-Info "Generated: $out"
            $results += [pscustomobject]@{ Course = $course; Status = 'OK'; Source = $src; Output = $out }
        }
    }
    catch {
        Write-Err "Exception while generating slides for '$course': $_"
        $results += [pscustomobject]@{ Course = $course; Status = 'Error'; Source = $src; Output = $out; Error = $_.Exception.Message }
    }
}

Write-Host "`nSummary:`n" -ForegroundColor Green
$results | Format-Table -AutoSize

# Exit with non-zero if any failures
if ($results | Where-Object { $_.Status -in @('Failed', 'Error', 'Missing') }) {
    Write-Warn "One or more courses were not successfully generated."
    exit 1
}

Write-Info "All requested slide decks generated successfully."
exit 0
