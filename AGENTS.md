# AGENTS.md — agent-personas

A library of conversational AI personas (system prompts). Any agent or framework can
read this file to work in the repo or consume it.

## For agents working IN this repo

- `index.yaml` and `dist/prompts/` are **generated**. Never edit them by hand.
- Each persona's single source is `roles/{category}/{slug}/role.md`: YAML frontmatter
  (metadata, governance, relations) followed by the prompt body. The frontmatter
  contract is `schemas/role.schema.json`.
- Module metadata and workflows live in `catalog.yaml` (hand-edited).
- After changing any `role.md` or `catalog.yaml`, run `python3 tools/build.py`
  (requires PyYAML) and commit the regenerated artifacts with the source. CI fails if
  they are stale.
- Validate with `scripts/validate-index.sh` and `scripts/test-roles.sh`.
- Never commit personal data. Personal context for a persona is supplied from
  outside the repo at use time.

## For agents CONSUMING this repo

1. Read `index.yaml`.
2. Find the persona by `id`, `category` or `tags`.
3. Read the file at `files.prompt` (relative to the repo root). It points into
   `dist/prompts/`.
4. `files.source` points to `role.md`. Use it only for the raw frontmatter.

Pin a git tag for reproducible use. See `VERSIONING.md`.

### Relations

Personas can declare relationships in `relations`: `companions` (peers, for example
`mentor` ↔ `scout`) and `group` (for example `health-crisis-safety`). Workflows in
`index.yaml` list ordered `steps` or unordered `members`.
