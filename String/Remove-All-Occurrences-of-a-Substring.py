def removeOccurrences(s: str, part: str) -> str:
    """
    ID: 1910
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given two strings s and part, perform the following operation on s until all occurrences of the
    substring part are removed:

    Find the leftmost occurrence of the substring part and remove it from s.
    Return s after removing all occurrences of part.

    A substring is a contiguous sequence of characters in a string.

    Parameters
    ----------
    s : str

    part: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> removeOccurrences("daabcbaabcbc", 'abc')
    'dab'

    Explanation: The following operations are done:
    - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
    - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
    - s = "dababc", remove "abc" starting at index 3, so s = "dab".
    Now s has no occurrences of "abc".

    >>> removeOccurrences("axxxxyyyyb", 'xy')
    'ab'

    Explanation: The following operations are done:
    - s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
    - s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
    - s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
    - s = "axyb", remove "xy" starting at index 1 so s = "ab".
    Now s has no occurrences of "xy".
    """
    while part in s:
        s = s.replace(part, '', 1)
    return s
