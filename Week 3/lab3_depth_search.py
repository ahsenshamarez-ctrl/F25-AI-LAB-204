GRAPH = {"A":["B","C"], "B":["D"], "C":["F","G"], "D":["E"], "E":["H"], "F":["H"], "G":["H"], "H":[]}
FOUND, CUTOFF, FAILURE = "FOUND", "CUTOFF", "FAILURE"

def dls(graph, start, goal, limit):
    order = []
    def visit(node, depth, path):
        order.append(node)
        if node == goal: return FOUND, path
        if depth == limit:
            return (CUTOFF, None) if any(n not in path for n in graph[node]) else (FAILURE, None)
        saw_cutoff = False
        for nxt in graph[node]:
            if nxt in path: continue
            status, found_path = visit(nxt, depth + 1, path + [nxt])
            if status == FOUND: return FOUND, found_path
            if status == CUTOFF: saw_cutoff = True
        return (CUTOFF, None) if saw_cutoff else (FAILURE, None)
    status, path = visit(start, 0, [start])
    return status, path, order

def iddfs(graph, start, goal, max_depth):
    attempts = []
    for limit in range(1, max_depth + 1):
        status, path, order = dls(graph, start, goal, limit)
        attempts.append((limit, status, path, order))
        if status == FOUND: return path, attempts
        if status == FAILURE: break
    return None, attempts

if __name__ == "__main__":
    for limit in range(1, 5):
        status, path, order = dls(GRAPH, "A", "H", limit)
        print(f"DLS limit {limit}: status={status}; path={' -> '.join(path) if path else '-'}; order={' -> '.join(order)}")
    path, attempts = iddfs(GRAPH, "A", "H", 4)
    print("IDDFS attempts:")
    for limit, status, _, order in attempts:
        print(f"  limit {limit}: {status}; order={' -> '.join(order)}")
    print(f"IDDFS final path: {' -> '.join(path) if path else 'NOT FOUND'}")
