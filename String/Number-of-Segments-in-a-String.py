def countSegments(s: str) -> int:
    """
    ID: 434
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, return the number of segments in the string.

    A segment is defined to be a contiguous sequence of non-space characters.

    Parameters
    ----------
    s : str

    Returns
    -------
    out : int

    Examples
    --------
    >>> countSegments("Hello, my name is John")
    5

    >>> countSegments("Hello")
    1
    """
    segments = [x for x in s.split(' ') if x]
    return len(segments)
