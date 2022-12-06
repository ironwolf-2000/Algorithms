from bisect import bisect_left


def exponentialSearch(nums: list[int], target: int) -> int:
    """
    M - index of target in nums
    -------------
    Time: O(logM)
    Space: O(1)
    """
    end = 1
    while end < len(nums) and nums[end] < target:
        end *= 2

    return bisect_left(nums, target, end // 2, min(end, len(nums)))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7


# [1]
# [1, 2]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5, 6, 7, 8]: nums[end] > target
# Binary Search on [5, 6, 7, 8]
print(exponentialSearch(nums, target))  # 6


nums = [1, 3, 5, 7, 9]
target = 10


# [1]
# [1, 3]
# [1, 3, 5, 7]
# [1, 3, 5, 7, 9]: end > len(nums)
# Binary Search on [9]
print(exponentialSearch(nums, target))  # 5
