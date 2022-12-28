def isConnected(graph: dict[int, list[int]]) -> bool:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    def dfs(u: int) -> None:
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)

    visited = set()
    start = list(graph.keys())[0]

    dfs(start)

    return len(visited) == len(graph)


graph = {
    1: [3, 4],
    2: [5],
    3: [1, 4],
    4: [1, 3],
    5: [2],
}
print(isConnected(graph))  # False

graph = {
    1: [3, 4],
    2: [3, 5],
    3: [1, 2, 4],
    4: [1, 3],
    5: [2],
}
print(isConnected(graph))  # True
