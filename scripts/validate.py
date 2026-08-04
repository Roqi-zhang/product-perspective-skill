#!/usr/bin/env python3
"""Validate portable Skill metadata and publication safety without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "agents/openai.yaml",
    "adapters/generic-prompt.md",
    "tests/cases.md",
]
FORBIDDEN = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[^\s<][^\s]*"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


for relative_path in REQUIRED:
    if not (ROOT / relative_path).is_file():
        fail(f"missing required file: {relative_path}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
match = re.match(r"\A---\n(?P<header>.*?)\n---\n", skill, re.DOTALL)
if not match:
    fail("SKILL.md must begin with YAML frontmatter")

header_lines = [line for line in match.group("header").splitlines() if line.strip()]
if len(header_lines) != 2 or not header_lines[0].startswith("name: product-perspective"):
    fail("SKILL.md frontmatter must contain only name: product-perspective and description")
if not header_lines[1].startswith("description:"):
    fail("SKILL.md frontmatter must contain a description")

metadata = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
if "allow_implicit_invocation: false" not in metadata:
    fail("Codex metadata must disable implicit invocation")
if "$product-perspective" not in metadata:
    fail("Codex metadata must include the explicit invocation prompt")

generic = (ROOT / "adapters/generic-prompt.md").read_text(encoding="utf-8").lower()
for phrase in ["recommend with conditions", "change only what the user explicitly requested", "explicit user approval"]:
    if phrase not in generic:
        fail(f"generic adapter is missing canonical behavior: {phrase}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    content = path.read_text(encoding="utf-8", errors="ignore")
    for pattern in FORBIDDEN:
        if pattern.search(content):
            fail(f"possible sensitive value found in {path.relative_to(ROOT)}")

print("Validation passed.")
