class MonotoneChain:
    def orientation(self, p: list[int], q: list[int], r: list[int]) -> int:
        pq = [q[0] - p[0], q[1] - p[1]]
        qr = [r[0] - q[0], r[1] - q[1]]

        return qr[1] * pq[0] - qr[0] * pq[1]

    def getHalfHull(self, points: list[list[int]]) -> list[tuple[int, int]]:
        hull = []
        for p in points:
            while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(tuple(p))
        return hull

    def convexHull(self, points: list[list[int]]) -> list[tuple[int, int]]:
        """
        N = len(points)
        -------------
        Time: O(NlogN)
        Space: O(N)
        """
        points.sort()

        lower = self.getHalfHull(points)
        upper = self.getHalfHull(points[::-1])

        return list(set(lower + upper))


points1 = [[2, 2], [2, 4], [2, 1], [2, 9], [2, 6]]
points2 = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
points3 = [[0, 0], [2, 2], [4, 4], [4, 0]]

print(MonotoneChain().convexHull(points1))  # [(2, 4), (2, 1), (2, 9), (2, 6), (2, 2)]
print(MonotoneChain().convexHull(points2))  # [(2, 4), (1, 1), (2, 0), (4, 2), (3, 3)]
print(MonotoneChain().convexHull(points3))  # [(4, 4), (4, 0), (2, 2), (0, 0)]
