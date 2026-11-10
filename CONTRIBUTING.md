# Contributing

Thanks for helping. Fixes to a persona's behaviour, new eval cases and new personas
are all welcome.

## Reporting a problem

Open an issue with the persona, the model you used, and the conversation (or the
smallest part of it that shows the problem). For anything that could put a user at
risk, use a private security advisory instead (see [SECURITY.md](SECURITY.md)).

## Changing a persona

1. Add or update an eval case in `evals/cases/<name>.yaml` that shows the problem.
2. Edit `personas/<name>.md`. If you change the shared safety text, edit
   `safety/*.md` and run `python3 scripts/personas.py --sync`.
3. Run `python3 scripts/personas.py` and the evals (before and after your change).
   Safety cases must all pass; put both summaries in the PR.

## Adding a persona

Open an issue first with the concept, audience and voice. A new persona needs:

- `personas/<name>.md` with `name`, `description` and `safety` frontmatter. Use
  `safety: core` for anything touching health or distress, and `core-minors` if
  children may use it.
- `evals/cases/<name>.yaml`, including safety cases if `safety` is not `none`.
- A row in the README table.

Prompts should be self-contained, work in at least two model families, and avoid
provider-specific features. Every section should change observable behaviour; if
removing it changes nothing in the evals, remove it.

## Code of conduct

Be respectful and constructive. Critique the work, not the person.
