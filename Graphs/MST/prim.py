from heapq import heappop, heappush


def prim(graph: dict[int, list[tuple[int, int]]]) -> list[list[int]]:
    """
    V = number of vertices in the graph
    E = number of edges in the graph
    -------------
    Time: O(ElogV)
    Space: O(V + E)
    """

    n = len(graph)  # number of vertices
    start = 1

    h = [(w, start, v) for v, w in graph[start]]
    selected = [False] * (n + 1)
    selected[start] = True

    mst = []

    while len(mst) < n - 1:
        w, u, v = heappop(h)
        if selected[v]:
            continue

        selected[v] = True
        mst.append([u, v, w])

        for x, xw in graph[v]:
            if not selected[x]:
                heappush(h, (xw, v, x))

    print(f"Minimum Spanning Tree weight = {sum(el[2] for el in mst)}")

    return mst


# G[from] = list[tuple[to, weight]]
G = {
    1: [(2, 3), (5, 5)],
    2: [(1, 3), (3, 5), (5, 6)],
    5: [(1, 5), (2, 6), (6, 2)],
    3: [(2, 5), (4, 9), (6, 3)],
    4: [(3, 9), (6, 7)],
    6: [(3, 3), (4, 7), (5, 2)],
}

print(prim(G))  # [[1, 2, 3], [1, 5, 5], [5, 6, 2], [6, 3, 3], [6, 4, 7]]
