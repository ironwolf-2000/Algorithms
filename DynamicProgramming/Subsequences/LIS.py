from bisect import bisect_left


# v1
def lengthOfLIS1(nums: list[int]) -> int:
    """
    N = len(nums)
    -------------
    Time: O(N^2)
    Space: O(N)
    """
    dp = [1] * len(nums)

    for j, el in enumerate(nums):
        for i in range(j):
            if nums[i] < el:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)


# v2: patience sorting
def lengthOfLIS2(nums: list[int]) -> int:
    """
    N = len(nums)
    -------------
    Time: O(NlogN)
    Space: O(N)
    """
    sub = []

    for el in nums:
        if not sub or el > sub[-1]:
            sub.append(el)
        elif el < sub[-1]:
            sub[bisect_left(sub, el)] = el

    return len(sub)


print(lengthOfLIS1([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(lengthOfLIS1([7, 7, 7, 7, 7]))  # 1

print(lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(lengthOfLIS2([7, 7, 7, 7, 7]))  # 1
