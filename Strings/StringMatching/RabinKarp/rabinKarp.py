class RabinKarp:
    @staticmethod
    def findMatches(text: str, pattern: str) -> list[int]:
        """
        N = len(text)
        M = len(pattern)
        -------------
        Time (average): O(M + N)
        Time (worst): O(MN)
        Space: O(1)
        """
        m, n = len(pattern), len(text)
        if m > n:
            return []
        if m == 0:
            return [0]

        base, mod = 256, 101
        res = []

        power = 1
        for _ in range(m - 1):
            power = (power * base) % mod

        p = 0
        for ch in pattern:
            p = (p * base + ord(ch)) % mod

        t = 0
        for i in range(m - 1):
            t = (t * base + ord(text[i])) % mod

        for i in range(n - m + 1):
            t = (t * base + ord(text[i + m - 1])) % mod

            if p == t:
                for j in range(m):
                    if text[i + j] != pattern[j]:
                        break
                else:
                    res.append(i)

            t -= power * ord(text[i])

        return res


# Examples
if __name__ == "__main__":
    print(RabinKarp.findMatches("aabxaayaab", "aab"))  # [0, 7]
    print(RabinKarp.findMatches("abacababadac", "aba"))  # [0, 4, 6]
    print(RabinKarp.findMatches("abxabcabcaby", "abcaby"))  # [6]
    print(RabinKarp.findMatches("", "abab"))  # []
    print(RabinKarp.findMatches("abc", ""))  # [0]
    print(RabinKarp.findMatches("", ""))  # [0]
