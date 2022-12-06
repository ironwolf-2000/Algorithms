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


# similar to indexOf in other languages
def index(nums: list[int], target: int) -> int:
    """
    N = len(nums)
    -------------
    Time: O(logN)
    Space: O(1)
    """
    step = len(nums) // 2
    i = -1

    while step:
        while i + step < len(nums) and nums[i + step] < target:
            i += step
        step //= 2

    if i + 1 == len(nums) or nums[i + 1] != target:
        return -1

    return i + 1


nums = [1, 2, 3, 4, 7, 9]

print(bisectLeft(nums, 4))  # 3
print(bisectRight(nums, 4))  # 4

print(bisectLeft(nums, 0))  # 0
print(bisectRight(nums, 0))  # 0

print(bisectLeft(nums, 10))  # 6
print(bisectRight(nums, 10))  # 6

print("-------------------")

nums = [1, 2, 3, 3, 3, 4, 7, 9]

print(index(nums, 0))  # -1
print(index(nums, 1))  # 0
print(index(nums, 3))  # 2
print(index(nums, 9))  # 7
print(index(nums, 10))  # -1
