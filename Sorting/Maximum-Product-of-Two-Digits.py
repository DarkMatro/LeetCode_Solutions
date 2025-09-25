def maxProduct(n: int) -> int:
    """
    ID: 3536
    Tags:   Math, Sorting
    Time:   O(Log(N)Log(Log(N)))
    Memory: O(Log(N))

    Task
    ----------
    You are given a positive integer n.

    Return the maximum product of any two digits in n.

    Note: You may use the same digit twice if it appears more than once in n.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxProduct(31)
    3

    Explanation:
    The digits of n are [3, 1].
    The possible products of any two digits are: 3 * 1 = 3.
    The maximum product is 3.

    >>> maxProduct(22)
    4

    Explanation:
    The digits of n are [2, 2].
    The possible products of any two digits are: 2 * 2 = 4.
    The maximum product is 4.

    >>> maxProduct(124)
    8

    Explanation:
    The digits of n are [1, 2, 4].
    The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
    The maximum product is 8.
    """
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    digits.sort()
    return digits[-1] * digits[-2]
