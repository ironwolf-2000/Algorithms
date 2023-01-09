from random import randint


# randomly selects k numbers from the stream where 0 < k < n
# n = len(stream) is either very large or unknown
def sample(stream: list[int], k: int) -> list[int]:
    """
    N = len(stream)
    -------------
    Time: O(N)
    Space: O(K)
    """
    reservoir = stream[:k]

    for i in range(k, len(stream)):
        j = randint(0, i)
        if j < k:
            reservoir[j] = stream[i]

    return reservoir


stream = [4, 3, 2, 5, 9, 6, 7, 1]
k = 3

print(sample(stream, k))
