def minCuttingCost(n: int, m: int, k: int) -> int:
    """
    ID: 3560
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given integers n, m, and k.

    There are two logs of lengths n and m units, which need to be transported in three trucks where each truck can
    carry one log with length at most k units.

    You may cut the logs into smaller pieces, where the cost of cutting a log of length x into logs of length len1 and
    len2 is cost = len1 * len2 such that len1 + len2 = x.

    Return the minimum total cost to distribute the logs onto the trucks. If the logs don't need to be cut, the total
    cost is 0.

    Parameters
    ----------
    n: int

    m: int

    k: int

    Returns
    -------
    int

    Examples
    --------
    >>> minCuttingCost(6, 5, 5)
    5

    Explanation:

    Cut the log with length 6 into logs with length 1 and 5, at a cost equal to 1 * 5 == 5. Now the three logs of
    length 1, 5, and 5 can fit in one truck each.

    >>> minCuttingCost(4, 4, 6)
    0

    Explanation:

    The two logs can fit in the trucks already, hence we don't need to cut the logs.
    """
    x = max(n, m)
    if x <= k:
        return 0
    return (x - k) * k
