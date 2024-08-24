def coloredCells(n: int) -> int:
    """
    ID: 2579
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a
    positive integer n, indicating that you must do the following routine for n minutes:

    At the first minute, color any arbitrary unit cell blue.
    Every minute thereafter, color blue every uncolored cell that touches a blue cell.
    Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.

    Return the number of colored cells at the end of n minutes.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> coloredCells(1)
    1

    Explanation: After 1 minute, there is only 1 blue cell, so we return 1.

    >>> coloredCells(2)
    5

    Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so
    we return 5.
    """
    return n ** 2 + (n - 1) ** 2
