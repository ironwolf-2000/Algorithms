from random import randint


def shuffle(nums: list[int]) -> None:
    """
    N = len(nums)
    -------------
    Time: O(N)
    Space: O(1)
    """
    for i in range(len(nums) - 1):
        j = randint(i, len(nums) - 1)
        nums[i], nums[j] = nums[j], nums[i]


nums = [1, 2, 3, 4, 5, 6]

shuffle(nums)
print(nums)
