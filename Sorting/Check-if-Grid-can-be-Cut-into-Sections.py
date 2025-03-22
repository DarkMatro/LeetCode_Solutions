def checkValidCuts(n: int, rectangles: list[list[int]]) -> bool:
    """
    ID: 3394
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given an integer n representing the dimensions of an n x n grid, with the origin at the
    bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where
    rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid.
    Each rectangle is defined as follows:

    (startx, starty): The bottom-left corner of the rectangle.
    (endx, endy): The top-right corner of the rectangle.
    Note that the rectangles do not overlap. Your task is to determine if it is possible to make
    either two horizontal or two vertical cuts on the grid such that:

    Each of the three resulting sections formed by the cuts contains at least one rectangle.
    Every rectangle belongs to exactly one section.
    Return true if such cuts can be made; otherwise, return false.

    Parameters
    ----------
    n: int

    rectangles: list[list[int]]

    Returns
    -------
    bool

    Examples
    --------
    >>> checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]])
    True

    Explanation: The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4.
    Hence, output is true.

    >>> checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]])
    False

    Explanation: We cannot make two horizontal or two vertical cuts that satisfy the conditions.
    Hence, output is false.
    """
    ranges_x, ranges_y = [], []
    for x_s, y_s, x_e, y_e in rectangles:
        ranges_x.append([x_s, x_e])
        ranges_y.append([y_s, y_e])
    if len(merge(ranges_y)) >= 3:
        return True
    if len(merge(ranges_x)) >= 3:
        return True
    return False


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    res = []
    res.append(intervals[0])
    for i, curr in enumerate(intervals):
        if i == 0:
            continue
        last = res[-1]
        if curr[0] < last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    return res
