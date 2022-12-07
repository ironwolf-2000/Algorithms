import random


def partition(nums: list[int], lo: int, hi: int) -> int:
    random_index = random.randint(lo, hi)
    nums[random_index], nums[hi] = nums[hi], nums[random_index]
    k = lo

    for i in range(lo, hi + 1):
        if nums[i] <= nums[hi]:
            nums[i], nums[k] = nums[k], nums[i]
            k += 1

    return k - 1


def _quickSelect(nums: list[int], k: int, lo: int, hi: int) -> None:
    """
    N = len(nums)
    -------------
    Time (average): O(N)
    Space (average): O(logN)
    """
    if lo > hi:
        return None

    partition_index = partition(nums, lo, hi)

    if partition_index < k:
        return _quickSelect(nums, k, partition_index + 1, hi)
    if partition_index > k:
        return _quickSelect(nums, k, lo, partition_index - 1)

    return nums[partition_index]


# finds the k-th smallest value in nums
def quickSelect(nums: list[int], k: int) -> int:
    return _quickSelect(nums, k, 0, len(nums) - 1)


print(quickSelect([4, 3, 4, 2, 1], 0))  # 1
print(quickSelect([4, 3, 4, 2, 1], 1))  # 2
print(quickSelect([4, 3, 4, 2, 1], 2))  # 3
print(quickSelect([4, 3, 4, 2, 1], 3))  # 4
print(quickSelect([4, 3, 4, 2, 1], 4))  # 4
print(quickSelect([4, 3, 4, 2, 1], 5))  # None
