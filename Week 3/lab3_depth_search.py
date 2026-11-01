"""DLS and IDDFS for the original graph, using a path-local cycle check."""
graph = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
    "D": [], "E": ["G"], "F": [], "G": []
}

def dls(start, goal, limit, adjacency=graph):
    processed = []
    def visit(node, path, depth):
        processed.append(node)
        if node == goal:
            return "FOUND", path
        if depth == limit:
            return ("CUTOFF", None) if adjacency.get(node, []) else ("FAILURE", None)
        saw_cutoff = False
        for nxt in adjacency.get(node, []):
            if nxt in path:
                continue
            status, result = visit(nxt, path + [nxt], depth + 1)
            if status == "FOUND":
                return status, result
            if status == "CUTOFF":
                saw_cutoff = True
        return ("CUTOFF", None) if saw_cutoff else ("FAILURE", None)
    status, path = visit(start, [start], 0)
    return status, path, processed

def iddfs(start, goal, max_depth, adjacency=graph):
    attempts = []
    for limit in range(1, max_depth + 1):
        status, path, processed = dls(start, goal, limit, adjacency)
        attempts.append((limit, status, path, processed))
        if status == "FOUND":
            return status, path, attempts
    return (attempts[-1][1] if attempts else "FAILURE"), None, attempts

if __name__ == "__main__":
    print("DLS results")
    for limit in range(1, 5):
        status, path, order = dls("A", "G", limit)
        print(f"limit={limit}: {status}; path={path}; processed={order}")
    print("\nIDDFS results")
    for maximum in range(1, 5):
        status, path, attempts = iddfs("A", "G", maximum)
        print(f"maximum={maximum}: {status}; path={path}; limits={[a[0] for a in attempts]}")
