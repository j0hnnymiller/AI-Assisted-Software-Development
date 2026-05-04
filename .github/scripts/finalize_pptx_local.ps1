param(
    [Parameter(Mandatory = $true)]
    [string]$Path,

    [Parameter(Mandatory = $false)]
    [string]$OutputPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Resolve-FullPath {
    param([Parameter(Mandatory = $true)][string]$InputPath)

    if ([System.IO.Path]::IsPathRooted($InputPath)) {
        return [System.IO.Path]::GetFullPath($InputPath)
    }

    return [System.IO.Path]::GetFullPath((Join-Path (Get-Location) $InputPath))
}

function Get-TextFrame2AvailableHeight {
    param(
        [Parameter(Mandatory = $true)]$Shape,
        [Parameter(Mandatory = $true)]$TextFrame2
    )

    $available = [double]$Shape.Height - [double]$TextFrame2.MarginTop - [double]$TextFrame2.MarginBottom
    if ($available -lt 1.0) {
        return 1.0
    }
    return $available
}

function Reduce-TextUntilFits {
    param(
        [Parameter(Mandatory = $true)]$Shape,
        [Parameter(Mandatory = $true)]$TextFrame2,
        [double]$MinFontSize = 14.0,
        [double]$Step = 0.5
    )

    try {
        $textRange = $TextFrame2.TextRange
        $availableHeight = Get-TextFrame2AvailableHeight -Shape $Shape -TextFrame2 $TextFrame2
        $boundHeight = [double]$textRange.BoundHeight

        if ($boundHeight -le $availableHeight) {
            return $false
        }

        $currentSize = [double]$textRange.Font.Size
        if ($currentSize -le 0) {
            # Mixed or undefined size; use a conservative starting point.
            $currentSize = 24.0
        }

        for ($size = $currentSize; $size -ge $MinFontSize; $size -= $Step) {
            $textRange.Font.Size = $size
            if ([double]$textRange.BoundHeight -le $availableHeight) {
                return $true
            }
        }

        return $false
    }
    catch {
        return $false
    }
}

function Force-ShrinkToFitTextFrame2 {
    param(
        [Parameter(Mandatory = $true)]$Shape,
        [Parameter(Mandatory = $true)]$TextFrame2
    )

    # Office MsoAutoSize constants:
    # 0 = msoAutoSizeNone
    # 2 = msoAutoSizeTextToFitShape ("Shrink text on overflow")
    try {
        $TextFrame2.WordWrap = -1
    }
    catch {
        # Ignore frames that do not support word wrap changes.
    }

    try {
        $TextFrame2.AutoSize = 0
        $TextFrame2.AutoSize = 2
        # If PowerPoint still doesn't recalculate shrink at open time, apply
        # deterministic fallback by reducing font until the text bounds fit.
        $fallbackApplied = Reduce-TextUntilFits -Shape $Shape -TextFrame2 $TextFrame2
        if ($fallbackApplied) {
            return "fallback"
        }
        return "updated"
    }
    catch {
        # Some frame types (for example certain table cell frames) can reject this mode.
        return "skipped"
    }
}

$inputFullPath = Resolve-FullPath -InputPath $Path
if (-not (Test-Path -LiteralPath $inputFullPath)) {
    throw "Input PPTX not found: $inputFullPath"
}

$targetFullPath = if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    $inputFullPath
}
else {
    Resolve-FullPath -InputPath $OutputPath
}

if ($targetFullPath -ne $inputFullPath) {
    $targetDir = Split-Path -Parent $targetFullPath
    if (-not (Test-Path -LiteralPath $targetDir)) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }
    Copy-Item -LiteralPath $inputFullPath -Destination $targetFullPath -Force
}

$powerPoint = $null
$presentation = $null

try {
    $powerPoint = New-Object -ComObject PowerPoint.Application
    $powerPoint.Visible = -1

    # Open(FileName, ReadOnly, Untitled, WithWindow)
    $presentation = $powerPoint.Presentations.Open($targetFullPath, $false, $false, $false)

    $updatedTextFrames = 0
    $fallbackAdjustedTextFrames = 0
    $skippedTextFrames = 0

    foreach ($slide in $presentation.Slides) {
        foreach ($shape in $slide.Shapes) {
            if ($shape.HasTextFrame -eq -1) {
                $textFrame2 = $shape.TextFrame2
                if ($null -ne $textFrame2) {
                    $status = Force-ShrinkToFitTextFrame2 -Shape $shape -TextFrame2 $textFrame2
                    if ($status -eq "updated") {
                        $updatedTextFrames++
                    }
                    elseif ($status -eq "fallback") {
                        $updatedTextFrames++
                        $fallbackAdjustedTextFrames++
                    }
                    else {
                        $skippedTextFrames++
                    }
                }
            }

            if ($shape.HasTable -eq -1) {
                $rows = $shape.Table.Rows.Count
                $cols = $shape.Table.Columns.Count
                for ($r = 1; $r -le $rows; $r++) {
                    for ($c = 1; $c -le $cols; $c++) {
                        $cellTextFrame2 = $shape.Table.Cell($r, $c).Shape.TextFrame2
                        if ($null -ne $cellTextFrame2) {
                            $cellShape = $shape.Table.Cell($r, $c).Shape
                            $status = Force-ShrinkToFitTextFrame2 -Shape $cellShape -TextFrame2 $cellTextFrame2
                            if ($status -eq "updated") {
                                $updatedTextFrames++
                            }
                            elseif ($status -eq "fallback") {
                                $updatedTextFrames++
                                $fallbackAdjustedTextFrames++
                            }
                            else {
                                $skippedTextFrames++
                            }
                        }
                    }
                }
            }
        }
    }

    $presentation.Save()
    Write-Host "Finalized PPTX: $targetFullPath"
    Write-Host "Updated text frames: $updatedTextFrames"
    Write-Host "Fallback-adjusted text frames: $fallbackAdjustedTextFrames"
    Write-Host "Skipped text frames: $skippedTextFrames"
}
finally {
    if ($null -ne $presentation) {
        $presentation.Close()
        [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($presentation)
    }
    if ($null -ne $powerPoint) {
        $powerPoint.Quit()
        [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($powerPoint)
    }

    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
