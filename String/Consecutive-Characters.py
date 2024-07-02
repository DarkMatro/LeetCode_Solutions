def maxPower(s: str) -> int:
    """
    ID: 1446
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    The power of the string is the maximum length of a non-empty substring that contains only one
    unique character.

    Given a string s, return the power of s.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: int

    Examples
    --------
    >>> maxPower("leetcode")
    2

    Explanation: The substring "ee" is of length 2 with the character 'e' only.

    >>> maxPower("abbcccddddeeeeedcba")
    5

    Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
    """
    if len(s) == 1:
        return 1
    ans = 0
    prev = s[0]
    sub_len = 1
    for i in range(1, len(s)):
        ch = s[i]
        if ch == prev:
            sub_len += 1
        else:
            ans = max(sub_len, ans)
            sub_len = 1
        prev = ch
    return max(sub_len, ans)
