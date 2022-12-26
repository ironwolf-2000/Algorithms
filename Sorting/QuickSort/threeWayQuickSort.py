import random


def partition(nums: list[int], lo: int, hi: int) -> tuple[int, int]:
    pivot = nums[random.randint(lo, hi)]
    i, j, k = lo, lo, hi

    while j <= k:
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] > pivot:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        else:
            j += 1

    return i, j


def _quickSort(nums: list[int], lo: int, hi: int) -> None:
    """
    N = len(nums)
    -------------
    Time (average): O(NlogN)
    Space (average): O(logN)
    """
    if lo >= hi:
        return

    pi1, pi2 = partition(nums, lo, hi)
    _quickSort(nums, lo, pi1 - 1)
    _quickSort(nums, pi2, hi)


def quickSort(nums: list[int]) -> None:
    _quickSort(nums, 0, len(nums) - 1)


nums1 = []
nums2 = [9, 1, 2, 4, 3, 1, 4, 5]
nums3 = [9, 2, 0, 5, 5, 5, 3, 5, 5, 3]

quickSort(nums1)
quickSort(nums2)
quickSort(nums3)

print(nums1)  # []
print(nums2)  # [1, 1, 2, 3, 4, 4, 5, 9]
print(nums3)  # [0, 2, 3, 3, 5, 5, 5, 5, 5, 9]
