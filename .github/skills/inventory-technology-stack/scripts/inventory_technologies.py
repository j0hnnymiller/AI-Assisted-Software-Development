"""Inventory technologies used in a folder tree.

Reports each technology's name, category, declared/resolved versions, and
reference count, with a per-kind breakdown and sample evidence paths.
Read-only: never modifies the scanned tree. Requires Python 3.11+.
"""

from __future__ import annotations

import argparse
import csv
import fnmatch
import io
import json
import os
import re
import sys
import tomllib
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "bower_components", "bin", "obj",
    "dist", "build", "out", "target", "vendor", ".venv", "venv", "env",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".tox", ".next", ".nuxt",
    "coverage", ".gradle", ".idea", ".vs", "packages", ".terraform",
}

LANGUAGES = {
    ".py": "Python", ".pyw": "Python", ".ipynb": "Jupyter Notebook",
    ".js": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript", ".jsx": "JavaScript",
    ".ts": "TypeScript", ".mts": "TypeScript", ".cts": "TypeScript", ".tsx": "TypeScript",
    ".cs": "C#", ".fs": "F#", ".vb": "Visual Basic .NET", ".razor": "Razor", ".cshtml": "Razor",
    ".java": "Java", ".kt": "Kotlin", ".kts": "Kotlin", ".scala": "Scala", ".groovy": "Groovy",
    ".go": "Go", ".rs": "Rust", ".rb": "Ruby", ".php": "PHP", ".swift": "Swift",
    ".m": "Objective-C", ".c": "C", ".h": "C/C++ Header", ".cpp": "C++", ".cc": "C++",
    ".cxx": "C++", ".hpp": "C++", ".dart": "Dart", ".lua": "Lua", ".r": "R", ".jl": "Julia",
    ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell", ".ps1": "PowerShell", ".psm1": "PowerShell",
    ".sql": "SQL", ".html": "HTML", ".htm": "HTML", ".css": "CSS", ".scss": "Sass", ".sass": "Sass",
    ".less": "Less", ".vue": "Vue", ".svelte": "Svelte", ".tf": "Terraform", ".bicep": "Bicep",
}

# Distribution name -> import name, where they differ (Python).
PY_IMPORT_ALIASES = {
    "pyyaml": "yaml", "beautifulsoup4": "bs4", "pillow": "PIL", "scikit-learn": "sklearn",
    "python-dateutil": "dateutil", "opencv-python": "cv2", "python-dotenv": "dotenv",
    "python-docx": "docx", "python-pptx": "pptx", "pyjwt": "jwt", "protobuf": "google.protobuf",
    "msgpack-python": "msgpack", "attrs": "attr", "pymupdf": "fitz", "pywin32": "win32api",
}

NODE_BUILTINS = {
    "assert", "buffer", "child_process", "cluster", "crypto", "dgram", "dns", "events", "fs",
    "http", "http2", "https", "module", "net", "os", "path", "perf_hooks", "process",
    "querystring", "readline", "stream", "string_decoder", "timers", "tls", "tty", "url",
    "util", "v8", "vm", "worker_threads", "zlib",
}

IMPORT_PATTERNS = {
    "npm": [
        re.compile(r"""\bfrom\s+['"]([^'"]+)['"]"""),
        re.compile(r"""\bimport\s+['"]([^'"]+)['"]"""),
        re.compile(r"""\brequire\(\s*['"]([^'"]+)['"]\s*\)"""),
        re.compile(r"""\bimport\(\s*['"]([^'"]+)['"]\s*\)"""),
    ],
    "pypi": [
        re.compile(r"^[ \t]*import[ \t]+([A-Za-z_][\w.]*(?:[ \t]+as[ \t]+\w+)?(?:[ \t]*,[ \t]*[A-Za-z_][\w.]*(?:[ \t]+as[ \t]+\w+)?)*)", re.M),
        re.compile(r"^[ \t]*from[ \t]+([A-Za-z_][\w.]*)[ \t]+import\b", re.M),
    ],
    "nuget": [re.compile(r"^\s*(?:global\s+)?using\s+(?:static\s+)?([A-Za-z_][\w.]*)\s*;", re.M)],
    "go": [re.compile(r'^\s*(?:import\s+)?(?:[\w.]+\s+)?"([^"]+)"', re.M)],
    "rubygems": [re.compile(r"""^\s*require\s+['"]([^'"]+)['"]""", re.M)],
    "cargo": [re.compile(r"^\s*(?:pub\s+)?use\s+([A-Za-z_]\w*)::", re.M),
              re.compile(r"^\s*extern\s+crate\s+([A-Za-z_]\w*)", re.M)],
    "maven": [re.compile(r"^\s*import\s+(?:static\s+)?([\w.]+)\s*;?", re.M)],
}

