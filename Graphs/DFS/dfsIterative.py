def dfs(graph: dict[list[int]], start: int) -> list[int]:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """
    visited = {start}
    stack = [start]
    res = []

    while stack:
        u = stack.pop()
        res.append(u)

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)

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

print(dfs(G, 1))  # [1, 3, 5, 4, 2, 7, 6]
print(dfs(G, 3))  # [3, 5, 4, 2, 7, 6, 1]
