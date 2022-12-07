def merge(nums: list[int], A: list[int], B: list[int]) -> None:
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            nums[i + j] = A[i]
            i += 1
        else:
            nums[i + j] = B[j]
            j += 1

    while i < len(A):
        nums[i + j] = A[i]
        i += 1

    while j < len(B):
        nums[i + j] = B[j]
        j += 1


def mergeSort(nums: list[int]) -> None:
    """
    N = len(nums)
    -------------
    Time: O(NlogN)
    Space: O(N)
    """
    if len(nums) < 2:
        return

    mi = len(nums) // 2
    left = nums[:mi]
    right = nums[mi:]

    mergeSort(left)
    mergeSort(right)
    merge(nums, left, right)


nums1 = []
nums2 = [9, 1, 2, 4, 3, 1, 4, 5]
nums3 = [9, 2, 0, 3, 1, 5, 3, 1, 0]

mergeSort(nums1)
mergeSort(nums2)
mergeSort(nums3)

print(nums1)  # []
print(nums2)  # [1, 1, 2, 3, 4, 4, 5, 9]
print(nums3)  # [0, 0, 1, 1, 2, 3, 3, 5, 9]
