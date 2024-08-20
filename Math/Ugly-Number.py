def isUgly(n: int) -> bool:
    """
    ID: 263
    Tags:   Math
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return true if n is an ugly number.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isUgly(6)
    True

    Explanation: 6 = 2 × 3

    >>> isUgly(1)
    True

    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3,
    and 5.

    >>> isUgly(14)
    False

    Explanation: 14 is not ugly since it includes the prime factor 7.
    """
    if n < 1:
        return False
    if n <= 6:
        return True
    while n % 5 == 0:
        n /= 5
    while n % 3 == 0:
        n /= 3
    while n % 2 == 0:
        n /= 2
    return n == 1
