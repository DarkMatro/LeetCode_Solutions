def canBeEqual(target: list[int], arr: list[int]) -> bool:
    """
    ID: 1460
    Tags:   Array, Hash Table, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    You are given two integer arrays of equal length target and arr. In one step, you can select any
    non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

    Return true if you can make arr equal to target or false otherwise.

    Parameters
    ----------
    target: list[int]

    arr: list[int]

    Returns
    -------
    bool

    Examples
    --------
    >>> canBeEqual([1,2,3,4], [2,4,1,3])
    True

    Explanation: You can follow the next steps to convert arr to target:
    1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
    2- Reverse subarray [4,2], arr becomes [1,2,4,3]
    3- Reverse subarray [4,3], arr becomes [1,2,3,4]
    There are multiple ways to convert arr to target, this is not the only way to do so.

    >>> canBeEqual([7], [7])
    True

    Explanation: arr is equal to target without any reverses.

    >>> canBeEqual([3,7,9], [3,7,11])
    False

    Explanation: arr does not have value 9 and it can never be converted to target.
    """
    return sorted(target) == sorted(arr)
