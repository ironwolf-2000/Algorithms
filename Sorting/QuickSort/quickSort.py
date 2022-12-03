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


# slow if there are many duplicates
def _quickSort(nums: list[int], lo: int, hi: int) -> None:
    """
    N = len(nums)
    -------------
    Time (average): O(NlogN)
    Space (average): O(logN)
    """
    if lo >= hi:
        return

    partition_index = partition(nums, lo, hi)
    _quickSort(nums, lo, partition_index - 1)
    _quickSort(nums, partition_index + 1, hi)


def quickSort(nums: list[int]) -> None:
    _quickSort(nums, 0, len(nums) - 1)


nums1 = []
nums2 = [9, 1, 2, 4, 3, 1, 4, 5]
nums3 = [9, 2, 0, 3, 1, 5, 3, 1, 0]

quickSort(nums1)
quickSort(nums2)
quickSort(nums3)

print(nums1)  # []
print(nums2)  # [1, 1, 2, 3, 4, 4, 5, 9]
print(nums3)  # [0, 0, 1, 1, 2, 3, 3, 5, 9]
