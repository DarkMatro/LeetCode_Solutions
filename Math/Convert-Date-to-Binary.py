def convertDateToBinary(date: str) -> str:
    """
    ID: 3280
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

    date can be written in its binary representation obtained by converting year, month, and day to
    their binary representations without any leading zeroes and writing them down in year-month-day
    format.

    Return the binary representation of date.

    Parameters
    ----------
    date: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> convertDateToBinary("2080-02-29")
    '100000100000-10-11101'

    Explanation:
    100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

    >>> convertDateToBinary("1900-01-01")
    '11101101100-1-1'

    Explanation:
    11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.
    """
    return f"{bin(int(date[:4]))[2:]}-{bin(int(date[5:7]))[2:]}-{bin(int(date[8:]))[2:]}"
