from math import isqrt


def getFactors(n: int) -> list[int]:
    """
    Time: O(sqrt(N))
    Space: O(1)
    """
    factors = []

    for i in range(2, isqrt(n) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 1:
        factors.append(n)

    return factors


print(getFactors(1))  # []
print(getFactors(3))  # [3]
print(getFactors(36))  # [2, 2, 3, 3]
print(getFactors(60))  # [2, 2, 3, 5]
