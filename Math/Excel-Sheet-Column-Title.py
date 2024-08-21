def convertToTitle(columnNumber: int) -> str:
    """
    ID: 168
    Tags:   Math, String
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    Given an integer columnNumber, return its corresponding column title as it appears in an Excel
    sheet.

    Parameters
    ----------
    columnNumber: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> convertToTitle(1)
    'A'

    >>> convertToTitle(28)
    'AB'

    >>> convertToTitle(701)
    'ZY'
    """
    result = []
    while columnNumber > 0:
        columnNumber -= 1  # Adjust for zero-based index
        remainder = columnNumber % 26
        result.append(chr(remainder + ord('A')))
        columnNumber //= 26
    return ''.join(reversed(result))