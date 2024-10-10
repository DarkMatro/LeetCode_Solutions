def alphabetBoardPath(target: str) -> str:
    """
    ID: 1138
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

    Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

    We may make the following moves:

    'U' moves our position up one row, if the position exists on the board;
    'D' moves our position down one row, if the position exists on the board;
    'L' moves our position left one column, if the position exists on the board;
    'R' moves our position right one column, if the position exists on the board;
    '!' adds the character board[r][c] at our current position (r, c) to the answer.
    (Here, the only positions that exist on the board are positions with letters on them.)

    Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
    You may return any path that does so.

    Parameters
    ----------
    target: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> alphabetBoardPath('leet')
    'DDR!UURRR!!DDD!'

    >>> alphabetBoardPath('code')
    'RR!DDRR!LUU!R!'
    """
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    d = {k: (i, j) for i, r in enumerate(board) for j, k in enumerate(r)}
    x = y = 0
    ans = ''
    for t in target:
        x_, y_ = d[t]
        if y_ < y:
            ans += 'L' * (y - y_)
        if x_ > x:
            ans += 'D' * (x_ - x)
        if x_ < x:
            ans += 'U' * (x - x_)
        if y_ > y:
            ans += 'R' * (y_ - y)
        ans += '!'
        x = x_
        y = y_
    return ans
