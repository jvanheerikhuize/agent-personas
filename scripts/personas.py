#!/usr/bin/env python3
"""Check every persona file, or copy the shared safety text into them.

    python3 scripts/personas.py           # check; exit 1 on any problem
    python3 scripts/personas.py --sync    # rewrite the safety blocks from safety/

A persona is personas/<name>.md: YAML frontmatter with exactly `name`,
`description` and `safety`, then the prompt itself (paste-ready as-is).

`safety: core` personas carry safety/core.md, `core-minors` personas carry
safety/core.md + safety/minors.md, between BEGIN/END markers placed just before
</MASTER_PROMPT>. The copy in the persona must match safety/ exactly.
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIELDS = {"name", "description", "safety"}
SAFETY = {"none": [], "core": ["core.md"], "core-minors": ["core.md", "minors.md"]}
BEGIN = "<!-- BEGIN safety block: edit safety/*.md, then run scripts/personas.py --sync -->"
END = "<!-- END safety block -->"
# The block plus the blank line with_safety() puts after it, so removal undoes insertion.
BLOCK_RE = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n\n?", re.S)
ANCHOR = "</MASTER_PROMPT>"


def safety_block(level):
    parts = [(ROOT / "safety" / f).read_text(encoding="utf-8").strip() for f in SAFETY[level]]
    return BEGIN + "\n" + "\n\n".join(parts) + "\n" + END + "\n"


def with_safety(text, level):
    """Return the persona text with exactly the right safety block (or none)."""
    text = BLOCK_RE.sub("", text)
    if level == "none":
        return text
    if text.count(ANCHOR) != 1:
        raise ValueError(f"needs exactly one {ANCHOR} to place the safety block")
    return text.replace(ANCHOR, safety_block(level) + "\n" + ANCHOR)


def split(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text:
        raise ValueError("missing YAML frontmatter")
    head, body = text[4:].split("\n---\n", 1)
    return yaml.safe_load(head), body


def check(path, sync):
    meta, _ = split(path)
    errors = []
    if not isinstance(meta, dict) or set(meta) != FIELDS:
        return [f"frontmatter must have exactly {sorted(FIELDS)}"]
    if meta["name"] != path.stem:
        errors.append(f"name '{meta['name']}' != file name '{path.stem}'")
    if meta["safety"] not in SAFETY:
        return errors + [f"safety must be one of {sorted(SAFETY)}"]
    if not (ROOT / "evals" / "cases" / f"{path.stem}.yaml").is_file():
        errors.append(f"no eval cases at evals/cases/{path.stem}.yaml")
    text = path.read_text(encoding="utf-8")
    wanted = with_safety(text, meta["safety"])
    if wanted != text:
        if sync:
            path.write_text(wanted, encoding="utf-8")
            print(f"synced {path.relative_to(ROOT)}")
        else:
            errors.append("safety block missing or out of date (run with --sync)")
    return errors


def main():
    sync = "--sync" in sys.argv[1:]
    failed = False
    for path in sorted((ROOT / "personas").glob("*.md")):
        try:
            errors = check(path, sync)
        except ValueError as e:
            errors = [str(e)]
        for e in errors:
            print(f"FAIL {path.relative_to(ROOT)}: {e}", file=sys.stderr)
        failed |= bool(errors)
    print("FAILED" if failed else "OK")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