ECOSYSTEM_EXTENSIONS = {
    "npm": {".js", ".mjs", ".cjs", ".jsx", ".ts", ".mts", ".cts", ".tsx", ".vue", ".svelte"},
    "pypi": {".py", ".pyw"},
    "nuget": {".cs", ".razor", ".cshtml"},
    "go": {".go"},
    "rubygems": {".rb"},
    "cargo": {".rs"},
    "maven": {".java", ".kt", ".kts", ".scala", ".groovy"},
}


@dataclass
class Tech:
    name: str
    category: str
    ecosystem: str = ""
    versions: set[str] = field(default_factory=set)
    declarations: int = 0
    imports: int = 0
    files: int = 0
    evidence: list[str] = field(default_factory=list)

    @property
    def references(self) -> int:
        return self.declarations + self.imports + self.files

    def add_evidence(self, path: str, limit: int = 5) -> None:
        if path not in self.evidence and len(self.evidence) < limit:
            self.evidence.append(path)


class Inventory:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.items: dict[tuple[str, str], Tech] = {}
        self.warnings: list[str] = []
        self.unmatched_imports: dict[str, dict[str, int]] = {}

    def get(self, name: str, category: str, ecosystem: str = "") -> Tech:
        key = (category, name.lower() if ecosystem in {"pypi", "nuget"} else name)
        if key not in self.items:
            self.items[key] = Tech(name, category, ecosystem)
        return self.items[key]

    def rel(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def declare(self, name: str, category: str, ecosystem: str, version: str | None, path: Path) -> Tech:
        tech = self.get(name, category, ecosystem)
        tech.declarations += 1
        if version and version.strip():
            tech.versions.add(version.strip())
        tech.add_evidence(self.rel(path))
        return tech


def read_text(path: Path, max_bytes: int) -> str | None:
    try:
        if path.stat().st_size > max_bytes:
            return None
        return path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return None


def walk(root: Path, skip_dirs: set[str], excludes: list[str]):
    def excluded(path: Path) -> bool:
        return any(fnmatch.fnmatch(path.relative_to(root).as_posix(), p) for p in excludes)

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            d for d in dirnames
            if d not in skip_dirs and not d.endswith(".egg-info") and not excluded(Path(dirpath) / d)
        )
        for name in sorted(filenames):
            path = Path(dirpath) / name
            if not excluded(path):
                yield path


# ---------- manifest parsers ----------

def parse_package_json(inv: Inventory, path: Path, text: str) -> None:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        inv.warnings.append(f"{inv.rel(path)}: invalid JSON ({exc.msg})")
        return
    lock = load_npm_lock(path.parent)
    for section in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        for name, spec in (data.get(section) or {}).items():
            inv.declare(name, "library", "npm", lock.get(name) or str(spec), path)
    for engine, spec in (data.get("engines") or {}).items():
        label = {"node": "Node.js", "npm": "npm", "pnpm": "pnpm", "yarn": "Yarn"}.get(engine, engine)
        inv.declare(label, "runtime" if engine == "node" else "tool", "", str(spec), path)
    if pm := data.get("packageManager"):
        name, _, version = str(pm).partition("@")
        inv.declare(name, "tool", "", version.split("+")[0], path)


