def dayOfYear(date: str) -> int:
    """
    ID: 1154
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the
    day number of the year.

    Parameters
    ----------
    date: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> dayOfYear("2019-01-09")
    9

    Explanation: Given date is the 9th day of the year in 2019.

    >>> dayOfYear("2019-02-10")
    41
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = map(int, date.split('-'))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    x = sum(days_in_month[:month - 1]) + day
    return x
