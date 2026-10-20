#Requires -Version 7
<#
.SYNOPSIS
Plans (default) or applies distribution of canonical config files to the other repos under the root.

Per target file the action is:
  in-sync        content matches canonical (line endings/trailing whitespace ignored)
  update         target holds an older canonical version (blob in canonical history) or a superseded variant
  add            target lacks the file and manifest distribute=all or lists the repo
  target-ahead   target holds a version that evolved from canonical; consolidate it first
  forked         unrelated edits on both sides; consolidate (merge) first
  uncommitted    target copy has uncommitted changes; skipped
  blocked-secret canonical copy looks like it contains a literal secret; skipped
  excluded       repository policy excludes the file
  distribution-disabled manifest distribute=none
  missing-not-distributed target lacks the file and additions are not authorized
Entries include a Reason. -Detailed also includes in-sync, excluded,
distribution-disabled, and missing-not-distributed files.

-Apply: for each repo with a clean working tree, creates -Branch, copies update/add files. -Commit also commits.
Never pushes, never deletes.
#>
[CmdletBinding()]
param(
  [string]$CanonicalRepo = (git rev-parse --show-toplevel 2>$null),
  [string]$ManifestPath,
  [string]$Root,
  # Target repo keys or wildcards, e.g. 'AIASD/*'.
  [string[]]$Repo,
  # In-scope file paths or globs to limit the sync to, e.g. '.github/instructions/*.md'.
  [string[]]$Path,
  # Include unchanged and policy-excluded files in both JSON and console reports.
  [switch]$Detailed,
  [switch]$Apply,
  [switch]$Commit,
  [string]$Branch = "chore/sync-github-config-$(Get-Date -Format yyyyMMdd)",
  [string]$ReportFile = (Join-Path ([IO.Path]::GetTempPath()) 'github-config-sync-plan.json')
)

Import-Module (Join-Path $PSScriptRoot '..\..\github-config-inventory\scripts\GithubConfigSync.psm1') -Force
if (-not $CanonicalRepo) { throw 'Run inside the canonical repo or pass -CanonicalRepo.' }
if ($Commit -and -not $Apply) { throw '-Commit requires -Apply.' }
$CanonicalRepo = Resolve-RepoPath $CanonicalRepo
if (-not $ManifestPath) { $ManifestPath = Join-Path $CanonicalRepo '.github/github-config-sync.json' }
$ManifestPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($ManifestPath)
Write-Host "Manifest: $ManifestPath"
$manifest = Read-SyncManifest $ManifestPath
if (-not $Root) { $Root = $manifest.root }
$Root = Resolve-RepoPath $Root
$scope = New-SyncScope $manifest

$canon = Get-RepoSnapshot $CanonicalRepo $Root $manifest $scope
$canonKey = $canon.State.Key
$canonUncommitted = @($canon.Files.Values | Where-Object WorkTree -ne 'clean' | ForEach-Object Path)
if ($canonUncommitted -and $Apply) { Write-Warning "Canonical repo has $($canonUncommitted.Count) uncommitted in-scope file(s); they are skipped. Commit them first." }

$targets = @(Find-GitRepository -Root $Root -MaxDepth $manifest.maxDepth -SkipDirs $manifest.skipDirs | Where-Object { $_ -ne $CanonicalRepo })
$plan = [Collections.Generic.List[object]]::new()
$repoResults = [Collections.Generic.List[object]]::new()

