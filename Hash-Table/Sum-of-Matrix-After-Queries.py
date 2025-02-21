def matrixSumQueries(n: int, queries: list[list[int]]) -> int:
    """
    ID: 2718
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an integer n and a 0-indexed 2D array queries where
    queries[i] = [typei, indexi, vali].

    Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one
    of the following changes:

    if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
    if typei == 1, set the values in the column with indexi to vali, overwriting any previous values
    Return the sum of integers in the matrix after all queries are applied.

    Parameters
    ----------
    n: int

    queries: list[list[int]]

    Returns
    -------
    int

    Examples
    --------
    >>> matrixSumQueries(3, [[0,0,1],[1,2,2],[0,2,3],[1,0,4]])
    23

    Explanation: The image above describes the matrix after each query. The sum of the matrix after
    all queries are applied is 23.

    >>> matrixSumQueries(3, [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]])
    17

    Explanation: The image above describes the matrix after each query. The sum of the matrix after
    all queries are applied is 17.
    """
    col_visited = set()
    row_visited = set()
    ans = 0
    for a, b, c in reversed(queries):
        if a == 1 and b not in col_visited:
            col_visited.add(b)
            ans += (n - len(row_visited)) * c
        elif a == 0 and b not in row_visited:
            row_visited.add(b)
            ans += (n - len(col_visited)) * c
    return ans
