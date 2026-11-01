"""Week 4: A* heuristic audit, UCS control, and overestimate experiment."""
from heapq import heappop, heappush
from math import inf

GRAPH = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}
HEURISTIC = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
TRUE_REMAINING = {"S": 6, "A": 5, "B": 5, "C": 3, "G": 0}
START, GOAL = "S", "G"


def frontier_snapshot(priority_queue):
    return [
        (node, g, f - g, f, path)
        for f, g, node, path in sorted(priority_queue)
    ]


def astar(graph, heuristic, start, goal):
    """A* graph search. Setting h=0 for every node produces UCS."""
    if start not in heuristic:
        raise KeyError(f"Missing heuristic for start node {start!r}")
    queue = [(heuristic[start], 0, start, [start])]
    best_g = {start: 0}
    processed, expanded, stale_entries, events = [], [], [], []

    while queue:
        f_value, g_value, node, path = heappop(queue)
        if g_value != best_g.get(node, inf):
            stale_entries.append((node, g_value, best_g.get(node)))
            events.append({"type": "stale", "node": node, "g": g_value})
            continue

        processed.append(node)
        events.append({
            "type": "pop", "node": node, "g": g_value,
            "h": heuristic.get(node, 0), "f": f_value, "path": path[:]
        })
        if node == goal:
            return {
                "cost": g_value, "path": path, "processed": processed,
                "expanded": expanded, "stale_entries": stale_entries,
                "events": events
            }

        expanded.append(node)
        for neighbour, edge_cost in graph.get(node, []):
            if edge_cost < 0:
                raise ValueError("A* / UCS requires nonnegative edge costs.")
            new_g = g_value + edge_cost
            if new_g < best_g.get(neighbour, inf):
                best_g[neighbour] = new_g
                new_h = heuristic.get(neighbour, 0)
                new_f = new_g + new_h
                new_path = path + [neighbour]
                heappush(queue, (new_f, new_g, neighbour, new_path))
                events.append({
                    "type": "push", "from": node, "node": neighbour,
                    "g": new_g, "h": new_h, "f": new_f, "path": new_path[:]
                })
        events.append({"type": "frontier", "entries": frontier_snapshot(queue)})

    return {
        "cost": None, "path": [], "processed": processed,
        "expanded": expanded, "stale_entries": stale_entries,
        "events": events
    }


def independently_sum_path(graph, path):
    total = 0
    for current, following in zip(path, path[1:]):
        weights = [w for nxt, w in graph.get(current, []) if nxt == following]
        if not weights:
            raise ValueError(f"No edge exists: {current} -> {following}")
        total += weights[0]
    return total


def audit_heuristic(graph, heuristic, true_remaining):
    print("HEURISTIC AUDIT")
    for node in graph:
        h, true_cost = heuristic[node], true_remaining[node]
        print(f"{node}: h={h}, true remaining={true_cost}, admissible={h <= true_cost}")
    print("CONSISTENCY AUDIT: h(u) <= cost(u,v) + h(v)")
    all_consistent = True
    for node, neighbours in graph.items():
        for nxt, weight in neighbours:
            left, right = heuristic[node], weight + heuristic[nxt]
            passed = left <= right
            all_consistent &= passed
            print(f"{node}->{nxt}: {left} <= {weight}+{heuristic[nxt]}={right}: {passed}")
    print("Admissible:", all(heuristic[n] <= true_remaining[n] for n in graph))
    print("Consistent:", all_consistent)


def print_run(label, result, graph):
    print(f"\n{label}")
    print("Processed trace:", " -> ".join(result["processed"]) or "(none)")
    print("Expanded nodes:", result["expanded"])
    print("Expansion count:", len(result["expanded"]))
    print("Stale entries ignored:", result["stale_entries"])
    if result["path"]:
        print("Path:", " -> ".join(result["path"]))
        print("Returned cost:", result["cost"])
        print("Independent path sum:", independently_sum_path(graph, result["path"]))
    else:
        print("Path: no path; cost: None")


def print_frontier_audit(result):
    print("\nMANUAL FRONTIER AUDIT")
    for event in result["events"]:
        if event["type"] == "pop":
            print(f"POP {event['node']}: g={event['g']}, h={event['h']}, f={event['f']}")
        elif event["type"] == "push":
            print(f"  PUSH {event['node']}: g={event['g']}, h={event['h']}, f={event['f']}")
        elif event["type"] == "frontier":
            entries = [
                f"{n}(g={g},h={h},f={f})"
                for n, g, h, f, path in event["entries"]
            ]
            print("  FRONTIER:", ", ".join(entries) or "(empty)")
    print("After C: G has f=6 and B has f=8, so G is selected next.")


def main():
    audit_heuristic(GRAPH, HEURISTIC, TRUE_REMAINING)
    informed = astar(GRAPH, HEURISTIC, START, GOAL)
    print_frontier_audit(informed)
    ucs = astar(GRAPH, {node: 0 for node in GRAPH}, START, GOAL)
    over_h = dict(HEURISTIC)
    over_h["C"] = 10
    overestimate = astar(GRAPH, over_h, START, GOAL)

    print_run("A* WITH SUPPLIED HEURISTIC", informed, GRAPH)
    print_run("UCS CONTROL (ALL h=0)", ucs, GRAPH)
    print("\nOVERESTIMATE EXPERIMENT: h(C) changes from 2 to 10; true remaining cost is 3.")
    print_run("A* WITH h(C)=10", overestimate, GRAPH)


if __name__ == "__main__":
    main()
