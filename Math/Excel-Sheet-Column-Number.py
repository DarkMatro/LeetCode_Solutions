def title_to_number(column_title: str) -> int:
    """
    ID: 0171
    Tags:   Math, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding
    column number.

    Parameters
    ----------
    column_title : int

    Returns
    -------
    res : int

    Examples
    --------
    >>> title_to_number('A')
    1

    >>> title_to_number('AB')
    28

    >>> title_to_number('ZY')
    701

    """
    nums = list(range(1, 27))
    lt = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
    n = len(column_title)
    if n == 1:
        return nums[lt.index(column_title)]
    p = []
    for i in column_title:
        p.append(nums[lt.index(i)])
    res = 0
    for i in range(1, n):
        res = res + p[i - 1] * 26 ** (n - i)
    res += p[-1]
    return res
