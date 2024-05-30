from bisect import bisect_right, bisect_left


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """
    ID: 57
    Tags:   Array
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    You are given an array of non-overlapping intervals intervals where
    intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals
    is sorted in ascending order by starti. You are also given an interval
    newInterval = [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by
    starti and intervals still does not have any overlapping intervals (merge overlapping intervals
    if necessary).

    Return intervals after the insertion.

    Note that you don't need to modify intervals in-place. You can make a new array and return it.

    Parameters
    ----------
    intervals: list[list[int]]

    newInterval: list[int]

    Returns
    -------
    out : list[list[int]]

    Examples
    --------
    >>> insert([[1,3],[6,9]], [2,5])
    [[1, 5], [6, 9]]

    >>> insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    [[1, 2], [3, 10], [12, 16]]

    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

    >>> insert([], [5,7])
    [[5, 7]]

    >>> insert([[1,5]], [2,3])
    [[1, 5]]

    >>> insert([[1,5]], [2,7])
    [[1, 7]]

    >>> insert([[1,5]], [6,8])
    [[1, 5], [6, 8]]

    >>> insert([[1,5]], [0,0])
    [[0, 0], [1, 5]]
    """
    if not intervals:
        return [newInterval]
    n = len(intervals)
    i_start, i_end = newInterval

    pos_l = bisect_left(intervals, i_start, key=lambda x: x[1])
    i_start = min(intervals[pos_l][0], i_start) if pos_l < n else i_start

    pos_r = bisect_right(intervals, i_end, key=lambda x: x[0])
    i_end = max(i_end, intervals[pos_r - 1][1]) if n >= pos_r > 0 else i_end

    return intervals[:pos_l] + [[i_start, i_end]] + intervals[pos_r:]

