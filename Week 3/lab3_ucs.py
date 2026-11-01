"""UCS on the manual's weighted extension: original edges plus C->G."""
import heapq
from itertools import count

weighted_graph = {
    "A": [("B", 1), ("C", 6)],
    "B": [("D", 2), ("E", 1)],
    "C": [("F", 2), ("G", 6)],  # C->G is the added corridor
    "D": [], "E": [("G", 1)], "F": [], "G": []
}

def ucs(start, goal, adjacency=weighted_graph):
    serial = count()
    frontier = [(0, next(serial), start, [start])]
    best = {start: 0}
    processed = []
    while frontier:
        cost, _, node, path = heapq.heappop(frontier)
        if cost != best.get(node):
            continue
        processed.append((node, cost))
        if node == goal:
            return path, cost, processed
        for nxt, weight in adjacency.get(node, []):
            if weight < 0:
                raise ValueError("UCS requires nonnegative edge costs")
            new_cost = cost + weight
            if new_cost < best.get(nxt, float("inf")):
                best[nxt] = new_cost
                heapq.heappush(frontier, (new_cost, next(serial), nxt, path + [nxt]))
    return None, float("inf"), processed

def path_cost(path, adjacency=weighted_graph):
    return sum(dict(adjacency[a])[b] for a, b in zip(path, path[1:]))

if __name__ == "__main__":
    path, cost, order = ucs("A", "G")
    print("UCS path:", " -> ".join(path))
    print("UCS cost:", cost)
    print("UCS processing order:", " -> ".join(f"{n}({c})" for n, c in order))
    print("Independent path-cost check:", path_cost(path))
    bfs_path = ["A", "C", "G"]
    print("BFS path on same topology:", " -> ".join(bfs_path))
    print("BFS path cost:", path_cost(bfs_path))
