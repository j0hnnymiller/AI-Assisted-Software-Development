#Requires -Version 7
<#
.SYNOPSIS
Consolidates the chosen version of config files into the canonical repo and records the replaced versions as
"supersedes" in the sync manifest, so distribution can safely overwrite stale copies in other repos.
Supports -WhatIf. Never commits.

.EXAMPLE
# Import the recommended version of each file
./Import-GithubConfigFile.ps1 -Path .github/instructions/x.instructions.md, .github/prompts/y.prompt.md

.EXAMPLE
# Import a specific repo's version
./Import-GithubConfigFile.ps1 -Path .github/agents/a.agent.md -FromRepo AIASD/Fleetly

.EXAMPLE
# After hand-merging a file in the canonical repo, record all other variants as superseded
./Import-GithubConfigFile.ps1 -Path .github/agents/a.agent.md -RecordOnly
#>
[CmdletBinding(SupportsShouldProcess)]
param(
  [Parameter(Mandatory)][string[]]$Path,
  # Repo key to take the file from; defaults to the recommended variant.
  [string]$FromRepo,
  [string]$InventoryPath = (Join-Path ([IO.Path]::GetTempPath()) 'github-config-inventory.json'),
  [switch]$RecordOnly,
  # Overwrite even if the canonical copy has uncommitted changes.
  [switch]$Force
)

Import-Module (Join-Path $PSScriptRoot '..\..\github-config-inventory\scripts\GithubConfigSync.psm1') -Force
if (-not (Test-Path -LiteralPath $InventoryPath)) { throw "Inventory not found: $InventoryPath. Run Get-GithubConfigInventory.ps1 first." }
$inv = Get-Content -LiteralPath $InventoryPath -Raw | ConvertFrom-Json
$manifest = Read-SyncManifest $inv.ManifestPath
$changed = $false

foreach ($p in $Path) {
  $rel = $p.Replace('\', '/')
  $f = $inv.Files | Where-Object Path -eq $rel
  if (-not $f) { Write-Warning "Not in inventory: $rel"; continue }
  $dest = Join-Path $inv.CanonicalPath $rel
  $current = $null

  if (-not $RecordOnly) {
    $variant = if ($FromRepo) { $f.Variants | Where-Object { $FromRepo -in $_.Repos } } else { $f.Variants | Where-Object Id -eq $f.Recommended }
    $variant = @($variant)[0]
    if (-not $variant) { Write-Warning "$rel : no variant from '$FromRepo'"; continue }
    if ($variant.HasCanonical) { Write-Host "$rel : canonical already holds $($variant.Id); nothing to copy" }
    else {
      $dirty = git -C $inv.CanonicalPath status --porcelain -- $rel
      if ($dirty -and -not $Force) { Write-Warning "$rel : uncommitted changes in canonical repo; commit/stash or use -Force"; continue }
      $source = ($f.Entries | Where-Object { $_.Repo -in $variant.Repos -and $_.WorkTree -eq 'clean' } | Select-Object -First 1).FullPath
      if (-not $source) { $source = $variant.Representative }
      if ($PSCmdlet.ShouldProcess($dest, "Copy $($variant.Id) from $source")) {
        New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
        Copy-Item -LiteralPath $source -Destination $dest -Force
        Write-Host "$rel : imported $($variant.Id) from $($variant.Repos -join ', ')" -ForegroundColor Green
      }
      $current = $variant.NormHash
    }
  }

  if (-not $current) {
    if (-not (Test-Path -LiteralPath $dest)) { Write-Warning "$rel : missing in canonical repo"; continue }
    $current = Get-NormalizedHash ([IO.File]::ReadAllText($dest))
  }
  $entry = if ($manifest.files.ContainsKey($rel)) { $manifest.files[$rel] } else { @{} }
  $old = @(if ($entry.ContainsKey('supersedes')) { $entry.supersedes })
  $new = @($old + @($f.Variants.NormHash) | Where-Object { $_ -and $_ -ne $current } | Sort-Object -Unique)
  if ($PSCmdlet.ShouldProcess($inv.ManifestPath, "Record $($new.Count) superseded variant(s) for $rel")) {
    $entry.supersedes = $new
    $entry.consolidated = (Get-Date).ToUniversalTime().ToString('o')
    $manifest.files[$rel] = $entry
    $changed = $true
  }
}

if ($changed) {
  Write-SyncManifest $manifest $inv.ManifestPath
  Write-Host "Manifest updated: $($inv.ManifestPath). Review, then commit in the canonical repo."
}
