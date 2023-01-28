from collections import Counter


def permute(nums: list[int]) -> list[list[int]]:
    """
    N = len(nums)
    ---------------
    Time: O(N! * N)
    Space: O(N), excluding output
    """

    def backtrack(cur: list[int], count: dict[int, int]) -> list[list[int]]:
        if len(cur) == len(nums):
            return [cur[:]]

        res = []

        for el in count:
            if count[el]:
                cur.append(el)
                count[el] -= 1

                res += backtrack(cur, count)

                count[el] += 1
                cur.pop()

        return res

    return backtrack([], Counter(nums))


print(permute([1, 1, 2]))  # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
