def smallestRepunitDivByK(k: int) -> int:
    """
    ID: 1015
    Tags: Hash Table, Math
    Time: O(N)
    Memory: O(1)

    Task
    ----------
    Given a positive integer k, you need to find the length of the smallest positive integer n such
    that n is divisible by k, and n only contains the digit 1.

    Return the length of n. If there is no such n, return -1.

    Note: n may not fit in a 64-bit signed integer.

    Parameters
    ----------
    k: int

    Returns
    -------
    int

    Examples
    --------
    >>> smallestRepunitDivByK(1)
    1

    Explanation:
    The smallest answer is n = 1, which has length 1.

    >>> smallestRepunitDivByK(2)
    -1

    Explanation:
    There is no such positive integer n divisible by 2.

    >>> smallestRepunitDivByK(3)
    3

    Explanation:
    The smallest answer is n = 111, which has length 3.
    """
    if k % 2 == 0 or k % 5 == 0:
        return -1
    rem = 0
    for i in range(1, k + 1):
        rem = (rem * 10 + 1) % k
        if rem == 0:
            return i
    return -1
