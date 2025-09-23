def checkDivisibility(n: int) -> bool:
    """
    ID: 3622
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

    The digit sum of n (the sum of its digits).

    The digit product of n (the product of its digits).

    Return true if n is divisible by this sum; otherwise, return false.

    Parameters
    ----------
    n: int

    Returns
    -------
    bool

    Examples
    --------
    >>> checkDivisibility(99)
    True

    Explanation:

    Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true

    >>> checkDivisibility(23)
    False

    Explanation:

    Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is
    false.
    """
    digits = []
    m = n + 0
    while m != 0:
        digits.append(m % 10)
        m //= 10
    s = sum(digits)
    p = 1
    for x in digits:
        p *= x
    return n % (s + p) == 0
