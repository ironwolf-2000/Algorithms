# v1
def longestCommonSubsequence1(s1: str, s2: str) -> int:
    """
    M = len(s1)
    N = len(s2)
    -------------
    Time: O(MN)
    Space: O(MN)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# v2
def longestCommonSubsequence2(s1: str, s2: str) -> int:
    """
    M = len(s1)
    N = len(s2)
    -------------
    Time: O(MN)
    Space: O(min(M, N))
    """
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    m, n = len(s1), len(s2)
    dp = [0] * (n + 1)

    for i in range(1, m + 1):
        pre = 0
        for j in range(1, n + 1):
            cur = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = pre + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            pre = cur

    return dp[n]


print(longestCommonSubsequence1("abcba", "abcbcba"))  # 5
print(longestCommonSubsequence1("ezupkr", "ubmrapg"))  # 2

print(longestCommonSubsequence2("abcba", "abcbcba"))  # 5
print(longestCommonSubsequence2("ezupkr", "ubmrapg"))  # 2
