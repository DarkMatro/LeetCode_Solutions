from itertools import pairwise

def hasIncreasingSubarrays(nums: list[int], k: int) -> bool:
    """
    ID: 3349
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array nums of n integers and an integer k, determine whether there exist two adjacent
    subarrays of length k such that both subarrays are strictly increasing. Specifically, check if
    there are two subarrays starting at indices a and b (a < b), where:

    Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
    The subarrays must be adjacent, meaning b = a + k.
    Return true if it is possible to find two such subarrays, and false otherwise.

    Parameters
    ----------
    nums: list[int]

    k: int

    Returns
    -------
    bool

    Examples
    --------
    >>> hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3)
    True

    Explanation:

    The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
    The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
    These two subarrays are adjacent, so the result is true.

    >>> hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5)
    False
    """
    for i in range(0, len(nums) - 2 * k + 1):
        if all(a < b for a, b in pairwise(nums[i:i + k])) and all(
                a < b for a, b in pairwise(nums[i + k:i + 2 * k])):
            return True
    return False