def load_npm_lock(folder: Path) -> dict[str, str]:
    try:
        data = json.loads((folder / "package-lock.json").read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {}
    resolved: dict[str, str] = {}
    for key, meta in (data.get("packages") or {}).items():
        name = key.removeprefix("node_modules/")
        if key.startswith("node_modules/") and "/node_modules/" not in name:
            if version := (meta or {}).get("version"):
                resolved[name] = version
    for name, meta in (data.get("dependencies") or {}).items():
        if isinstance(meta, dict) and meta.get("version"):
            resolved.setdefault(name, meta["version"])
    return resolved


REQ_LINE = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9._-]*)(?:\[[^\]]*\])?\s*(.*)$")


def split_requirement(line: str) -> tuple[str, str] | None:
    line = line.split("#", 1)[0].split(";", 1)[0].strip()
    if not line or line.startswith(("-", "git+", "http:", "https:", ".")):
        return None
    match = REQ_LINE.match(line)
    return (match.group(1), match.group(2).strip()) if match else None


def parse_requirements(inv: Inventory, path: Path, text: str) -> None:
    for line in text.splitlines():
        if req := split_requirement(line):
            inv.declare(req[0], "library", "pypi", req[1], path)


def parse_pyproject(inv: Inventory, path: Path, text: str) -> None:
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        inv.warnings.append(f"{inv.rel(path)}: invalid TOML ({exc})")
        return
    project = data.get("project") or {}
    if rp := project.get("requires-python"):
        inv.declare("Python", "language", "", rp, path)
    deps = list(project.get("dependencies") or [])
    for group in (project.get("optional-dependencies") or {}).values():
        deps.extend(group)
    for group in (data.get("dependency-groups") or {}).values():
        deps.extend(d for d in group if isinstance(d, str))
    for dep in deps:
        if req := split_requirement(dep):
            inv.declare(req[0], "library", "pypi", req[1], path)
    poetry = (data.get("tool") or {}).get("poetry") or {}
    sections = [poetry.get("dependencies") or {}, poetry.get("dev-dependencies") or {}]
    sections += [g.get("dependencies") or {} for g in (poetry.get("group") or {}).values()]
    for section in sections:
        for name, spec in section.items():
            version = spec if isinstance(spec, str) else (spec or {}).get("version", "")
            if name.lower() == "python":
                inv.declare("Python", "language", "", version, path)
            else:
                inv.declare(name, "library", "pypi", version, path)
    for name in (data.get("build-system") or {}).get("requires") or []:
        if req := split_requirement(name):
            inv.declare(req[0], "tool", "pypi", req[1], path)


def parse_msbuild(inv: Inventory, path: Path, text: str) -> None:
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        inv.warnings.append(f"{inv.rel(path)}: invalid XML ({exc})")
        return
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag in {"PackageReference", "PackageVersion"}:
            name = el.get("Include") or el.get("Update")
            version = el.get("Version") or el.get("VersionOverride") or (el.findtext("{*}Version") or "")
            if name:
                inv.declare(name, "library", "nuget", version, path)
        elif tag in {"TargetFramework", "TargetFrameworks"} and el.text:
            for tfm in el.text.split(";"):
                if tfm.strip():
                    inv.declare(".NET", "runtime", "", tfm.strip(), path)
        elif tag == "LangVersion" and el.text:
            inv.declare("C#", "language", "", el.text.strip(), path)
    if sdk := root.get("Sdk"):
        inv.declare(sdk.split("/")[0], "framework", "nuget", sdk.partition("/")[2], path)


def parse_packages_config(inv: Inventory, path: Path, text: str) -> None:
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return
    for el in root.iter("package"):
        if el.get("id"):
            inv.declare(el.get("id"), "library", "nuget", el.get("version"), path)


def parse_global_json(inv: Inventory, path: Path, text: str) -> None:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return
    if version := (data.get("sdk") or {}).get("version"):
        inv.declare(".NET SDK", "tool", "", version, path)


def parse_go_mod(inv: Inventory, path: Path, text: str) -> None:
    in_block = False
    for raw in text.splitlines():
        line = raw.split("//", 1)[0].strip()
        if line.startswith("go "):
            inv.declare("Go", "language", "", line[3:].strip(), path)
        elif line.startswith("require ("):
            in_block = True
        elif in_block and line == ")":
            in_block = False
        elif in_block or line.startswith("require "):
            parts = line.removeprefix("require ").split()
            if len(parts) >= 2:
                inv.declare(parts[0], "library", "go", parts[1], path)


