def is_power_of_three(n: int) -> bool:
    """
    ID: 0326
    Tags:   Math, Recursion
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given an integer n, return true if it is a power of three. Otherwise, return false.

    An integer n is a power of three, if there exists an integer x such that n == 3x.

    Parameters
    ----------
    n : int

    Returns
    -------
    out: bool

    Examples
    --------
    >>> is_power_of_three(27)
    True

    Explanation: 27 = 3^3

    >>> is_power_of_three(0)
    False

    Explanation: There is no x where 3x = 0.

    >>> is_power_of_three(-1)
    False

    Explanation: There is no x where 3x = (-1).
    """

    if n <= 0:
        return False
    while True:
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        n = n // 3

