#!/usr/bin/env pwsh
# Simple MCP Server in PowerShell

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Read-MCPMessage {
    $headers = @{}
    while ($true) {
        $line = [Console]::In.ReadLine()
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
        $read = [Console]::In.Read($buffer, $offset, $length - $offset)
        if ($read -le 0) {
            return $null
        }

        $offset += $read
    }

    $json = -join $buffer
    return $json | ConvertFrom-Json -Depth 20
}

function Write-MCPMessage([hashtable]$obj) {
    $json = $obj | ConvertTo-Json -Depth 20 -Compress
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($json)
    $header = "Content-Length: $($bytes.Length)`r`n`r`n"
    $headerBytes = [System.Text.Encoding]::ASCII.GetBytes($header)

    $stdout = [Console]::OpenStandardOutput()
    $stdout.Write($headerBytes, 0, $headerBytes.Length)
    $stdout.Write($bytes, 0, $bytes.Length)
    $stdout.Flush()
}

function Get-ToolDefinitions {
    return @(
        @{
            name        = "echo"
            description = "Echo text back to the caller"
            inputSchema = @{
                type                 = "object"
                properties           = @{
                    text = @{ type = "string" }
                }
                required             = @("text")
                additionalProperties = $false
            }
        }
    )
}

function Handle-Initialize($msg) {
    return @{
        jsonrpc = "2.0"
        id      = $msg.id
        result  = @{
            protocolVersion = "2024-11-05"
            serverInfo      = @{
                name    = "PowerShell-MCP"
                version = "0.1.0"
            }
            capabilities    = @{
                tools = @{}
            }
        }
    }
}

function Handle-ToolsList($msg) {
    return @{
        jsonrpc = "2.0"
        id      = $msg.id
        result  = @{
            tools = @(Get-ToolDefinitions)
        }
    }
}

function Handle-ToolsCall($msg) {
    $toolName = $msg.params.name
    $arguments = $msg.params.arguments

    switch ($toolName) {
        "echo" {
            $text = ""
            if ($null -ne $arguments -and $null -ne $arguments.text) {
                $text = [string]$arguments.text
            }

            return @{
                jsonrpc = "2.0"
                id      = $msg.id
                result  = @{
                    content = @(
                        @{
                            type = "text"
                            text = $text
                        }
                    )
                    isError = $false
                }
            }
        }

        default {
            return @{
                jsonrpc = "2.0"
                id      = $msg.id
                error   = @{
                    code    = -32601
                    message = "Unknown tool: $toolName"
                }
            }
        }
    }
}

function Handle-DirectMethod($msg) {
    # Backward compatibility: direct method call like { "method": "echo", ... }
    if ($msg.method -eq "echo") {
        $text = ""
        if ($null -ne $msg.params -and $null -ne $msg.params.text) {
            $text = [string]$msg.params.text
        }

        return @{
            jsonrpc = "2.0"
            id      = $msg.id
            result  = @{
                text = $text
            }
        }
    }

    return @{
        jsonrpc = "2.0"
        id      = $msg.id
        error   = @{
            code    = -32601
            message = "Unknown method: $($msg.method)"
        }
    }
}

while ($true) {
    $msg = Read-MCPMessage
    if ($null -eq $msg) {
        continue
    }

    if ($msg.method -eq "initialize") {
        Write-MCPMessage (Handle-Initialize $msg)
        continue
    }

    if ($msg.method -eq "notifications/initialized") {
        continue
    }

    if ($msg.method -eq "tools/list") {
        Write-MCPMessage (Handle-ToolsList $msg)
        continue
    }

    if ($msg.method -eq "tools/call") {
        Write-MCPMessage (Handle-ToolsCall $msg)
        continue
    }

    if ($null -ne $msg.method) {
        Write-MCPMessage (Handle-DirectMethod $msg)
        continue
    }
}
