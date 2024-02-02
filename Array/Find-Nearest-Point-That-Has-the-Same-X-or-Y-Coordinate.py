def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
    """
    ID: 1779
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are
    also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is
    valid if it shares the same x-coordinate or the same y-coordinate as your location.

    Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
    If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

    The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

    Parameters
    ----------
    x: int

    y: int

    points: list[list[int]]

    Returns
    -------
    out : int

    Examples
    --------
    >>> nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]])
    2

    Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have
    the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index,
    so return 2.

    >>> nearestValidPoint(3, 4, [[3,4]])
    0

    Explanation: The answer is allowed to be on the same location as your current location.

    >>> nearestValidPoint(3, 4, [[2,3]])
    -1

    Explanation: There are no valid points.
    """
    ans = -1
    min_dist = 1e8
    for i, point in enumerate(points):
        if point[0] == x and point[1] == y:
            return i
        elif point[0] == x or point[1] == y:
            dist = abs(x - point[0]) + abs(y - point[1])
            if dist < min_dist:
                min_dist = dist
                ans = i
    return ans

