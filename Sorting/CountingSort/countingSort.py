# v1: for non-negative integers
def countingSort(nums: list[int]) -> None:
    """
    N = len(nums)
    K = max(nums)
    -------------
    Time: O(N + K)
    Space: O(K)
    """
    count = [0] * (max(nums, default=-1) + 1)
    for num in nums:
        count[num] += 1

    i = 0
    for num, freq in enumerate(count):
        for _ in range(freq):
            nums[i] = num
            i += 1


# v2: for both positive and negative integers
def countingSort(nums: list[int]) -> None:
    """
    N = len(nums)
    K = max(nums) - min(nums)
    -------------
    Time: O(N + K)
    Space: O(K)
    """
    if not nums:
        return

    mn, mx = min(nums), max(nums)

    count = [0] * (mx - mn + 1)
    for num in nums:
        count[num - mn] += 1

    i = 0
    for num, freq in enumerate(count):
        for _ in range(freq):
            nums[i] = num + mn
            i += 1


nums1 = []
nums2 = [4, -4]
nums3 = [9, -2, 0, -3, 1, 5, 3, -1, 0]
nums4 = [5, 4, 3, 2, 1]

countingSort(nums1)
countingSort(nums2)
countingSort(nums3)
countingSort(nums4)

print(nums1)  # []
print(nums2)  # [-4, 4]
print(nums3)  # [-3, -2, -1, 0, 0, 1, 3, 5, 9]
print(nums4)  # [1, 2, 3, 4, 5]
