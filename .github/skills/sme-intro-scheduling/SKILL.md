---
name: sme-intro-scheduling
description: "Schedule introductory meetings with subject-matter experts from supplied availability and status data, respecting time zones, constraints, and privacy."
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  Merge useful gaps and create proposed new skills
started: "2026-10-17T19:33:05.9169653-07:00"
ended: "2026-10-17T19:52:32.094572-07:00"
task_durations:
  - task: "Approved cross-repository prompt-to-skill migration"
    duration: "00:19:26"
total_duration: "00:19:26"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "V&S/.github/prompts/sme-intro-invites.prompt.md"
---

# SME Introductory Meeting Scheduling

Use this skill to propose meeting slots and attendee groupings from a supplied availability table or scheduling export.

## Procedure

1. Confirm meeting duration, date range, working-hour limits, time zones, required attendees, platform, and prioritization rules.
2. Parse the supplied availability/status data. Map source-specific status values to explicit meanings; ask when a value is ambiguous.
3. Normalize times to a consistent zone while preserving each attendee's local time and daylight-saving context.
4. Exclude unavailable, already scheduled, or otherwise ineligible participants according to the user's rules.
5. Find slots satisfying required attendees and constraints. Optimize overlap or number of meetings only when the objective is specified.
6. Check conflicts, duplicate participants, minimum notice, and schedule feasibility. Present alternatives where no slot satisfies all constraints.
7. Draft an invite list or calendar-ready proposal only; create or send invitations only with explicit authorization.

## Output

Provide proposed slot(s) with time zone, included participants, exclusions and reasons, unresolved availability, and any assumptions. Keep raw contact information out of summaries unless needed for the approved invite workflow.

## Guardrails

- Do not infer availability from missing or stale data.
- Do not expose personal email addresses or other contact details in broad reports.
- Do not send invitations, reserve calendars, or change source records without approval.
- Clearly mark tentative proposals and conflicts.
