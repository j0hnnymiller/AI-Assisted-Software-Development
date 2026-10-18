BeforeAll {
    $scriptPath = Join-Path $PSScriptRoot '..\copy-copilot-files.ps1'
}

Describe 'copy-copilot-files' {
    BeforeEach {
        $source = Join-Path $TestDrive ([guid]::NewGuid().ToString())
        $destination = Join-Path $TestDrive ([guid]::NewGuid().ToString())
        $instructions = Join-Path $source '.github\instructions'
        $agents = Join-Path $source '.github\agents'
        $prompts = Join-Path $source '.github\prompts'
        New-Item -ItemType Directory -Path $instructions, $agents, $prompts | Out-Null
        Set-Content -LiteralPath (Join-Path $instructions 'ai-assisted-output.instructions.md') -Value 'instruction'
        Set-Content -LiteralPath (Join-Path $agents 'example.agent.md') -Value 'agent'
        Set-Content -LiteralPath (Join-Path $prompts 'check-context.prompt.md') -Value 'retired prompt'
    }

    It 'previews without creating the destination or reporting completed copies' {
        $output = & pwsh -NoProfile -File $scriptPath -SourceRoot $source -DestinationRoot $destination -WhatIf 2>&1
        $LASTEXITCODE | Should -Be 0
        Test-Path -LiteralPath $destination | Should -BeFalse
        ($output -join "`n") | Should -Match 'Total files planned: 2'
        ($output -join "`n") | Should -Not -Match 'Copied:|Total files copied:'
    }

    It 'leaves existing destination contents unchanged during preview with Force' {
        New-Item -ItemType Directory -Path (Join-Path $destination '.github\instructions') -Force | Out-Null
        $existing = Join-Path $destination '.github\instructions\ai-assisted-output.instructions.md'
        Set-Content -LiteralPath $existing -Value 'original'
        $before = (Get-FileHash -LiteralPath $existing).Hash
        & pwsh -NoProfile -File $scriptPath -SourceRoot $source -DestinationRoot $destination -WhatIf -Force | Out-Null
        $LASTEXITCODE | Should -Be 0
        (Get-FileHash -LiteralPath $existing).Hash | Should -Be $before
        Test-Path -LiteralPath (Join-Path $destination '.github\agents') | Should -BeFalse
    }

    It 'copies agents and instructions but never retired prompts' {
        $output = & pwsh -NoProfile -File $scriptPath -SourceRoot "$source\" -DestinationRoot $destination 2>&1
        $LASTEXITCODE | Should -Be 0
        Get-Content -LiteralPath (Join-Path $destination '.github\agents\example.agent.md') | Should -Be 'agent'
        Get-Content -LiteralPath (Join-Path $destination '.github\instructions\ai-assisted-output.instructions.md') | Should -Be 'instruction'
        Test-Path -LiteralPath (Join-Path $destination '.github\prompts') | Should -BeFalse
        ($output -join "`n") | Should -Match 'Total files copied: 2'
        ($output -join "`n") | Should -Not -Match 'Planned:'
    }

    It 'fails when directory creation is blocked instead of reporting successful copies' {
        New-Item -ItemType Directory -Path $destination | Out-Null
        Set-Content -LiteralPath (Join-Path $destination '.github') -Value 'blocking file'
        $output = & pwsh -NoProfile -File $scriptPath -SourceRoot $source -DestinationRoot $destination 2>&1
        $LASTEXITCODE | Should -Be 1
        ($output -join "`n") | Should -Match 'Failed to copy|Total operations failed:'
        ($output -join "`n") | Should -Not -Match 'Copied:|Total files copied:'
    }

    It 'returns failure for a blocked copy while still counting completed files' {
        $blockedTarget = Join-Path $destination '.github\agents\example.agent.md'
        New-Item -ItemType Directory -Path $blockedTarget -Force | Out-Null
        Set-Content -LiteralPath (Join-Path $blockedTarget 'example.agent.md') -Value 'read-only'
        $blockedFile = Get-Item -LiteralPath (Join-Path $blockedTarget 'example.agent.md')
        $blockedFile.IsReadOnly = $true
        try {
            $output = & pwsh -NoProfile -File $scriptPath -SourceRoot $source -DestinationRoot $destination 2>&1
            $LASTEXITCODE | Should -Be 1
            ($output -join "`n") | Should -Match 'Total operations failed: 1'
            ($output -join "`n") | Should -Match 'Total files copied: 1'
        }
        finally {
            $blockedFile.IsReadOnly = $false
        }
    }

    It 'returns failure for a missing source root' {
        & pwsh -NoProfile -File $scriptPath -SourceRoot (Join-Path $TestDrive 'missing') -DestinationRoot $destination 2>&1 | Out-Null
        $LASTEXITCODE | Should -Be 1
        Test-Path -LiteralPath $destination | Should -BeFalse
    }

    It 'skips absent optional directories and unmatched patterns without treating them as failures' {
        $emptySource = Join-Path $TestDrive 'empty-source'
        New-Item -ItemType Directory -Path $emptySource | Out-Null
        $output = & pwsh -NoProfile -File $scriptPath -SourceRoot $emptySource -DestinationRoot $destination 2>&1
        $LASTEXITCODE | Should -Be 0
        ($output -join "`n") | Should -Match 'No files copied'
        Test-Path -LiteralPath $destination | Should -BeFalse
    }

    It 'preserves Force support for overwriting a read-only target' {
        New-Item -ItemType Directory -Path (Join-Path $destination '.github\agents') -Force | Out-Null
        $existing = Join-Path $destination '.github\agents\example.agent.md'
        Set-Content -LiteralPath $existing -Value 'original'
        $existingFile = Get-Item -LiteralPath $existing
        $existingFile.IsReadOnly = $true
        try {
            & pwsh -NoProfile -File $scriptPath -SourceRoot $source -DestinationRoot $destination -Force | Out-Null
            $LASTEXITCODE | Should -Be 0
            Get-Content -LiteralPath $existing | Should -Be 'agent'
        }
        finally {
            (Get-Item -LiteralPath $existing).IsReadOnly = $false
        }
    }
}
