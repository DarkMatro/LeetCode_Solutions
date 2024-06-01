def scoreOfString(s: str) -> int:
    """
    ID: 3110
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string s. The score of a string is defined as the sum of the absolute difference
    between the ASCII values of adjacent characters.

    Return the score of s.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> scoreOfString("hello")
    13

    Explanation: The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108,
    'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| =
    3 + 7 + 0 + 3 = 13.

    >>> scoreOfString("zaz")
    50

    Explanation: The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of
    s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
    """
    prev = s[0]
    ans = 0
    for i in range(1, len(s)):
        ch = s[i]
        ans += abs(ord(prev) - ord(ch))
        prev = ch
    return ans
