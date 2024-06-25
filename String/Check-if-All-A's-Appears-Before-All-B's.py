def checkString(s: str) -> bool:
    """
    ID: 2124
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears
    before every 'b' in the string. Otherwise, return false.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: bool

    Examples
    --------
    >>> checkString("aaabbb")
    True

    Explanation:
    The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
    Hence, every 'a' appears before every 'b' and we return true.

    >>> checkString("abab")
    False

    Explanation:
    There is an 'a' at index 2 and a 'b' at index 1.
    Hence, not every 'a' appears before every 'b' and we return false.

    >>> checkString("bbb")
    True

    Explanation:
    There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
    """
    was_b = False
    ans = True
    for ch in s:
        if ch == 'b' and not was_b:
            was_b = True
        if ch == 'a' and was_b:
            ans = False
    return ans
