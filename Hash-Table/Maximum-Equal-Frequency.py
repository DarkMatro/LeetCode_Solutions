from collections import defaultdict

def maxEqualFreq(nums: list[int]) -> int:
    """
    ID: 1224
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an array nums of positive integers, return the longest possible length of an array prefix
    of nums, such that it is possible to remove exactly one element from this prefix so that every
    number that has appeared in it will have the same number of occurrences.

    If after removing one element there are no remaining elements, it's still considered that every
    appeared number has the same number of ocurrences (0).

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> maxEqualFreq([2,2,1,1,5,3,3,5])
    7

    Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5, we will get
    [2,2,1,1,3,3], so that each number will appear exactly twice.

    >>> maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5])
    13
    """
    cnt, freq, maxfreq, ans = defaultdict(int), defaultdict(int), 0, 0
    for i, num in enumerate(nums):
        cnt[num] = cnt.get(num, 0) + 1
        freq[cnt[num]] += 1
        freq[cnt[num] - 1] -= 1
        maxfreq = max(maxfreq, cnt[num])
        if maxfreq == 1:
            ans = i + 1
        elif maxfreq * freq[maxfreq] == i:
            ans = i + 1
        elif (maxfreq - 1) * (freq[maxfreq - 1] + 1) == i:
            ans = i + 1
    return ans
