---
name: create-ai-assisted-output-policy
description: "Generate comprehensive AI provenance and logging policy for all AI-assisted outputs"

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
source: ".github/prompts/create-ai-assisted-output-instructions.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added host-capability verification, clear mandatory/recommended status, safe examples, and an approval boundary for policy replacement."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Generate AI-Assisted Output Policy

Create comprehensive policy defining required metadata, workflow, and enforcement for all AI-assisted outputs.

## Purpose
Clear provenance and reliable logging for all AI-assisted artifacts to enable audits and understand how artifacts were produced.

## Output: `.github/instructions/ai-assisted-output.instructions.md`

### Structure:
1. **Overview**: Purpose, audience (contributors, developers), scope (all AI-assisted content), terminology (chat ID, not session)
2. **Metadata Placement Policy**: 
   - Formats supporting front matter (Markdown): embed YAML at top
   - Formats not supporting (images, binaries): sidecar `<artifact>.meta.md`
   - No sidecars for Markdown
3. **Required Provenance Metadata** (11 fields):
   - `ai_generated: true` (boolean)
   - `model: "<provider>/<model-name>@<version>"` (explicit format, e.g., "openai/gpt-4o@2024-11-20")
   - `operator: "<github-username>"`
   - `chat_id: "<chat-identifier>"`
   - `prompt: |` (exact prompt text, multiline)
   - `started: "<ISO8601-timestamp>"`
   - `ended: "<ISO8601-timestamp>"`
   - `task_durations:` (array of task/duration objects)
   - `total_duration: "<hh:mm:ss>"`
   - `ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"`
   - `source: "<creator or prompt path>"`
4. **Chat Logging Workflow**:
   - Structure: `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/` with `conversation.md` and `summary.md`
   - Conversation format: Chat ID, operator, model, timestamps, context, exchanges, work burst closure, artifacts
   - Summary format: Overview, methodology, decisions, alternatives, edge cases, testing, validation, next steps
5. **Task Durations**: Capture per-task (analysis, design, implementation, testing) and total
6. **Placement & Naming**: Conventions for different artifact types
7. **Quality Checklist**: All 11 fields present, model explicit format, chat_id matches ai_log path, timestamps ISO8601
8. **Copilot Integration**: Model identification, chat management, file generation workflow
9. **Enforcement (CI)**: Example validation scripts (Linux/Mac, PowerShell)
10. **Non-Compliance & Remediation**: What happens if missing, how to fix

### Key Requirements:
- Model format MUST be `"<provider>/<model-name>@<version>"` (NOT "Auto (copilot)")
- Use GitHub username, not "USER"
- Each chat creates new conversation.md and summary.md
- Update README.md with link to new artifacts

### Templates to Include:
- Standard metadata front matter
- conversation.md template
- summary.md template
- CI validation scripts

## Deliverable
Complete policy with YAML front matter per its own requirements, all sections, templates, enforcement examples.

## Authoring Workflow

- Read the existing policy, relevant Copilot guidance, CI workflows, and log conventions. Distinguish implemented automation from recommended practice.
- Separate mandatory requirements from recommendations. Verify host capabilities before claiming automatic transcript export, model discovery, file interception, or enforcement.
- Ensure metadata, conversation, summary, and CI examples use valid YAML and commands that exist in the repository. Do not include credentials, private chat content, or sensitive personal data.
- Validate links, examples, metadata, and referenced scripts or workflows.

## Boundaries

- Do not create a competing policy.
- Do not promise automation or enforcement without implementation evidence.
- Preserve the existing canonical policy unless the user explicitly approves replacing it.


