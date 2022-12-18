from math import isqrt


# v1
def isPrime(n: int) -> bool:
    """
    -------------
    Time: O(sqrt(N))
    Space: O(1)
    """

    if n < 2:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False

    return True


# v2
def isPrime(n: int) -> bool:
    """
    -------------
    Time: O(sqrt(N))
    Space: O(1)
    """

    if n < 4:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


print(isPrime(-7))  # False
print(isPrime(1))  # False
print(isPrime(2))  # True
print(isPrime(17))  # True
print(isPrime(49))  # False
print(isPrime(10**9 + 7))  # True
