def reverseStr(s: str, k: int) -> str:
    """
    ID: 541
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start
    of the string.

    If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal
    to k characters, then reverse the first k characters and leave the other as original.

    Parameters
    ----------
    s: str

    k: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> reverseStr("abcdefg", 2)
    'bacdfeg'

    >>> reverseStr("abcd", 2)
    'bacd'
    """
    ans = list(s)
    for i in range(0, len(ans), 2 * k):
        ans[i: i + k] = reversed(s[i:i + k])
    return ''.join(ans)
