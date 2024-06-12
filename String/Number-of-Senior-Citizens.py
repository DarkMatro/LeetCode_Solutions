def countSeniors(details: list[str]) -> int:
    """
    ID: 2678
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed array of strings details. Each element of details provides information
    about a given passenger compressed into a string of length 15. The system is such that:

    The first ten characters consist of the phone number of passengers.
    The next character denotes the gender of the person.
    The following two characters are used to indicate the age of the person.
    The last two characters determine the seat allotted to that person.
    Return the number of passengers who are strictly more than 60 years old.

    Parameters
    ----------
    details: list[str]

    Returns
    -------
    out: int
        number of passengers who are strictly more than 60 years old.

    Examples
    --------
    >>> countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"])
    2

    >>> countSeniors(["1313579440F2036","2921522980M5644"])
    0
    """
    ans = 0
    for d in details:
        age = int(d[11:13])
        if age > 60:
            ans += 1
    return ans
