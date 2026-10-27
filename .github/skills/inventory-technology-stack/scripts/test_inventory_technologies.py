import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import inventory_technologies as it  # noqa: E402

FIXTURE = {
    "web/package.json": json.dumps({
        "dependencies": {"react": "^18.2.0", "@azure/msal-browser": "^3.0.0"},
        "devDependencies": {"typescript": "~5.4.0"},
        "engines": {"node": ">=20"},
    }),
    "web/package-lock.json": json.dumps({
        "lockfileVersion": 3,
        "packages": {"": {}, "node_modules/react": {"version": "18.3.1"},
                     "node_modules/foo/node_modules/react": {"version": "17.0.0"}},
    }),
    "web/src/App.tsx": (
        "import React from 'react';\n"
        "import { PublicClientApplication } from '@azure/msal-browser/dist/x';\n"
        "import fs from 'fs';\nimport local from './local';\n"
    ),
    "web/src/index.ts": "const r = require('react');\nimport('lodash');\n",
    "web/node_modules/react/index.js": "import x from 'react';\n",
    "api/requirements.txt": "fastapi==0.110.0\nPyYAML>=6.0  # yaml\n-r other.txt\n",
    "api/pyproject.toml": '[project]\nrequires-python = ">=3.11"\ndependencies = ["httpx>=0.27"]\n',
    "api/main.py": (
        "import os, yaml\nfrom fastapi import FastAPI\nimport httpx as h\n"
        "from helpers import util\nimport requests\n"
    ),
    "api/helpers.py": "VALUE = 1\n",
    "svc/Svc.csproj": (
        '<Project Sdk="Microsoft.NET.Sdk.Web"><PropertyGroup>'
        "<TargetFramework>net8.0</TargetFramework></PropertyGroup><ItemGroup>"
        '<PackageReference Include="Newtonsoft.Json" Version="13.0.3" />'
        "</ItemGroup></Project>"
    ),
    "svc/Program.cs": "using System;\nusing Newtonsoft.Json.Linq;\nusing Newtonsoft.Json;\n",
    "go/go.mod": "module example.com/app\n\ngo 1.22\n\nrequire (\n\tgithub.com/gin-gonic/gin v1.9.1\n)\n",
    "go/main.go": 'package main\n\nimport (\n\t"fmt"\n\t"github.com/gin-gonic/gin"\n)\n\nvar s = "github.com/gin-gonic/gin"\n',
    "Dockerfile": "FROM node:20-alpine AS build\nFROM build\nFROM nginx\n",
    ".github/workflows/ci.yml": "jobs:\n  b:\n    steps:\n      - uses: actions/checkout@v4\n      - uses: ./local\n",
}


class InventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        for rel, content in FIXTURE.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        cls.inv = it.build_inventory(root, it.DEFAULT_SKIP_DIRS, [], 2_000_000, track_undeclared=True)
        cls.rows = {(r["name"], r["category"]): r for r in it.to_rows(cls.inv, 1)}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def row(self, name, category="library"):
        return self.rows[(name, category)]

    def test_npm_uses_lock_version_and_counts_imports(self):
        react = self.row("react")
        self.assertEqual(react["version"], "18.3.1")
        self.assertEqual(react["breakdown"], {"declarations": 1, "imports": 2})
        self.assertEqual(react["references"], 3)
        self.assertEqual(self.row("@azure/msal-browser")["breakdown"]["imports"], 1)
        self.assertEqual(self.row("typescript")["references"], 1)

    def test_skip_dirs_are_not_scanned(self):
        self.assertFalse(any("node_modules" in e for r in self.rows.values() for e in r["evidence"]))

    def test_python_aliases_and_versions(self):
        self.assertEqual(self.row("PyYAML")["version"], ">=6.0")
        self.assertEqual(self.row("PyYAML")["breakdown"]["imports"], 1)
        self.assertEqual(self.row("fastapi")["version"], "==0.110.0")
        self.assertEqual(self.row("httpx")["breakdown"]["imports"], 1)
        python = self.row("Python", "language")
        self.assertEqual(python["version"], ">=3.11")
        self.assertEqual(python["breakdown"], {"declarations": 1, "files": 2})

    def test_dotnet(self):
        self.assertEqual(self.row("Newtonsoft.Json")["references"], 3)
        self.assertEqual(self.row(".NET", "runtime")["version"], "net8.0")
        self.assertEqual(self.row("Microsoft.NET.Sdk.Web", "framework")["references"], 1)

    def test_go_counts_import_block_only(self):
        gin = self.row("github.com/gin-gonic/gin")
        self.assertEqual(gin["version"], "v1.9.1")
        self.assertEqual(gin["breakdown"], {"declarations": 1, "imports": 1})
        self.assertEqual(self.row("Go", "language")["version"], "1.22")

    def test_containers_and_actions(self):
        self.assertEqual(self.row("node", "container-image")["version"], "20-alpine")
        self.assertEqual(self.row("nginx", "container-image")["version"], "latest")
        self.assertNotIn(("build", "container-image"), self.rows)
        self.assertEqual(self.row("actions/checkout", "ci-action")["version"], "v4")
        self.assertEqual(self.row("Node.js", "runtime")["version"], ">=20")

    def test_undeclared_imports_exclude_stdlib_builtins_and_local(self):
        self.assertEqual(self.inv.unmatched_imports["pypi"], {"requests": 1})
        self.assertEqual(self.inv.unmatched_imports["npm"], {"lodash": 1})

    def test_render_formats(self):
        rows = it.to_rows(self.inv, 1)
        data = json.loads(it.render(rows, self.inv, "json"))
        self.assertEqual(len(data["technologies"]), len(rows))
        self.assertIn("| react | library | 18.3.1 | 3 |", it.render(rows, self.inv, "markdown"))
        self.assertTrue(it.render(rows, self.inv, "csv").startswith("name,category,ecosystem,version"))


if __name__ == "__main__":
    unittest.main()
