from bisect import bisect, bisect_left


def findSpecialInteger(arr: list[int]) -> int:
    """
    ID: 1287
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more
    than 25% of the time, return that integer.

    Parameters
    ----------
    arr : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> findSpecialInteger([1,2,2,6,6,6,6,7,10])
    6

    >>> findSpecialInteger([1,1])
    1

    """
    for x in [arr[len(arr) // 4], arr[len(arr) // 2], arr[len(arr) * 3 // 4]]:
        if (bisect(arr, x) - bisect_left(arr, x)) * 4 > len(arr):
            return x
    return -1

