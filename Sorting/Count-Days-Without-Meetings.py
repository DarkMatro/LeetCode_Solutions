def countDays(days: int, meetings: list[list[int]]) -> int:
    """
    ID: 3169
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given a positive integer days representing the total number of days an employee is
    available for work (starting from day 1). You are also given a 2D array meetings of size n
    where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i
    (inclusive).

    Return the count of days when the employee is available for work but no meetings are scheduled.

    Note: The meetings may overlap.

    Parameters
    ----------
    days: int

    meetings: list[list[int]]

    Returns
    -------
    int

    Examples
    --------
    >>> countDays(10, [[5,7],[1,3],[9,10]])
    2

    Explanation: There is no meeting scheduled on the 4th and 8th days.

    >>> countDays(5, [[2,4],[1,3]])
    1

    Explanation: There is no meeting scheduled on the 5th day.

    >>> countDays(6, [[1,6]])
    0

    Explanation: Meetings are scheduled for all working days.
    """

    def merge(intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i, curr in enumerate(intervals):
            if i == 0:
                continue
            last = res[-1]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr)

        return res

    meetings = merge(meetings)
    ans = 0
    prev = meetings[0][1]
    for i, (start, end) in enumerate(meetings):
        if i == 0:
            continue
        ans += start - prev - 1
        prev = end
    return ans + (meetings[0][0] - 1) + (days - meetings[-1][1])
