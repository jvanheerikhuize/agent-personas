#!/usr/bin/env python3
"""Check every persona file. Exit 1 on any problem.

    python3 scripts/personas.py

A persona is personas/<name>.md: YAML frontmatter with exactly `name`,
`description` and `safety`, then the prompt itself (paste-ready as-is).
"""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIELDS = {"name", "description", "safety"}
SAFETY = {"none", "core", "core-minors"}


def split(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text:
        raise ValueError("missing YAML frontmatter")
    head, body = text[4:].split("\n---\n", 1)
    return yaml.safe_load(head), body


def check(path):
    meta, body = split(path)
    errors = []
    if not isinstance(meta, dict) or set(meta) != FIELDS:
        errors.append(f"frontmatter must have exactly {sorted(FIELDS)}")
        return errors
    if meta["name"] != path.stem:
        errors.append(f"name '{meta['name']}' != file name '{path.stem}'")
    if meta["safety"] not in SAFETY:
        errors.append(f"safety must be one of {sorted(SAFETY)}")
    if not (ROOT / "evals" / "cases" / f"{path.stem}.yaml").is_file():
        errors.append(f"no eval cases at evals/cases/{path.stem}.yaml")
    return errors


def main():
    failed = False
    for path in sorted((ROOT / "personas").glob("*.md")):
        try:
            errors = check(path)
        except ValueError as e:
            errors = [str(e)]
        for e in errors:
            print(f"FAIL {path.relative_to(ROOT)}: {e}", file=sys.stderr)
        failed |= bool(errors)
    print("FAILED" if failed else "OK")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
