class ZAlgorithm:
    def calculate(self, s: str) -> list[int]:
        z = [0] * len(s)
        left = right = 0

        for i in range(1, len(s)):
            if i > right:
                left = right = i
                while right < len(s) and s[right] == s[right - left]:
                    right += 1
                z[i] = right - left
                right -= 1
            else:
                k = i - left
                if i + z[k] <= right:
                    z[i] = z[k]
                else:
                    left = i
                    while right < len(s) and s[right] == s[right - left]:
                        right += 1
                    z[i] = right - left
                    right -= 1

        return z

    def findMatches(self, text: str, pattern: str) -> list[int]:
        """
        N = len(text)
        M = len(pattern)
        -------------
        Time: O(N + M)
        Space: O(N + M)
        """
        z = self.calculate(f"{pattern}${text}")
        return [i - len(pattern) - 1 for i in range(len(z)) if z[i] == len(pattern)]


print(ZAlgorithm().findMatches("abaxabab", "aba"))  # [0, 4]
