# AGENTS.md — agent-personas

Conversational AI personas. Each persona is one paste-ready prompt:
`personas/<name>.md`. Edit it directly; there is no build step.

- Write personas as plain Markdown: an H1, a short role paragraph with the
  safety-first line, then sections such as How you talk, How a session goes,
  Boundaries, Safety and Example. No XML tags or state schemas; put verbatim
  wording in blockquotes.
- Never weaken a persona's crisis or safety section without saying so in the PR.
- Never commit personal data.
