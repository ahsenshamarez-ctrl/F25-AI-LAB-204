from collections import deque

GRAPH = {"A":["B","C"], "B":["D"], "C":["F","G"], "D":["E"], "E":["H"], "F":["H"], "G":["H"], "H":[]}

def bfs(graph, start, goal):
    queue = deque([(start, [start])]); seen = {start}; order = []
    while queue:
        node, path = queue.popleft(); order.append(node)
        if node == goal: return path, order
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt); queue.append((nxt, path + [nxt]))
    return None, order

def dfs(graph, start, goal):
    stack = [(start, [start])]; seen = set(); order = []
    while stack:
        node, path = stack.pop()
        if node in seen: continue
        seen.add(node); order.append(node)
        if node == goal: return path, order
        for nxt in reversed(graph[node]):
            if nxt not in seen: stack.append((nxt, path + [nxt]))
    return None, order

if __name__ == "__main__":
    for name, fn in (("BFS", bfs), ("DFS", dfs)):
        path, order = fn(GRAPH, "A", "H")
        print(f"{name} visit order: {' -> '.join(order)}")
        print(f"{name} path: {' -> '.join(path) if path else 'NOT FOUND'}")
