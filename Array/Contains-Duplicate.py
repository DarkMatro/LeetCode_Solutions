from collections import defaultdict


def contains_duplicate(nums: list[int]) -> bool:
    """
    ID: 0217
    Tags:   Array, Hash Table, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if
    every element is distinct.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> contains_duplicate([1,2,3,1])
    True

    >>> contains_duplicate([1,2,3,4])
    False

    >>> contains_duplicate([1,1,1,3,3,4,3,2,4,2])
    True
    """
    d = defaultdict(int)
    for num in nums:
        d[num] += 1
        if d[num] > 1:
            return True
    return False
