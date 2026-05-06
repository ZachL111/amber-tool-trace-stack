# amber-tool-trace-stack

`amber-tool-trace-stack` is a compact Python repository for cli tools, centered on this goal: Package a Python local lab for trace analysis with capacity fixtures, allocation and spill reports, and documented operating limits.

## Why I Keep It Small

The project exists to keep a narrow engineering decision visible and testable. For this repo, that decision is how file span and argument risk should influence a review result.

## Amber Tool Trace Stack Review Notes

Start with `file span` and `file span`. Those cases create the widest score spread in this repo, so they are the best quick check when the model changes.

## Included Behavior

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/amber-tool-trace-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `file span` and `file span`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Internal Model

The implementation keeps the scoring rule plain: reward signal and confidence, preserve slack, penalize drag, then classify the result into a review lane.

The Python code keeps the review rule close to the tests.

## Try It Locally

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Validation

The same command runs the local verification path. The highest-scoring domain case is `stale` at 244, which lands in `ship`. The most cautious case is `baseline` at 84, which lands in `hold`.

## Scope

No external service is required. A deeper version would add more negative cases and a clearer boundary around invalid input.
