class NegativeBase:
    def __init__(self, base: int, val: int) -> None:
        """
        val: number in decimal base
        base: target negative base
        """
        self._base = base
        self._num = self._encode(val)

    @property
    def num(self):
        return self._num

    def _encode(self, val: int) -> list[int]:
        res = []

        while val:
            val, r = divmod(val, self._base)
            if r < 0:
                val += 1
                r -= self._base

            res.append(r)

        return res[::-1] or [0]

    def decode(self) -> int:
        res = 0

        for x in self._num:
            res = res * self._base + x

        return res


nb = NegativeBase(-10, 8163)
nb = NegativeBase(-10, -8163)
nb = NegativeBase(-10, 0)

print(nb.decode())
