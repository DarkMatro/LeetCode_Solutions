def isFascinating(n: int) -> bool:
    """
    ID: 2729
    Tags:   Hash Table, Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given an integer n that consists of exactly 3 digits.

    We call the number n fascinating if, after the following modification, the resulting number
    contains all the digits from 1 to 9 exactly once and does not contain any 0's:

    Concatenate n with the numbers 2 * n and 3 * n.
    Return true if n is fascinating, or false otherwise.

    Concatenating two numbers means joining them together. For example, the concatenation of 121 and
    371 is 121371.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isFascinating(192)
    True

    Explanation: We concatenate the numbers n = 192 and 2 * n = 384 and 3 * n = 576. The resulting
    number is 192384576. This number contains all the digits from 1 to 9 exactly once.

    >>> isFascinating(100)
    False

    Explanation: We concatenate the numbers n = 100 and 2 * n = 200 and 3 * n = 300. The resulting
    number is 100200300. This number does not satisfy any of the conditions.
    """
    if n > 333:
        return False
    x = n * 1_000_000 + 2_000 * n + 3 * n
    digits = []
    while x != 0:
        dig = x % 10
        if dig == 0:
            return False
        digits.append(dig)
        x //= 10
    return len(set(digits)) == 9
