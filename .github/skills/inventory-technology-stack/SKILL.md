---
name: inventory-technology-stack
description: "Analyze a folder tree and list the technologies it uses - languages, runtimes, frameworks, libraries, container images, CI actions, and infrastructure providers - with each one's name, version, and reference count. Use when asked what tech stack, dependencies, packages, or frameworks a codebase uses, for a technology inventory or bill of materials, or to count how often each dependency is referenced."
argument-hint: "Folder to scan, e.g. src/ (default: workspace root)"
metadata:
  ai_generated: true
  model: "unknown/unknown@unknown"
  operator: "johnmillerATcodemag-com"
  chat_id: "e27f92b4-c5a3-4353-baeb-5ee39ffac8c1"
  prompt: "create a new skill that analyzes the code in a folder tree and returns a list of the technologies utilized. Include the name, the version, and the number of references"
  started: "2026-10-27T21:25:13Z"
  ended: "2026-10-27T21:40:00Z"
  task_durations:
    - task: "Skill and scanner script authoring"
      duration: "00:04:30"
    - task: "Unit tests and smoke validation"
      duration: "00:02:17"
    - task: "Software Archeologist agent association"
      duration: "00:02:57"
  total_duration: "00:09:44"
  ai_log: "ai-logs/2026/10/27/e27f92b4-c5a3-4353-baeb-5ee39ffac8c1/conversation.md"
  source: "user"
---

# Inventory Technology Stack

Read-only analysis of a folder tree that returns each technology used, its
version, and how many times it is referenced.

## When to Use

- "What technologies/frameworks/packages does this code use?"
- Building a technology inventory, dependency list, or lightweight bill of materials
- Comparing how heavily each dependency is actually used before an upgrade or removal

Not for vulnerability, license, or outdated-version checks; use a dedicated
dependency-audit tool for those.

The [Software Archeologist agent](../../agents/software-archeologist.agent.md)
uses this skill for dependency archaeology (`@inventory-stack`).

## Inputs

- **Root folder** (required; default: workspace root). Confirm it exists.
- Optional: exclude globs, folders normally skipped to include (for example
  `vendor`), output format (`markdown`, `json`, `csv`), and whether to list
  undeclared third-party imports.

## Procedure

1. Confirm the root folder and any exclusions. Ask before scanning a tree outside
   the workspace.
2. Run the [scanner](./scripts/inventory_technologies.py) (Python 3.11+, standard
   library only):
   ```powershell
   python .github/skills/inventory-technology-stack/scripts/inventory_technologies.py <root> --undeclared
   python .github/skills/inventory-technology-stack/scripts/inventory_technologies.py <root> --format json --exclude "tests/fixtures/*"
   ```
   Options: `--format markdown|json|csv`, `--output <file>`, `--exclude <glob>`
   (repeatable, relative to root), `--include-dir <name>` (repeatable),
   `--min-references <n>`, `--max-file-bytes <n>`, `--undeclared`.
3. Review the output. Check warnings (unparseable or skipped manifests) and the
   undeclared-imports list, which can reveal dependencies installed without a
   manifest entry.
4. If the tree contains ecosystems the scanner does not cover (see
   [Coverage](#coverage)), inspect those manifests directly and add rows, marking
   them as manually identified.
5. Report using the format below. Do not modify the scanned tree, install
   packages, or run builds. Write a report file only when the user asks.

## Reference counting

`References` = declarations + imports + files:

| Kind | Counted as |
| --- | --- |
| declarations | Each manifest/config entry naming the technology (package entry, `TargetFramework`, `engines`, `FROM`, `uses:`, `.nvmrc`, and similar) |
| imports | Each source import/using/require statement that resolves to a declared package (statements, not files) |
| files | Source files of a language, by extension |

## Versions

- Declared version specs are reported as written (`^18.2.0`, `>=3.11`).
- npm versions come from `package-lock.json` when it exists next to `package.json`.
- Multiple distinct versions are comma-separated; flag them as possible drift.
- `unspecified` means no version was found. Do not guess a version.

## Coverage

| Ecosystem | Manifests and config | Import matching |
| --- | --- | --- |
| JavaScript/TypeScript | `package.json`, `package-lock.json`, `.nvmrc`, `.node-version` | `import`, `require`, dynamic `import()` |
| Python | `requirements*.txt`/`.in`, `pyproject.toml` (PEP 621, Poetry, dependency groups), `.python-version`, `runtime.txt` | `import`, `from ... import`, common distribution aliases |
| .NET | `*.csproj`/`*.fsproj`/`*.vbproj`, `Directory.Packages.props`, `Directory.Build.props`, `packages.config`, `global.json` | C# `using` by longest package-ID prefix |
| Go | `go.mod` | import blocks by module path |
| Java/Kotlin | `pom.xml`, `build.gradle(.kts)` | `import` by group ID prefix (approximate) |
| Ruby, Rust, PHP | `Gemfile`, `.ruby-version`, `Cargo.toml`, `composer.json` | Ruby `require`, Rust `use` (no PHP imports) |
| Containers, CI, IaC | `Dockerfile*`, `compose*.yml`, `.github/workflows/*.yml`, `azure-pipelines.yml`, `*.tf` | n/a |

Languages are counted by file extension. Dependency folders and build output
(`node_modules`, `bin`, `obj`, `dist`, `.venv`, `vendor`, `target`, and similar)
are skipped by default.

## Limitations

- Static, regex-based import detection: aliased, generated, reflective, or
  string-built imports are missed; commented-out imports may be counted.
- Import names that differ from package names are matched only for npm, Go, and
  .NET prefixes and a small Python alias list; such packages may show
  declarations only.
- Lock files other than `package-lock.json` are not read; transitive
  dependencies are not listed.
- Bicep, Helm, Kubernetes manifests, and Swift/Dart package files are not parsed;
  Bicep and other languages still appear by file count.

## Report Format

1. Root scanned, exclusions, and command used.
2. Table sorted by references (descending):

   | Name | Category | Version | References | Breakdown |
   | --- | --- | --- | ---: | --- |

3. Notes: version drift, undeclared imports, warnings, manually added rows, and
   any coverage gaps relevant to this tree.

## Validation

Run the bundled tests after changing the scanner:

```powershell
python -m unittest discover -s .github/skills/inventory-technology-stack/scripts -p "test_*.py"
```
