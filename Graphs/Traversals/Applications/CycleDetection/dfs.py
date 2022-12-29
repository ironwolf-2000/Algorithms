from collections import defaultdict


# v1: for undirected simple graphs
def hasCycleU(graph: dict[int, list[int]]) -> bool:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    def dfs(u: int, p: int) -> bool:
        visited.add(u)

        for v in graph[u]:
            if v != p and (v in visited or dfs(v, u)):
                return True

        return False

    visited = set()
    return any(dfs(u, u) for u in graph if u not in visited)


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

    def dfs(u: int) -> bool:
        color[u] = 1

        for v in graph[u]:
            if color[v] == 1 or color[v] == 0 and dfs(v):
                return True

        color[u] = 2
        return False

    color = defaultdict(int)
    return any(dfs(u) for u in graph if color[u] == 0)


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
