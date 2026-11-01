# Lab 3 Report — Uninformed Search

**Student:** Rasikh Ali | **Roll No.:** 42365 | **Course:** CAI601400

## 1. Objective and state-space formulation
Model a rescue robot moving through a directed building graph. Each vertex is a location and each directed edge is a corridor. Initial state: A. Goal test: current node is G. In the original graph, every edge has equal step cost. Root depth is 0. Search stops when G is removed from the frontier and processed.

## 2. Original graph and successor order
The supplied Section 3.2 graph is used exactly:
- A: B, C
- B: D, E
- C: F
- D: none
- E: G
- F: none
- G: none

## 3. Manual BFS frontier trace
Queue is shown front to rear.
| Step | Queue before | Processed | Queue after expansion |
|---|---|---|---|
| 1 | [A] | A | [B, C] |
| 2 | [B, C] | B | [C, D, E] |
| 3 | [C, D, E] | C | [D, E, F] |
| 4 | [D, E, F] | D | [E, F] |
| 5 | [E, F] | E | [F, G] |
| 6 | [F, G] | F | [G] |
| 7 | [G] | G | [] — stop |

**BFS processing order:** A, B, C, D, E, F, G.  
**BFS path:** A → B → E → G.

## 4. Manual DFS frontier trace
Stack top is shown first. Successors are pushed in reverse order so the first listed successor is visited first.
| Step | Stack before | Processed | Stack after expansion |
|---|---|---|---|
| 1 | [A] | A | [B, C] |
| 2 | [B, C] | B | [D, E, C] |
| 3 | [D, E, C] | D | [E, C] |
| 4 | [E, C] | E | [G, C] |
| 5 | [G, C] | G | [C] — stop |

**DFS processing order:** A, B, D, E, G.  
**DFS path:** A → B → E → G.

## 5. DLS and IDDFS
DLS uses a path-local cycle check. CUTOFF means a continuation exists beyond the current depth boundary; FAILURE means all reachable branches were exhausted without a cutoff.
| DLS limit | Status | Path |
|---|---|---|
| 1 | CUTOFF | — |
| 2 | CUTOFF | — |
| 3 | FOUND | A → B → E → G |
| 4 | FOUND | A → B → E → G |

IDDFS restarts DLS with fresh path state at each limit. For maximum depths 1 and 2 it returns CUTOFF; for maximum depths 3 and 4 it finds G at limit 3 and stops. Repeated shallow work is the cost of keeping memory low. A limit below 3 cannot reach a goal at depth 3, but CUTOFF is not proof of global unreachability.

## 6. Weighted extension and UCS
All original corridors are retained and the explicitly required corridor C→G is added. Nonnegative costs used:
| Edge | Cost | Note |
|---|---:|---|
| A→B | 1 | Original |
| A→C | 6 | Original |
| B→D | 2 | Original |
| B→E | 1 | Original |
| C→F | 2 | Original |
| E→G | 1 | Original |
| C→G | 6 | Added corridor |

The weights are stated assumptions selected to satisfy the manual's reference comparison: A→C→G costs 12; A→B→E→G costs 3.
**UCS processing order (node, cumulative cost):** A(0), B(1), E(2), D(3), G(3).  
**UCS path:** A → B → E → G. Independent sum: 1 + 1 + 1 = 3.

BFS on the same weighted topology returns the fewest-edge path A → C → G (2 edges), with cost 6 + 6 = 12. UCS returns a 3-edge path with cost 3. BFS minimizes hops; UCS minimizes total nonnegative travel cost.

## 7. Complexity comparison
| Strategy | Complete? | Optimal? | Main resource behaviour |
|---|---|---|---|
| BFS | Yes, finite branching | Yes for equal step costs | High memory; broad frontier |
| DFS | Not always | No | Low memory; may follow deep branches |
| DLS | If limit is sufficient | No | Bounded depth; may return CUTOFF |
| IDDFS | Yes, finite branching | Yes for equal step costs | Repeats shallow work; low memory |
| UCS | Yes with positive costs | Yes for nonnegative costs | Priority queue ordered by path cost |

## 8. Edge-case tests
- **Start equals goal:** BFS, DFS, DLS and UCS are tested from G to G; each returns [G], UCS cost 0.
- **Unreachable goal:** search A to isolated node X; BFS and DFS return None after exhausting reachable nodes.
- **Cycle:** graph A→B, B→A and B→G; both BFS and DFS terminate and find A→B→G.
The depth-2 DLS cutoff is a bounded-search result only. UCS rejects negative edge costs because its guarantee requires nonnegative costs.

## 9. Limitations and improvement
The graph is a small directed abstraction and does not represent changing obstacles, uncertain travel times or robot dynamics. The manual states target path costs but not every edge's numeric weight on the copied pages; the edge values above are therefore explicit illustrative assumptions consistent with the stated comparison. A future version could load graph data from a file, validate edge costs, and test more start/goal pairs.

## 10. Reflection and responsible practice
I learned that BFS and DFS may return the same route but process nodes in different orders, and UCS optimizes accumulated cost rather than number of edges. These methods can help a rescue robot compare routes without a heuristic. The surprising result was that the fewest-edge route cost more. Next time I would draw the frontier before coding and independently sum every returned path. I kept successor order fixed, reported actual processing order, disclosed the added corridor and documented the assumed costs rather than presenting them as supplied facts.
