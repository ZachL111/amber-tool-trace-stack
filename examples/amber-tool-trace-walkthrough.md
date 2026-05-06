# Amber Tool Trace Stack Walkthrough

I use this file as a small checklist before changing the Python implementation.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | file span | 84 | hold |
| stress | terminal width | 239 | ship |
| edge | argument risk | 176 | ship |
| recovery | report density | 209 | ship |
| stale | file span | 244 | ship |

Start with `stale` and `baseline`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

`stale` is the optimistic case; use it to make sure the scoring path still rewards strong signal.
