from math import isqrt


def jumpSearch(nums: list[int], target: int) -> int:
    """
    N = len(nums)
    -------------
    Time: O(sqrt(N))
    Space: O(1)
    """

    step = isqrt(len(nums))
    i = 0

    while i + step < len(nums) and nums[i + step - 1] < target:
        i += step

    for j in range(i, min(i + step, len(nums))):
        if nums[j] == target:
            return j

    return -1


print(jumpSearch([2, 4, 6, 11, 13, 14, 19, 20, 27], 27))  # 8
print(jumpSearch([2, 4, 6, 11, 13, 14, 19, 20, 27], 13))  # 4
print(jumpSearch([2, 4], 1))  # -1
print(jumpSearch([], 3))  # -1
