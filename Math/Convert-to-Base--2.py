def baseNeg2(n: int) -> str:
    """
    ID: 789
    Tags:   Array, Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given an integer n, return a binary string representing its representation in base -2.

    Note that the returned string should not have leading zeros unless the string is "0".

    Parameters
    ----------
    n: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> baseNeg2(2)
    '110'

    Explanation: (-2)^2 + (-2)^1 = 2


    >>> baseNeg2(3)
    '111'

    Explanation: (-2)^2 + (-2)^1 + (-2)^0 = 3

    >>> baseNeg2(4)
    '100'

    Explanation: (-2)^2 = 4
    """
    if n == 0:
        return "0"

    result = []

    while n != 0:
        remainder = n % -2
        n //= -2

        if remainder < 0:
            remainder += 2
            n += 1

        result.append(str(remainder))

    return ''.join(result[::-1])
