from collections import defaultdict


def adjacent_lamps(i: int, j: int, n: int) -> set[tuple[int]]:
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Верхний ряд
        (0, -1), (0, 1),  # Слева и справа
        (1, -1), (1, 0), (1, 1)  # Нижний ряд
    ]
    ans = set()
    ans.add((i, j))
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            ans.add((ni, nj))
    return ans

def gridIllumination(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    ID: 1001
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially
    turned off.

    You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that
    the lamp at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is
    turned on.

    When a lamp is turned on, it illuminates its cell and all other cells in the same row, column,
    or diagonal.

    You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query,
    determine whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn
    off the lamp at grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if
    its cell shares either a side or corner with grid[rowj][colj].

    Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was
    illuminated, or 0 if the lamp was not.

    Parameters
    ----------
    n: int

    lamps: list[list[int]]

    queries: list[list[int]]

    Returns
    -------
    list[int]

    Examples
    --------
    >>> gridIllumination(5, [[0,0],[4,4]], [[1,1],[1,0]])
    [1, 0]

    Explanation: We have the initial grid with all lamps turned off. In the above picture we see the
    grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
    The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is
    illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.
    The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not
    illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.

    >>> gridIllumination(5, [[0,0],[4,4]], [[1,1],[1,1]])
    [1, 1]

    >>> gridIllumination(5, [[0,0],[0,4]], [[0,4],[0,1],[1,4]])
    [1, 1, 0]
    """
    rows = defaultdict(int)
    cols = defaultdict(int)
    pos_diag = defaultdict(int)
    neg_diag = defaultdict(int)
    lamps_pos = set()
    for row, col in lamps:
        if (row, col) in lamps_pos:
            continue
        rows[row] += 1
        cols[col] += 1
        pos_diag[col - row] += 1
        neg_diag[row + col - (n - 1)] += 1
        lamps_pos.add((row, col))
    ans = []
    for x, y in queries:
        is_on = 1 if (rows.get(x, 0) > 0 or cols.get(y, 0) > 0 or pos_diag.get(y - x, 0) > 0
                      or neg_diag.get(x + y - (n - 1), 0) > 0) else 0
        ans.append(is_on)
        intercept = adjacent_lamps(x, y, n) & lamps_pos
        for i, j in intercept:
            rows[i] -= 1
            cols[j] -= 1
            pos_diag[j - i] -= 1
            neg_diag[i + j - (n - 1)] -= 1
        for lp in intercept:
            lamps_pos.remove(lp)
    return ans
