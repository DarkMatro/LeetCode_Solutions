def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    """
    ID: 1637
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between
    two points such that no points are inside the area.

    A vertical area is an area of fixed-width extending infinitely along the y-axis
    (i.e., infinite height). The widest vertical area is the one with the maximum width.

    Note that points on the edge of a vertical area are not considered included in the area.

    Parameters
    ----------
    points: list[list[int]]

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])
    1

    Explanation: Both the red and the blue area are optimal.

    >>> maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])
    3
    """
    pnts = sorted([x for x, y in points])
    ans = 0
    prev = pnts[0]
    for i in range(1, len(pnts)):
        x = pnts[i]
        ans = max(ans, x - prev)
        prev = x
    return ans
