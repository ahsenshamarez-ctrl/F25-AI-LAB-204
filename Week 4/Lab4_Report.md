# Lab 4 Report — Informed Search: Heuristics & A*

**Student:** Rasikh Ali  
**Roll No.:** 42365  
**Course:** CAI601400 — Artificial Intelligence Lab  
**Week:** 4 | **Lectures:** L7–L8 | **CLO:** CLO2 (C3: Apply)

## 1. Objective
Compute and interpret g(n), h(n), and f(n)=g(n)+h(n); implement A* with a priority queue; audit admissibility and consistency; and compare A* with UCS using measured expansion counts.

## 2. Problem and assumptions
The graph represents abstract campus travel-time units. These are supplied teaching values, not measured campus distances. Heuristic estimates use the same units as edge costs.

| Directed edge | Cost |
|---|---:|
| S → A | 1 |
| S → B | 4 |
| A → C | 2 |
| B → G | 5 |
| C → G | 3 |

Start: **S**. Goal: **G**.

| Node | Supplied h(n) | True remaining cost |
|---|---:|---:|
| S | 5 | 6 |
| A | 4 | 5 |
| B | 4 | 5 |
| C | 2 | 3 |
| G | 0 | 0 |

All edge costs are nonnegative. The priority queue uses tuple order (f, g, node, path): lower f first, then lower g, then node label. The same implementation is used for A* and UCS; UCS is produced by setting every h-value to zero.

## 3. Evaluation function
- g(n): actual cost from start to n.
- h(n): estimated remaining cost from n to the goal.
- f(n)=g(n)+h(n): priority for selecting the next frontier node.

When a cheaper route to a node is found, its best-known g-value is updated and a new queue entry is inserted. Outdated entries are ignored when popped.

## 4. Task 1 — Manual frontier trace

Initial entry: S has g=0, h=5, f=0+5=5.

| Expansion | Selected | g | h | f | Remaining frontier after expansion |
|---|---|---:|---:|---:|---|
| 1 | S | 0 | 5 | 5 | A(1,4,5), B(4,4,8) |
| 2 | A | 1 | 4 | 5 | C(3,2,5), B(4,4,8) |
| 3 | C | 3 | 2 | 5 | G(6,0,6), B(4,4,8) |

Arithmetic:
1. Expand S. A: g=0+1=1, f=1+4=5. B: g=0+4=4, f=4+4=8. Select A because 5<8.
2. Expand A. C: g=1+2=3, f=3+2=5. Select C because 5<8.
3. Expand C. G: g=3+3=6, f=6+0=6. Select G because 6<8. G is the goal and the search stops when it is popped.

The first three expanded nodes are S, A, C. The processed trace includes the goal: S, A, C, G.

## 5. Task 2 — Heuristic audit and comparison

### 5.1 Admissibility
An admissible heuristic never overestimates the true remaining cost. The supplied values pass at every node:
- S: 5 ≤ 6
- A: 4 ≤ 5
- B: 4 ≤ 5
- C: 2 ≤ 3
- G: 0 ≤ 0

### 5.2 Consistency
For each directed edge u→v, consistency requires h(u) ≤ cost(u,v)+h(v).

| Edge | Check | Result |
|---|---|---|
| S → A | 5 ≤ 1+4=5 | Pass |
| S → B | 5 ≤ 4+4=8 | Pass |
| A → C | 4 ≤ 2+2=4 | Pass |
| B → G | 4 ≤ 5+0=5 | Pass |
| C → G | 2 ≤ 3+0=3 | Pass |

The supplied heuristic is admissible on all supplied nodes and consistent on every directed edge in this instance.

### 5.3 Measured A*/UCS comparison
A node is counted as expanded only when its successors are examined. The goal is included in the processed trace but excluded from the expansion count. Stale entries are ignored.

| Run | Returned path | Independent path cost | Processed trace | Expanded nodes | Count |
|---|---|---:|---|---|---:|
| A* supplied h | S → A → C → G | 6 | S, A, C, G | S, A, C | 3 |
| UCS h=0 | S → A → C → G | 6 | S, A, C, B, G | S, A, C, B | 4 |

Independent cost: 1+2+3=6. A* selects G after C because G has f=6 and B has f=8. UCS uses only g-values; B has g=4 and is therefore processed before G at g=6. Both return the optimal cost 6, while A* expands one fewer node.

There are no stale entries in either run. The goal is popped and logged but not expanded in both runs.

## 6. Task 3 — Deliberate overestimate

Only one heuristic value changes:
- Original h(C)=2
- Modified h(C)=10
- True remaining cost from C=3

The modified heuristic is inadmissible at C because 10>3.

1. S is expanded; A has f=5 and B has f=8.
2. A is expanded; C gets g=3, h=10, f=13.
3. B is selected before C because f(B)=8. B generates G with g=9, h=0, f=9.
4. G is selected before C because 9<13, so the search returns the route through B.

| Run | Path | Cost | Processed trace | Expansion count |
|---|---|---:|---|---:|
| Supplied heuristic | S → A → C → G | 6 | S, A, C, G | 3 |
| Overestimate h(C)=10 | S → B → G | 9 | S, A, B, G | 3 |

The route and cost change from 6 to 9. The expansion count happens to remain 3, but the expanded nodes differ. This demonstrates that an overestimate can cause A* to pop a goal before exploring a cheaper route. An overestimate does not make every individual run fail; an unchanged result in a different test would not prove the heuristic safe.

## 7. Edge-case tests
The included edge_case_tests.py checks:
1. Start equals goal: graph S has no outgoing edges, start S and goal S. Expected and observed: path [S], cost 0, processed [S], zero expansions.
2. Unreachable goal: S connects to A, while G is disconnected. Expected and observed: no path, cost None; search terminates after processing S and A.

## 8. Implementation choices and limitations
- Python heapq implements the min-priority queue.
- Heap tuple order (f, g, node, path) makes tie-breaking deterministic.
- best_g stores the cheapest known path cost; stale entries are skipped.
- Returned path cost is independently recomputed from its edges.
- The algorithm assumes nonnegative edge costs.
- The graph is small and abstract. A real campus system would need calibrated travel-time costs and a heuristic in matching units.

## 9. Reflection and responsible practice
**What did I learn?** A* combines cost already paid with estimated remaining cost. An admissible heuristic can reduce unnecessary expansions while preserving an optimal result.

**How can this apply to a real AI system?** A navigation system can prioritize promising routes using travel-time estimates, provided the estimates use compatible units and their assumptions are validated.

**What failed or surprised me?** Changing only h(C) to 10 made the search return the more expensive route. Expansion count alone did not reveal answer quality; path cost also needed checking.

**What would I do differently?** Validate heuristic values and units, retain trace output, and compare path costs against an independent calculation and a UCS baseline.

**Responsible practice:** The graph and heuristic are identified as abstract lab data, not real campus measurements. Assumptions are documented for reproducibility. No credentials or private data are included.

## 10. Conclusion
With the supplied admissible and consistent heuristic, A* returned the optimal cost-6 route and expanded 3 nodes, compared with UCS's 4 expansions. The overestimate experiment returned a cost-9 route, showing why heuristic quality matters to A*'s optimality guarantee.

## References
- Artificial Intelligence Lab Manual, Lab 4: Informed Search: Heuristics & A*, pages 16–18.
- Python standard-library documentation: heapq, https://docs.python.org/3/library/heapq.html
