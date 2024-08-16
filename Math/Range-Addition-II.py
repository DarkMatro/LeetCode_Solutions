def maxCount(m: int, n: int, ops: list[list[int]]) -> int:
    """
    ID: 598
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an m x n matrix M initialized with all 0's and an array of operations ops, where
    ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai
    and 0 <= y < bi.

    Count and return the number of maximum integers in the matrix after performing all the
    operations.

    Parameters
    ----------
    m: int

    n: int

    ops: list[list[int]]

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxCount(3, 3, [[2,2],[3,3]])
    4

    Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

    >>> maxCount(3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]])
    4

    >>> maxCount(3, 3, [])
    9
    """
    if not ops:
        return m * n
    min_a = min(op[0] for op in ops)
    min_b = min(op[1] for op in ops)
    return min_a * min_b
