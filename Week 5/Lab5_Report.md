# Lab 5 Report: Adversarial Search — Minimax & Alpha-Beta Pruning

**Student:** Rasikh Ali — 42365  
**Course:** CAI601400 — Artificial Intelligence Lab  
**Week:** 5 | **Lectures:** L11–L12 | **CLO:** CLO2 (C3: Apply)

## 1. Objective
Implement Minimax and Alpha-Beta pruning for a fixed-depth, two-player, zero-sum game tree. Compute the root decision, count terminal leaves evaluated, compare branch orderings, and verify that pruning preserves the Minimax value.

## 2. Problem and assumptions
MAX chooses moves to maximize utility. MIN is assumed to choose moves that minimize MAX's eventual utility. Terminal utilities are known and are evaluated from MAX's perspective. The supplied eight-leaf sequence is `[3, 5, 2, 9, 3, 5, 2, 9]`. The tree is complete and binary, with MAX at the root, alternating MIN/MAX levels, and terminal leaves at depth three.

These are illustrative game scores, not measurements from a real game. The implementation counts a leaf when its terminal utility is actually read.

## 3. Minimax hand trace
Evaluate upward from the leaves:
- Bottom MAX nodes: max(3,5)=5; max(2,9)=9; max(3,5)=5; max(2,9)=9.
- MIN nodes: min(5,9)=5 on the left and min(5,9)=5 on the right.
- Root MAX: max(5,5)=**5**.

The root value is 5. Under the fixed left-to-right tree, both root alternatives have value 5, so either tied action is optimal. The manual's leaf-only representation does not label distinct action names; therefore the report identifies the optimal value rather than inventing move labels.

## 4. Alpha-Beta bounds and pruning
Alpha is the best value MAX can already guarantee along the current path (a lower bound). Beta is the best value MIN can already guarantee for MAX (an upper bound). When `alpha >= beta`, the remaining children of the current node cannot change the ancestor's decision, so they can be skipped.

For the supplied ordering, Alpha-Beta returns **5** and evaluates **6** of the 8 terminal leaves. It prunes 2 leaves after the right MIN node reaches beta=5 while the root already has alpha=5. Plain Minimax evaluates all 8 leaves.

## 5. Branch-order experiment
| Ordering | Minimax value | Minimax leaves | Alpha-Beta value | Alpha-Beta leaves |
|---|---:|---:|---:|---:|
| Supplied: 3,5,2,9,3,5,2,9 | 5 | 8 | 5 | 6 |
| Reversed: 9,2,5,3,9,2,5,3 | 5 | 8 | 5 | 6 |

Both orders preserve the root value. These two particular orderings happen to have the same count; this does not mean ordering is irrelevant. In other trees, examining strong candidate moves early can cause earlier cutoffs and fewer leaf evaluations. Poor ordering can reduce the benefit, while the Minimax result remains unchanged.

## 6. Edge-case and comparison tests
1. **Single terminal node:** both algorithms return 7 and evaluate exactly one leaf.
2. **Mixed utilities:** for `[-4, 6, -2, 8]`, both return -2; plain Minimax evaluates four leaves and Alpha-Beta evaluates no more than four.
3. **Consistency assertion:** the program asserts that both algorithms return equal root values for each ordering.
4. **Work assertion:** the program asserts that Alpha-Beta does not evaluate more leaves than plain Minimax for the same tree and ordering.

## 7. Implementation choices
- The tree is represented by a list of terminal utilities in left-to-right order. Recursive slicing divides it into equal left and right subtrees.
- MAX and MIN alternate at every level.
- The terminal case increments the leaf counter exactly once.
- Alpha and beta are updated after each child result.
- The cutoff condition is `alpha >= beta`.
- Both algorithms receive identical utilities and move order during each comparison, making the leaf counts comparable.

## 8. Important limitation in the manual's six-score example
The manual's Minimax snippet starts with six scores and pads the list to eight using zeros. Padding is only valid if the added zero values are genuine terminal outcomes in the intended game. Otherwise, it invents outcomes and may change the root decision. This submission uses the manual's separate eight-score Alpha-Beta example as the common complete tree for a fair algorithm comparison.

## 9. Interpretation and learning outcome
The experiment demonstrates that Alpha-Beta pruning can avoid evaluating branches while preserving the exact Minimax decision. Here it evaluates 6 rather than 8 leaves for both tested orders, saving 2 evaluations (25%). Alpha-Beta is most useful when a game tree is large and good moves are searched early. It does not make the worst-case search cost disappear; poor ordering can make pruning much less effective.

## 10. Reflection
- **What did I learn?** Minimax models optimal opposing decisions, while alpha and beta track bounds that prove when a branch is unnecessary.
- **How can this be applied?** Game-playing agents can use Alpha-Beta to search deeper under a limited computation budget.
- **What surprised me?** The root value stayed the same even though Alpha-Beta did not inspect every terminal outcome.
- **What would I change next time?** I would test more move orderings and larger trees to quantify how ordering affects pruning.

## 11. Responsible practice and transparency
The source code, utility list, trace, counters, and assertions are included so another student can reproduce the results. Utilities are clearly identified as synthetic. No claim is made that this small example represents the complexity or performance of a production game engine.

## 12. Viva-ready explanation
**Why does MAX assume MIN chooses the worst outcome for MAX?** Because Minimax models a rational opponent who also plays optimally in a zero-sum game.

**What do alpha and beta mean?** Alpha is MAX's current lower bound; beta is MIN's current upper bound.

**Why is pruning safe?** Once alpha is at least beta, the remaining branch cannot improve the decision for the player whose ancestor will choose, so it cannot affect the root result.

**Does pruning change the answer?** No. It changes the amount of search, not the Minimax value.

**Why does move ordering matter?** Strong moves found early tighten bounds sooner, allowing more branches to be cut off.

## 13. Conclusion
Both algorithms selected the same optimal root value, 5. Plain Minimax evaluated all 8 leaves; Alpha-Beta evaluated 6 for the tested orderings. The implementation, output, trace, comparison, and edge-case checks provide reproducible evidence for the Week 5 learning outcomes.
