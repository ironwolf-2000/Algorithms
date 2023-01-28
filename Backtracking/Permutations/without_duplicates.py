def permute(nums: list[int]) -> list[list[int]]:
    """
    N = len(nums)
    ---------------
    Time: O(N! * N)
    Space: O(N), excluding output
    """

    def backtrack(cur: list, mask: int) -> list[list[int]]:
        if len(cur) == len(nums):
            return [cur[:]]

        res = []

        for i, el in enumerate(nums):
            if 1 << i & mask == 0:
                cur.append(el)
                res += backtrack(cur, 1 << i | mask)
                cur.pop()

        return res

    return backtrack([], 0)


nums = []
print(permute(nums))  # [[]]

nums = [1]
print(permute(nums))  # [[1]]

nums = [1, 2]
print(permute(nums))  # [[1,2], [2,1]]

nums = [1, 2, 3]
print(permute(nums))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
