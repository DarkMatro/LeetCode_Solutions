from collections import Counter

def uniqueOccurrences(nums: list[int]) -> int:
    """
    ID: 961
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums with the following properties:

    nums.length == 2 * n.
    nums contains n + 1 unique elements.
    Exactly one element of nums is repeated n times.
    Return the element that is repeated n times.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> uniqueOccurrences([1,2,3,3])
    3

    >>> uniqueOccurrences([2,1,2,5,3,2])
    2

    >>> uniqueOccurrences([5,1,5,2,5,3,5,4])
    5
    """
    cnt = Counter(nums)
    n = len(nums) // 2
    for k, v in cnt.items():
        if v == n:
            return k
