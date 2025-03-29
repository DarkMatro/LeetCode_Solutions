def countArrays(original: list[int], bounds: list[list[int]]) -> int:
    """
    ID: 3468
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an array original of length n and a 2D array bounds of length n x 2, where
    bounds[i] = [ui, vi].

    You need to find the number of possible arrays copy of length n such that:

    (copy[i] - copy[i - 1]) == (original[i] - original[i - 1]) for 1 <= i <= n - 1.
    ui <= copy[i] <= vi for 0 <= i <= n - 1.
    Return the number of such arrays.

    Parameters
    ----------
    original: list[int]

    bounds: list[list[int]]

    Returns
    -------
    int

    Examples
    --------
    >>> countArrays([1,2,3,4], [[1,2],[2,3],[3,4],[4,5]])
    2

    Explanation: The possible arrays are:
    [1, 2, 3, 4]
    [2, 3, 4, 5]

    >>> countArrays([1,2,3,4], [[1,10],[2,9],[3,8],[4,7]])
    4

    Explanation: The possible arrays are:
    [1, 2, 3, 4]
    [2, 3, 4, 5]
    [3, 4, 5, 6]
    [4, 5, 6, 7]

    >>> countArrays([1,2,1,2], [[1,1],[2,3],[3,3],[2,3]])
    0

    Explanation: No array is possible.
    """
    n = len(original)

    # Initialize dp range
    dp_low, dp_high = bounds[0][0], bounds[0][1]

    for i in range(1, n):
        diff = original[i] - original[i - 1]

        # Update dp range
        dp_low = max(bounds[i][0], dp_low + diff)
        dp_high = min(bounds[i][1], dp_high + diff)

        # If no valid range exists, return 0
        if dp_low > dp_high:
            return 0

    return dp_high - dp_low + 1
