from collections import defaultdict
from heapq import heappop, heappush
from math import inf


def dijkstra(G: list[list[tuple[int, int]]], start: int, end: int) -> int:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O((V + E) * logV)
    Space: O(V)
    """

    dist = defaultdict(lambda: inf)
    dist[start] = 0
    parent = defaultdict(int)  # only needed to restore the path
    parent[start] = -1

    q = [(0, start)]

    while q:
        d, u = heappop(q)
        for v, w in G[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                parent[v] = u
                heappush(q, (dist[v], v))

    if dist[end] == inf:
        return inf

    u, path = end, []
    while u != -1:
        path.append(u)
        u = parent[u]

    print(f"min_dist={dist[end]}: {'->'.join(str(el) for el in path[::-1])}")

    return dist[end]


# edge = [from, to, weight]
edges = [
    [1, 2, 6],
    [1, 3, 3],
    [1, 4, 8],
    [2, 1, 6],
    [2, 4, 1],
    [2, 5, 7],
    [3, 1, 3],
    [3, 4, 2],
    [4, 1, 8],
    [4, 2, 1],
    [4, 3, 2],
    [4, 5, 1],
    [5, 2, 7],
    [5, 4, 1],
    [6, 7, 5],
]

G = defaultdict(list)
for u, v, w in edges:
    G[u].append((v, w))

# min_dist=6: 1->3->4->5
print(dijkstra(G, 1, 5))  # 6

print(dijkstra(G, 1, 7))  # inf
