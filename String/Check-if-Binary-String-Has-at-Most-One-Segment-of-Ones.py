def checkOnesSegment(s: str) -> bool:
    """
    ID: 1784
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a binary string s without leading zeros, return true if s contains at most one contiguous
    segment of ones. Otherwise, return false.

    Parameters
    ----------
    s: str

    Returns
    -------
    bool

    Examples
    --------
    >>> checkOnesSegment("1001")
    False

    Explanation: The ones do not form a contiguous segment.

    >>> checkOnesSegment("110")
    True
    """
    return s.count('01') == 0
