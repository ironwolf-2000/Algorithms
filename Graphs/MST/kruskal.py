# Note: alpha here refers to the Inverse Ackermann function.


class UnionFind:
    def __init__(self, n: int) -> None:
        """
        Time: O(N)
        Space: O(N)
        """
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        """
        Time: O(alpha(N))
        """
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def unite(self, x: int, y: int) -> None:
        """
        Time: O(alpha(N))
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1

    def connected(self, x: int, y: int) -> None:
        """
        Time: O(alpha(N))
        """
        return self.find(x) == self.find(y)


def kruskal(n: int, edges: list[list[int]]) -> list[list[int]]:
    """
    V = n = number of vertices in the graph
    E = len(edges)
    -------------
    Time: O(ElogE)
    Space: O(V + E)
    """
    uf = UnionFind(n + 1)
    mst = []

    for edge in sorted(edges, key=lambda x: x[2]):
        if not uf.connected(edge[0], edge[1]):
            uf.unite(edge[0], edge[1])
            mst.append(edge)

    print(f"Minimum Spanning Tree weight = {sum(el[2] for el in mst)}")

    return mst


# edge = [v0, v1, weight]
edges = [[1, 2, 3], [1, 5, 5], [2, 3, 5], [2, 5, 6], [3, 4, 9], [3, 6, 3], [4, 6, 7], [5, 6, 2]]
n = 6

print(kruskal(n, edges))  # [[5, 6, 2], [1, 2, 3], [3, 6, 3], [1, 5, 5], [4, 6, 7]]
