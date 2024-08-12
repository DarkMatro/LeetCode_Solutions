def sumOfMultiples(n: int) -> int:
    """
    ID: 2652
    Tags:   Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are
    divisible by 3, 5, or 7.

    Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumOfMultiples(7)
    21

    Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The
    sum of these numbers is 21.

    >>> sumOfMultiples(10)
    40

    Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9,
    10. The sum of these numbers is 40.

    >>> sumOfMultiples(9)
    30

    Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9.
    The sum of these numbers is 30.
    """
    return sum([i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0])