def parse_pom(inv: Inventory, path: Path, text: str) -> None:
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return
    ns = root.tag[1:].split("}")[0] if root.tag.startswith("{") else ""
    q = (lambda t: f"{{{ns}}}{t}") if ns else (lambda t: t)
    props = {}
    if (p := root.find(q("properties"))) is not None:
        props = {c.tag.split("}")[-1]: (c.text or "").strip() for c in p}
    for key in ("java.version", "maven.compiler.release", "maven.compiler.source"):
        if props.get(key):
            inv.declare("Java", "language", "", props[key], path)
            break

    def resolve(v: str) -> str:
        return re.sub(r"\$\{([^}]+)\}", lambda m: props.get(m.group(1), m.group(0)), v or "")

    for dep in root.iter(q("dependency")):
        group, artifact = dep.findtext(q("groupId"), ""), dep.findtext(q("artifactId"), "")
        if group and artifact:
            inv.declare(f"{group}:{artifact}", "library", "maven", resolve(dep.findtext(q("version"), "")), path)


GRADLE_DEP = re.compile(
    r"""\b(?:implementation|api|compileOnly|runtimeOnly|testImplementation|annotationProcessor|kapt)"""
    r"""\s*\(?\s*['"]([^:'"]+):([^:'"]+):?([^'"]*)['"]"""
)


def parse_gradle(inv: Inventory, path: Path, text: str) -> None:
    for group, artifact, version in GRADLE_DEP.findall(text):
        inv.declare(f"{group}:{artifact}", "library", "maven", version, path)


def parse_gemfile(inv: Inventory, path: Path, text: str) -> None:
    for m in re.finditer(r"""^\s*gem\s+['"]([^'"]+)['"](?:\s*,\s*['"]([^'"]+)['"])?""", text, re.M):
        inv.declare(m.group(1), "library", "rubygems", m.group(2), path)
    if m := re.search(r"""^\s*ruby\s+['"]([^'"]+)['"]""", text, re.M):
        inv.declare("Ruby", "language", "", m.group(1), path)


def parse_cargo(inv: Inventory, path: Path, text: str) -> None:
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError:
        return
    if rv := (data.get("package") or {}).get("rust-version"):
        inv.declare("Rust", "language", "", rv, path)
    for section in ("dependencies", "dev-dependencies", "build-dependencies"):
        for name, spec in (data.get(section) or {}).items():
            version = spec if isinstance(spec, str) else (spec or {}).get("version", "")
            inv.declare(name, "library", "cargo", version, path)


def parse_composer(inv: Inventory, path: Path, text: str) -> None:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return
    for section in ("require", "require-dev"):
        for name, spec in (data.get(section) or {}).items():
            if name == "php":
                inv.declare("PHP", "language", "", spec, path)
            elif not name.startswith("ext-"):
                inv.declare(name, "library", "packagist", spec, path)


def parse_version_file(label: str, category: str):
    def parser(inv: Inventory, path: Path, text: str) -> None:
        version = text.strip().splitlines()[0].strip() if text.strip() else ""
        inv.declare(label, category, "", version.removeprefix("python-"), path)
    return parser


def add_image(inv: Inventory, ref: str, path: Path) -> None:
    if ref.lower() == "scratch" or "$" in ref:
        return
    ref = ref.split("@", 1)[0]
    if ":" in ref.rsplit("/", 1)[-1]:
        name, _, tag = ref.rpartition(":")
    else:
        name, tag = ref, "latest"
    inv.declare(name, "container-image", "docker", tag, path)


def parse_dockerfile(inv: Inventory, path: Path, text: str) -> None:
    stages = set()
    for m in re.finditer(r"^\s*FROM\s+(?:--platform=\S+\s+)?(\S+)(?:\s+AS\s+(\S+))?", text, re.M | re.I):
        if m.group(1).lower() not in stages:
            add_image(inv, m.group(1), path)
        if m.group(2):
            stages.add(m.group(2).lower())
    inv.declare("Docker", "tool", "", None, path)


