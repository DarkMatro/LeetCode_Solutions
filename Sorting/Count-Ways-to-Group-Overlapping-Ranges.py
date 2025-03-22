def countWays(ranges: list[list[int]]) -> int:
    """
    ID: 2580
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given a 2D integer array ranges where ranges[i] = [starti, endi] denotes that all
    integers between starti and endi (both inclusive) are contained in the ith range.

    You are to split ranges into two (possibly empty) groups such that:

    Each range belongs to exactly one group.
    Any two overlapping ranges must belong to the same group.
    Two ranges are said to be overlapping if there exists at least one integer that is present in
    both ranges.

    For example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges.
    Return the total number of ways to split ranges into two groups. Since the answer may be very
    large, return it modulo 109 + 7.

    Parameters
    ----------
    ranges: list[list[int]]

    Returns
    -------
    int

    Examples
    --------
    >>> countWays([[6,10],[5,15]])
    2

    Explanation: The two ranges are overlapping, so they must be in the same group.
    Thus, there are two possible ways:
    - Put both the ranges together in group 1.
    - Put both the ranges together in group 2.

    >>> countWays([[1,3],[10,20],[2,5],[4,8]])
    4

    Explanation: Ranges [1,3], and [2,5] are overlapping. So, they must be in the same group.
    Again, ranges [2,5] and [4,8] are also overlapping. So, they must also be in the same group.
    Thus, there are four possible ways to group them:
    - All the ranges in group 1.
    - All the ranges in group 2.
    - Ranges [1,3], [2,5], and [4,8] in group 1 and [10,20] in group 2.
    - Ranges [1,3], [2,5], and [4,8] in group 2 and [10,20] in group 1.
    """
    ranges.sort()

    components = 0
    prev_start, prev_end = -1, -1

    for start, end in ranges:
        if start > prev_end:
            # Found a new connected component
            components += 1
            prev_start, prev_end = start, end
        else:
            # Merge overlapping ranges
            prev_end = max(prev_end, end)

    # The number of ways to split the ranges is 2^components % MOD
    return pow(2, components, 10 ** 9 + 7)
