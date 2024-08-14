def alternateDigitSum(n: int) -> int:
    """
    ID: 2544
    Tags:   Math
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a positive integer n. Each digit of n has a sign according to the following rules:

    The most significant digit is assigned a positive sign.
    Each other digit has an opposite sign to its adjacent digits.
    Return the sum of all digits with their corresponding sign.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> alternateDigitSum(521)
    4

    Explanation: (+5) + (-2) + (+1) = 4.

    >>> alternateDigitSum(111)
    1

    Explanation: (+1) + (-1) + (+1) = 1.

    >>> alternateDigitSum(886996)
    0

    Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
    """
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    sign = 1
    ans = 0
    for d in digits[::-1]:
        ans += sign * d
        sign *= -1
    return ans