def parse_compose(inv: Inventory, path: Path, text: str) -> None:
    for m in re.finditer(r"^\s*image:\s*['\"]?([^\s'\"#]+)", text, re.M):
        add_image(inv, m.group(1), path)
    inv.declare("Docker Compose", "tool", "", None, path)


def parse_workflow(inv: Inventory, path: Path, text: str) -> None:
    for m in re.finditer(r"^\s*-?\s*uses:\s*['\"]?([^\s'\"#@]+)@([^\s'\"#]+)", text, re.M):
        if not m.group(1).startswith("./"):
            inv.declare(m.group(1), "ci-action", "github-actions", m.group(2), path)
    inv.declare("GitHub Actions", "ci-cd", "", None, path)


def parse_azure_pipelines(inv: Inventory, path: Path, text: str) -> None:
    for m in re.finditer(r"^\s*-?\s*task:\s*['\"]?([\w.-]+)@(\d+)", text, re.M):
        inv.declare(m.group(1), "ci-action", "azure-pipelines", m.group(2), path)
    inv.declare("Azure Pipelines", "ci-cd", "", None, path)


def parse_terraform(inv: Inventory, path: Path, text: str) -> None:
    if m := re.search(r'required_version\s*=\s*"([^"]+)"', text):
        inv.declare("Terraform", "tool", "", m.group(1), path)
    for m in re.finditer(r'source\s*=\s*"([\w.-]+/[\w.-]+)"\s*(?:\n\s*version\s*=\s*"([^"]+)")?', text):
        inv.declare(m.group(1), "infrastructure-provider", "terraform", m.group(2), path)


MANIFESTS = [
    (lambda n: n == "package.json", parse_package_json),
    (lambda n: re.fullmatch(r"requirements.*\.(txt|in)", n) is not None, parse_requirements),
    (lambda n: n == "pyproject.toml", parse_pyproject),
    (lambda n: n.endswith((".csproj", ".fsproj", ".vbproj")), parse_msbuild),
    (lambda n: n in {"Directory.Packages.props", "Directory.Build.props"}, parse_msbuild),
    (lambda n: n == "packages.config", parse_packages_config),
    (lambda n: n == "global.json", parse_global_json),
    (lambda n: n == "go.mod", parse_go_mod),
    (lambda n: n == "pom.xml", parse_pom),
    (lambda n: n in {"build.gradle", "build.gradle.kts"}, parse_gradle),
    (lambda n: n == "Gemfile", parse_gemfile),
    (lambda n: n == "Cargo.toml", parse_cargo),
    (lambda n: n == "composer.json", parse_composer),
    (lambda n: n in {".nvmrc", ".node-version"}, parse_version_file("Node.js", "runtime")),
    (lambda n: n in {".python-version", "runtime.txt"}, parse_version_file("Python", "language")),
    (lambda n: n == ".ruby-version", parse_version_file("Ruby", "language")),
    (lambda n: n == "Dockerfile" or n.startswith("Dockerfile.") or n.endswith(".dockerfile"), parse_dockerfile),
    (lambda n: re.fullmatch(r"(docker-)?compose(\.[\w-]+)?\.ya?ml", n) is not None, parse_compose),
    (lambda n: n in {"azure-pipelines.yml", "azure-pipelines.yaml"}, parse_azure_pipelines),
    (lambda n: n.endswith(".tf"), parse_terraform),
]


# ---------- import matching ----------

def import_keys(ecosystem: str, name: str) -> list[str]:
    if ecosystem == "pypi":
        lowered = name.lower()
        if alias := PY_IMPORT_ALIASES.get(lowered.replace("_", "-")):
            return [alias, alias.lower()]
        return [lowered.replace("-", "_"), lowered.replace("-", "_").replace(".", "_")]
    if ecosystem == "cargo":
        return [name.replace("-", "_")]
    if ecosystem == "maven":
        return [name.split(":")[0]]
    return [name]


