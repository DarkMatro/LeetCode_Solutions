def longestContinuousSubstring(s: str) -> int:
    """
    ID: 2414
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    An alphabetical continuous string is a string consisting of consecutive letters in the alphabet.
    In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

    For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
    Given a string s consisting of lowercase letters only, return the length of the longest
    alphabetical continuous substring.

    Parameters
    ----------
    s : str

    Returns
    -------
    out : int

    Examples
    --------
    >>> longestContinuousSubstring("abacaba")
    2

    Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
    "ab" is the longest continuous substring.

    >>> longestContinuousSubstring("abcde")
    5

    Explanation: "abcde" is the longest continuous substring.
    """
    n, ans = 1, 1
    prev = None
    for x in s:
        if prev is None:
            prev = ord(x)
            continue
        cur = ord(x)
        if prev + 1 == cur:
            n += 1
            ans = max(ans, n)
        else:
            n = 1
        prev = cur
    return ans
