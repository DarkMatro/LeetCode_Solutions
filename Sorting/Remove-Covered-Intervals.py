def removeCoveredIntervals(intervals: list[list[int]]) -> int:
    """
    ID: 1288
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove
    all intervals that are covered by another interval in the list.

    The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

    Return the number of remaining intervals.

    Parameters
    ----------
    intervals: list[list[int]]

    Returns
    -------
    int

    Examples
    --------
    >>> removeCoveredIntervals([[1,4],[3,6],[2,8]])
    2

    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

    >>> removeCoveredIntervals([[1,4],[2,3]])
    1
    """
    res, longest = len(intervals), 0
    intervals.sort(key=lambda x: (x[0], -x[1]))
    for _, end in intervals:
        if end <= longest:
            res -= 1
        else:
            longest = end
    return res
