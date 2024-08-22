def checkPowersOfThree(n: int) -> bool:
    """
    ID: 1780
    Tags:   Math
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    Given an integer n, return true if it is possible to represent n as the sum of distinct powers
    of three. Otherwise, return false.

    An integer y is a power of three if there exists an integer x such that y == 3x.

    Parameters
    ----------
    N: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> checkPowersOfThree(12)
    True

    Explanation: 12 = 3^1 + 3^2

    >>> checkPowersOfThree(91)
    True

    Explanation: 91 = 3^0 + 3^2 + 3^4

    >>> checkPowersOfThree(21)
    False
    """
    while n > 0:
        if n % 3 == 2:
            return False
        n //= 3
    return True