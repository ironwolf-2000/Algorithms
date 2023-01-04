class KMP:
    @staticmethod
    def calculateLPS(pattern: str) -> list[int]:
        """
        M = len(pattern)
        -------------
        Time: O(M)
        Space: O(M)
        """
        lps = [0] * len(pattern)
        i = 0

        for j in range(1, len(pattern)):
            while i and pattern[j] != pattern[i]:
                i = lps[i - 1]

            if pattern[j] == pattern[i]:
                lps[j] = i + 1
                i += 1

        return lps

    @staticmethod
    def findMatches(text: str, pattern: str) -> list[int]:
        """
        N = len(text)
        M = len(pattern)
        -------------
        Time: O(N + M)
        Space: O(M)
        """
        if not pattern:
            return [0]

        lps = KMP.calculateLPS(pattern)
        res, i = [], 0

        for j in range(len(text)):
            while i and text[j] != pattern[i]:
                i = lps[i - 1]

            if text[j] == pattern[i]:
                i += 1

            if i == len(pattern):
                res.append(j - i + 1)
                i = lps[i - 1]

        return res


# Examples
if __name__ == "__main__":
    print(KMP.findMatches("aabxaayaab", "aab"))  # [0, 7]
    print(KMP.findMatches("abacababadac", "aba"))  # [0, 4, 6]
    print(KMP.findMatches("abxabcabcaby", "abcaby"))  # [6]
    print(KMP.findMatches("", "abab"))  # []
    print(KMP.findMatches("abc", ""))  # [0]
    print(KMP.findMatches("", ""))  # [0]
