from collections import defaultdict


def isBipartite(graph: dict[list[int]]) -> bool:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    def dfs(u, c):
        color[u] = c
        for v in graph[u]:
            if color[v] == c or color[v] == -1 and not dfs(v, 1 - c):
                return False
        return True

    color = defaultdict(lambda: -1)

    return all(dfs(u, 0) for u in graph if color[u] == -1)


graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2],
}
print(isBipartite(graph))  # True

graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2],
}
print(isBipartite(graph))  # False
