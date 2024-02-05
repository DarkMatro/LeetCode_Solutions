def threeConsecutiveOdds(arr: list[int]) -> bool:
    """
    ID: 1550
    Tags:   Array
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise,
    return false.

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    bool

    Examples
    --------
    >>> threeConsecutiveOdds([2,6,4,1])
    False

    Explanation: There are no three consecutive odds.

    >>> threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])
    True

    Explanation: [5,7,23] are three consecutive odds.
    """
    tmp = 0
    for i in arr:
        if i % 2 != 0:
            tmp += 1
        else:
            tmp = 0
        if tmp == 3:
            return True
    return False
