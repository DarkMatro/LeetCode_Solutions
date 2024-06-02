def generate(num_rows: int) -> list[list[int]]:
    """
    ID: 0118
    Tags:   Array, Dynamic Programming
    Time:   O(N^2)
    Memory: O(1)

    Task
    ----------
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    Parameters
    ----------
    num_rows : int

    Returns
    -------
    res : list[list[int]]

    Examples
    --------
    >>> generate(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    >>> generate(1)
    [[1]]
    """
    res = []
    for i in range(1, num_rows + 1):
        tmp = [1] * i
        if i <= 2:
            res.append(tmp)
            continue
        for j in range(1, i - 1):
            tmp[j] = res[i - 2][j] + res[i - 2][j - 1]
        res.append(tmp)
    return res
