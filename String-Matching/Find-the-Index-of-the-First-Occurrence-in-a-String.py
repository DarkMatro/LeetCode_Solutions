def str_str(haystack: str, needle: str) -> int:
    """
    ID: 0028
    Tags:   Two Pointers, String, String Matching
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if
    needle is not part of haystack.

    Parameters
    ----------
    haystack : str
    needle : str

    Returns
    -------
    res : int

    Examples
    --------
    >>> str_str("sadbutsad", "sad")
    0

    "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

    >>> str_str("leetcode", "leeto")
    -1

    "leeto" did not occur in "leetcode", so we return -1.
    """
    len_needle = len(needle)
    len_haystack = len(haystack)
    if len_haystack < len_needle:
        return -1
    for i in range(len_haystack - len_needle + 1):
        if haystack[i] == needle[0] and haystack[i:i + len_needle] == needle:
            return i
    return -1
