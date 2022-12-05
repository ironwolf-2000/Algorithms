# similar to bisect.bisect_left
def bisectLeft(nums: list[int], target: int) -> int:
    """
    N = len(nums)
    -------------
    Time: O(logN)
    Space: O(1)
    """
    lo, hi = 0, len(nums)
    while lo < hi:
        mi = (lo + hi) // 2
        if nums[mi] < target:
            lo = mi + 1
        else:
            hi = mi
    return lo


# similar to bisect.bisect_right
def bisectRight(nums: list[int], target: int) -> int:
    """
    N = len(nums)
    -------------
    Time: O(logN)
    Space: O(1)
    """
    lo, hi = 0, len(nums)
    while lo < hi:
        mi = (lo + hi) // 2
        if nums[mi] <= target:
            lo = mi + 1
        else:
            hi = mi
    return lo


nums = [1, 2, 3, 4, 7, 9]

print(bisectLeft(nums, 4))  # 3
print(bisectRight(nums, 4))  # 4

print(bisectLeft(nums, 0))  # 0
print(bisectRight(nums, 0))  # 0

print(bisectLeft(nums, 10))  # 6
print(bisectRight(nums, 10))  # 6
