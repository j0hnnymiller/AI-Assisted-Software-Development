---
name: meeting-briefs-from-transcripts
description: "Turn a meeting transcript or notes into a concise brief of status, decisions, risks, open questions, and owners with attribution grounded in the source."
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
source: "Messer/.github/prompts/meeting-brief-from-transcript.prompt.md"
---

# Meeting Briefs from Transcripts

Use this skill to prepare a decision-focused meeting brief from a supplied transcript or notes.

## Procedure

1. Identify the meeting purpose, date, participants, and source limitations. Do not infer missing details.
2. Extract current status, decisions, commitments, risks/blockers, open questions, and next steps.
3. Attribute statements or actions to a speaker only when the source supports that attribution; otherwise mark the owner as unknown.
4. Distinguish decisions from proposals and unresolved questions. Preserve important qualifiers and dates.
5. Deduplicate repeated points and prioritize items relevant to the intended audience.
6. Verify each brief item against the source and omit unrelated transcript detail.

## Output

Use a one-page brief where feasible: purpose, status, decisions, risks/blockers, questions requiring resolution, and action table (`Action | Owner | Due date | Source/status`). State unavailable owners or dates as unknown.

## Guardrails

- Do not invent decisions, commitments, owners, deadlines, or consensus.
- Handle personal or confidential information according to the user's data policy; omit unnecessary sensitive details.
- Do not reproduce a transcript in full unless explicitly requested.
