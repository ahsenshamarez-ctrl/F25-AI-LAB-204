# Week 3 — Graph Search (A–H)

**Important:** The original class diagram and starter code were not supplied. This package uses a simple example graph with A–H and makes that assumption explicit. If your teacher's graph has different edges or successor order, update the adjacency lists and report before submitting.

Successor order: A→B,C; B→D; C→F,G; D→E; E→H; F→H; G→H; H has no successors. Start A, goal H, root depth 0. BFS/DFS stop when H is processed.

## Files
- `lab3_search.py`: BFS and DFS
- `lab3_depth_search.py`: DLS and IDDFS with FOUND/CUTOFF/FAILURE
- `lab3_ucs.py`: UCS
- `data/graph.txt`: adjacency list
- `outputs/`: captured outputs
- `Lab3_Report.docx`: report (downloadable package; binary report is not uploaded by this text-file connector)

## Run
Requires Python 3.10+; scripts use only the standard library:
```bash
python lab3_search.py
python lab3_depth_search.py
python lab3_ucs.py
```

## UCS weights
A→B=1, A→C=1, B→D=1, D→E=1, E→H=1, C→F=2, C→G=2, F→H=2, G→H=2. UCS chooses A→B→D→E→H at cost 4. The BFS route A→C→F→H costs 5 despite using fewer edges.
