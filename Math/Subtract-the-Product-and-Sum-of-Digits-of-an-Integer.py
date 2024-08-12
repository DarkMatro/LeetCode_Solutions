def subtractProductAndSum(n: int) -> int:
    """
    ID: 1281
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given an integer number n, return the difference between the product of its digits and the sum of its digits.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> subtractProductAndSum(234)
    15

    Explanation:
    Product of digits = 2 * 3 * 4 = 24
    Sum of digits = 2 + 3 + 4 = 9
    Result = 24 - 9 = 15

    >>> subtractProductAndSum(4421)
    21

    Explanation:
    Product of digits = 4 * 4 * 2 * 1 = 32
    Sum of digits = 4 + 4 + 2 + 1 = 11
    Result = 32 - 11 = 21
    """
    prod = 1
    s = 0
    prev = None
    for i in [10, 100, 1000, 10_000, 100_000]:
        dig = n % i
        if prev is not None:
            dig = int((dig - prev) / (i / 10))
        prod *= dig
        s += dig
        if n % i == n:
            break
        prev = dig
    return prod - s
