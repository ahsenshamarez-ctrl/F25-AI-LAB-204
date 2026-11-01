"""BFS and DFS for the original A-G graph in the lab manual."""
from collections import deque

graph = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
    "D": [], "E": ["G"], "F": [], "G": []
}

def bfs(start, goal, adjacency=graph):
    queue = deque([(start, [start])])
    seen = {start}
    processed = []
    while queue:
        node, path = queue.popleft()
        processed.append(node)
        if node == goal:
            return path, processed
        for nxt in adjacency.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None, processed

def dfs(start, goal, adjacency=graph):
    stack = [(start, [start])]
    seen = set()
    processed = []
    while stack:
        node, path = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        processed.append(node)
        if node == goal:
            return path, processed
        for nxt in reversed(adjacency.get(node, [])):
            if nxt not in seen:
                stack.append((nxt, path + [nxt]))
    return None, processed

if __name__ == "__main__":
    for name, fn in (("BFS", bfs), ("DFS", dfs)):
        path, order = fn("A", "G")
        print(f"{name} path: {' -> '.join(path) if path else 'Not found'}")
        print(f"{name} processing order: {' -> '.join(order)}")
