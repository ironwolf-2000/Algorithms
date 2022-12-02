def selectionSort(nums: list[int]) -> None:
    """
    N = len(nums)
    -------------
    Time: O(N^2)
    Space: O(1)
    """
    for i in range(len(nums) - 1):
        mn_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[mn_index]:
                mn_index = j
        nums[i], nums[mn_index] = nums[mn_index], nums[i]


nums1 = []
nums2 = [9, 1, 2, 4, 3, 1, 4, 5]
nums3 = [9, 2, 0, 3, 1, 5, 3, 1, 0]

selectionSort(nums1)
selectionSort(nums2)
selectionSort(nums3)

print(nums1)  # []
print(nums2)  # [1, 1, 2, 3, 4, 4, 5, 9]
print(nums3)  # [0, 0, 1, 1, 2, 3, 3, 5, 9]
