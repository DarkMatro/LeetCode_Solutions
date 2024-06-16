def minDeletionSize(strs: list[str]) -> int:
    """
    ID: 0944
    Tags:   Array, String
    Time:   O(N * M)
    Memory: O(1)

    Task
    ----------
    You are given an array of n strings strs, all the same length.

    The strings can be arranged such that there is one on each line, making a grid.

    For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
    abc
    bce
    cae
    You want to delete the columns that are not sorted lexicographically. In the above example
    (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1
    ('b', 'c', 'a') is not, so you would delete column 1.

    Return the number of columns that you will delete.

    Parameters
    ----------
    strs: list[str]

    Returns
    -------
    out: int

    Examples
    --------
    >>> minDeletionSize(["cba","daf","ghi"])
    1

    Explanation: The grid looks as follows:
      cba
      daf
      ghi
    Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

    >>> minDeletionSize(["a","b"])
    0

    Explanation: The grid looks as follows:
      a
      b
    Column 0 is the only column and is sorted, so you will not delete any columns.

    >>> minDeletionSize(["zyx","wvu","tsr"])
    3

    Explanation: The grid looks as follows:
      zyx
      wvu
      tsr
    All 3 columns are not sorted, so you will delete all 3.
    """
    n = len(strs[0])
    ans = 0
    for col_id in range(n):
        prev_id = ord(strs[0][col_id])
        for i in range(1, len(strs)):
            current_id = ord(strs[i][col_id])
            if current_id < prev_id:
                ans += 1
                break
            prev_id = current_id
    return ans
