from itertools import groupby


def hasSpecialSubstring(s: str, k: int) -> bool:
    """
    ID: 3456
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string s and an integer k.

    Determine if there exists a substring of length exactly k in s that satisfies the following
    conditions:

    The substring consists of only one distinct character (e.g., "aaa" or "bbb").
    If there is a character immediately before the substring, it must be different from the
    character in the substring.
    If there is a character immediately after the substring, it must also be different from the
    character in the substring.
    Return true if such a substring exists. Otherwise, return false.

    Parameters
    ----------
    s: str

    k: int

    Returns
    -------
    bool

    Examples
    --------
    >>> hasSpecialSubstring('aaabaaa', 3)
    True

    Explanation: The substring s[4..6] == "aaa" satisfies the conditions.

    It has a length of 3.
    All characters are the same.
    The character before "aaa" is 'b', which is different from 'a'.
    There is no character after "aaa".

    >>> hasSpecialSubstring('abc', 2)
    False

    Explanation: There is no substring of length 2 that consists of one distinct character and
    satisfies the conditions.
    """
    return any([len(list(x)) == k for _, x in groupby(s)])

