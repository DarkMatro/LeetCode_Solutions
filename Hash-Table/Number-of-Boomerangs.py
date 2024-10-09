from collections import defaultdict


def numberOfBoomerangs(points: list[list[int]]) -> int:
    """
    ID: 447
    Tags:   Array, Hash Table, Math
    Time:   O(N^2)
    Memory: O(N)

    Task
    ----------
    You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A
    boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the
    distance between i and k (the order of the tuple matters).

    Return the number of boomerangs.

    Parameters
    ----------
    points: list[list[int]]

    Returns
    -------
    out : int

    Examples
    --------
    >>> numberOfBoomerangs([[0,0],[1,0],[2,0]])
    2

    Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

    >>> numberOfBoomerangs([[1,1],[2,2],[3,3]])
    2

    >>> numberOfBoomerangs([[1,1]])
    0
    """
    if len(points) < 3:
        return 0
    ans = 0
    for x, y in points:
        d = defaultdict(int)
        for z, q in points:
            dist = (x - z) ** 2 + (y - q) ** 2
            d[dist] += 1
        for dist in d.values():
            ans += dist * (dist - 1)
    return ans
