# PowerShell script to convert PPTX to Markdown via DOCX
param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath
)

try {
    # Check if input file exists
    if (-not (Test-Path $InputPath)) {
        throw "Input file not found: $InputPath"
    }

    # Get absolute paths
    $InputPath = Resolve-Path $InputPath
    $TempDocx = [System.IO.Path]::ChangeExtension($InputPath, ".docx")

    Write-Host "Converting PPTX to DOCX..."

    # Create PowerPoint application
    $PowerPoint = New-Object -ComObject PowerPoint.Application
    $PowerPoint.Visible = $false

    # Open the presentation
    $Presentation = $PowerPoint.Presentations.Open($InputPath)

    # Save as DOCX (outline format)
    $Presentation.SaveAs($TempDocx, 16) # 16 = ppSaveAsRTF, but we'll use Export
    $Presentation.Export($TempDocx, "RTF")

    # Close and cleanup
    $Presentation.Close()
    $PowerPoint.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($PowerPoint) | Out-Null

    Write-Host "Converting DOCX to Markdown..."

    # Use Pandoc to convert DOCX to Markdown
    $pandocArgs = @($TempDocx, "-o", $OutputPath, "--wrap=none")
    & pandoc @pandocArgs

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Successfully converted to: $OutputPath" -ForegroundColor Green

        # Clean up temporary DOCX file
        if (Test-Path $TempDocx) {
            Remove-Item $TempDocx
        }
    }
    else {
        throw "Pandoc conversion failed with exit code: $LASTEXITCODE"
    }

}
catch {
    Write-Error "Conversion failed: $($_.Exception.Message)"

    # Cleanup on error
    if ($PowerPoint) {
        try {
            $PowerPoint.Quit()
            [System.Runtime.Interopservices.Marshal]::ReleaseComObject($PowerPoint) | Out-Null
        }
        catch {}
    }

    exit 1
}
