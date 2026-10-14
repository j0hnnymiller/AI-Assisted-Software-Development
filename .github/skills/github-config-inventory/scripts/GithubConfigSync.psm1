#Requires -Version 7
# Shared helpers for the github-config-* skills (inventory, canonical, consolidate, distribute).
Set-StrictMode -Version Latest

$script:DefaultManifest = @{
  root        = 'c:\git'
  maxDepth    = 3
  include     = @('.github/**', 'AGENTS.md', 'CLAUDE.md', '.vscode/mcp.json')
  exclude     = @('.github/.stfolder/**', '.github/github-config-sync.json')
  skipDirs    = @('node_modules', 'archive', 'bin', 'obj', '.venv', '__pycache__')
  defaultMode = 'sync'
  repos       = @{}
  files       = @{}
}

# Literal credentials only; ${input:..} and ${env:..} references are not matched.
$script:SecretPattern = '(?i)(api[_-]?key|secret|password|token)["'']?\s*[:=]\s*["''][^"''$\{\s]{8,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|xox[bp]-[A-Za-z0-9-]{10,}'

function Resolve-RepoPath([string]$Path) {
  [IO.Path]::GetFullPath(($Path -replace '/', '\')).TrimEnd('\')
}

function Get-RepoKey([string]$Repo, [string]$Root) {
  $rel = [IO.Path]::GetRelativePath($Root, $Repo)
  if ($rel.StartsWith('..')) { return $Repo }
  $rel.Replace('\', '/')
}

function Read-SyncManifest([string]$Path) {
  $m = @{}
  foreach ($k in $script:DefaultManifest.Keys) { $m[$k] = $script:DefaultManifest[$k] }
  if ($Path -and (Test-Path -LiteralPath $Path)) {
    $j = Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json -AsHashtable
    foreach ($k in $j.Keys) { $m[$k] = $j[$k] }
  }
  if (-not $m.repos) { $m.repos = @{} }
  if (-not $m.files) { $m.files = @{} }
  $m
}

function Write-SyncManifest([hashtable]$Manifest, [string]$Path) {
  $out = [ordered]@{}
  foreach ($k in @('root', 'maxDepth', 'include', 'exclude', 'skipDirs', 'defaultMode', 'repos')) { if ($Manifest.ContainsKey($k)) { $out[$k] = $Manifest[$k] } }
  $files = [ordered]@{}
  foreach ($k in ($Manifest.files.Keys | Sort-Object)) { $files[$k] = $Manifest.files[$k] }
  $out.files = $files
  foreach ($k in $Manifest.Keys) { if (-not $out.Contains($k)) { $out[$k] = $Manifest[$k] } }
  $out | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $Path -Encoding utf8NoBOM
}

function ConvertTo-GlobRegex([string]$Glob) {
  $sb = [Text.StringBuilder]::new('^')
  $i = 0
  while ($i -lt $Glob.Length) {
    $c = $Glob[$i]
    if ($c -eq '*' -and $i + 1 -lt $Glob.Length -and $Glob[$i + 1] -eq '*') {
      if ($i + 2 -lt $Glob.Length -and $Glob[$i + 2] -eq '/') { [void]$sb.Append('(?:.*/)?'); $i += 3 }
      else { [void]$sb.Append('.*'); $i += 2 }
      continue
    }
    if ($c -eq '*') { [void]$sb.Append('[^/]*') }
    elseif ($c -eq '?') { [void]$sb.Append('[^/]') }
    else { [void]$sb.Append([regex]::Escape([string]$c)) }
    $i++
  }
  [void]$sb.Append('$')
  $sb.ToString()
}

function Test-GlobMatch([string]$Path, [string[]]$Globs) {
  foreach ($g in @($Globs)) { if ($g -and $Path -match (ConvertTo-GlobRegex $g)) { return $true } }
  $false
}

function New-SyncScope([hashtable]$Manifest) {
  $pathspec = foreach ($g in $Manifest.include) {
    $prefix = ($g -split '[\*\?]', 2)[0]
    if ($prefix -ne $g) { $prefix = $prefix.Substring(0, $prefix.LastIndexOf('/') + 1) }
    if ($prefix) { $prefix } else { '.' }
  }
  [pscustomobject]@{
    Include  = @($Manifest.include | ForEach-Object { ConvertTo-GlobRegex $_ })
    Exclude  = @($Manifest.exclude | ForEach-Object { ConvertTo-GlobRegex $_ })
    Pathspec = @($pathspec | Sort-Object -Unique)
  }
}

function Test-InScope([string]$Path, $Scope) {
  $hit = $false
  foreach ($r in $Scope.Include) { if ($Path -match $r) { $hit = $true; break } }
  if (-not $hit) { return $false }
  foreach ($r in $Scope.Exclude) { if ($Path -match $r) { return $false } }
  $true
}

function Find-GitRepository([string]$Root, [int]$MaxDepth = 3, [string[]]$SkipDirs = @()) {
  $queue = [Collections.Generic.Queue[object]]::new()
  $queue.Enqueue(@((Resolve-RepoPath $Root), 0))
  while ($queue.Count) {
    $path, $depth = $queue.Dequeue()
    # .git as a directory only: skips worktrees and submodule checkouts.
    if (Test-Path -LiteralPath (Join-Path $path '.git') -PathType Container) { $path; continue }
    if ($depth -ge $MaxDepth) { continue }
    Get-ChildItem -LiteralPath $path -Directory -Force -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -notin $SkipDirs -and $_.Name -notlike '*.worktrees' -and -not $_.Name.StartsWith('.') } |
    ForEach-Object { $queue.Enqueue(@($_.FullName, ($depth + 1))) }
  }
}

function Get-NormalizedHash([string]$Text) {
  $n = (($Text -replace "`r`n", "`n") -replace '[ \t]+(?=\n)', '').TrimEnd()
  [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($n))).Substring(0, 16).ToLower()
}

function Get-FileHistoryIndex([string]$Repo, [string[]]$Pathspec) {
  $index = @{}
  $commit = $null
  $lines = git -C $Repo -c core.quotepath=off log --no-renames --format='@@%H|%cI|%an|%s' --raw --no-abbrev -- @Pathspec 2>$null
  foreach ($line in $lines) {
    if ($line.StartsWith('@@')) {
      $p = $line.Substring(2).Split('|', 4)
      $commit = @{ Sha = $p[0]; Date = ([datetimeoffset]$p[1]).UtcDateTime.ToString('o'); Author = $p[2]; Subject = $p[3] }
      continue
    }
    if ($commit -and $line -match '^:\d+ \d+ [0-9a-f]+ ([0-9a-f]+) (\w)\d*\t(.+)$') {
      $path = $Matches[3]
      if (-not $index.ContainsKey($path)) { $index[$path] = [Collections.Generic.List[object]]::new() }
      $index[$path].Add([pscustomobject]@{ Sha = $commit.Sha; Date = $commit.Date; Author = $commit.Author; Subject = $commit.Subject; Blob = $Matches[1]; Status = $Matches[2] })
    }
  }
  $index
}

function Get-RepoConfig([hashtable]$Manifest, [string]$Key) {
  if ($Manifest.repos.ContainsKey($Key)) { return $Manifest.repos[$Key] }
  # Wildcard keys (e.g. 'Teleflex/*'); first match in manifest order wins.
  foreach ($k in $Manifest.repos.Keys) { if ($Key -like $k) { return $Manifest.repos[$k] } }
  @{}
}

function Get-RepoState([string]$Repo, [string]$Root, [hashtable]$Manifest) {
  $key = Get-RepoKey $Repo $Root
  $cfg = Get-RepoConfig $Manifest $key
  $mode = if ($cfg.ContainsKey('mode') -and $cfg.mode) { $cfg.mode } else { $Manifest.defaultMode }
  [pscustomobject]@{
    Key    = $key
    Path   = $Repo
    Branch = (git -C $Repo branch --show-current 2>$null)
    Head   = (git -C $Repo rev-parse --short HEAD 2>$null)
    Remote = (git -C $Repo remote get-url origin 2>$null)
    Dirty  = [bool](git -C $Repo status --porcelain 2>$null)
    Mode   = $mode
  }
}

function Get-RepoSnapshot([string]$Repo, [string]$Root, [hashtable]$Manifest, $Scope) {
  $state = Get-RepoState $Repo $Root $Manifest
  $paths = @(git -C $Repo -c core.quotepath=off ls-files --cached --others --exclude-standard -- @($Scope.Pathspec) 2>$null |
    Where-Object { (Test-InScope $_ $Scope) -and (Test-Path -LiteralPath (Join-Path $Repo $_) -PathType Leaf) } |
    Sort-Object -Unique)
  $history = Get-FileHistoryIndex $Repo $Scope.Pathspec

  $workTree = @{}
  $raw = (git -C $Repo -c core.quotepath=off status --porcelain -z --untracked-files=all -- @($Scope.Pathspec) 2>$null) -join "`n"
  foreach ($rec in ($raw -split "`0")) { if ($rec.Length -gt 3) { $workTree[$rec.Substring(3)] = $rec.Substring(0, 2).Trim() } }

  $blobs = [Collections.Generic.List[string]]::new()
  for ($i = 0; $i -lt $paths.Count; $i += 100) {
    $chunk = $paths[$i..([Math]::Min($i + 99, $paths.Count - 1))]
    foreach ($b in (git -C $Repo hash-object -- @chunk)) { $blobs.Add($b) }
  }

  $files = @{}
  for ($i = 0; $i -lt $paths.Count; $i++) {
    $p = $paths[$i]
    $full = Join-Path $Repo $p
    $item = Get-Item -LiteralPath $full
    $text = [IO.File]::ReadAllText($full)
    $hist = @(if ($history.ContainsKey($p)) { $history[$p] })
    $last = $hist | Select-Object -First 1
    $files[$p] = [pscustomobject]@{
      Repo             = $state.Key
      Path             = $p
      FullPath         = $full
      Blob             = $blobs[$i]
      NormHash         = Get-NormalizedHash $text
      Bytes            = $item.Length
      Lines            = ($text -split "`n").Count
      LastCommitDate   = if ($last) { $last.Date } else { $null }
      LastCommitSha    = if ($last) { $last.Sha.Substring(0, 8) } else { $null }
      LastCommitAuthor = if ($last) { $last.Author } else { $null }
      LastCommitMsg    = if ($last) { $last.Subject } else { $null }
      CommitCount      = $hist.Count
      WorkTree         = if ($workTree.ContainsKey($p)) { $workTree[$p] } else { 'clean' }
      ModifiedDate     = $item.LastWriteTimeUtc.ToString('o')
      SecretHits       = [regex]::Matches($text, $script:SecretPattern).Count
      HistoryBlobs     = @($hist | ForEach-Object Blob | Sort-Object -Unique)
    }
  }
  [pscustomobject]@{ State = $state; Files = $files }
}

function Get-VariantAnalysis([object[]]$Entries, [string]$CanonicalKey, [string[]]$Superseded = @()) {
  $i = 0
  $variants = @($Entries | Group-Object NormHash | ForEach-Object {
      $es = @($_.Group)
      $hash = $_.Name
      $blobs = @($es | ForEach-Object Blob | Sort-Object -Unique)
      # Stale: another repo's history contains this content and that repo has since moved on.
      $staleIn = @($Entries | Where-Object { $_.NormHash -ne $hash -and @($_.HistoryBlobs | Where-Object { $_ -in $blobs }).Count } | ForEach-Object Repo | Sort-Object -Unique)
      if ($hash -in $Superseded) { $staleIn += 'manifest:supersedes' }
      $dates = @($es | ForEach-Object { if ($_.WorkTree -ne 'clean') { $_.ModifiedDate } else { $_.LastCommitDate } } | Where-Object { $_ })
      $rep = $es | Sort-Object { $_.Repo -ne $CanonicalKey }, { $_.WorkTree -ne 'clean' } | Select-Object -First 1
      [pscustomobject]@{
        Id             = $null
        NormHash       = $hash
        Repos          = @($es | ForEach-Object Repo)
        Blobs          = $blobs
        Newest         = ($dates | Sort-Object -Descending | Select-Object -First 1)
        Lines          = [int]($es | Measure-Object Lines -Maximum).Maximum
        CommitCount    = [int]($es | Measure-Object CommitCount -Maximum).Maximum
        Uncommitted    = @($es | Where-Object WorkTree -ne 'clean' | ForEach-Object Repo)
        SecretHits     = [int]($es | Measure-Object SecretHits -Maximum).Maximum
        StaleIn        = $staleIn
        HasCanonical   = $CanonicalKey -in $es.Repo
        Representative = $rep.FullPath
      }
    })
  $ordered = @($variants | Sort-Object @{ Expression = { $_.StaleIn.Count -eq 0 }; Descending = $true },
    @{ Expression = 'Newest'; Descending = $true }, @{ Expression = { $_.Repos.Count }; Descending = $true },
    @{ Expression = 'Lines'; Descending = $true }, @{ Expression = 'HasCanonical'; Descending = $true })
  foreach ($v in $ordered) { $v.Id = "V$((++$i))" }

  $fresh = @($ordered | Where-Object { $_.StaleIn.Count -eq 0 })
  $rec = $ordered[0]
  $confidence, $reason = if ($ordered.Count -eq 1) { 'n/a', 'single version' }
  elseif ($fresh.Count -eq 1) { 'high', 'all other versions appear in git history (or manifest supersedes) of repos that moved past them' }
  elseif ($fresh.Count -gt 1) { 'low', "forked: $($fresh.Count) independent versions; review content and merge" }
  else { 'low', 'no clear lineage; picked newest commit' }

  $inCanon = $CanonicalKey -in $Entries.Repo
  $status = if (-not $inCanon) { 'missing-here' }
  elseif ($Entries.Count -eq 1) { 'canonical-only' }
  elseif ($ordered.Count -eq 1) { if (@($Entries.Blob | Sort-Object -Unique).Count -eq 1) { 'identical' } else { 'whitespace-only' } }
  else { 'diverged' }

  [pscustomobject]@{
    Status        = $status
    Recommended   = $rec.Id
    RecommendedIn = $rec.Repos
    Confidence    = $confidence
    Reason        = $reason
    Variants      = $ordered
  }
}

Export-ModuleMember -Function Resolve-RepoPath, Get-RepoKey, Read-SyncManifest, Write-SyncManifest, ConvertTo-GlobRegex,
Test-GlobMatch, New-SyncScope, Test-InScope, Find-GitRepository, Get-NormalizedHash, Get-FileHistoryIndex, Get-RepoConfig, Get-RepoState,
Get-RepoSnapshot, Get-VariantAnalysis
