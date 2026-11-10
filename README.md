<div align="center">

# Agent Personas

**Conversational AI personas you paste into any chat or system prompt.**
One file per persona, written to work in any capable model.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

</div>

---

A persona tells a general-purpose AI *who to be for a whole conversation*: what it
knows, how it speaks, where its limits are, and when it hands off to a human. Paste
one into a fresh chat and the model becomes that companion. No fine-tuning, no
plugins, no API key.

> **Health and education personas are not a substitute for professional care.**
> Before deploying one in a product, read [SECURITY.md](SECURITY.md).

## Personas

| Persona | Area | What it does |
|---|---|---|
| [P.S.Y.](personas/psy.md) | Health | Trauma-informed companion for grounding, psychoeducation and crisis referral (Phase 1 stabilisation only). |
| [F.R.A.N.K.](personas/frank.md) | Health | Relationship reflection grounded in attachment theory, EFT and Gottman research, with dry wit and no sugarcoating. |
| [V.I.T.A.](personas/vita.md) | Health | Lifestyle coach for food, movement and mental health, using Motivational Interviewing and CBT. |
| [P.A.P.A.](personas/papa.md) | Health | Co-parenting companion for separated dads with a teenage son: the words to say, and what is going on for both of you. |
| [A.G.O.R.A.](personas/agora.md) | Education | Socratic philosophy companion for curious minds of all ages. |
| [M.E.N.T.O.R.](personas/mentor.md) | Education | Socratic study coach for Dutch VWO klas 3 maths and sciences. Never gives away answers. Dutch. |
| [S.C.O.U.T.](personas/scout.md) | Education | Curriculum briefing for parents of VWO students, the companion of M.E.N.T.O.R. Dutch. |
| [M.U.S.E.](personas/muse.md) | Creative | An artist's companion that generates inspiration, pushes comfort zones and turns impulses into creation plans. |

## Using a persona

**In a chat:** open the persona file, copy the raw file, paste it into a fresh
conversation (or into a Project / GPT / Gem's instructions) and send.

**As a system prompt:**

```python
import anthropic, pathlib

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=2048,
    system=pathlib.Path("personas/muse.md").read_text(),
    messages=[{"role": "user", "content": "Hi"}],
)
```

Any API that accepts a system prompt works the same way. Pin a git tag if you need
the text to stay fixed.

**Your own context:** some personas work better with personal details (a child's
age, a handover day). Add them in your own copy or after the persona in the
conversation. Never commit them here; `.local/` is git-ignored for that.

## Working on the repo

Edit `personas/<name>.md`, then:

```bash
python3 scripts/personas.py      # file and safety-block checks (requires PyYAML)
```

and run the evals for the persona you changed (see [evals/README.md](evals/README.md)).

## License

[MIT](LICENSE). Whoever deploys a persona is responsible for regional crisis
resources, data protection and fitness for their audience.
