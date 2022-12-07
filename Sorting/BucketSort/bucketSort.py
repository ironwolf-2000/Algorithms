from math import ceil, isqrt


# good if the input list is mostly sorted
def insertionSort(nums: list[int]) -> None:
    for i, el in enumerate(nums):
        while i > 0 and el < nums[i - 1]:
            nums[i] = nums[i - 1]
            i -= 1
        nums[i] = el


def bucketSort(nums: list[int], n_buckets: int) -> None:
    """
    N = len(nums)
    K = number of buckets
    -------------
    Time (best): O(N + K)
    Time (worst): O(N^2)
    Space: O(N + K)
    """
    if not nums:
        return

    mn, mx = min(nums), max(nums)
    capacity = ceil((mx - mn + 1) / n_buckets)

    buckets = [[] for _ in range(n_buckets)]
    for el in nums:
        buckets[(el - mn) // capacity].append(el)

    i = 0
    for bucket in buckets:
        insertionSort(bucket)
        for el in bucket:
            nums[i] = el
            i += 1


nums1 = [3, 3, 3, 3]
nums2 = [4, -2, 3]
nums3 = [9, -2, 0, -3, 1, 5, 3, -1, 0]
nums4 = [5, 4, 3, 2, 1]

bucketSort(nums1, 2)
bucketSort(nums2, 3)
bucketSort(nums3, isqrt(len(nums3)))
bucketSort(nums4, 1)

print(nums1)  # [3, 3, 3, 3]
print(nums2)  # [-2, 3, 4]
print(nums3)  # [-3, -2, -1, 0, 0, 1, 3, 5, 9]
print(nums4)  # [1, 2, 3, 4, 5]
