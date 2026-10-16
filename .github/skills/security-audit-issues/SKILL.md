---
name: security-audit-issues
description: "Analyze codebase for security concerns and generate GitHub issues"

ai_generated: true
model: "OpenAI/GPT-6@Luna"
operator: "johnmillerATcodemag-com"
chat_id: "convert-prompt-files-to-skills-20261016"
prompt: |
  help me convert the prompt files in the prompts folder into skills.
started: "2026-10-16T21:25:07.811Z"
ended: "2026-10-16T21:43:11.234Z"
task_durations:
  - task: "Converting repository prompt files to skills"
    duration: "00:18:03"
total_duration: "00:18:03"
ai_log: "ai-logs/2026/10/16/convert-prompt-files-to-skills-20261016/conversation.md"
source: ".github/prompts/security-audit-issues.prompt.md"
---
# Security Audit — Findings to GitHub Issues

What are security concerns in the codebase? Create GitHub issues from findings.

## Inputs
Source code and configs, signals (secrets, insecure deps, unsafe APIs, missing validations, weak crypto, authz gaps, misconfigs, CI/CD exposures)

## Exclusions
`.git/`, `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, binaries

## Checks
- **Secrets**: Hardcoded keys/tokens, `.env` handling, `.gitignore` gaps
- **Dependencies**: Known-vulnerable packages, lockfiles, audit scripts
- **Injection**: Unsanitized input in queries/commands/templates, improper parameterization
- **XSS/templating**: Unescaped user input in UI, DOM sinks
- **AuthN/AuthZ**: Missing checks, insecure session/token handling, CSRF protections
- **Crypto**: Unsafe algorithms/modes, missing salting/IVs, homegrown crypto
- **Transport/headers**: Missing HTTPS/HSTS, CSP, X-Frame-Options
- **Logging**: Sensitive data in logs, lack of error boundaries, PII leakage
- **Config**: Default creds, permissive CORS, debug flags in prod

## Process
1. **Discover**: Security-relevant files (configs, auth/crypto, DB, HTTP clients/servers, CI/CD)
2. **Scan**: Collect evidence (file:line), minimize speculation
3. **Classify**: Severity (Critical/High/Medium/Low), impact, map to OWASP Top 10/CWE
4. **Create issues**: Title, evidence, impact, remediation, refs, severity/area labels
5. **Summarize**: Executive summary + durations

## Output (Markdown)

### Executive summary
2–3 sentences on security posture and top risks

### Findings table
| ID | Category | File:Lines | Severity | Impact | OWASP/CWE | Remediation |
|----|----------|------------|----------|--------|-----------|-------------|
| SEC-001 | Hardcoded secret | `path:lines` | High | Key leakage | A02/CWE-798 | Move to vault/env, rotate |

### GitHub issue drafts per finding
**[SEC-001] Hardcoded secret in path**
- Severity: High
- Category: Secrets management
- Affected: `file:lines`
- Standards: OWASP A02, CWE-798
- Description: Evidence of hardcoded API key/token in repo
- Impact: Exposure enables unauthorized access
- Remediation: Remove from source, use env vars/secret manager, rotate key, add pre-commit/CI secret scan
- References: OWASP/CWE links
- Labels: security, severity:high, area:config

### Sources scanned
Key files/dirs consulted

### Durations
Per-step + total

## Constraints
- Evidence-driven with file:line refs
- No external calls/code changes
- Actionable, minimal remediations





