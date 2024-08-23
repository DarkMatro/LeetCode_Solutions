def closestDivisors(num: int) -> list[int]:
    """
    ID: 1362
    Tags:   Math
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    Given an integer num, find the closest two integers in absolute difference whose product equals
    num + 1 or num + 2.

    Return the two integers in any order.

    Parameters
    ----------
    NUM: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> closestDivisors(8)
    [3, 3]

    Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest
    divisors are 2 & 5, hence 3 & 3 is chosen.

    >>> closestDivisors(123)
    [5, 25]

    >>> closestDivisors(999)
    [25, 40]
    """
    for i in reversed(range(1, int((num + 2) ** 0.5) + 1)):
        if not (num + 1) % i:
            return [i, (num + 1) // i]
        if not (num + 2) % i:
            return [i, (num + 2) // i]
