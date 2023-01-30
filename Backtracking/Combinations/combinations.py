# returns all possible combinations of k numbers chosen from the range [1, n]
def combine(n: int, k: int) -> list[list[int]]:
    """
    Time: O(C(n,k) * k), where C(n,k) is the binomial coefficient
    Space: O(k), excluding the output
    """

    def backtrack(i: int, cur: list[int]) -> list[list[int]]:
        if len(cur) == k:
            return [cur[:]]

        res = []

        for j in range(i, n + 1):
            cur.append(j)
            res += backtrack(j + 1, cur)
            cur.pop()

        return res

    return backtrack(1, [])


print(combine(3, 0))  # []
print(combine(3, 1))  # [[1], [2], [3]]
print(combine(3, 2))  # [[1, 2], [1, 3], [2, 3]]
print(combine(3, 3))  # [[1, 2, 3]]
