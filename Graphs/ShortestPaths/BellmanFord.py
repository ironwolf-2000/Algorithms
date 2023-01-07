from collections import defaultdict
from math import inf


# for directed graphs
def shortestPath(n: int, edges: list[tuple[int, int, int]], src: int, dst: int) -> float | int | None:
    """
    V = n = number of vertices in the graph
    E = len(edges)
    -------------
    Time: O(VE)
    Space: O(V)
    """

    dist = defaultdict(lambda: inf)
    dist[src] = 0
    relaxed = False
    cnt = 0

    while not cnt or relaxed:
        relaxed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                relaxed = True
                dist[v] = dist[u] + w
        cnt += 1
        if cnt == n:
            print("The graph contains a negative cycle.")
            return

    return dist[dst]


edges = [(3, 2, -11), (4, 3, 3), (1, 4, 5), (1, 2, 4), (2, 4, 5)]
print(shortestPath(4, edges, 1, 2))  # None

edges = [(1, 3, 3), (1, 2, 5), (1, 4, 7), (3, 4, -1), (2, 4, 1), (2, 6, 2), (4, 6, 2)]
print(shortestPath(5, edges, 1, 6))  # 4
