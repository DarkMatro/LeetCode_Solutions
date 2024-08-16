import datetime

def dayOfTheWeek(day: int, month: int, year: int) -> str:
    """
    ID: 1185
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given a date, return the corresponding day of the week for that date.

    The input is given as three integers representing the day, month and year respectively.

    Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday"}.

    Parameters
    ----------
    day: int

    month: int

    year: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> dayOfTheWeek(31, 8, 2019)
    'Saturday'

    >>> dayOfTheWeek(18, 7, 1999)
    'Sunday'

    >>> dayOfTheWeek(15, 8, 1993)
    'Sunday'

    """
    # Create a date object
    date_obj = datetime.date(year, month, day)

    # Get the day of the week, where Monday is 0 and Sunday is 6
    day_of_week = date_obj.weekday()

    # Map to day names
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return days[day_of_week]
