BeforeAll {
    $scriptPath = Join-Path $PSScriptRoot '..\..\skills\github-config-distribute\scripts\Sync-GithubConfig.ps1'
    Import-Module (Join-Path $PSScriptRoot '..\..\skills\github-config-inventory\scripts\GithubConfigSync.psm1') -Force

    function Write-Config($Repository, $Name, $Content) {
        $file = Join-Path $Repository ".github\$Name"
        New-Item -ItemType Directory -Path (Split-Path $file) -Force | Out-Null
        Set-Content -LiteralPath $file -Value $Content
    }

    function Save-Repository($Repository) {
        git -C $Repository add --all
        git -C $Repository -c user.name=Test -c user.email=test@example.invalid commit --quiet -m fixture
        if ($LASTEXITCODE) { throw "Fixture commit failed: $Repository" }
    }

    function Invoke-Plan([hashtable]$Options = @{}) {
        $manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $manifestPath
        & $scriptPath -CanonicalRepo $hub -ManifestPath $manifestPath -ReportFile $reportPath @Options | Out-Null
        Get-Content -LiteralPath $reportPath -Raw | ConvertFrom-Json
    }
}

Describe 'Complete config distribution plans' {
    BeforeEach {
        $root = Join-Path $TestDrive ([guid]::NewGuid().ToString())
        $hub = Join-Path $root 'hub'
        $spoke = Join-Path $root 'spoke'
        $manifestPath = Join-Path $root 'manifest.json'
        $reportPath = Join-Path $root 'plan.json'
        foreach ($repository in @($hub, $spoke)) {
            New-Item -ItemType Directory -Path $repository -Force | Out-Null
            git -C $repository init --quiet
            git -C $repository config core.autocrlf false
            foreach ($name in @('same.md', 'old.md', 'ahead.md', 'fork.md', 'dirty.md', 'excluded.md', 'disabled.md', 'superseded.md', 'canonical-dirty.md', 'mcp.json')) {
                Write-Config $repository $name 'base'
            }
            Save-Repository $repository
        }
        foreach ($name in @('old.md', 'fork.md', 'superseded.md', 'canonical-dirty.md')) {
            Write-Config $hub $name 'hub revision'
        }
        Write-Config $hub 'add.md' 'new file'
        Write-Config $hub 'missing.md' 'not authorized for addition'
        Write-Config $hub 'mcp.json' '{"token":"literal-test-credential"}'
        Save-Repository $hub
        Write-Config $hub 'canonical-dirty.md' 'uncommitted hub revision'
        foreach ($name in @('ahead.md', 'fork.md', 'superseded.md')) {
            Write-Config $spoke $name 'spoke revision'
        }
        Write-Config $spoke 'only.md' 'spoke only'
        Write-Config $spoke 'prompts\legacy.prompt.md' 'migration input'
        Save-Repository $spoke
        Write-Config $spoke 'dirty.md' 'uncommitted spoke revision'
        $manifest = @{
            root = $root
            repos = @{ spoke = @{ exclude = @('.github/excluded.md') } }
            files = @{
                '.github/add.md' = @{ distribute = 'all' }
                '.github/disabled.md' = @{ distribute = 'none' }
                '.github/superseded.md' = @{ supersedes = @((Get-NormalizedHash "spoke revision`n")) }
            }
        }
    }

    It 'reports every spoke file and missing hub file exactly once with a reason' {
        $report = Invoke-Plan @{ Detailed = $true }
        $expected = @{
            'same.md' = 'in-sync'
            'old.md' = 'update'
            'ahead.md' = 'target-ahead'
            'fork.md' = 'forked'
            'dirty.md' = 'uncommitted'
            'excluded.md' = 'excluded'
            'disabled.md' = 'distribution-disabled'
            'superseded.md' = 'update'
            'canonical-dirty.md' = 'canonical-uncommitted'
            'mcp.json' = 'blocked-secret'
            'add.md' = 'add'
            'missing.md' = 'missing-not-distributed'
            'only.md' = 'target-only'
            'prompts/legacy.prompt.md' = 'target-only'
        }
        $report.Plan.Count | Should -Be $expected.Count
        foreach ($name in $expected.Keys) {
            $entry = @($report.Plan | Where-Object Path -eq ".github/$name")
            $entry.Count | Should -Be 1
            $entry[0].Action | Should -Be $expected[$name]
            $entry[0].Reason | Should -Not -BeNullOrEmpty
        }
        ($report.Plan | Where-Object Path -eq '.github/old.md').Reason | Should -Match 'working tree is clean'
        ($report.Plan | Where-Object Path -eq '.github/superseded.md').Reason | Should -Match 'explicitly superseded'
        ($report.Plan | Where-Object Path -eq '.github/prompts/legacy.prompt.md').Reason | Should -Match 'not an import target'
        $report.Applied | Should -BeFalse
        Get-Content -LiteralPath (Join-Path $spoke '.github\old.md') | Should -Be 'base'
    }

    It 'includes target-only files in console output with their rationale' {
        $manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $manifestPath
        $output = & pwsh -NoProfile -File $scriptPath -CanonicalRepo $hub -ManifestPath $manifestPath -ReportFile $reportPath -Detailed 2>&1
        $LASTEXITCODE | Should -Be 0
        ($output -join "`n") | Should -Match 'Reason'
        ($output -join "`n") | Should -Match 'only.md'
        ($output -join "`n") | Should -Match 'Exists only in the spoke'
    }

    It 'honors path filters without suppressing matching non-write entries' {
        $report = Invoke-Plan @{ Path = @('.github/same.md', '.github/only.md'); Detailed = $true }
        $report.Plan.Count | Should -Be 2
        $report.Plan.Action | Should -Contain 'in-sync'
        $report.Plan.Action | Should -Contain 'target-only'
    }

    It 'keeps globally excluded files and ignored repos outside the report' {
        $manifest.exclude = @('.github/only.md')
        $report = Invoke-Plan @{ Detailed = $true }
        $report.Plan.Path | Should -Not -Contain '.github/only.md'
        $manifest.repos.spoke.mode = 'ignore'
        $report = Invoke-Plan @{ Detailed = $true }
        $report.Plan.Count | Should -Be 0
        $report.Repos.Count | Should -Be 0
    }

    It 'defaults to a concise plan while preserving reasons and eligible writes' {
        $concise = Invoke-Plan
        $detailed = Invoke-Plan @{ Detailed = $true }
        $concise.Plan.Count | Should -Be 10
        foreach ($status in @('in-sync', 'excluded', 'distribution-disabled', 'missing-not-distributed')) {
            $concise.Plan.Action | Should -Not -Contain $status
            $detailed.Plan.Action | Should -Contain $status
        }
        foreach ($entry in $concise.Plan) {
            $entry.Reason | Should -Not -BeNullOrEmpty
        }
        $conciseWrites = @($concise.Plan | Where-Object Action -in 'add', 'update' | Select-Object -ExpandProperty Path)
        $detailedWrites = @($detailed.Plan | Where-Object Action -in 'add', 'update' | Select-Object -ExpandProperty Path)
        Compare-Object $conciseWrites $detailedWrites | Should -BeNullOrEmpty
    }

    It 'plans exactly the requested repository and supports repository wildcards' {
        $other = Join-Path $root 'other'
        New-Item -ItemType Directory -Path $other | Out-Null
        git -C $other init --quiet
        Write-Config $other 'only.md' 'other config'
        Save-Repository $other
        foreach ($filter in @('spoke', 'spo*')) {
            $report = Invoke-Plan @{ Repo = @($filter); Detailed = $true }
            $report.Repos.Count | Should -Be 1
            $report.Repos[0].Repo | Should -Be 'spoke'
            @($report.Plan.Repo | Sort-Object -Unique) | Should -Be @('spoke')
        }
    }

    It 'explains report-mode restrictions and does not write on apply' {
        $manifest.repos.spoke.mode = 'report'
        $report = Invoke-Plan @{ Apply = $true }
        ($report.Plan | Where-Object Path -eq '.github/old.md').Reason | Should -Match 'mode=report'
        $report.Repos[0].Result | Should -Be 'skipped (mode=report)'
        Get-Content -LiteralPath (Join-Path $spoke '.github\old.md') | Should -Be 'base'
    }

    It 'skips all writes when the spoke is dirty' {
        $report = Invoke-Plan @{ Apply = $true }
        $report.Repos[0].Result | Should -Be 'skipped (working tree not clean)'
        Get-Content -LiteralPath (Join-Path $spoke '.github\old.md') | Should -Be 'base'
        Test-Path -LiteralPath (Join-Path $spoke '.github\add.md') | Should -BeFalse
    }

    It 'only copies eligible updates and additions to a clean spoke (Detailed=<Detailed>)' -TestCases @(
        @{ Detailed = $false }
        @{ Detailed = $true }
    ) {
        param($Detailed)
        Save-Repository $spoke
        $report = Invoke-Plan @{ Apply = $true; Branch = 'test-sync'; Detailed = $Detailed }
        $report.Repos[0].Result | Should -Be 'written on test-sync'
        Get-Content -LiteralPath (Join-Path $spoke '.github\old.md') | Should -Be 'hub revision'
        Get-Content -LiteralPath (Join-Path $spoke '.github\add.md') | Should -Be 'new file'
        Get-Content -LiteralPath (Join-Path $spoke '.github\fork.md') | Should -Be 'spoke revision'
        Get-Content -LiteralPath (Join-Path $spoke '.github\only.md') | Should -Be 'spoke only'
        Get-Content -LiteralPath (Join-Path $spoke '.github\excluded.md') | Should -Be 'base'
        Get-Content -LiteralPath (Join-Path $spoke '.github\disabled.md') | Should -Be 'base'
        Test-Path -LiteralPath (Join-Path $spoke '.github\missing.md') | Should -BeFalse
        (git -C $spoke branch --show-current) | Should -Be 'test-sync'
    }
}
