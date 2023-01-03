# v1: finds the sum of the largest subarray
def kadane1(nums: list[int]) -> int:
    """
    N = len(nums)
    -------------
    Time: O(N)
    Space: O(1)
    """
    mx, cur = nums[0], 0

    for el in nums:
        cur = max(cur, 0) + el
        mx = max(mx, cur)

    return mx


print(kadane1([1, 2, -3, 4]))  # 4
print(kadane1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6


# -----------------------------------------------------


# v2: returns the indices of the first largest subarray
def kadane2(nums: list[int]) -> tuple[int, int]:
    """
    N = len(nums)
    -------------
    Time: O(N)
    Space: O(1)
    """
    mx, cur = nums[0], 0
    L, R = 0, 0
    i = 0

    for j, el in enumerate(nums):
        cur += el
        if cur > mx:
            mx = cur
            L, R = i, j
        if cur <= 0:
            cur = 0
            i = j + 1

    return L, R


print(kadane2([1, 2, -3, 4]))  # (3, 3)
print(kadane2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # (3, 6)
