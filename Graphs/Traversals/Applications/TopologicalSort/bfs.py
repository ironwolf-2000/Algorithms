from collections import defaultdict, deque


# Also known as Kahn's algorithm
def topsort(graph: dict[int, list[int]]) -> list[int]:
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
    res = []

    while q:
        u = q.popleft()
        res.append(u)

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if any(indegree.values()):
        print("Cycle found!")
        return []

    return res


graph = {
    1: [2, 4],
    2: [4],
    3: [],
    4: [3, 8],
    5: [],
    6: [5],
    7: [],
    8: [],
}
print(topsort(graph))  # [1, 6, 7, 2, 5, 4, 3, 8]

graph = {
    1: [2],
    2: [3],
    3: [1],
}
print(topsort(graph))  # []
