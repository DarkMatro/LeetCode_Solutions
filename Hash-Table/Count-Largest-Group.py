from collections import defaultdict

def countLargestGroup(n: int) -> int:
    """
    ID: 1399
    Tags:   Hash Table, Math
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an integer n.

    Each number from 1 to n is grouped according to the sum of its digits.

    Return the number of groups that have the largest size.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> countLargestGroup(13)
    4

    Explanation: There are 9 groups in total, they are grouped according sum of its digits of
    numbers from 1 to 13:
    [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
    There are 4 groups with largest size.

    >>> countLargestGroup(2)
    2

    Explanation: There are 2 groups [1], [2] of size 1.
    """
    d = defaultdict(int)
    for i in range(1, n + 1):
        s = sum_of_digits(i)
        d[s] += 1
    max_v = d[max(d, key=d.get)]
    return sum([1 for v in d.values() if v == max_v])


def sum_of_digits(n: int) -> int:
    ans = 0
    while True:
        ans += n % 10
        n //= 10
        if n == 0:
            break
    return ans
