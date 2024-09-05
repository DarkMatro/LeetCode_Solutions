def climb_stairs(n: int) -> int:
    """
    ID: 0070
    Tags:   Math, Dynamic Programming, Memoization
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Parameters
    ----------
    n : int

    Returns
    -------
    res : int

    Examples
    --------
    >>> climb_stairs(2)
    2

    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    >>> climb_stairs(3)
    3

    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

    >>> climb_stairs(4)
    5
    >>> climb_stairs(5)
    8
    >>> climb_stairs(6)
    13
    >>> climb_stairs(7)
    21
    >>> climb_stairs(8)
    34
    """
    s, q = 1, 2
    for _ in range(2, n):
        # swapping `s` and `q`
        s, q = q, s + q
    return q if n > 1 else s
