from datetime import datetime

def daysBetweenDates(date1: str, date2: str) -> int:
    """
    ID: 1360
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Write a program to count the number of days between two dates.

    The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

    Parameters
    ----------
    date1: str

    date2: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> daysBetweenDates("2019-06-29", "2019-06-30")
    1

    >>> daysBetweenDates("2020-01-15", "2019-12-31")
    15
    """
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate the difference in days
    diff = abs((d2 - d1).days)

    return diff
