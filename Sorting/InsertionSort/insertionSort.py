def insertionSort(nums: list[int]) -> None:
    """
    N = len(nums)
    -------------
    Time: O(N^2)
    Space: O(1)
    """
    for i, el in enumerate(nums):
        while i > 0 and el < nums[i - 1]:
            nums[i] = nums[i - 1]
            i -= 1
        nums[i] = el


nums1 = []
nums2 = [9, 2, 0, 3, 1, 5, 3, 1, 0]
nums3 = [5, 4, 3, 2, 1]

insertionSort(nums1)
insertionSort(nums2)
insertionSort(nums3)

print(nums1)  # []
print(nums2)  # [0, 0, 1, 1, 2, 3, 3, 5, 9]
print(nums3)  # [1, 2, 3, 4, 5]
