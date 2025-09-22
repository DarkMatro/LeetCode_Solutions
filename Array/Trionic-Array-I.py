def isTrionic(nums: list[int]) -> bool:
    """
    ID: 3637
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums of length n.

    An array is trionic if there exist indices 0 < p < q < n − 1 such that:

    nums[0...p] is strictly increasing,
    nums[p...q] is strictly decreasing,
    nums[q...n − 1] is strictly increasing.
    Return true if nums is trionic, otherwise return false.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    bool

    Examples
    --------
    >>> isTrionic([1,3,5,4,2,6])
    True

    Explanation:

    Pick p = 2, q = 4:

    nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
    nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
    nums[4...5] = [2, 6] is strictly increasing (2 < 6).

    >>> isTrionic([2,1,3])
    False

    Explanation:

    There is no way to pick p and q to form the required three segments.
    """
    n = len(nums)
    if n < 3:
        return False

    i = 0

    # Step 1: strictly increasing
    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1

    p = i
    if p == 0 or p == n - 1:  # must increase at least once, not at end
        return False

    # Step 2: strictly decreasing
    while i + 1 < n and nums[i] > nums[i + 1]:
        i += 1

    q = i
    if q == p or q == n - 1:  # must decrease at least once, not at end
        return False

    # Step 3: strictly increasing again
    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1

    # If we consumed the array and all conditions satisfied
    return i == n - 1
