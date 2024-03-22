def partitionDisjoint(nums: list[int]) -> int:
    """
    ID: 0915
    Tags:   Array
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

    Every element in left is less than or equal to every element in right.
    left and right are non-empty.
    left has the smallest possible size.
    Return the length of left after such a partitioning.

    Test cases are generated such that partitioning exists.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> partitionDisjoint([5,0,3,8,6])
    3

    Explanation: left = [5,0,3], right = [8,6]

    >>> partitionDisjoint([1,1,1,0,6,12])
    4

    Explanation: left = [1,1,1,0], right = [6,12]

    >>> partitionDisjoint([90,47,69,10,43,92,31,73,61,97])
    9
    """
    lm = rm = nums[0]
    idx = 0
    for i in range(1, len(nums)):
        num = nums[i]
        rm = max(rm, num)
        if num < lm:
            lm = rm
            idx = i
    return idx + 1
