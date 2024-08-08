def queryString(s: str, n: int) -> bool:
    """
    ID: 1016
    Tags:   String
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Given a binary string s and a positive integer n, return true if the binary representation of
    all the integers in the range [1, n] are substrings of s, or false otherwise.

    A substring is a contiguous sequence of characters within a string.

    Parameters
    ----------
    s : str

    n: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> queryString("0110", 3)
    True

    >>> queryString("0110", 4)
    False
    """
    ans = True
    for i in range(n, 0, -1):
        if s.find(bin(i)[2:]) == -1:
            return False
    return ans
