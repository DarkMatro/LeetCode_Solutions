def findLUSlength(a: str, b: str) -> int:
    """
    ID: 0521
    Tags:   String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given two strings a and b, return the length of the longest uncommon subsequence between a and
    b. If no such uncommon subsequence exists, return -1.

    An uncommon subsequence between two strings is a string that is a subsequence of exactly one of
    them.

    Parameters
    ----------
    a: str

    b: str

    Returns
    -------
    out: int

    Examples
    --------
    >>> findLUSlength("aba", "cdc")
    3

    Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba"
    but not "cdc".
    Note that "cdc" is also a longest uncommon subsequence.

    >>> findLUSlength("aaa", "bbb")
    3

    Explanation: The longest uncommon subsequences are "aaa" and "bbb".

    >>> findLUSlength("aaa", "aaa")
    -1

    Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every
    subsequence of string b is also a subsequence of string a. So the answer would be -1.
    """
    return -1 if a == b else max(len(a), len(b))