foreach ($t in $targets) {
  $key = Get-RepoKey $t $Root
  if ($Repo -and -not ($Repo | Where-Object { $key -like $_ })) { continue }
  $cfg = Get-RepoConfig $manifest $key
  $mode = if ($cfg.ContainsKey('mode')) { $cfg.mode } else { $manifest.defaultMode }
  if ($mode -eq 'ignore') { continue }
  $repoExclude = @(if ($cfg.ContainsKey('exclude')) { $cfg.exclude })

  Write-Progress -Activity 'Sync plan' -Status $key
  $snap = Get-RepoSnapshot $t $Root $manifest $scope

  $paths = @(@($canon.Files.Keys) + @($snap.Files.Keys) | Sort-Object -Unique)
  foreach ($filePath in $paths) {
    if ($Path -and -not (Test-GlobMatch $filePath $Path)) { continue }
    $c = if ($canon.Files.ContainsKey($filePath)) { $canon.Files[$filePath] } else { $null }
    $tf = if ($snap.Files.ContainsKey($filePath)) { $snap.Files[$filePath] } else { $null }
    $fcfg = if ($manifest.files.ContainsKey($filePath)) { $manifest.files[$filePath] } else { @{} }
    $distribute = if ($fcfg.ContainsKey('distribute')) { $fcfg.distribute } else { 'existing' }
    $supersedes = @(if ($fcfg.ContainsKey('supersedes')) { $fcfg.supersedes })

    $action, $reason = if (Test-GlobMatch $filePath $repoExclude) {
      'excluded', 'Repository exclusion policy prevents distribution of this file.'
    }
    elseif ($distribute -eq 'none') {
      'distribution-disabled', 'Manifest sets distribute=none; this file is not distributed.'
    }
    elseif (-not $c) {
      'target-only', $(if ($filePath -like '.github/prompts/*') {
          'Exists only in the spoke; legacy prompt is a skill-migration candidate, not an import target.'
        } else { 'Exists only in the spoke; retain for repository-specific use or review for consolidation.' })
    }
    elseif ($tf) {
      if ($tf.NormHash -eq $c.NormHash) { 'in-sync', 'Content matches the hub after normalizing line endings and trailing whitespace.' }
      elseif ($tf.WorkTree -ne 'clean') { 'uncommitted', 'Spoke content differs and has uncommitted changes; preserve local edits.' }
      elseif ($tf.Blob -in $c.HistoryBlobs) { 'update', 'Spoke content is a recorded version in hub history for this path.' }
      elseif ($tf.NormHash -in $supersedes) { 'update', 'Spoke content is explicitly superseded by the canonical version in the manifest.' }
      elseif ($c.Blob -in $tf.HistoryBlobs) { 'target-ahead', 'Current hub content appears in spoke history; consolidate the spoke version first.' }
      else { 'forked', 'No recognized history or supersession establishes a safe overwrite; review and consolidate first.' }
    }
    elseif ($distribute -eq 'all' -or ($fcfg.ContainsKey('repos') -and ($fcfg.repos | Where-Object { $key -like $_ }))) {
      'add', 'Missing from the spoke; manifest authorizes adding this file to this repository.'
    }
    else {
      'missing-not-distributed', 'Missing from the spoke; manifest does not authorize adding this file to this repository.'
    }

    if ($action -in 'update', 'add') {
      if ($filePath -in $canonUncommitted) {
        $action = 'canonical-uncommitted'
        $reason = 'Hub file has uncommitted changes; commit the canonical version before distribution.'
      }
      elseif ($c.SecretHits -and $filePath -like '*mcp.json') {
        $action = 'blocked-secret'
        $reason = 'Canonical MCP configuration matches the literal-secret heuristic; remove credentials before distribution.'
      }
      else {
        if ($mode -ne 'sync') { $reason += " Writes are blocked by repository mode=$mode." }
        if ($snap.State.Dirty) { $reason += ' Writes are blocked until the entire spoke working tree is clean.' }
      }
    }
    if (-not $Detailed -and $action -in 'in-sync', 'excluded', 'distribution-disabled', 'missing-not-distributed') { continue }
    $plan.Add([pscustomobject]@{
        Repo = $key; Mode = $mode; Path = $filePath; Action = $action; Reason = $reason
        Source = if ($c) { $c.FullPath } else { $null }
        Target = Join-Path $t $filePath
      })
  }

  $writes = @($plan | Where-Object { $_.Repo -eq $key -and $_.Action -in 'update', 'add' })
  $result = 'planned'
  if ($Apply -and $writes) {
    $result = if ($mode -ne 'sync') { "skipped (mode=$mode)" }
    elseif ($snap.State.Dirty) { 'skipped (working tree not clean)' }
    elseif ($snap.State.Branch -ne $Branch -and (git -C $t rev-parse --verify --quiet "refs/heads/$Branch")) { "skipped (branch $Branch exists)" }
    else { 'apply' }

    if ($result -eq 'apply') {
      if ($snap.State.Branch -ne $Branch) {
        git -C $t switch -c $Branch 2>&1 | Out-Null
        if ($LASTEXITCODE) { $result = 'failed (git switch)' }
      }
      if ($result -eq 'apply') {
        foreach ($w in $writes) {
          New-Item -ItemType Directory -Force -Path (Split-Path $w.Target) | Out-Null
          Copy-Item -LiteralPath $w.Source -Destination $w.Target -Force
        }
        $result = "written on $Branch"
        if ($Commit) {
          git -C $t add -- @($writes.Path) 2>&1 | Out-Null
          git -C $t commit -m "chore: sync .github config from $canonKey@$($canon.State.Head)" 2>&1 | Out-Null
          $result = if ($LASTEXITCODE) { 'failed (git commit)' } else { "committed on $Branch" }
        }
      }
    }
  }
  $counts = $plan | Where-Object Repo -eq $key | Group-Object Action
  $repoResults.Add([pscustomobject]@{
      Repo    = $key
      Branch  = $snap.State.Branch
      Dirty   = $snap.State.Dirty
      Mode    = $mode
      Actions = ($counts | ForEach-Object { "$($_.Name)=$($_.Count)" }) -join ' '
      Result  = if ($writes) { $result } else { 'nothing to write' }
    })
}
Write-Progress -Activity 'Sync plan' -Completed

[pscustomobject]@{
  Generated = (Get-Date).ToUniversalTime().ToString('o'); Canonical = $canonKey; CanonicalHead = $canon.State.Head
  ManifestPath = $ManifestPath
  Applied = [bool]$Apply; Branch = $Branch; Repos = $repoResults; Plan = $plan
} | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $ReportFile -Encoding utf8NoBOM

$repoResults | Where-Object Actions | Format-Table -AutoSize -Wrap | Out-String -Width 220 | Out-Host
$plan | Sort-Object Repo, Path |
Format-Table Repo, Path, Action, Reason -Wrap | Out-String -Width 220 | Out-Host
Write-Host "Plan written to $ReportFile$(if (-not $Apply) { ' (dry run; use -Apply to write)' })"
