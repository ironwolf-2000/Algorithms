# v1: recursive
def pow(x: float, n: int) -> float:
    """
    Time: O(logN)
    Space: O(logN)
    """
    if n < 0:
        return pow(1 / x, -n)
    if n == 0:
        return 1
    if n % 2:
        return x * pow(x, n - 1)
    return pow(x * x, n // 2)


# v2: iterative
def pow(x: float, n: int) -> float:
    """
    Time: O(logN)
    Space: O(1)
    """
    if n < 0:
        x, n = 1 / x, -n

    res = 1
    while n:
        if n % 2:
            res *= x
        x *= x
        n //= 2

    return res


print(pow(2, -3))  # 0.125
print(pow(5, 0))  # 1
print(pow(3, 3))  # 27
print(pow(1.25, 2))  # 1.5625
