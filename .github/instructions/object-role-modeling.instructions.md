---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
prompt: |
  go ahead
started: "2026-10-18T21:18:06.5025075Z"
ended: "2026-10-18T21:21:10.0332460Z"
task_durations:
  - task: "ORM terminology review and guide adaptation"
    duration: "00:03:03"
total_duration: "00:03:03"
ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
source: "Approved ORM authoring gap; adapted Fleetly object-role-models.instruction.md and verified terminology against orm.net"
description: "Use when creating or reviewing an Object Role Modeling (ORM) conceptual model; covers scope, elementary fact types, object types, constraints, verbalization, sample populations, conceptual queries, and model validation."
---

# Object Role Modeling

## Overview

Use this guide to develop or review a conceptual information model with Object
Role Modeling (ORM). ORM is fact-oriented: at the conceptual level, represent
elementary facts as relationships among objects playing roles rather than
introducing attributes into those fact types. Keep business meaning and
validation independent of a particular database schema or modeling tool.

This instruction covers conceptual model authoring and review. For deriving
user-goal use cases from an existing ORM model, use
[use-cases-from-conceptual-model](../skills/use-cases-from-conceptual-model/SKILL.md).
That skill consumes a model; it does not establish or validate the model's
business rules. For diagram rendering, also follow
[Mermaid guidance](mermaid.instructions.md) when using Mermaid to explain a model;
do not treat Mermaid flowcharts as a substitute for ORM notation.

## Modeling workflow

1. **Set the boundary and evidence.**
   - State the universe of discourse, intended use, included/excluded concepts,
     stakeholders, and required business questions.
   - Gather domain terms, policies, examples, existing records, and approved
     requirements. Label stakeholder statements, observed facts, assumptions,
     decisions, and unresolved questions distinctly.
   - Clarify whether a rule states what must be true, what is permitted, or what
     actors are obliged to do. Do not model a policy obligation as an
     impossible-to-violate structural fact without an explicit domain decision.

2. **Define object types and terms.**
   - Describe each relevant kind of object in domain language. Distinguish
     object types from individual instances and avoid creating types solely to
     mirror tables, classes, screens, or implementation components.
   - Record how each object is identified, including any agreed reference scheme.
     Do not assume a name or descriptive value is unique without evidence.
   - Where scalar or value-like concepts are modeled, represent them according
     to the chosen ORM dialect and tool; keep their role in facts explicit.

3. **Express elementary fact types.**
   - Capture the smallest meaningful claims that domain experts can understand
     and confirm. Identify the participating object types and the meaning of
     each role.
   - Use complete predicate readings that make role order and meaning clear.
     Split compound statements into elementary facts when doing so preserves
     their meaning; do not decompose a domain concept mechanically.
   - Record synonyms and preferred terms. Avoid overloaded or ambiguous words.

4. **Add constraints from stated rules.**
   - Map every modeled constraint to a source rule, decision, or explicit
     modeling assumption. Identify the affected fact type, role, object type,
     or schema path.
   - Specify identification and uniqueness constraints and mandatory roles
     where evidence requires them. Consider value, frequency, subtype,
     subset/equality, exclusion, ring, and join constraints only when the
     domain rule and selected ORM dialect support them.
   - State modality, scope, and exceptions precisely. If two plausible
     readings produce different constraints, retain the ambiguity and ask the
     domain owner; do not choose silently.

5. **Use objectification and derivation deliberately.**
   - Objectify a fact type only when the business meaning requires referring
     to that relationship as an object. Document the reason, identification,
     and affected uniqueness constraints; check the selected ORM dialect's
     objectification rules.
   - Record derived facts and their derivation rule separately from directly
     asserted facts. Identify the assumptions and dependencies used.

6. **Validate verbalizations and populations.**
   - Produce natural-language readings for facts and constraints. Review them
     with domain experts, including role direction, quantifiers, uniqueness,
     mandatory participation, modality, and exceptions.
   - Populate small, synthetic example fact populations. Check valid examples
     against each constraint and construct counterexamples that should be
     rejected. Record which rule each example tests.
   - Resolve contradictions and uncovered cases before treating the model as
     accepted. A plausible diagram or a tool's successful parse is not domain
     validation.

7. **Test conceptual questions.**
   - Express important stakeholder questions using paths through the conceptual
     facts and constraints. Check that each question has a clear reading and
     that the model supplies the required concepts without assuming table or
     storage layout.
   - Keep conceptual queries separate from use-case scenarios and from SQL,
     APIs, or other implementation queries.

8. **Keep implementation mapping separate.**
   - If requested, document a logical or physical mapping as a distinct output,
     preserving links back to the conceptual facts and constraints.
   - Do not alter conceptual meaning merely to fit a preferred relational,
     object-oriented, object-relational mapping technology, or vendor-specific implementation.
   - State mapping decisions, transformations, and unresolved trade-offs.

## Suggested deliverable structure

Adapt to an existing project template; this is a review checklist, not a
mandatory file format.

```markdown
# <Domain> Conceptual Model

## Scope and Evidence
- Universe of discourse:
- Intended questions:
- Sources, decisions, assumptions, open issues:

## Object Types and Identification
- <Object type>: <meaning>; identified by <verified reference scheme>

## Elementary Fact Types
- <Complete predicate reading with role meanings>

## Constraints
- <Constraint>: <precise scope and reading>; source: <rule or decision>

## Derivations and Objectification
- <Rule or objectified fact type, rationale, and implications>

## Verbalization and Sample Populations
- <Reviewed reading, example facts, counterexample, validation result>

## Conceptual Queries
- <Question and its path/readings>

## Mapping Notes (if requested)
- <Separate implementation mapping and trade-offs>
```

## Validation checklist

- [ ] Scope, sources, decisions, assumptions, and unresolved questions are explicit.
- [ ] Object types and identification schemes use domain evidence.
- [ ] Fact types are elementary where meaningful, attribute-free at the
      conceptual fact level, and fully verbalizable.
- [ ] Each constraint has a source and an unambiguous scope, modality, and reading.
- [ ] Objectification and derivation are justified; dialect-specific conditions
      are checked rather than assumed.
- [ ] Synthetic fact populations test both satisfying and violating examples.
- [ ] Domain experts reviewed material verbalizations and exceptions, or the
      missing validation is stated.
- [ ] Required business questions can be read against the conceptual model.
- [ ] Conceptual rules remain distinct from logical/physical mapping and use cases.
- [ ] Tool, notation, version, and renderer limitations are stated; no validation
      is claimed beyond checks actually performed.
- [ ] Examples contain no secrets or private personal data.

## References

The ORM site describes ORM as a fact-oriented approach for specifying,
transforming, and querying information conceptually, and discusses elementary
facts, constraints, derivation rules, conceptual queries, and objectification.
Its materials describe related ORM dialects and historical tools; confirm exact
syntax and support in the selected dialect/tool documentation.

- [ORM overview](https://orm.net/overview.html)
- [Modeling issues](https://orm.net/issues.html)
- [Conceptual queries](https://orm.net/queries.html)
- [UML and ORM](https://orm.net/uml_orm.html)
