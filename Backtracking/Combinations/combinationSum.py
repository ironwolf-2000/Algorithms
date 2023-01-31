# Finds all unique combinations in nums where the elements sum to target.
# Each number in nums may only be used once in the combination.
def combinationSum(nums: list[int], target: int) -> list[list[int]]:
    """
    N = len(nums)
    ---------------
    Time: O(N * 2^N)
    Space: O(N), excluding the output
    """

    def backtrack(i: int, sm: int, cur: list[int]) -> list[list[int]]:
        if sm == target and cur:
            return [cur[:]]

        res = []

        for j in range(i, len(nums)):
            if j == i or nums[j] != nums[j - 1]:
                cur.append(nums[j])
                res += backtrack(j + 1, sm + nums[j], cur)
                cur.pop()

        return res

    nums.sort()
    return backtrack(0, 0, [])


nums = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum(nums, target))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]


nums = [-3, -1, 0, 2, 4]
target = 0
print(combinationSum(nums, target))  # [[-3, -1, 0, 4], [-3, -1, 4], [0]]
