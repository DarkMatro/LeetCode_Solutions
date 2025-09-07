def findMaxK(nums: list[int]) -> int:
    """
    ID: 2441
    Tags:   Array, Hash Table, Two Pointers, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also
    exists in the array.

    Return the positive integer k. If there is no such integer, return -1.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> findMaxK([-1,2,-3,3])
    3

    Explanation: 3 is the only valid k we can find in the array.

    >>> findMaxK([-1,10,6,7,-7,1])
    7

    Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

    >>> findMaxK([-10,8,6,7,-2,-3])
    -1

    Explanation: There is no a single valid k, we return -1.
    """
    neg_k = set([-x for x in nums if x < 0])
    return max([x for x in nums if x in neg_k], default=-1)
