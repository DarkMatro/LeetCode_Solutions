def isSubstringPresent(s: str) -> bool:
    """
    ID: 3083
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s, find any substring of length 2 which is also present in the reverse of s.

    Return true if such a substring exists, and false otherwise.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isSubstringPresent('leetcode')
    True

    Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

    >>> isSubstringPresent('abcba')
    True

    Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in
    reverse(s) == "abcba".

    >>> isSubstringPresent('abcd')
    False

    Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.
    """
    if len(s) == 1:
        return False
    s_ = s[::-1]
    if s_ == s:
        return True
    d = set()
    for i in range(len(s) - 1):
        d.add(s[i:i + 2])
    for i in range(len(s_) - 1):
        if s_[i:i + 2] in d:
            return True
    return False
