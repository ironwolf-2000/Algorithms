class NegativeBase:
    def __init__(self, base: int, num: list[int]) -> None:
        """
        val: number in decimal base
        base: target negative base
        """
        self._base = base
        self._num = num
        self._decimal_num = self._to_decimal(num)

    @property
    def num(self):
        return self._num

    @property
    def decimal_num(self):
        return self._decimal_num

    def _to_initial(self, val: int) -> list[int]:
        res = []

        while val:
            val, r = divmod(val, self._base)
            if r < 0:
                val += 1
                r -= self._base

            res.append(r)

        return res[::-1] or [0]

    def _to_decimal(self, num: list[int]) -> int:
        res = 0

        for x in num:
            res = res * self._base + x

        return res

    def _add(self, A: list[int], B: list[int]) -> list[int]:
        res = []
        carry = 0

        while A or B or carry:
            d1, d2 = (A or [0]).pop(), (B or [0]).pop()
            sm = d1 + d2 + carry
            d = sm % -self._base

            res.append(d)
            carry = (sm - d) // self._base

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return res[::-1]

    def __add__(self, other: "NegativeBase") -> "NegativeBase":
        A = self.num[:]
        B = other.num[:]

        return NegativeBase(self._base, self._add(A, B))

    def __sub__(self, other: "NegativeBase") -> "NegativeBase":
        A = self.num[:]
        B = [-el for el in other.num]

        return NegativeBase(self._base, self._add(A, B))


# Representation
nb1 = NegativeBase(-10, [1, 2, 2, 4, 3])
print(nb1.decimal_num)  # 8163

nb2 = NegativeBase(-10, [9, 9, 7, 7])
print(nb2.decimal_num)  # -8163

nb3 = NegativeBase(-10, [1, 2, 3])  # 83
print(nb3.decimal_num)


# Addition
print((nb1 + nb2).decimal_num)  # 0
print((nb1 + nb3).decimal_num)  # 8246
print((nb2 + nb3).decimal_num)  # -8080


# Subtraction
print((nb1 - nb2).decimal_num)  # 16326
print((nb1 - nb3).decimal_num)  # 8080
print((nb2 - nb3).decimal_num)  # -8246
