def trailingZeroes(n: int) -> int:
    """
    ID: 172
    Tags:   Math
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    Given an integer n, return the number of trailing zeroes in n!.

    Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> trailingZeroes(3)
    0

    Explanation: 3! = 6, no trailing zero.

    >>> trailingZeroes(5)
    1

    Explanation: 5! = 120, one trailing zero.

    >>> trailingZeroes(0)
    0
    """
    count = 0
    while n > 0:
        x = n // 5
        count += x
        n = x
    return count
