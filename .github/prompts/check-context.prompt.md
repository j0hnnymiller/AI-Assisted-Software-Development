---
mode: chat
name: check-context-conflicts
model: "<provider>/<model-name>@<version>"
tools: ["search", "read"]
description: Analyze supplied and relevant repository context for contradictions, ambiguities, inconsistencies, duplication, and missing information.
prompt_metadata:
  id: check-context-conflicts
  title: Context Analysis and Conflict Detection
  owner: johnmillerATcodemag-com
  version: "1.1.0"
  created: "2025-02-05"
  updated: "2026-08-13"
  output_path: null
  category: analysis
  tags: [analysis, conflicts, validation, context, instructions]
  output_format: markdown

# Include the repository-required AI provenance fields here when this file is regenerated.
---

# Context Analysis and Conflict Detection

Analyze the context supplied by the user and any directly relevant repository files. Return a read-only analysis report in chat. Do not modify files unless the user explicitly requests changes.

## Scope

Inspect only:

1. Context explicitly supplied by the user
2. The current file and directly referenced files
3. Applicable repository instruction files
4. Supporting files that are necessary to verify a reported issue

If the available context is incomplete, state that limitation. Do not infer that the context is consistent merely because no conflict was found.

## Source Precedence

When statements conflict, evaluate them according to:

1. System and developer instructions
2. Applicable repository instructions
3. Explicit user requirements
4. Project documentation and specifications
5. Informational examples, comments, and inferred conventions

Report a precedence issue when a lower-priority source attempts to override a higher-priority source.

## Classification Rules

Classify each finding using exactly one primary category:

- **Conflict**: Two directives cannot both be followed within the same scope.
- **Inconsistency**: Facts, dates, names, versions, identifiers, or values disagree.
- **Logical contradiction**: A conclusion or rule cannot follow from, or contradicts, the stated premises.
- **Ambiguity**: A statement has multiple reasonable interpretations.
- **Duplication**: Information is repeated without adding meaning or is presented inconsistently in multiple places.
- **Missing information**: Required context, definition, dependency, or acceptance criterion is absent.

## Analysis Procedure

1. Identify directives, facts, assumptions, terminology, and scope boundaries.
2. Normalize equivalent terms and distinguish true conflicts from wording differences.
3. Compare statements only when they apply to the same subject and scope.
4. Verify each finding against the cited source.
5. Avoid reporting preferences as conflicts.
6. Avoid inventing facts that are not present in the context.
7. Consolidate duplicate findings that have the same root cause.
8. Identify unresolved questions separately from confirmed findings.

## Severity

Use one severity:

- **Critical**: Prevents execution or creates serious security, safety, legal, or compliance risk.
- **High**: Likely causes incorrect implementation, invalid output, or a significant behavioral defect.
- **Medium**: Creates substantial ambiguity, inconsistency, or maintenance risk.
- **Low**: Cosmetic, terminology-related, or low-impact redundancy.

Also assign confidence: `high`, `medium`, or `low`.

## Response Format

Begin with a summary:

- Overall assessment
- Number of findings by severity
- Whether the analysis was limited by missing context

Then report each finding using this format:

### [ID] [Severity] [Category]

- **Confidence**: high | medium | low
- **Location A**: File, section, heading, or line when available
- **Location B**: File, section, heading, or line when available
- **Evidence**: Quote or accurately paraphrase both relevant statements
- **Explanation**: Why the statements conflict, disagree, or leave a material gap
- **Impact**: What could happen if the issue remains unresolved
- **Recommendation**: Specific resolution, including which statement should change when determinable

Finish with:

## Open Questions

List unresolved questions that require user or stakeholder input.

## Assumptions and Limitations

List assumptions made and context that was unavailable.

## No-Finding Result

If no confirmed issues exist, state:

> No confirmed conflicts or inconsistencies were found in the analyzed context.

Then separately list any ambiguities, open questions, assumptions, or limitations.
