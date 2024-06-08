def removeTrailingZeros(num: str) -> str:
    """
    ID: 2710
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a positive integer num represented as a string, return the integer num without trailing
    zeros as a string.

    Parameters
    ----------
    num: str

    Returns
    -------
    str

    Examples
    --------
    >>> removeTrailingZeros('51230100')
    '512301'

    Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

    >>> removeTrailingZeros('123')
    '123'

    Explanation: Integer "123" has no trailing zeros, we return integer "123".
    """
    idx = -1
    for i in range(len(num) - 1, -1, -1):
        ch = num[i]
        if ch != '0':
            idx = i
            break
    return num[:idx + 1]
