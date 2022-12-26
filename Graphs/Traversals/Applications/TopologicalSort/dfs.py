from collections import defaultdict


def topsort(graph: dict[int, list[int]]) -> list[int]:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(V + E)
    Space: O(V)
    """

    def dfs(u: int) -> bool:
        color[u] = 1  # visited

        for v in graph[u]:
            if color[v] == 1 or not color[v] and dfs(v):
                return True  # cycle found

        color[u] = 2  # fully explored
        res.append(u)

        return False  # no cycle found

    color = defaultdict(int)
    res = []

    for u in graph:
        if not color[u] and dfs(u):
            print("Cycle found!")
            return []

    return res[::-1]


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
print(topsort(graph))  # [7, 6, 5, 1, 2, 4, 8, 3]

graph = {
    1: [2],
    2: [3],
    3: [1],
}
print(topsort(graph))  # []
