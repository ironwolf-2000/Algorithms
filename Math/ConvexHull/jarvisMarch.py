class JarvisMarch:
    def orientation(self, p: list[int], q: list[int], r: list[int]) -> int:
        pq = [q[0] - p[0], q[1] - p[1]]
        qr = [r[0] - q[0], r[1] - q[1]]

        return qr[1] * pq[0] - qr[0] * pq[1]

    def onSegment(self, p: list[int], q: list[int], r: list[int]) -> bool:
        return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

    # doesn't preserve the order of traversal
    def convexHull(self, points: list[list[int]]) -> list[list[int]]:
        """
        N = len(points)
        M = number of points in the output
        -------------
        Time: O(MN)
        Space: O(M)
        """
        if len(points) < 4:
            return points

        points = [tuple(point) for point in points]
        hull = set()
        i0 = points.index(min(points))
        i, j = i0, None

        while j != i0:
            j = (i + 1) % len(points)
            collinear_points = []

            for k in range(len(points)):
                val = self.orientation(points[i], points[j], points[k])
                if val > 0:
                    j = k
                    collinear_points.clear()
                elif val == 0:
                    if self.onSegment(points[i], points[j], points[k]):
                        collinear_points.append(points[j])
                        j = k
                    else:
                        collinear_points.append(points[k])

            for point in collinear_points:
                hull.add(point)
            hull.add(points[j])

            i = j

        return [list(point) for point in hull]


points1 = [[2, 2], [2, 4], [2, 1], [2, 9], [2, 6]]
points2 = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
points3 = [[0, 0], [2, 2], [4, 4], [4, 0]]

print(JarvisMarch().convexHull(points1))  # [[2, 4], [2, 1], [2, 9], [2, 6], [2, 2]]
print(JarvisMarch().convexHull(points2))  # [[2, 4], [1, 1], [2, 0], [4, 2], [3, 3]]
print(JarvisMarch().convexHull(points3))  # [[4, 4], [4, 0], [2, 2], [0, 0]]
