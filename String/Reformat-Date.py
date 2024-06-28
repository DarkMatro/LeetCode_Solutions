def reformatDate(date: str) -> str:
    """
    ID: 1507
    Tags:   String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given a date string in the form Day Month Year, where:

    Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
    Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
    "Nov", "Dec"}.
    Year is in the range [1900, 2100].
    Convert the date string to the format YYYY-MM-DD, where:

    YYYY denotes the 4 digit year.
    MM denotes the 2-digit month.
    DD denotes the 2 digit day.

    Parameters
    ----------
    date: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> reformatDate("20th Oct 2052")
    '2052-10-20'

    >>> reformatDate("6th Jun 1933")
    '1933-06-06'

    >>> reformatDate("26th May 1960")
    '1960-05-26'
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    words = date.split(' ')
    day = int(words[0][:-2])
    day = f"0{day}" if day < 10 else day
    month = months.index(words[1]) + 1
    month = f"0{month}" if month < 10 else month
    year = words[2]
    return f"{year}-{month}-{day}"
