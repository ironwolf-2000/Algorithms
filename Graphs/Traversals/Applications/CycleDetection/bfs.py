from collections import defaultdict, deque


# v1: for undirected simple graphs
def hasCycleU(graph: dict[int, list[int]]) -> bool:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    def bfs(start: int) -> bool:
        q = deque([(start, start)])
        visited.add(start)

        while q:
            u, p = q.popleft()

            for v in graph[u]:
                if v not in visited:
                    q.append((v, u))
                    visited.add(v)
                elif v != p:
                    return True

        return False

    visited = set()
    return any(bfs(u) for u in graph if u not in visited)


graph = {
    1: [2],
    2: [1, 3, 4],
    3: [2, 4],
    4: [2, 3],
}
print(hasCycleU(graph))  # True

graph = {
    1: [2],
    2: [1, 3, 5, 6],
    3: [2, 4],
    4: [3],
    5: [2],
    6: [2],
}
print(hasCycleU(graph))  # False


# ------------------------------------------------


# v2: for directed graphs
def hasCycleD(graph: dict[int, list[int]]) -> bool:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    indegree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque([u for u in graph if indegree[u] == 0])

    while q:
        u = q.popleft()
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return any(indegree.values())


graph = {
    1: [2],
    2: [3],
    3: [1, 4],
    4: [],
}
print(hasCycleD(graph))  # True

graph = {
    1: [],
    2: [1, 4],
    3: [1],
    4: [3],
}
print(hasCycleD(graph))  # False
