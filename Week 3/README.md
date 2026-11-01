# Lab 3 — Uninformed Search

Uses the exact original A–G graph from the supplied lab manual.

## Files
- `lab3_search.py`: BFS and DFS
- `lab3_depth_search.py`: DLS and IDDFS
- `lab3_ucs.py`: UCS on the weighted extension
- `edge_case_tests.py`: start=goal, unreachable goal and cycle tests
- `data/graph.txt`: original graph
- `outputs/`: captured outputs and manual frontier traces
- `Lab3_Report.docx`: required Word report (also see `Lab3_Report.md`)

## Run (Python 3)
```bash
python lab3_search.py
python lab3_depth_search.py
python lab3_ucs.py
python edge_case_tests.py
```

## Weighted extension assumptions
Retain every original corridor and add C→G as required by Section 3.7. The manual says A→C→G costs 12 and A→B→E→G costs 3. The explicit edge weights used are A-B=1, A-C=6, B-D=2, B-E=1, C-F=2, E-G=1, C-G=6. All costs are nonnegative.