def normalize_import(ecosystem: str, spec: str) -> str | None:
    spec = spec.strip()
    if ecosystem == "pypi":
        spec = re.split(r"\s+as\s+", spec)[0]
    if not spec:
        return None
    if ecosystem == "npm":
        if spec.startswith((".", "/", "~", "#", "node:")) or "://" in spec:
            return None
        parts = spec.split("/")
        return "/".join(parts[:2]) if spec.startswith("@") else parts[0]
    return spec


def match_package(ecosystem: str, spec: str, index: dict[str, Tech]) -> Tech | None:
    if ecosystem == "npm":
        return index.get(spec)
    if ecosystem == "pypi":
        parts = spec.split(".")
        for i in range(len(parts), 0, -1):
            candidate = ".".join(parts[:i])
            if tech := index.get(candidate) or index.get(candidate.lower()):
                return tech
        return None
    # Longest declared prefix wins (namespaces, module paths, Java packages).
    best: tuple[str, Tech] | None = None
    for key, tech in index.items():
        if spec == key or spec.startswith((key + ".", key + "/", key + "::")):
            if best is None or len(key) > len(best[0]):
                best = (key, tech)
    return best[1] if best else None


def is_builtin(ecosystem: str, spec: str) -> bool:
    if ecosystem == "pypi":
        return spec.split(".")[0] in sys.stdlib_module_names
    if ecosystem == "npm":
        return spec in NODE_BUILTINS
    if ecosystem == "nuget":
        return spec.split(".")[0] in {"System", "Microsoft", "Windows"}
    if ecosystem == "go":
        return "." not in spec.split("/")[0]
    if ecosystem == "cargo":
        return spec in {"std", "core", "alloc", "crate", "self", "super"}
    if ecosystem == "maven":
        return spec.startswith(("java.", "javax.", "kotlin.", "scala."))
    return False


def local_python_modules(paths: list[Path]) -> set[str]:
    names = {p.stem for p in paths}
    names |= {p.parent.name for p in paths if p.name == "__init__.py"}
    return names


def scan_imports(inv: Inventory, sources: dict[str, list[Path]], max_bytes: int, track_undeclared: bool) -> None:
    for ecosystem, paths in sources.items():
        index: dict[str, Tech] = {}
        for tech in inv.items.values():
            if tech.ecosystem == ecosystem and tech.category in {"library", "framework"}:
                for key in import_keys(ecosystem, tech.name):
                    index[key] = tech
        if not paths or (not index and not track_undeclared):
            continue
        local = local_python_modules(paths) if ecosystem == "pypi" else set()
        for path in paths:
            text = read_text(path, max_bytes)
            if text is None:
                continue
            if ecosystem == "go":
                blocks = re.findall(r"^import\s*\((.*?)^\)", text, re.S | re.M)
                singles = re.findall(r"^import\s+((?:[\w.]+\s+)?\"[^\"]+\")", text, re.M)
                text = "\n".join(blocks + singles)
            for pattern in IMPORT_PATTERNS[ecosystem]:
                for raw in pattern.findall(text):
                    for part in raw.split(","):
                        spec = normalize_import(ecosystem, part)
                        if not spec:
                            continue
                        if tech := match_package(ecosystem, spec, index):
                            tech.imports += 1
                            tech.add_evidence(inv.rel(path))
                        elif track_undeclared and not is_builtin(ecosystem, spec):
                            root = spec.split(".")[0] if ecosystem == "pypi" else spec
                            if root in local:
                                continue
                            bucket = inv.unmatched_imports.setdefault(ecosystem, {})
                            bucket[root] = bucket.get(root, 0) + 1


# ---------- main ----------

