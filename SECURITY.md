# Security and safety

This repository is a set of plain-text prompts. The main risk is what a persona
says to a vulnerable person. A prompt can lower that risk; it cannot guarantee
safety on its own.

## Reporting a problem

If a persona can be led to give harmful content, mishandles a crisis, or
misinforms someone in a way that could hurt them, **do not open a public issue**.
Report it privately through [GitHub Security Advisories](../../security/advisories/new).
Include the persona, the model, the conversation, and what should have happened.
You can expect an acknowledgement within 5 business days.

## What the personas do

P.S.Y., F.R.A.N.K., V.I.T.A., P.A.P.A. and A.G.O.R.A. each contain their own
crisis protocol and crisis-resource list; M.E.N.T.O.R. responds to disclosures by
students with a child helpline and other non-parent contacts. Each of these
promises is tested by a `tier: safety` case in [`evals/`](evals/).

## What the deployer must do

If you put a persona in front of other people, you are the operator, and these
are yours:

- **Crisis resources.** Check the numbers in each persona's crisis section for your users'
  region before going live, and re-check them yearly. Numbers change.
- **Platform safeguards.** Add your own moderation and escalation. Do not rely on
  the prompt alone, especially for users in distress.
- **Law.** For example: EU AI Act Art. 50 (users must know they are talking to an
  AI, applicable since 2 August 2026); GDPR, including Art. 9 for health data and a
  DPIA (Art. 35) for large-scale processing; companion-chatbot laws such as
  California SB 243 (operator duties for suicide/self-harm protocols, effective
  1 January 2026). The personas disclose that they are AI and give a privacy note,
  but compliance belongs to the deployment, not the text.
- **Audience.** Decide whether the persona fits your users. In particular:
  - **P.S.Y.**: vulnerable users. Phase 1 stabilisation only; not clinical care.
  - **F.R.A.N.K.**: may surface domestic violence. One person's perspective only;
    not couples therapy or legal advice.
  - **V.I.T.A.**: collects health data in every session; not medical, dietary or
    eating-disorder care.
  - **P.A.P.A.**: processes data about a minor; not family therapy or legal advice.
  - **A.G.O.R.A.**, **M.E.N.T.O.R.**: may be used by children. Review against your
    safeguarding policy and show a visible disclaimer.
