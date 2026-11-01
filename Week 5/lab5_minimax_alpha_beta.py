"""Week 5: Minimax and Alpha-Beta pruning.
Rasikh Ali - 42365 | CAI601400
Run: python lab5_minimax_alpha_beta.py
"""
from math import inf

class LeafCounter:
    def __init__(self):
        self.count = 0

def minimax(values, maximizing=True, counter=None):
    """Evaluate a complete binary tree represented by terminal values."""
    if len(values) == 1:
        if counter is not None:
            counter.count += 1
        return values[0]
    midpoint = len(values) // 2
    left = minimax(values[:midpoint], not maximizing, counter)
    right = minimax(values[midpoint:], not maximizing, counter)
    return max(left, right) if maximizing else min(left, right)

def alpha_beta(values, maximizing=True, alpha=-inf, beta=inf, counter=None):
    """Alpha-Beta search; left-to-right ordering is the supplied move order."""
    if len(values) == 1:
        if counter is not None:
            counter.count += 1
        return values[0]

    midpoint = len(values) // 2
    children = (values[:midpoint], values[midpoint:])
    value = -inf if maximizing else inf

    for child_values in children:
        child_value = alpha_beta(
            child_values, not maximizing, alpha, beta, counter
        )
        if maximizing:
            value = max(value, child_value)
            alpha = max(alpha, value)
        else:
            value = min(value, child_value)
            beta = min(beta, value)
        if alpha >= beta:
            break
    return value

def run_comparison(label, utilities):
    plain_count = LeafCounter()
    pruned_count = LeafCounter()
    plain_value = minimax(utilities, counter=plain_count)
    pruned_value = alpha_beta(utilities, counter=pruned_count)
    print(f"{label}")
    print(f"  Utilities: {utilities}")
    print(f"  Minimax value: {plain_value}; leaves evaluated: {plain_count.count}")
    print(f"  Alpha-Beta value: {pruned_value}; leaves evaluated: {pruned_count.count}")
    print(f"  Leaves avoided: {plain_count.count - pruned_count.count}")
    assert plain_value == pruned_value, "Minimax and Alpha-Beta must agree"
    assert pruned_count.count <= plain_count.count

def edge_case_tests():
    # A single terminal node: root is already a terminal state.
    one_leaf_count = LeafCounter()
    one_leaf_value = minimax([7], counter=one_leaf_count)
    assert one_leaf_value == 7 and one_leaf_count.count == 1

    one_leaf_ab_count = LeafCounter()
    one_leaf_ab_value = alpha_beta([7], counter=one_leaf_ab_count)
    assert one_leaf_ab_value == 7 and one_leaf_ab_count.count == 1

    # A depth-two tree containing negative and positive utilities.
    mixed = [-4, 6, -2, 8]
    mm_count, ab_count = LeafCounter(), LeafCounter()
    mm_value = minimax(mixed, counter=mm_count)
    ab_value = alpha_beta(mixed, counter=ab_count)
    assert mm_value == ab_value == -2
    assert mm_count.count == 4 and ab_count.count <= 4
    print("Edge cases: PASS (single terminal node; mixed negative/positive utilities)")

if __name__ == "__main__":
    supplied_order = [3, 5, 2, 9, 3, 5, 2, 9]
    reversed_order = list(reversed(supplied_order))
    print("WEEK 5 — MINIMAX AND ALPHA-BETA")
    run_comparison("Supplied left-to-right ordering", supplied_order)
    run_comparison("Reversed branch ordering", reversed_order)
    edge_case_tests()
    print("All checks passed.")
