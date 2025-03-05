from collections import Counter


def frequencySort(nums: list[int]) -> list[int]:
    """
    ID: 1636
    Tags:   Array, Hash Table, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Given an array of integers nums, sort the array in increasing order based on the frequency of
    the values. If multiple values have the same frequency, sort them in decreasing order.

    Return the sorted array.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    list[int]

    Examples
    --------
    >>> frequencySort([1,1,2,2,2,3])
    [3, 1, 1, 2, 2, 2]

    Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

    >>> frequencySort([2,3,1,3,2])
    [1, 3, 3, 2, 2]

    Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

    >>> frequencySort([-1,1,-6,4,5,-6,1,4,1])
    [5, -1, 4, 4, -6, -6, 1, 1, 1]
    """
    c = Counter(nums)
    ans = []
    sc = []
    for v in sorted(c.values()):
        if v not in sc:
            sc.append(v)
    for x in sc:
        ans.extend(sorted([k for k, v in c.items() if v == x] * x, reverse=True))
    return ans
