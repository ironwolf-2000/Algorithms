from math import gcd


def _lcm(a: int, b: int):
    """
    Time: O(log(a + b))
    Space: O(1)
    """
    return a * b // gcd(a, b)


# similar to math.lcm
def lcm(*values: int):
    """
    N = len(values)
    M = max(values)
    -------------
    Time: O(NlogM)
    Space: O(1)
    """
    res = 1
    for el in values:
        res = _lcm(res, el)
    return res

    # shorter syntax:
    # return reduce(_lcm, values, 1)


print(lcm(25, 50, 15))  # 150
print(lcm(38, 57))  # 114
print(lcm(4))  # 4
print(lcm())  # 1
