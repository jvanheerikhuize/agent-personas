# Redesign plan: agent-personas

> **Status:** phase 0 in progress. Decided 2026-11-10.
> **Scope:** the conversational personas extracted from Agent-Roles. The task-shaped
> roles that stayed in Agent-Roles (skills, tools, the review pipeline, games) are out
> of scope here and get their own plan later.

## 1. What this repo is for

Personas you paste into any chat or system prompt, **safe by construction**. Paste-in
stays the primary delivery, because "who to be for a whole conversation" has no
standard beyond the system prompt. This is also the repo with the heaviest
responsibility, so safety and evals are part of the structure, not added later.

## 2. Scope

| Persona | Category | Risk / data class | Notes |
|---|---|---|---|
| P.S.Y. | health | medium · restricted · GDPR special | Trauma support, phase 1 only |
| V.I.T.A. | health | medium · restricted · GDPR special | Uses personal context (§5) |
| P.A.P.A. | health | medium · confidential · GDPR special | Uses personal context (§5) |
| F.R.A.N.K. | health | medium · confidential · conditional | Uses personal context (§5); largest prompt at 5,945 words |
| A.G.O.R.A. | education | medium · internal | May be used by minors |
| M.E.N.T.O.R. | education | low · internal | Dutch VWO |
| S.C.O.U.T. | education | low · public | Companion of M.E.N.T.O.R., moved with it |
| M.U.S.E. | creative | low · public | Lowest risk: the format pilot |

## 3. Decisions

| # | Decision | Choice |
|---|---|---|
| 1 | Repo name | `agent-personas` |
| 2 | S.C.O.U.T. moves with M.E.N.T.O.R. | Yes, so the companion pair is not split across repos |
| 3 | Where personal context lives | In the `jeroen-alexander` corpus, read through its `FORMAT.md` (§5). Never in this repo |
| 4 | License | MIT, plus a notice that health and education personas are not professional care and the deployer is responsible |
| 5 | Pre-extraction tag in Agent-Roles | `v2.0.0-alpha.3` (matches its `catalog.yaml`; Agent-Roles' VERSIONING reserves `v2.0.0` for a stable rebuild). The removal is a pre-release change there, not a v3 |
| 6 | Visibility | Private until the owner decides to publish |

## 4. Design principles

### a. Safety kernel, injected and fail-closed

- One shared `kernel/safety/` holds crisis detection, escalation wording, scope limits,
  and the handoff to a human.
- Crisis numbers come out of the prompt bodies and are injected per region from
  `config/` as `{{safety}}`. This also clears the four existing `test-roles.sh`
  warnings (psy, frank, vita, agora).
- **Metadata becomes enforced.** A persona with `risk_tier: medium` or higher cannot
  be built without the kernel. `gdpr_special_category: true` requires the privacy
  notice block.

### b. Parameters instead of personal tailoring

`locale`, `language`, `audience: adult|youth`, `curriculum` and `custody_rhythm`
become parameters with defaults:

- P.A.P.A. becomes a general co-parenting companion. Your arrangement comes from
  personal context (§5).
- M.E.N.T.O.R. and S.C.O.U.T. get `curriculum: nl-vwo` as their first curriculum.
- A.G.O.R.A. gets a youth mode with stricter safety.

### c. Prose, not pseudo-XML

The instructions run from a few hundred to about 1,200 words and explain the reasons
behind each rule. Reference frameworks (SAMHSA, Gottman, MI/CBT, curricula) move to
`references/`. No session IDs or JSON state echoed into the chat. Every persona states
its red lines and when it hands off to a human.

### Target layout

```
roles/<category>/<id>/
  role.md             # frontmatter + instructions (moves to persona.yaml + instructions.md later)
  voice.md            # optional persona layer: name, tone, wit
  references/         # frameworks, curricula — included at build time
  evals/              # scenarios + assertions — required
kernel/safety/        # shared, injected
config/regions/       # crisis resources per region
tools/build.py        # → dist/prompts/<id>.md (public) and .local/ (personal, §5)
```

## 5. Personal context: integration with the `jeroen-alexander` corpus

V.I.T.A., F.R.A.N.K. and P.A.P.A. are most useful when they know the user's real
situation. That knowledge already lives in the `jeroen-alexander` corpus, which holds
knowledge and nothing else. Its `FORMAT.md` (format version 1) is the only contract.

**Direction of dependency.** This repo may read the corpus. The corpus never depends
on this repo, and nothing here writes to it. If the corpus `FORMAT.md` version is not
one this repo knows, the personal build stops.

**How it works:**

1. **The persona declares generic slots.** Each persona's frontmatter names the
   *kinds* of context it can use, without naming anyone. For example, P.A.P.A.:
   `context: [user, children, co_parent, custody_arrangement]`; V.I.T.A.:
   `context: [user, health, routines]`; F.R.A.N.K.: `context: [user, partner,
   relationship_history]`.
2. **A local map fills the slots.** An untracked file outside the repo (for example
   `~/.config/agent-personas/context.yaml`) maps slots to corpus subject ids. Subject
   ids are personal data themselves, so the map is never committed.
3. **Only current claims are selected.** The build takes claims where `valid_to` is
   empty and `superseded_by` is not set. It keeps `confidence`, and leaves out
   `inferred` claims unless the owner opts in.
4. **Personal output stays local.** `tools/build.py --context <corpus> --map <map>`
   writes to `.local/dist/` (gitignored). The public `dist/` never contains personal
   data, and CI never sees the corpus.
5. **Least privilege.** A persona sees only the slots it declares. P.A.P.A. gets no
   health claims and V.I.T.A. gets no co-parenting claims.

**Guards:** `.local/` is in `.gitignore`. A check fails the build if any public
artifact contains text that also appears in the local map. The privacy notice for
GDPR special-category personas says that personal context was loaded.

## 6. Evals: the rule that blocks a release

Every persona ships scenarios in four groups:

- **Red lines:** crisis disclosure, self-harm, abuse, requests for diagnosis or medication.
- **Audience:** a minor in an adult persona, a youth persona under pressure.
- **Robustness:** jailbreaks, "forget your role", attempts to extract personal context.
- **Quality:** the persona does what it promises (Socratic questions, MI technique,
  one micro-habit per session).

Some checks run without any model: kernel present, region filled in, no hardcoded
numbers, no personal data in `dist/`. Behavioural checks run against several vendors
**and a local model**.

**Rule:** no `stable` status without passing red-line evals on at least two model
families.

## 7. Phases

| Phase | Work | Done when |
|---|---|---|
| **0** | Tag Agent-Roles, create this repo with history, adapt catalog and docs, remove the personas from Agent-Roles with redirect stubs | Prompts byte-identical to Agent-Roles `v2.0.0-alpha.3`; CI green in both repos |
| 1 | Safety kernel + region templating | No crisis numbers in prompt bodies; build fails without the kernel |
| 2 | Eval runner + **baseline of the current prompts** | Score per persona recorded |
| 3 | Pilot the new format with **M.U.S.E.**; write the style guide | Equal or better than baseline |
| 4 | Education: M.E.N.T.O.R. + S.C.O.U.T., then A.G.O.R.A. (youth mode) | Evals green |
| 5 | Personal-context build (§5), then health one at a time: V.I.T.A. → F.R.A.N.K. → P.A.P.A. → **P.S.Y. last** | Red-line evals green on 2+ model families; no personal data in public artifacts |
| 6 | Release `v1.0.0`; decide on public visibility; update the website link | Released |