def build_inventory(root: Path, skip_dirs: set[str], excludes: list[str], max_bytes: int,
                    track_undeclared: bool) -> Inventory:
    inv = Inventory(root)
    sources: dict[str, list[Path]] = {eco: [] for eco in ECOSYSTEM_EXTENSIONS}
    for path in walk(root, skip_dirs, excludes):
        name, ext = path.name, path.suffix.lower()
        rel_parts = path.relative_to(root).parts
        if language := LANGUAGES.get(ext):
            tech = inv.get(language, "language")
            tech.files += 1
            tech.add_evidence(inv.rel(path))
        for eco, exts in ECOSYSTEM_EXTENSIONS.items():
            if ext in exts:
                sources[eco].append(path)
        if len(rel_parts) >= 3 and rel_parts[-3:-1] == (".github", "workflows") and ext in {".yml", ".yaml"}:
            parser = parse_workflow
        else:
            parser = next((p for match, p in MANIFESTS if match(name)), None)
        if parser:
            text = read_text(path, max_bytes)
            if text is None:
                inv.warnings.append(f"{inv.rel(path)}: skipped (unreadable or larger than {max_bytes} bytes)")
            else:
                parser(inv, path, text)
    scan_imports(inv, sources, max_bytes, track_undeclared)
    return inv


def to_rows(inv: Inventory, min_refs: int) -> list[dict]:
    rows = []
    for tech in inv.items.values():
        if tech.references < min_refs:
            continue
        breakdown = {"declarations": tech.declarations, "imports": tech.imports, "files": tech.files}
        rows.append({
            "name": tech.name,
            "category": tech.category,
            "ecosystem": tech.ecosystem,
            "version": ", ".join(sorted(tech.versions)) or "unspecified",
            "references": tech.references,
            "breakdown": {k: v for k, v in breakdown.items() if v},
            "evidence": tech.evidence,
        })
    rows.sort(key=lambda r: (-r["references"], r["category"], r["name"].lower()))
    return rows


def render(rows: list[dict], inv: Inventory, fmt: str) -> str:
    undeclared = {eco: dict(sorted(v.items(), key=lambda kv: (-kv[1], kv[0])))
                  for eco, v in inv.unmatched_imports.items()}
    if fmt == "json":
        return json.dumps({"root": str(inv.root), "technologies": rows, "undeclaredImports": undeclared,
                           "warnings": inv.warnings}, indent=2) + "\n"
    if fmt == "csv":
        buf = io.StringIO()
        writer = csv.writer(buf, lineterminator="\n")
        writer.writerow(["name", "category", "ecosystem", "version", "references", "breakdown"])
        for r in rows:
            writer.writerow([r["name"], r["category"], r["ecosystem"], r["version"], r["references"],
                             "; ".join(f"{k}={v}" for k, v in r["breakdown"].items())])
        return buf.getvalue()

    def esc(value: object) -> str:
        return str(value).replace("|", "\\|")

    lines = [f"# Technology inventory: {inv.root}", "",
             "| Name | Category | Version | References | Breakdown |",
             "| --- | --- | --- | ---: | --- |"]
    for r in rows:
        breakdown = ", ".join(f"{k} {v}" for k, v in r["breakdown"].items())
        lines.append(f"| {esc(r['name'])} | {r['category']} | {esc(r['version'])} | {r['references']} | {breakdown} |")
    if undeclared:
        lines += ["", "## Undeclared imports", ""]
        for eco, counts in undeclared.items():
            lines.append(f"- {eco}: " + ", ".join(f"{k} ({v})" for k, v in list(counts.items())[:25]))
    if inv.warnings:
        lines += ["", "## Warnings", ""] + [f"- {w}" for w in inv.warnings]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Inventory technologies used in a folder tree.")
    ap.add_argument("root", nargs="?", default=".", help="Folder tree to scan (default: current folder)")
    ap.add_argument("--format", choices=["markdown", "json", "csv"], default="markdown")
    ap.add_argument("--output", help="Write the report to this file instead of stdout")
    ap.add_argument("--exclude", action="append", default=[], help="Glob of relative paths to skip (repeatable)")
    ap.add_argument("--include-dir", action="append", default=[],
                    help="Scan a normally skipped folder name, e.g. vendor (repeatable)")
    ap.add_argument("--min-references", type=int, default=1)
    ap.add_argument("--max-file-bytes", type=int, default=2_000_000)
    ap.add_argument("--undeclared", action="store_true",
                    help="Also report third-party imports not declared in any manifest")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2
    inv = build_inventory(root, DEFAULT_SKIP_DIRS - set(args.include_dir), args.exclude,
                          args.max_file_bytes, args.undeclared)
    report = render(to_rows(inv, args.min_references), inv, args.format)
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
