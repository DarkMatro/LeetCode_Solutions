def maximumValue(strs: list[str]) -> int:
    """
    ID: 2496
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    The value of an alphanumeric string can be defined as:

    The numeric representation of the string in base 10, if it comprises of digits only.
    The length of the string, otherwise.
    Given an array strs of alphanumeric strings, return the maximum value of any string in strs.

    Parameters
    ----------
    strs: List[str]

    Returns
    -------
    out: int

    Examples
    --------
    >>> maximumValue(["alic3","bob","3","4","00000"])
    5

    Explanation:
    - "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
    - "bob" consists only of letters, so its value is also its length, i.e. 3.
    - "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
    - "4" also consists only of digits, so its value is 4.
    - "00000" consists only of digits, so its value is 0.
    Hence, the maximum value is 5, of "alic3".

    >>> maximumValue(["1","01","001","0001"])
    1

    Explanation:
    Each string in the array has value 1. Hence, we return 1.
    """
    ans = 0
    for s in strs:
        if s.isnumeric():
            ans = max(ans, int(s))
        else:
            ans = max(ans, len(s))
    return ans
