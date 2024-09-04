def isReachableAtTime(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    """
    ID: 2849
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given four integers sx, sy, fx, fy, and a non-negative integer t.

    In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its
    adjacent cells.

    Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

    A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You
    can visit the same cell several times.

    Parameters
    ----------
    sx: int
    sy: int
    fx: int
    fy: int
    t: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isReachableAtTime(2, 4, 7, 7, 6)
    True

    Explanation: Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going
    through the cells depicted in the picture above.

    >>> isReachableAtTime(3, 1, 7, 3, 3)
    False

    Explanation: Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going
    through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third
    second.
    """
    if sx == fx and sy == fy and t == 1:
        return False
    chebyshev_distance = max(abs(fx - sx), abs(fy - sy))
    return t >= chebyshev_distance
