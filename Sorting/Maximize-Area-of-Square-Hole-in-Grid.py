def maximizeSquareHoleArea(n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
    """
    ID: 2943
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has
    n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed
    starting from 1.

    You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from
    vertical bars. Note that other bars are fixed and cannot be removed.

    Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing
    some bars (possibly none).

    Parameters
    ----------
    n: int

    m: int

    hBars: list[int]

    vBars: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> maximizeSquareHoleArea(2, 1, [2,3], [2])
    4

    Explanation: The left image shows the initial grid formed by the bars. The horizontal bars are
    [1,2,3,4], and the vertical bars are [1,2,3].

    One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2

    >>> maximizeSquareHoleArea(1, 1, [2], [2])
    4

    Explanation: To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar
    2.

    >>> maximizeSquareHoleArea(2, 3, [2,3], [2,4])
    4

    Explanation: One way to get the maximum square-shaped hole is by removing horizontal bar 3, and
    vertical bar 4.
    """

    def max_consecutive_length(bars):
        bars.sort()
        max_len = 1
        current_len = 1

        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1

        return max(max_len, current_len)

    max_h = max_consecutive_length(hBars)
    max_v = max_consecutive_length(vBars)

    return (min(max_h, max_v) + 1) ** 2
