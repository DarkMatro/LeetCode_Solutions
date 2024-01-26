def is_happy(n: int) -> bool:
    """
    ID: 0202
    Tags:   Hash Table, Math, Two Pointers
    Time:   O(k) , where k is the steps to be happy number
    Memory: O(k)

    Task
    ----------
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
    include 1.
    Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.


    Parameters
    ----------
    n : int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> is_happy(19)
    True

    Explanation:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

    >>> is_happy(2)
    False
    """
    ns = list(str(n))
    prev = None
    res = 0
    k = 0
    while res != 1 and k < 10:
        res = 0
        for i in ns:
            res += int(i) ** 2
        if res == prev:
            return False
        prev = res
        if res == 1:
            return True
        ns = list(str(res))
        k += 1
    return False
