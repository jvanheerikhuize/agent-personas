# Contributing

Thanks for helping.

- **Problem with a persona:** open an issue with the persona, the model and the
  conversation. If it could put a user at risk, report it privately instead
  (see [SECURITY.md](SECURITY.md)).
- **Changing a persona:** add an eval case in `evals/cases/<name>.yaml` that shows
  the problem, edit `personas/<name>.md`, and run the evals before and after.
  Safety cases must all pass; put both summaries in the PR.
- **New persona:** open an issue first. Add `personas/<name>.md`,
  `evals/cases/<name>.yaml` (with safety cases if it touches health or children)
  and a row in the README table.

Be respectful and constructive.
