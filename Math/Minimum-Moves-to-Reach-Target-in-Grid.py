def minMoves(sx: int, sy: int, tx: int, ty: int) -> int:
    """
    ID: 3609
    Tags:   Math
    Time:   O(log(max(tx, yx)))
    Memory: O(1)

    Task
    ----------
    You are given four integers sx, sy, tx, and ty, representing two points (sx, sy) and (tx, ty) on an infinitely large
    2D grid.

    You start at (sx, sy).

    At any point (x, y), define m = max(x, y). You can either:

    Move to (x + m, y), or
    Move to (x, y + m).
    Return the minimum number of moves required to reach (tx, ty). If it is impossible to reach the target, return -1.

    Parameters
    ----------
    sx: int

    sy: int

    tx: int

    ty: int

    Returns
    -------
    int

    Examples
    --------
    >>> minMoves(1, 2, 5, 4)
    2

    Explanation:

    The optimal path is:

    Move 1: max(1, 2) = 2. Increase the y-coordinate by 2, moving from (1, 2) to (1, 2 + 2) = (1, 4).
    Move 2: max(1, 4) = 4. Increase the x-coordinate by 4, moving from (1, 4) to (1 + 4, 4) = (5, 4).
    Thus, the minimum number of moves to reach (5, 4) is 2.

    >>> minMoves(0, 1, 2, 3)
    3

    Explanation:

    The optimal path is:

    Move 1: max(0, 1) = 1. Increase the x-coordinate by 1, moving from (0, 1) to (0 + 1, 1) = (1, 1).
    Move 2: max(1, 1) = 1. Increase the x-coordinate by 1, moving from (1, 1) to (1 + 1, 1) = (2, 1).
    Move 3: max(2, 1) = 2. Increase the y-coordinate by 2, moving from (2, 1) to (2, 1 + 2) = (2, 3).
    Thus, the minimum number of moves to reach (2, 3) is 3.

    >>> minMoves(1, 1, 2, 2)
    -1

    Explanation:

    It is impossible to reach (2, 2) from (1, 1) using the allowed moves. Thus, the answer is -1.
    """
    ans = 0
    x = tx + 0
    y = ty + 0
    while x > sx or y > sy:
        ans += 1

        if x < y or x == y and sx > sy:
            x, y, sx, sy = y, x, sy, sx

        if x >= 2 * y:
            if x % 2:
                return -1
            x //= 2
        else:
            x -= y

    return ans if x == sx and y == sy else -1
