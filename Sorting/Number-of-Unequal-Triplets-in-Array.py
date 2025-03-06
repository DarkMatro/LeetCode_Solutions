from collections import Counter
from itertools import accumulate


def unequalTriplets(nums: list[int]) -> int:
    """
    ID: 2475
    Tags:   Array, Hash Table, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k)
    that meet the following conditions:

    0 <= i < j < k < nums.length
    nums[i], nums[j], and nums[k] are pairwise distinct.
    In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
    Return the number of triplets that meet the conditions.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> unequalTriplets([4,4,2,4,3])
    3

    Explanation: The following triplets meet the conditions:
    - (0, 2, 4) because 4 != 2 != 3
    - (1, 2, 4) because 4 != 2 != 3
    - (2, 3, 4) because 2 != 4 != 3
    Since there are 3 triplets, we return 3.
    Note that (2, 0, 4) is not a valid triplet because 2 > 0.

    >>> unequalTriplets([1,1,1,1,1])
    0

    Explanation: No triplets meet the conditions so we return 0.
    """
    s = list(accumulate(Counter(nums).values()))
    return sum(s[i - 1] * (s[i] - s[i - 1]) * (s[-1] - s[i]) for i in range(1, len(s)))
