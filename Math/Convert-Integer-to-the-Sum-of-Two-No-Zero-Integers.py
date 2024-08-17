def getNoZeroIntegers(n: int) -> list[int]:
    """
    ID: 1317
    Tags:   Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

    Given an integer n, return a list of two integers [a, b] where:

    a and b are No-Zero integers.
    a + b = n
    The test cases are generated so that there is at least one valid solution. If there are many
    valid solutions, you can return any of them.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> getNoZeroIntegers(2)
    [1, 1]

    Explanation: Let a = 1 and b = 1.
    Both a and b are no-zero integers, and a + b = 2 = n.

    >>> getNoZeroIntegers(11)
    [2, 9]

    Explanation: Let a = 2 and b = 9.
    Both a and b are no-zero integers, and a + b = 9 = n.
    Note that there are other valid answers as [8, 3] that can be accepted.
    """
    for i in range(1, n):
        b = n - i
        if not int_contain_zero(b) and not int_contain_zero(i):
            return [i, b]


def int_contain_zero( b: int) -> bool:
    while True:
        dig = b % 10
        if dig == 0:
            return True
        b //= 10
        if b == 0:
            return False
