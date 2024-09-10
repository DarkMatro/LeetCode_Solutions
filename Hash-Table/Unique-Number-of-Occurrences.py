from collections import Counter

def uniqueOccurrences(arr: list[int]) -> bool:
    """
    ID: 1207
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array of integers arr, return true if the number of occurrences of each value in the
    array is unique or false otherwise.

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> uniqueOccurrences([1,2,2,1,1,3])
    True

    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same
    number of occurrences.

    >>> uniqueOccurrences([1,2])
    False

    >>> uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
    True
    """
    cnt = Counter(arr)
    return len(cnt.values()) == len(set(cnt.values()))
