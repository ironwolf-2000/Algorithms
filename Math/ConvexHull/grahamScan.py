from math import atan2


class GrahamScan:
    def polar_angle(self, p1: list[int], p2: list[int]) -> float:
        return atan2(p2[1] - p1[1], p2[0] - p1[0])

    def distSquared(self, p1: list[int], p2: list[int]) -> int:
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def orientation(self, p: list[int], q: list[int], r: list[int]) -> int:
        pq = [q[0] - p[0], q[1] - p[1]]
        qr = [r[0] - q[0], r[1] - q[1]]

        return qr[1] * pq[0] - qr[0] * pq[1]

    def sortPoints(self, points: list[list[int]]) -> None:
        p0 = min(points, key=lambda p: (p[1], p[0]))
        points.sort(key=lambda p: (self.polar_angle(p0, p), self.distSquared(p0, p)))

        i = len(points) - 1
        while i > 0 and self.orientation(p0, points[-1], points[i - 1]) == 0:
            i -= 1

        points[i:] = points[i:][::-1]

    def convexHull(self, points: list[list[int]]) -> list[list[int]]:
        """
        N = len(points)
        -------------
        Time: O(NlogN)
        Space: O(N)
        """
        self.sortPoints(points)
        hull = []

        for p in points:
            while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)

        return hull


points1 = [[2, 2], [2, 4], [2, 1], [2, 9], [2, 6]]
points2 = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
points3 = [[0, 0], [2, 2], [4, 4], [4, 0]]

print(GrahamScan().convexHull(points1))  # [[2, 9], [2, 6], [2, 4], [2, 2], [2, 1]]
print(GrahamScan().convexHull(points2))  # [[2, 0], [4, 2], [3, 3], [2, 4], [1, 1]]
print(GrahamScan().convexHull(points3))  # [[0, 0], [4, 0], [4, 4], [2, 2]]
