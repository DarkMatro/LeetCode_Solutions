def selfDividingNumbers(left: int, right: int) -> list[int]:
    """
    ID: 728
    Tags:   Math
    Time:   O((Right−Left)∗Log(Right))
    Memory: O(1)

    Task
    ----------
    A self-dividing number is a number that is divisible by every digit it contains.

    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
    A self-dividing number is not allowed to contain the digit zero.

    Given two integers left and right, return a list of all the self-dividing numbers in the range
    [left, right].

    Parameters
    ----------
    left: int

    right: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> selfDividingNumbers(1, 22)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


    >>> selfDividingNumbers(47, 85)
    [48, 55, 66, 77]
    """
    ans = []
    for i in range(left, right + 1):
        n = i + 0
        while True:
            dig = n % 10
            if dig == 0 or i % dig != 0:
                break
            n //= 10
            if n == 0:
                ans.append(i)
                break
    return ans
