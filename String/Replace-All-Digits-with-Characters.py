def replaceDigits(s: str) -> str:
    """
    ID: 1844
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed string s that has lowercase English letters in its even indices and
    digits in its odd indices.

    There is a function shift(c, x), where c is a character and x is a digit, that returns the xth
    character after c.

    For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
    For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

    Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never
    exceed 'z'.

    Parameters
    ----------
    s: str

    Returns
    -------
    str

    Examples
    --------
    >>> replaceDigits("a1c1e1")
    'abcdef'

    Explanation: The digits are replaced as follows:
    - s[1] -> shift('a',1) = 'b'
    - s[3] -> shift('c',1) = 'd'
    - s[5] -> shift('e',1) = 'f'

    >>> replaceDigits("a1b2c3d4e")
    'abbdcfdhe'

    Explanation: The digits are replaced as follows:
    - s[1] -> shift('a',1) = 'b'
    - s[3] -> shift('b',2) = 'd'
    - s[5] -> shift('c',3) = 'f'
    - s[7] -> shift('d',4) = 'h'
    """
    ans = s[0]
    for i in range(1, len(s)):
        ch = s[i]
        if i % 2 != 0:
            ans += chr(ord(ans[i - 1]) + int(ch))
        else:
            ans += ch
    return ans
