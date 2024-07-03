def makeFancyString(s: str) -> str:
    """
    ID: 1957
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A fancy string is a string where no three consecutive characters are equal.

    Given a string s, delete the minimum possible number of characters from s to make it fancy.

    Return the final string after the deletion. It can be shown that the answer will always be
    unique.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> makeFancyString("leeetcode")
    'leetcode'

    Explanation: Remove an 'e' from the first group of 'e's to create "leetcode".
    No three consecutive characters are equal, so return "leetcode".

    >>> makeFancyString("aaabaaaa")
    'aabaa'

    Explanation: Remove an 'a' from the first group of 'a's to create "aabaaaa".
    Remove two 'a's from the second group of 'a's to create "aabaa".
    No three consecutive characters are equal, so return "aabaa".

    >>> makeFancyString("aab")
    'aab'

    Explanation: No three consecutive characters are equal, so return "aab".
    """
    ans = ''
    prev = s[0]
    substr = prev
    for i in range(1, len(s)):
        ch = s[i]
        if ch == prev and len(substr) < 2:
            substr += ch
        elif ch != prev:
            ans += substr
            substr = ch
        prev = ch
    else:
        ans += substr
    return ans
