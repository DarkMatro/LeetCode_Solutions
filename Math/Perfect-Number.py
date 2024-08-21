def checkPerfectNumber(num: int) -> bool:
    """
    ID: 507
    Tags:   Math
    Time:   O(sqrt(num))
    Memory: O(1)

    Task
    ----------
    A perfect number is a positive integer that is equal to the sum of its positive divisors,
    excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

    Given an integer n, return true if n is a perfect number, otherwise return false.

    Parameters
    ----------
    num: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> checkPerfectNumber(28)
    True

    Explanation: 28 = 1 + 2 + 4 + 7 + 14
    1, 2, 4, 7, and 14 are all divisors of 28.

    >>> checkPerfectNumber(7)
    False
    """
    if num == 1:
        return False

    ans = 1

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            ans += i + num // i

    return ans == num
