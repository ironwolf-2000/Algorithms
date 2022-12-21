# similar to math.isqrt
def sqrt(x: int) -> int:
    """
    Time: O(logN)
    Space: O(1)
    """
    lo, hi = 0, x

    while lo < hi:
        mi = (lo + hi + 1) // 2

        if mi * mi > x:
            hi = mi - 1
        else:
            lo = mi

    return lo


print(sqrt(0))  # 0
print(sqrt(1))  # 1
print(sqrt(2))  # 1
print(sqrt(5))  # 2
print(sqrt(9))  # 3
