def isPrefixString(s: str, words: list[str]) -> bool:
    """
    ID: 1961
    Tags:   Array, Two Pointers, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s and an array of strings words, determine whether s is a prefix string of words.

    A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some
    positive k no larger than words.length.

    Return true if s is a prefix string of words, or false otherwise.

    Parameters
    ----------
    s: str

    words: list[str]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isPrefixString("iloveleetcode", ["i","love","leetcode","apples"])
    True

    Explanation: s can be made by concatenating "i", "love", and "leetcode" together.

    >>> isPrefixString("iloveleetcode", ["apples","i","love","leetcode"])
    False

    Explanation: It is impossible to make s using a prefix of arr.
    """
    t = ''
    for w in words:
        t += w
        if t == s:
            return True
    return False
