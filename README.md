<div align="center">

# Agent Personas

**Conversational AI personas you paste into any chat or system prompt.**
Safe by construction, LLM-agnostic, one file per persona.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Personas](https://img.shields.io/badge/roles-8-brightgreen.svg)](index.yaml)

</div>

---

## What is a persona?

A persona tells a general-purpose AI *who to be for a whole conversation*: what it
knows, how it speaks, where its limits are, and when it hands off to a human. Paste
one into a fresh chat and the model becomes that companion. No fine-tuning, no
plugins, no API key.

Personas are the part of AI behaviour that no standard covers yet. Procedures have
Agent Skills and policies have `AGENTS.md`, but "be this companion for the whole
conversation" is still a system prompt. That is why this repo exists separately from
[Agent-Roles](https://github.com/jvanheerikhuize/Agent-Roles), which keeps the
task-shaped roles (code review, QA, utilities, games).

> **Health and education personas are not a substitute for professional care.**
> Before deploying any persona in a product, verify the crisis resources for your
> region (see [`config/`](config/README.md)) and read the safety notes in its README.

## Personas

### 🩺 Health

| Persona | What it does |
|---|---|
| [**P.S.Y.**](dist/prompts/psy.md) | Trauma-informed companion for grounding, psychoeducation and crisis referral (phase 1 support only). |
| [**F.R.A.N.K.**](dist/prompts/frank.md) | Relationship coach grounded in attachment theory, EFT and Gottman research, with dry wit and no sugarcoating. |
| [**V.I.T.A.**](dist/prompts/vita.md) | Lifestyle coach for food, movement and mental health, using Motivational Interviewing and CBT. |
| [**P.A.P.A.**](dist/prompts/papa.md) | Co-parenting companion for divorced dads with a teenage son: the words to say, and what is going on for both of you. |

### 📚 Education

| Persona | What it does |
|---|---|
| [**A.G.O.R.A.**](dist/prompts/agora.md) | Socratic philosophy companion for curious minds of all ages. |
| [**M.E.N.T.O.R.**](dist/prompts/mentor.md) | Socratic study coach for Dutch VWO students. Never gives away answers. |
| [**S.C.O.U.T.**](dist/prompts/scout.md) | Curriculum briefing for parents, the companion of M.E.N.T.O.R. Dutch output. |

### 🎨 Creative

| Persona | What it does |
|---|---|
| [**M.U.S.E.**](dist/prompts/muse.md) | An artist's companion that generates inspiration, pushes comfort zones and turns impulses into creation plans. |

## Using a persona

**Paste into a chat:** open a prompt in [`dist/prompts/`](dist/prompts/), copy the
code block into a fresh conversation in any capable model, and send.

**As a system prompt:**

```python
import anthropic, pathlib

system_prompt = pathlib.Path("dist/prompts/muse.md").read_text()
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=2048,
    system=system_prompt,
    messages=[{"role": "user", "content": "Hi"}],
)
```

Any API that accepts a system prompt works the same way.

**As a library:** `index.yaml` is the generated manifest of every persona with its
metadata and file paths. Pin a git tag for reproducible use (see
[VERSIONING.md](VERSIONING.md)).

## How the repo works

Each persona is authored once, in `roles/<category>/<slug>/role.md` (YAML
frontmatter + prompt body). The build compiles it:

```bash
python3 tools/build.py   # requires Python 3 + PyYAML
```

It writes `dist/prompts/<slug>.md` and `index.yaml`. Both are committed and CI fails if
they are stale. **Edit `role.md`, never `dist/` or `index.yaml`.**

## Where this is going

The personas came over from Agent-Roles unchanged. The redesign (safety kernel,
parameters instead of personal tailoring, short prose instructions, mandatory
behavioural evals) is planned in [docs/PLAN.md](docs/PLAN.md).

## Provenance

Extracted from [Agent-Roles](https://github.com/jvanheerikhuize/Agent-Roles) at tag
`v2.0.0-alpha.3`, with full git history for every persona.

## License

[MIT](LICENSE). The health and education personas are educational and supportive
tools. Whoever deploys them is responsible for regional crisis resources, data
protection and fitness for their audience.
