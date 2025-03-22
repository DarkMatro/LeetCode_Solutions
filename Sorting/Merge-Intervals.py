def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    ID: 56
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
    intervals, and return an array of the non-overlapping intervals that cover all the intervals in
    the input.

    Parameters
    ----------
    intervals: list[list[int]]

    Returns
    -------
    list[list[int]]

    Examples
    --------
    >>> merge([[1,3],[2,6],[8,10],[15,18]])
    [[1, 6], [8, 10], [15, 18]]

    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

    >>> merge([[1,4],[4,5]])
    [[1, 5]]

    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    """
    intervals.sort()

    res = []
    res.append(intervals[0])
    for i, curr in enumerate(intervals):
        if i == 0:
            continue
        last = res[-1]
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res
