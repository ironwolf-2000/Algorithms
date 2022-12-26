from math import isqrt


# finds all prime numbers < n
def findPrimes(n: int) -> list[int]:
    """
    Time: O(Nlog(logN))
    Space: O(N)
    """

    if n < 2:
        return []

    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, isqrt(n) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return [i for i in range(n) if primes[i]]


print(findPrimes(1))  # []
print(findPrimes(11))  # [2, 3, 5, 7]
print(findPrimes(50))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
