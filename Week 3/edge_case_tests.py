"""Reproducible edge-case tests for BFS, DFS, DLS and UCS."""
from lab3_search import bfs, dfs
from lab3_depth_search import dls
from lab3_ucs import ucs

assert bfs("G", "G")[0] == ["G"]
assert dfs("G", "G")[0] == ["G"]
assert dls("G", "G", 0)[0:2] == ("FOUND", ["G"])
assert ucs("G", "G")[0:2] == (["G"], 0)
print("START=GOAL: BFS, DFS, DLS and UCS return [G]; UCS cost=0")

unreachable = {"A": ["B"], "B": [], "X": []}
assert bfs("A", "X", unreachable)[0] is None
assert dfs("A", "X", unreachable)[0] is None
print("UNREACHABLE GOAL: BFS and DFS return None after exhausting reachable nodes")

cycle = {"A": ["B"], "B": ["A", "G"], "G": []}
assert bfs("A", "G", cycle)[0] == ["A", "B", "G"]
assert dfs("A", "G", cycle)[0] == ["A", "B", "G"]
print("CYCLE: A->B->A is safely skipped; both searches find A->B->G")
