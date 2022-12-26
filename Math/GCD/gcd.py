# v1: recursive
def _gcd(a: int, b: int) -> int:
    """
    Time: O(log(a + b))
    Space: O(log(a + b))
    """
    return a if not b else _gcd(b, a % b)


# v2: iterative
def _gcd(a: int, b: int) -> int:
    """
    Time: O(log(a + b))
    Space: O(1)
    """
    while b:
        a, b = b, a % b
    return a


# similar to math.gcd
def gcd(*values: int) -> int:
    """
    N = len(values)
    M = max(values)
    -------------
    Time: O(NlogM)
    Space: O(1)
    """
    res = 0
    for el in values:
        res = _gcd(res, el)
    return res

    # shorter syntax:
    # return reduce(_gcd, values, 0)


print(gcd(25, 50, 15))  # 5
print(gcd(38, 57))  # 19
print(gcd(4))  # 4
print(gcd())  # 0
