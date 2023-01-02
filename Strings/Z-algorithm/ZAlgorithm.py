class ZAlgorithm:
    def calculateZ(self, s: str) -> list[int]:
        """
        N + M = len(s)
        -------------
        Time: O(N + M)
        Space: O(N + M)
        """
        z = [0] * len(s)
        L, R = 0, 0

        for j in range(1, len(s)):
            if j + z[j - L] <= R:
                z[j] = z[j - L]
            else:
                L, R = j, max(R, j)
                while R < len(s) and s[R] == s[R - L]:
                    R += 1

                z[j] = R - L
                R -= 1

        return z

    def findMatches(self, text: str, pattern: str) -> list[int]:
        """
        N = len(text)
        M = len(pattern)
        -------------
        Time: O(N + M)
        Space: O(N + M)
        """
        if not pattern:
            return [0]

        z = self.calculateZ(f"{pattern}${text}")
        res = []

        for i, el in enumerate(z):
            if el == len(pattern):
                res.append(i - el - 1)

        return res


print(ZAlgorithm().findMatches("aabxaayaab", "aab"))  # [0, 7]
print(ZAlgorithm().findMatches("abacababadac", "aba"))  # [0, 4, 6]
print(ZAlgorithm().findMatches("abxabcabcaby", "abcaby"))  # [6]
print(ZAlgorithm().findMatches("ababab", "abab"))  # [0, 2]
