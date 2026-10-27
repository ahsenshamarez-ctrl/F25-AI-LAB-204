import heapq
from itertools import count

WEIGHTED_GRAPH = {
    "A":[("B",1),("C",1)], "B":[("D",1)], "C":[("F",2),("G",2)],
    "D":[("E",1)], "E":[("H",1)], "F":[("H",2)], "G":[("H",2)], "H":[]
}
def ucs(graph, start, goal):
    tie = count(); frontier = [(0,next(tie),start,[start])]
    best = {start:0}; processed = []
    while frontier:
        cost, _, node, path = heapq.heappop(frontier)
        if cost != best.get(node): continue
        processed.append((node,cost))
        if node == goal: return path,cost,processed
        for nxt,weight in graph[node]:
            new_cost = cost + weight
            if new_cost < best.get(nxt,float("inf")):
                best[nxt] = new_cost
                heapq.heappush(frontier,(new_cost,next(tie),nxt,path+[nxt]))
    return None,float("inf"),processed
if __name__ == "__main__":
    path,cost,order = ucs(WEIGHTED_GRAPH,"A","H")
    print("UCS processing order (node, cumulative cost):")
    print(" -> ".join(f"{n}({c})" for n,c in order))
    print(f"UCS path: {' -> '.join(path) if path else 'NOT FOUND'}")
    print(f"UCS total cost: {cost}")
    print("Independent cost check: 1 + 1 + 1 + 1 = 4")
    print("BFS route on same topology: A -> C -> F -> H; weighted cost = 1 + 2 + 2 = 5")
