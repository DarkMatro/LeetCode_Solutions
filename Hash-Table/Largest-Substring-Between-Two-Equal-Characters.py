def maxLengthBetweenEqualCharacters(s: str) -> int:
    """
    ID: 1624
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, return the length of the longest substring between two equal characters,
    excluding the two characters. If there is no such substring return -1.

    A substring is a contiguous sequence of characters within a string.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxLengthBetweenEqualCharacters('aa')
    0

    Explanation: The optimal substring here is an empty substring between the two 'a's.

    >>> maxLengthBetweenEqualCharacters('abca')
    2

    Explanation: The optimal substring here is "bc".

    >>> maxLengthBetweenEqualCharacters('cbzxy')
    -1

    Explanation: There are no characters that appear twice in s.
    """
    ans = 0
    has_equal = False
    d = {}
    for i, x in enumerate(s):
        if x in d:
            has_equal = True
            ans = max(ans, i - d[x] - 1)
        else:
            d[x] = i
    if not has_equal:
        return -1
    return ans
