def minOperations(nums: list[int], k: int) -> int:
    """
    ID: 3065
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed integer array nums, and an integer k.

    In one operation, you can remove one occurrence of the smallest element of nums.

    Return the minimum number of operations needed so that all elements of the array are greater
    than or equal to k.

    Parameters
    ----------
    nums : list[int]

    k: int

    Returns
    -------
    ans : int

    Examples
    --------
    >>> minOperations([2,11,10,1,3], 10)
    3

    Explanation: After one operation, nums becomes equal to [2, 11, 10, 3].
    After two operations, nums becomes equal to [11, 10, 3].
    After three operations, nums becomes equal to [11, 10].
    At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
    It can be shown that 3 is the minimum number of operations needed so that all elements of the
    array are greater than or equal to 10.
    Example 2:

    >>> minOperations([1,1,2,4,9], 1)
    0

    Explanation: All elements of the array are greater than or equal to 1 so we do not need to
    apply any operations on nums.

    >>> minOperations([1,1,2,4,9], 9)
    4

    Explanation: only a single element of nums is greater than or equal to 9 so we need to apply
    the operations 4 times on nums.
    """
    ans = 0
    for num in nums:
        if num < k:
            ans += 1
    return ans
