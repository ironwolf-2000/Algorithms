# v1
def bubbleSort(nums: list[int]) -> None:
    """
    N = len(nums)
    -------------
    Time: O(N^2)
    Space: O(1)
    """
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# v2
def bubbleSort(nums: list[int]) -> None:
    """
    N = len(nums)
    -------------
    Time: O(N^2)
    Space: O(1)
    """
    for i in range(len(nums)):
        is_sorted = True
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_sorted = False
        if is_sorted:
            break


nums1 = []
nums2 = [4, 1, 4, 1, 3]
nums3 = [9, 1, 2, 3, 4, 5]

bubbleSort(nums1)
bubbleSort(nums2)
bubbleSort(nums3)

print(nums1)  # []
print(nums2)  # [1, 1, 3, 4, 4]
print(nums3)  # [1, 2, 3, 4, 5, 9]
