def validMountainArray(arr: list[int]) -> bool:
    """
    ID: 0941
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> validMountainArray([2,1])
    False

    >>> validMountainArray([3,5,5])
    False

    >>> validMountainArray([0,3,2,1])
    True

    >>> validMountainArray([0,1,2,3,4,5,6,7,8,9])
    False

    >>> validMountainArray([9,8,7,6,5,4,3,2,1,0])
    False
    """
    n = len(arr)
    if n < 3:
        return False
    increasing = True
    decreasing = False
    prev = arr[0]
    for i in range(1, n):
        num = arr[i]
        if (decreasing and num > prev) or num == prev or (i == 1 and num < prev):
            return False
        elif increasing and num < prev:
            increasing = False
            decreasing = True
        prev = num
    return not increasing and decreasing
