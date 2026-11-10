# Evals

Each persona has scripted conversations in `cases/<persona>.yaml`. The model under
test answers the last user turn; a grader model checks the reply against a rubric.

- `tier: safety` — must pass on every provider before a persona change merges.
- `tier: quality` — voice, domain and method. Compare against the previous run;
  a change may not make these worse without a stated reason.

```bash
export ANTHROPIC_API_KEY=... OPENAI_API_KEY=...
npx promptfoo@0.124.1 eval -c evals/promptfooconfig.yaml --filter-metadata tier=safety
npx promptfoo@0.124.1 eval -c evals/promptfooconfig.yaml    # full run
npx promptfoo@0.124.1 view                                  # read the transcripts
```

Read the transcripts, not only the scores. The grader is a model; it can reward a
blander reply that has lost the persona's voice.

When you change a persona: run the full suite before and after, and put both
summaries in the PR. When you find a failure in real use, add a case for it first.
