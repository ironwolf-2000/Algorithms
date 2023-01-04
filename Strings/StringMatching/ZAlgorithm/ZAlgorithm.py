class ZAlgorithm:
    @staticmethod
    def calculateZ(s: str) -> list[int]:
        """
        N + M = len(s)
        -------------
        Time: O(N + M)
        Space: O(N + M)
        """
        z = [0] * len(s)
        L, R = 0, 0

        for i in range(1, len(s)):
            if i + z[i - L] <= R:
                z[i] = z[i - L]
            else:
                L, R = i, max(R, i)
                while R < len(s) and s[R] == s[R - L]:
                    R += 1

                z[i] = R - L
                R -= 1

        return z

    @staticmethod
    def findMatches(text: str, pattern: str) -> list[int]:
        """
        N = len(text)
        M = len(pattern)
        -------------
        Time: O(N + M)
        Space: O(N + M)
        """
        if not pattern:
            return [0]

        z = ZAlgorithm.calculateZ(f"{pattern}${text}")
        res = []

        for i, el in enumerate(z):
            if el == len(pattern):
                res.append(i - el - 1)

        return res


# Examples
if __name__ == "__main__":
    print(ZAlgorithm.findMatches("aabxaayaab", "aab"))  # [0, 7]
    print(ZAlgorithm.findMatches("abacababadac", "aba"))  # [0, 4, 6]
    print(ZAlgorithm.findMatches("abxabcabcaby", "abcaby"))  # [6]
    print(ZAlgorithm.findMatches("", "abab"))  # []
    print(ZAlgorithm.findMatches("abc", ""))  # [0]
    print(ZAlgorithm.findMatches("", ""))  # [0]
