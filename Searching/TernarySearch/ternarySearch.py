def ternarySearch(nums: list[int], target: int) -> int:
    """
    N = len(nums)
    -------------
    Time: O(logN)
    Space: O(1)
    """
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        partition_size = (hi - lo) // 3
        mid1 = lo + partition_size
        mid2 = hi - partition_size

        if nums[mid1] == target:
            return mid1
        if nums[mid2] == target:
            return mid2

        if target < nums[mid1]:
            hi = mid1 - 1
        elif target > nums[mid2]:
            lo = mid2 + 1
        else:
            lo = mid1 + 1
            hi = mid2 - 1

    return -1


nums = [1, 2, 3, 3, 3, 4, 7, 9]

print(ternarySearch(nums, 0))  # -1
print(ternarySearch(nums, 1))  # 0
print(ternarySearch(nums, 3))  # 2
print(ternarySearch(nums, 9))  # 7
print(ternarySearch(nums, 10))  # -1
