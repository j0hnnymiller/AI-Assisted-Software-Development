#Requires -Version 7
<#
.SYNOPSIS
Shows the versions (variants) of one or more config files from an inventory, the git-history evidence for each,
the recommended canonical version, and diffs of every other variant against it. Read-only.
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory)][string[]]$Path,
  [string]$InventoryPath = (Join-Path ([IO.Path]::GetTempPath()) 'github-config-inventory.json'),
  # Full unified diff instead of --stat.
  [switch]$Full
)

if (-not (Test-Path -LiteralPath $InventoryPath)) { throw "Inventory not found: $InventoryPath. Run Get-GithubConfigInventory.ps1 first." }
$inv = Get-Content -LiteralPath $InventoryPath -Raw | ConvertFrom-Json

foreach ($p in $Path) {
  $f = $inv.Files | Where-Object Path -eq $p.Replace('\', '/')
  if (-not $f) { Write-Warning "Not in inventory: $p"; continue }

  Write-Host "`n=== $($f.Path)" -ForegroundColor Cyan
  Write-Host "Status: $($f.Status)  Recommended: $($f.Recommended) ($($f.Confidence)) - $($f.Reason)"
  $f.Variants | Format-Table Id, @{ n = 'Repos'; e = { $_.Repos -join ', ' } }, Newest, Lines, CommitCount,
  @{ n = 'Uncommitted'; e = { $_.Uncommitted -join ', ' } }, @{ n = 'StaleIn'; e = { $_.StaleIn -join ', ' } }, SecretHits -AutoSize -Wrap |
  Out-String -Width 220 | Out-Host
  $f.Entries | Sort-Object LastCommitDate -Descending |
  Format-Table Repo, NormHash, LastCommitDate, LastCommitSha, LastCommitAuthor, LastCommitMsg, WorkTree -AutoSize |
  Out-String -Width 220 | Out-Host

  $base = @($f.Variants | Where-Object Id -eq $f.Recommended)[0]
  foreach ($v in ($f.Variants | Where-Object Id -ne $f.Recommended)) {
    Write-Host "--- $($base.Id) (recommended) -> $($v.Id)  [$($v.Repos -join ', ')]" -ForegroundColor Yellow
    $gitArgs = @('--no-pager', 'diff', '--no-index', '--ignore-cr-at-eol')
    if (-not $Full) { $gitArgs += '--stat' }
    $gitArgs += @('--', [string]$base.Representative, [string]$v.Representative)
    git @gitArgs | Out-Host
  }
}
