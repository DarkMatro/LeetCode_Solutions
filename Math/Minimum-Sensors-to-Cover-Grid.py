import math


def minSensors(n: int, m: int, k: int) -> int:
    """
    ID: 3648
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given n × m grid and an integer k.

    A sensor placed on cell (r, c) covers all cells whose Chebyshev distance from (r, c) is at most k.

    The Chebyshev distance between two cells (r1, c1) and (r2, c2) is max(|r1 − r2|,|c1 − c2|).

    Your task is to return the minimum number of sensors required to cover every cell of the grid.

    Parameters
    ----------
    n: int

    m: int

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> minSensors(5, 5, 1)
    4

    Explanation: Placing sensors at positions (0, 3), (1, 0), (3, 3), and (4, 1) ensures every cell in the grid is
    covered. Thus, the answer is 4.

    >>> minSensors(2, 2, 2)
    1

    Explanation: With k = 2, a single sensor can cover the entire 2 * 2 grid regardless of its position.
    Thus, the answer is 1.
    """
    size = 2 * k + 1
    return math.ceil(n / size) * math.ceil(m / size)
