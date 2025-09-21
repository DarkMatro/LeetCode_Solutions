def lastSubstring(s: str) -> str:
    """
    ID: 1163
    Tags: Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, return the last substring of s in lexicographical order.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> lastSubstring("abab")
    'bab'

    >>> lastSubstring("leetcode")
    'tcode'
    """
    n = len(s)
    i, j, k = 0, 1, 0  # i = best start, j = candidate, k = offset
    while j + k < n:
        if s[i + k] == s[j + k]:
            k += 1
            continue
        if s[i + k] > s[j + k]:
            j += k + 1
        else:
            i = max(i + k + 1, j)
            j = i + 1
        k = 0
    return s[i:]