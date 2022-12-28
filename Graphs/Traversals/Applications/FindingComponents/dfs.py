def getComponents(graph: dict[int, list[int]]) -> list[list[int]]:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    def dfs(u: int) -> None:
        visited.add(u)
        components[-1].append(u)

        for v in graph[u]:
            if v not in visited:
                dfs(v)

    visited = set()
    components = []

    for u in graph:
        if u not in visited:
            components.append([])
            dfs(u)

    return components


graph = {
    1: [3, 4],
    2: [5],
    3: [1, 4],
    4: [1, 3],
    5: [2],
    6: [],
}
print(getComponents(graph))  # [[1, 3, 4], [2, 5], [6]]
