def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
    """
    ID: 780
    Tags:   Math
    Time:   O(log(max(tx,ty)))
    Memory: O(1)

    Task
    ----------
    Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point
    (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

    The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

    Parameters
    ----------
    sx: int
    sy: int
    tx: int
    ty: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> reachingPoints(1, 1, 3, 5)
    True

    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)

    >>> reachingPoints(1, 1, 2, 2)
    False

    >>> reachingPoints(1, 1, 1, 1)
    True
    """
    while tx > sx and ty > sy:
        if tx > ty:
            tx %= ty
        else:
            ty %= tx

    # Now either tx == sx or ty == sy
    if tx == sx and ty >= sy and (ty - sy) % sx == 0:
        return True
    if ty == sy and tx >= sx and (tx - sx) % sy == 0:
        return True

    return False
