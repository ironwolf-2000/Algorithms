def merge(nums: list[int], lo: int, mi: int, hi: int) -> None:
    nums_copy = nums[:]
    i, j = lo, mi
    k = lo

    while i < mi and j < hi:
        if nums_copy[i] < nums_copy[j]:
            nums[k] = nums_copy[i]
            i += 1
        else:
            nums[k] = nums_copy[j]
            j += 1
        k += 1

    while i < mi:
        nums[k] = nums_copy[i]
        i += 1
        k += 1

    while j < hi:
        nums[k] = nums_copy[j]
        j += 1
        k += 1


def mergeSort(nums: list[int]) -> None:
    """
    N = len(nums)
    -------------
    Time: O(NlogN)
    Space: O(N)
    """
    span = 1

    while span < len(nums):
        for lo in range(0, len(nums), span * 2):
            mi = min(lo + span, len(nums))
            hi = min(lo + span * 2, len(nums))
            merge(nums, lo, mi, hi)

        span *= 2


# nums1 = []
# nums2 = [9, 1, 2, 4, 3, 1, 4, 5]
nums3 = [9, 2, 0, 3, 1, 5, 3, 1, 0]

# mergeSort(nums1)
# mergeSort(nums2)
mergeSort(nums3)

# print(nums1)  # []
# print(nums2)  # [1, 1, 2, 3, 4, 4, 5, 9]
print(nums3)  # [0, 0, 1, 1, 2, 3, 3, 5, 9]
