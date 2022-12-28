from collections import deque


def getComponents(graph: dict[int, list[int]]) -> list[list[int]]:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    def bfs(start: int) -> None:
        q = deque([start])
        visited.add(start)
        components.append([start])

        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in visited:
                    q.append(v)
                    visited.add(v)
                    components[-1].append(v)

    visited = set()
    components = []

    for u in graph:
        if u not in visited:
            bfs(u)

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
