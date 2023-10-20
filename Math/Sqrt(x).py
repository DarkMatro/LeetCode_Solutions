def my_sqrt(x: int) -> int:
    """
    ID: 0069
    Tags:   Math, Binary Search
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.
    You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

    Parameters
    ----------
    x : int

    Returns
    -------
    out : int

    Examples
    --------
    >>> my_sqrt(4)
    2

    The square root of 4 is 2, so we return 2.

    >>> my_sqrt(8)
    2

    The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
    """
    # sqrt(1) = 1, sqrt(0) = 0.
    if x < 2:
        return x
    # left bound for binary search.
    left = 1
    # right bound for binary search, result is always less than x / 2.
    right = x // 2

    while left <= right:
        mid = (right + left) // 2
        mid2 = mid**2
        if mid2 > x:
            right = mid - 1
        elif mid2 == x:
            return mid
        else:
            left = mid + 1
    return int(right)
