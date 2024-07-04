def thousandSeparator(n: int) -> str:
    """
    ID: 1556
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer n, add a dot (".") as the thousands separator and return it in string format.

    Parameters
    ----------
    n: int

    Returns
    -------
    out: str

    Examples
    --------
    >>> thousandSeparator(987)
    '987'

    >>> thousandSeparator(1234)
    '1.234'
    """
    s = str(n)[::-1]
    return '.'.join([s[i:i + 3] for i in range(0, len(s), 3)])[::-1]
