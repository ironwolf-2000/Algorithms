from collections import defaultdict
from math import inf


def shortestPaths(G: dict[int, list[tuple[int, int]]]) -> list[list[float | int]] | None:
    """
    V = number of vertices in the graph
    E = len(edges)
    -------------
    Time: O(V^3)
    Space: O(V^2)
    """

    n = len(G)
    dist = [[inf] * n for _ in range(n)]

    for u in G:
        dist[u][u] = 0
        for v, w in G[u]:
            dist[u][v] = w

    for x in range(n):
        for u in range(n):
            for v in range(n):
                dist[u][v] = min(dist[u][v], dist[u][x] + dist[x][v])
                if u == v and dist[u][v] < 0:
                    print("The graph contains a negative cycle.")
                    return

    return dist


# Example 1: undirected graph
edges = [(0, 1, 5), (0, 3, 9), (0, 4, 1), (1, 2, 2), (2, 3, 7), (3, 4, 2)]

G = defaultdict(list)
for u, v, w in edges:
    G[u].append((v, w))
    G[v].append((u, w))

print(shortestPaths(G))


# Example 2: directed graph
edges = [(0, 1, 4), (0, 3, 5), (1, 3, 5), (2, 1, -8), (3, 2, 3)]

G = defaultdict(list)
for u, v, w in edges:
    G[u].append((v, w))

print(shortestPaths(G))


# Example 3: directed graph with a negative cycle
edges = [(2, 1, -11), (3, 2, 3), (0, 3, 5), (0, 1, 4), (1, 3, 5)]

G = defaultdict(list)
for u, v, w in edges:
    G[u].append((v, w))

print(shortestPaths(G))
