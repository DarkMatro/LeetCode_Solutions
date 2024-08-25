def countHomogenous(s: str) -> int:
    """
    ID: 1759
    Tags:   Math, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, return the number of homogenous substrings of s. Since the answer may be too
    large, return it modulo 109 + 7.

    A string is homogenous if all the characters of the string are the same.

    A substring is a contiguous sequence of characters within a string.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> countHomogenous('abbcccaa')
    13

    Explanation: The homogenous substrings are listed as below:
    "a"   appears 3 times.
    "aa"  appears 1 time.
    "b"   appears 2 times.
    "bb"  appears 1 time.
    "c"   appears 3 times.
    "cc"  appears 2 times.
    "ccc" appears 1 time.
    3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

    >>> countHomogenous('xy')
    2

    Explanation: The homogenous substrings are "x" and "y".

    >>> countHomogenous('zzzzz')
    15
    """
    MOD = 10 ** 9 + 7
    ans = 0
    prev = None
    n = 1
    for i, x in enumerate(s):
        if i == 0:
            prev = x
            continue
        if prev == x:
            n += 1
        else:
            ans += (n * (n + 1)) / 2
            n = 1
        prev = x
    else:
        ans += (n * (n + 1)) / 2
    return int(ans % MOD)

