# AGENTS.md — agent-personas

Conversational AI personas. Each persona is one paste-ready file:
`personas/<name>.md` (frontmatter `name`, `description`, `safety`, then the prompt).

- Edit the persona file directly; there is no build step.
- Never edit text between `<!-- safety:... -->` markers by hand. Edit `safety/*.md`
  and run `python3 scripts/personas.py --sync`.
- Run `python3 scripts/personas.py` before committing.
- Any behaviour change to a persona needs its evals run before and after
  (`evals/README.md`). Safety cases must all pass.
- Never commit personal data. Personal context belongs in `.local/` (git-ignored).
