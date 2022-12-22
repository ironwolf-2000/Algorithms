from collections import defaultdict, deque


def isBipartite(graph: dict[list[int]]) -> bool:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """
    color = defaultdict(lambda: -1)

    for u in graph:
        if color[u] != -1:
            continue

        q = deque([(u, 0)])
        color[u] = 0

        while q:
            u, c = q.popleft()

            for v in graph[u]:
                if color[v] == c:
                    return False

                if color[v] == -1:
                    q.append((v, 1 - c))
                    color[v] = 1 - c

    return True


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
