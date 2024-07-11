def modifyString(s: str) -> str:
    """
    ID: 1576
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s containing only lowercase English letters and the '?' character, convert all
    the '?' characters into lowercase letters such that the final string does not contain any
    consecutive repeating characters. You cannot modify the non '?' characters.

    It is guaranteed that there are no consecutive repeating characters in the given string except
    for '?'.

    Return the final string after all the conversions (possibly zero) have been made. If there is
    more than one solution, return any of them. It can be shown that an answer is always possible
    with the given constraints.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> modifyString("?zs")
    'bzs'

    Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only
    "z" is an invalid modification as the string will consist of consecutive repeating characters in
    "zzs".

    >>> modifyString("ubv?w")
    'ubvaw'

    Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications
    as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
    """
    ans = ''
    comp = ['a', 'b', 'c']
    for i, x in enumerate(s):
        if x == '?':
            prev = ans[i - 1] if i > 0 else 'a'
            next_ = s[i + 1] if i < len(s) - 1 else 'b'
            x = [q for q in comp if q not in [prev, next_]][0]
        ans += x
    return ans
