def isIsomorphic(s: str, t: str) -> bool:
    """
    ID: 205
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the
    order of characters. No two characters may map to the same character, but a character may map to
    itself.

    Parameters
    ----------
    s: str

    t: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isIsomorphic('egg', 'add')
    True

    Explanation: The strings s and t can be made identical by:

    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

    >>> isIsomorphic('foo', 'bar')
    False

    Explanation: The strings s and t can not be made identical as 'o' needs to be mapped to both
    'a' and 'r'.

    >>> isIsomorphic('paper', 'title')
    True
    """
    for i, v in enumerate(s):
        if s.index(v) != t.index(t[i]):
            return False
    return True
