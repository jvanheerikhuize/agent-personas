# Purpose

**Problem:** "Who to be for a whole conversation" has no standard home. Skills cover
procedures and `AGENTS.md` covers policy, but a companion persona is still a system
prompt, and the ones that touch health, relationships or minors carry real risk
when they are written as ad-hoc prompts.

**Audience:** People who paste a persona into a chat, and developers who load one as
a system prompt in any model.

**Key constraints:**
- Paste-in is first-class: one self-contained prompt per persona, no tools required.
- LLM-agnostic, and proven so by evals across model families, not just claimed.
- Safety is structural: personas at medium risk or above cannot be built without the
  shared safety kernel.
- No personal data in this repo. Personal context comes from outside the repo and is
  never committed here.

**Success metric:** Anyone can take a persona, paste it in, and get consistent,
safe behaviour, and every safety promise a persona makes is covered by a passing
eval.
