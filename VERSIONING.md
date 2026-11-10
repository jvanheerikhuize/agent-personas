# Versioning

This library follows [Semantic Versioning](https://semver.org/).

## Version source

`module.version` in `catalog.yaml` is the source of truth; the build copies it into
the generated `index.yaml`. Every release is tagged with a matching `v`-prefixed tag
(for example `v0.1.0`).

**Current status:** `0.1.0`, the extraction from Agent-Roles. The personas are
unchanged from Agent-Roles `v2.0.0-alpha.3`. While the version is `0.x`, the layout
and the persona format may still change between minor versions, as planned in
[docs/PLAN.md](docs/PLAN.md). `v1.0.0` is released at the end of that plan.

Each persona also carries its own `version` in its frontmatter, bumped when its
behaviour changes.

## What constitutes each level (from 1.0.0 on)

| Level | When to bump | Examples |
|---|---|---|
| **PATCH** | Wording fixes, metadata corrections | Fix a crisis line number, rephrase a section |
| **MINOR** | New personas, new optional fields, non-breaking changes | Add a persona, add a parameter with a default |
| **MAJOR** | Breaking manifest or layout changes, removing personas | Rename a manifest field, move `dist/` |

## Immutability

Once a tag is pushed, its content never changes. A fix gets a new version and tag.

## Pinning

Consume the built artifacts (`index.yaml`, `dist/prompts/`), never the `role.md`
sources, and pin a tag:

```bash
git submodule add https://github.com/jvanheerikhuize/agent-personas.git lib/personas
cd lib/personas && git checkout v0.1.0
```
