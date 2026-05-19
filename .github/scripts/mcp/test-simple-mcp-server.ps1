#!/usr/bin/env pwsh
# End-to-end test for scripts/mcp/simple-mcp-server.ps1

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$serverPath = Join-Path $PSScriptRoot "simple-mcp-server.ps1"
if (-not (Test-Path $serverPath)) {
    throw "Server script not found: $serverPath"
}

$psi = [System.Diagnostics.ProcessStartInfo]::new()
$psi.FileName = "pwsh"
$psi.Arguments = "-NoLogo -NoProfile -File `"$serverPath`""
$psi.WorkingDirectory = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$psi.UseShellExecute = $false
$psi.RedirectStandardInput = $true
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$psi.StandardOutputEncoding = [System.Text.Encoding]::UTF8
$psi.StandardErrorEncoding = [System.Text.Encoding]::UTF8

$proc = [System.Diagnostics.Process]::new()
$proc.StartInfo = $psi

if (-not $proc.Start()) {
    throw "Failed to start MCP server process."
}

function Send-McpMessage {
    param(
        [Parameter(Mandatory = $true)]
        [hashtable]$Message
    )

    $json = $Message | ConvertTo-Json -Depth 20 -Compress
    $payload = [System.Text.Encoding]::UTF8.GetBytes($json)
    $header = [System.Text.Encoding]::ASCII.GetBytes("Content-Length: $($payload.Length)`r`n`r`n")

    $stream = $proc.StandardInput.BaseStream
    $stream.Write($header, 0, $header.Length)
    $stream.Write($payload, 0, $payload.Length)
    $stream.Flush()
}

function Read-McpMessage {
    $headers = @{}

    while ($true) {
        $line = $proc.StandardOutput.ReadLine()
        if ($null -eq $line) {
            return $null
        }

        if ([string]::IsNullOrWhiteSpace($line)) {
            break
        }

        if ($line -match "^(.*?):\s*(.*)$") {
            $headers[$matches[1]] = $matches[2]
        }
    }

    if (-not $headers.ContainsKey("Content-Length")) {
        return $null
    }

    $length = [int]$headers["Content-Length"]
    $buffer = New-Object char[] $length
    $offset = 0
    while ($offset -lt $length) {
        $read = $proc.StandardOutput.Read($buffer, $offset, $length - $offset)
        if ($read -le 0) {
            return $null
        }

        $offset += $read
    }

    $json = -join $buffer
    return $json | ConvertFrom-Json -Depth 20
}

try {
    Send-McpMessage @{
        jsonrpc = "2.0"
        id      = 1
        method  = "initialize"
        params  = @{
            protocolVersion = "2024-11-05"
            capabilities    = @{}
            clientInfo      = @{ name = "mcp-test"; version = "1.0.0" }
        }
    }

    $initResponse = Read-McpMessage
    if ($null -eq $initResponse -or $null -eq $initResponse.result) {
        throw "Initialize failed: no response or missing result."
    }

    Send-McpMessage @{
        jsonrpc = "2.0"
        id      = 2
        method  = "tools/list"
        params  = @{}
    }

    $toolsResponse = Read-McpMessage
    if ($null -eq $toolsResponse.result.tools) {
        throw "tools/list failed: missing tools array."
    }

    $echoExists = $false
    foreach ($tool in $toolsResponse.result.tools) {
        if ($tool.name -eq "echo") {
            $echoExists = $true
            break
        }
    }

    if (-not $echoExists) {
        throw "tools/list failed: echo tool was not returned."
    }

    Send-McpMessage @{
        jsonrpc = "2.0"
        id      = 3
        method  = "tools/call"
        params  = @{
            name      = "echo"
            arguments = @{ text = "hello mcp" }
        }
    }

    $callResponse = Read-McpMessage
    $text = $callResponse.result.content[0].text
    if ($text -ne "hello mcp") {
        throw "tools/call failed: expected 'hello mcp', got '$text'."
    }

    Write-Host "MCP test passed."
    Write-Host "initialize -> ok"
    Write-Host "tools/list -> echo available"
    Write-Host "tools/call -> echo returned expected text"
}
finally {
    try {
        if (-not $proc.HasExited) {
            $proc.Kill()
            $proc.WaitForExit(2000) | Out-Null
        }
    }
    catch {
        # ignore cleanup errors
    }

    $stderr = $proc.StandardError.ReadToEnd()
    if (-not [string]::IsNullOrWhiteSpace($stderr)) {
        Write-Host "Server stderr:"
        Write-Host $stderr
    }

    $proc.Dispose()
}
