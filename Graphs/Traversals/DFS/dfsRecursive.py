def dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    def dfs(u: int) -> None:
        visited.add(u)
        res.append(u)

        for v in graph[u]:
            if v not in visited:
                dfs(v)

    visited = set()
    res = []
    dfs(start)

    return res


G = {
    1: [2, 3],
    2: [1, 3, 6, 7],
    3: [1, 2, 4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [2, 7],
    7: [2, 6],
}

print(dfs(G, 1))  # [1, 2, 3, 4, 5, 6, 7]
print(dfs(G, 3))  # [3, 1, 2, 6, 7, 4, 5]
