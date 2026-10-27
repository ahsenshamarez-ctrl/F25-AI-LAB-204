# Lab 3 Report: Graph Search

## 1. Aim
Implement and compare BFS, DFS, depth-limited search (DLS), iterative deepening DFS (IDDFS), and uniform-cost search (UCS).

## 2. Assumptions and graph
The prompt said the graph has nodes A through H, but the original diagram and starter code were not available. This report therefore uses a clearly stated example graph. Replace it with the instructor's exact graph and successor order if they differ.

Directed adjacency list, successor order:
- A: B, C
- B: D
- C: F, G
- D: E
- E: H
- F: H
- G: H
- H: no successors

Start=A, goal=H, root depth=0. The goal is counted as visited when removed from the frontier and processed.

## 3. BFS trace
Queue front is on the left.

| Step | Queue before | Processed | Queue after expansion |
|---|---|---|---|
| 1 | [A] | A | [B, C] |
| 2 | [B, C] | B | [C, D] |
| 3 | [C, D] | C | [D, F, G] |
| 4 | [D, F, G] | D | [F, G, E] |
| 5 | [F, G, E] | F | [G, E, H] |
| 6 | [G, E, H] | G | [E, H] |
| 7 | [E, H] | E | [H] |
| 8 | [H] | H | [] — stop |

BFS visit order: A, B, C, D, F, G, E, H. BFS path: A → C → F → H (3 edges).

## 4. DFS trace
Stack top is on the left. Successors are pushed in reverse so the leftmost successor is explored first.

| Step | Stack before | Processed | Stack after expansion |
|---|---|---|---|
| 1 | [A] | A | [B, C] |
| 2 | [B, C] | B | [D, C] |
| 3 | [D, C] | D | [E, C] |
| 4 | [E, C] | E | [H, C] |
| 5 | [H, C] | H | [C] — stop |

DFS visit order: A, B, D, E, H. DFS path: A → B → D → E → H (4 edges).

## 5. DLS and IDDFS
DLS uses path-local cycle checking. FOUND means goal reached; CUTOFF means the depth limit blocked a possible continuation; FAILURE means no goal and no remaining cutoff branch.

| DLS limit | Status | Path | Reason |
|---|---|---|---|
| 1 | CUTOFF | — | Goal is deeper than limit. |
| 2 | CUTOFF | — | Goal is deeper than limit. |
| 3 | FOUND | A → C → F → H | Goal found at depth 3 after earlier branch is explored. |
| 4 | FOUND | A → B → D → E → H | Depth-4 branch reaches H first in DFS order. |

IDDFS attempts limits 1, 2, then 3. Limits 1 and 2 return CUTOFF; limit 3 returns FOUND with A → C → F → H. Limit 4 is not attempted because the search stops after success.

IDDFS repeats work because each iteration restarts at A and re-expands shallow nodes. It uses relatively little memory and finds a shallow solution when step costs are equal.

## 6. UCS weighted graph
Weights: A→B=1, A→C=1, B→D=1, D→E=1, E→H=1, C→F=2, C→G=2, F→H=2, G→H=2. These costs are an illustrative weighted version of the same topology.

UCS processing order with cumulative cost: A(0), B(1), C(1), D(2), F(3), G(3), E(3), H(4). Equal-cost nodes are processed in the order they enter the priority queue. UCS path: A → B → D → E → H.

Independent sum: 1 + 1 + 1 + 1 = 4. BFS route A → C → F → H costs 1 + 2 + 2 = 5. BFS minimizes edge count; UCS minimizes total cost, so a route with fewer edges can cost more.

## 7. Comparison, limitation, edge case, reflection
BFS finds a minimum-edge route in an unweighted graph. DFS may reach a deeper route first and depends on successor order. DLS restricts depth but may miss a goal if the limit is too small. IDDFS repeats shallow work but keeps memory use low. UCS uses cumulative non-negative costs to find a least-cost route.

Edge case: with limits below the goal depth, DLS returns CUTOFF rather than FOUND. CUTOFF differs from FAILURE because a continuation may exist beyond the limit. Useful extra tests include start=goal, an unreachable goal, and a graph containing a cycle.

Responsible practice: the original graph was not supplied, so this example graph and its costs are labelled as assumptions rather than claimed to be the instructor's graph. Check and replace the graph before final submission. Fixed successor order affects BFS/DFS traces.

## 8. References
Russell, S. J., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

Python Software Foundation. *Python 3 documentation: heapq — Heap queue algorithm*. https://docs.python.org/3/library/heapq.html
