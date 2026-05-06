# amber-tool-trace-stack

`amber-tool-trace-stack` is a focused Python codebase around package a Python local lab for trace analysis with capacity fixtures, allocation and spill reports, and documented operating limits. It is meant to be easy to inspect, run, and extend without a hosted service.

## Amber Tool Trace Stack Walkthrough

I would read the project from the outside in: command, fixture, model, then roadmap. That keeps the cli tools idea grounded in files that can be checked locally.

## Reason For The Project

The goal is to capture the core behavior in code and make the surrounding assumptions obvious. A reader should be able to run the verifier, open the fixtures, and understand why each decision was made.

## How It Is Put Together

The core is a scoring model over demand, capacity, latency, risk, and weight. That keeps terminal output, argument shape, and file input in one explicit decision path. The threshold is 159, with risk penalty 5, latency penalty 2, and weight bonus 3. The Python code favors standard library tools and direct tests over framework weight.

## Data Notes

`examples/extended_cases.csv` adds six named cases. I kept the names plain so failures are easy to read in a terminal: baseline, pressure, surge, degraded, recovery, and boundary.

## Capabilities

- Uses fixture data to keep argument shape changes visible in code review.
- Includes extended examples for file input, including `surge` and `degraded`.
- Documents repeatable reports tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.
- Stores project constants and verification metadata in `metadata/project.json`.

## Getting It Running

Clone the repository, enter the directory, and run the verifier. No database server, cloud account, or token is required.

## Check The Work

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Where Things Live

- `src`: primary implementation
- `tests`: verification harness
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands
- `pyproject.toml`: Python project metadata

## Tradeoffs

The examples cover useful edges, not every edge. A larger version would add malformed-input tests, richer reports, and deeper domain parsers.

## Possible Extensions

- Split the scoring constants into a typed configuration object and validate it before use.
- Add a comparison mode that shows how decisions change when one signal is adjusted.
- Add a loader for `examples/extended_cases.csv` and promote selected cases into the language test suite.
- Add one more cli tools fixture that focuses on a malformed or borderline input.

## Command Examples

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.
