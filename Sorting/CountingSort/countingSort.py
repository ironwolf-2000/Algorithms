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


nums1 = []
nums2 = [9, 2, 0, 3, 1, 5, 3, 1, 0]
nums3 = [5, 4, 3, 2, 1]

countingSort(nums1)
countingSort(nums2)
countingSort(nums3)

print(nums1)  # []
print(nums2)  # [0, 0, 1, 1, 2, 3, 3, 5, 9]
print(nums3)  # [1, 2, 3, 4, 5]
