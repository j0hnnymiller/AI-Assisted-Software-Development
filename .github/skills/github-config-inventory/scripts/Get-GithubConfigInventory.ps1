#Requires -Version 7
<#
.SYNOPSIS
Inventories in-scope config files (.github/**, AGENTS.md, CLAUDE.md, .vscode/mcp.json) across all git repos under a root,
classifies drift against the canonical repo, and recommends a main version per file from git history and content.
Read-only.
#>
[CmdletBinding()]
param(
  [string]$CanonicalRepo = (git rev-parse --show-toplevel 2>$null),
  [string]$ManifestPath,
  [string]$Root,
  # Repo keys (relative to root, forward slashes) or wildcards to include, e.g. 'AIASD/*'.
  [string[]]$Repo,
  [string]$OutFile = (Join-Path ([IO.Path]::GetTempPath()) 'github-config-inventory.json'),
  [switch]$ShowIdentical
)

Import-Module (Join-Path $PSScriptRoot 'GithubConfigSync.psm1') -Force
if (-not $CanonicalRepo) { throw 'Run inside the canonical repo or pass -CanonicalRepo.' }
$CanonicalRepo = Resolve-RepoPath $CanonicalRepo
if (-not $ManifestPath) { $ManifestPath = Join-Path $CanonicalRepo '.github/github-config-sync.json' }
$manifest = Read-SyncManifest $ManifestPath
if (-not $Root) { $Root = $manifest.root }
$Root = Resolve-RepoPath $Root
$scope = New-SyncScope $manifest
$canonicalKey = Get-RepoKey $CanonicalRepo $Root

$repoPaths = @(Find-GitRepository -Root $Root -MaxDepth $manifest.maxDepth -SkipDirs $manifest.skipDirs)
if ($CanonicalRepo -notin $repoPaths) { $repoPaths += $CanonicalRepo }

$snapshots = foreach ($r in $repoPaths) {
  $key = Get-RepoKey $r $Root
  if ($key -ne $canonicalKey -and $Repo -and -not ($Repo | Where-Object { $key -like $_ })) { continue }
  Write-Progress -Activity 'Inventory' -Status $key
  $snap = Get-RepoSnapshot $r $Root $manifest $scope
  if ($snap.State.Mode -eq 'ignore' -and $key -ne $canonicalKey) { continue }
  $snap
}
Write-Progress -Activity 'Inventory' -Completed

$byPath = @{}
foreach ($s in $snapshots) {
  foreach ($f in $s.Files.Values) {
    if (-not $byPath.ContainsKey($f.Path)) { $byPath[$f.Path] = [Collections.Generic.List[object]]::new() }
    $byPath[$f.Path].Add($f)
  }
}

$files = foreach ($p in ($byPath.Keys | Sort-Object)) {
  $entries = @($byPath[$p])
  $superseded = @()
  if ($manifest.files.ContainsKey($p) -and $manifest.files[$p].supersedes) { $superseded = @($manifest.files[$p].supersedes) }
  $a = Get-VariantAnalysis $entries $canonicalKey $superseded
  [pscustomobject]@{
    Path          = $p
    Status        = $a.Status
    Recommended   = $a.Recommended
    RecommendedIn = $a.RecommendedIn
    Confidence    = $a.Confidence
    Reason        = $a.Reason
    Variants      = $a.Variants
    Entries       = @($entries | Select-Object * -ExcludeProperty HistoryBlobs)
  }
}
$files = @($files)

$result = [pscustomobject]@{
  Generated     = (Get-Date).ToUniversalTime().ToString('o')
  Root          = $Root
  CanonicalRepo = $canonicalKey
  CanonicalPath = $CanonicalRepo
  ManifestPath  = $ManifestPath
  Scope         = @{ include = $manifest.include; exclude = $manifest.exclude }
  Repos         = @($snapshots | ForEach-Object { $_.State | Add-Member -NotePropertyName FileCount -NotePropertyValue $_.Files.Count -PassThru })
  Summary       = @($files | Group-Object Status | ForEach-Object { [pscustomobject]@{ Status = $_.Name; Count = $_.Count } })
  Files         = $files
}
$result | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $OutFile -Encoding utf8NoBOM

Write-Host "Canonical: $canonicalKey   Repos scanned: $(@($snapshots).Count)   Files: $($files.Count)"
Write-Host "Inventory written to $OutFile`n"
$result.Repos | Where-Object FileCount | Sort-Object Key | Format-Table Key, Branch, Head, Dirty, Mode, FileCount -AutoSize | Out-Host
$result.Summary | Sort-Object Status | Format-Table -AutoSize | Out-Host
$files | Where-Object { $ShowIdentical -or $_.Status -notin 'identical', 'canonical-only' } |
Format-Table Path, Status, @{ n = 'Variants'; e = { $_.Variants.Count } }, @{ n = 'Repos'; e = { $_.Entries.Count } },
@{ n = 'Recommended'; e = { ($_.RecommendedIn | Select-Object -First 2) -join ', ' } }, Confidence -AutoSize -Wrap | Out-String -Width 220 | Out-Host
$secrets = @($files | ForEach-Object { $_.Entries } | Where-Object SecretHits)
if ($secrets) {
  Write-Warning 'Possible literal secrets (values not shown):'
  $secrets | Format-Table Repo, Path, SecretHits -AutoSize | Out-Host
}
