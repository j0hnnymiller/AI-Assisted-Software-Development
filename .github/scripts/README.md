---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
prompt: |
  go ahead
started: "2026-10-18T12:55:34.864-07:00"
ended: "2026-10-18T12:57:39.092-07:00"
task_durations:
  - task: "Copy helper remediation and focused Pester validation"
    duration: "00:02:04"
total_duration: "00:02:04"
ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
source: "User approval of the copy-helper remediation recommendations"
---

# Hub Script Support

Course-specific slide scripts are maintained in the Course repository, not this
shared configuration hub. The standalone instruction-sync and copy helpers have
been retired.

Use [config distribution](../skills/github-config-distribute/SKILL.md) for
manifest-controlled planning and approved synchronization. Its
[manifest](../github-config-sync.json) defines the shared configuration scope.

Run the distribution regression tests from the hub root:

```powershell
Invoke-Pester -Path .\.github\scripts\tests\sync-github-config.Tests.ps1 -Output Detailed
```
