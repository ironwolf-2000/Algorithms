def countingSort(nums: list[int], k: int, pos: int) -> None:
    """
    N = len(nums)
    K = the base of representing numbers
    -------------
    Time: O(N + K)
    Space: O(N + K)
    """
    indices = [0] * k
    res = [0] * len(nums)

    for el in nums:
        indices[el // pos % k] += 1

    sm = 0
    for i, el in enumerate(indices):
        indices[i] = sm
        sm += el

    for el in nums:
        d = el // pos % k
        res[indices[d]] = el
        indices[d] += 1

    nums[:] = res


def radixSort(nums: list[int]) -> None:
    """
    N = len(nums)
    W = max number of digits of nums[i]
    K = the base of representing numbers
    -------------
    Time: O(W * (N + K))
    Space: O(N + K)
    """
    if not nums:
        return

    mn = min(nums)
    nums[:] = [el - mn for el in nums]
    mx = max(nums)

    k, pos = 10, 1

    while pos <= mx:
        countingSort(nums, k, pos)
        pos *= k

    nums[:] = [el + mn for el in nums]


nums1 = [256, 336, 36, 443, 831, 9, 11]
nums2 = [11, 100, 100, 12, 0]
nums3 = [-1, 2, -8, -10]
nums4 = []

radixSort(nums1)
radixSort(nums2)
radixSort(nums3)
radixSort(nums4)

print(nums1)  # [9, 11, 36, 256, 336, 443, 831]
print(nums2)  # [0, 11, 12, 100, 100]
print(nums3)  # [-10, -8, -1, 2]
print(nums4)  # []
