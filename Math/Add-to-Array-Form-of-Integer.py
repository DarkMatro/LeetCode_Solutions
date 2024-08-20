def addToArrayForm(num: list[int], k: int) -> list[int]:
    """
    ID: 989
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].
    Given num, the array-form of an integer, and an integer k, return the array-form of the integer
    num + k.

    Parameters
    ----------
    num: list[int]

    k: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> addToArrayForm([1,2,0,0], 34)
    [1, 2, 3, 4]

    Explanation: 1200 + 34 = 1234

    >>> addToArrayForm([2,7,4], 181)
    [4, 5, 5]

    Explanation: 274 + 181 = 455

    >>> addToArrayForm([2, 1, 5], 806)
    [1, 0, 2, 1]

    Explanation: 215 + 806 = 1021
    """
    for i in range(len(num) - 1, -1, -1):
        k, num[i] = divmod(num[i] + k, 10)
    if k == 0:
        return num
    digits = []
    while k != 0:
        digits.append(k % 10)
        k //= 10
    return digits[::-1] + num
