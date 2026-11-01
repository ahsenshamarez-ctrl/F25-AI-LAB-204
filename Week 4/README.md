# Week 4 — Informed Search: Heuristics & A*

**Course:** CAI601400 — Artificial Intelligence Lab  
**Lab:** 4 — Informed Search: Heuristics & A*  
**Student details on manual:** Rasikh Ali — 42365

## Files
- lab4_astar_audit.py — A* implementation, heuristic audit, frontier trace, UCS control, and overestimate experiment.
- edge_case_tests.py — start-equals-goal and unreachable-goal tests.
- data/campus_graph.json — weighted graph, supplied heuristic, and true remaining costs.
- outputs/ — captured traces and comparisons.
- Lab4_Report.md — full report.

## Requirements
Python 3.8 or newer. No third-party packages are required.

## Run
From this folder:
```bash
python lab4_astar_audit.py
python edge_case_tests.py
```

## Priority and counting rules
The heap tuple is (f, g, node, path): lower f is primary, then lower g, then node label. A node is expanded only when its successors are examined. The goal is included in the processed/popped trace but excluded from the expansion count. Stale queue entries are ignored and are not counted.

## Assumptions
All edge costs are nonnegative. Heuristic values use the same abstract travel-time units as edge costs. These are supplied teaching values, not measured campus distances.
