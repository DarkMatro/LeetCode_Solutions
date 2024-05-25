def longestMonotonicSubarray(nums: list[int]) -> int:
    """
    ID: 3105
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an array of integers nums. Return the length of the longest  subarray
    of nums which is either strictly increasing or strictly decreasing.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> longestMonotonicSubarray([1,4,3,3,2])
    2

    Explanation: The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
    The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
    Hence, we return 2.

    >>> longestMonotonicSubarray([3,3,3,3])
    1

    Explanation: The strictly increasing subarrays of nums are [3], [3], [3], and [3].
    The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
    Hence, we return 1.

    >>> longestMonotonicSubarray([3,2,1])
    3

    Explanation: The strictly increasing subarrays of nums are [3], [2], and [1].
    The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
    Hence, we return 3.
    """
    inc = 1
    max_inc = 1
    dec = 1
    max_dec = 1
    prev = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num > prev:
            inc += 1
        if num <= prev:
            inc = 1
        if num >= prev:
            dec = 1
        if num < prev:
            dec += 1
        max_inc = max(max_inc, inc)
        max_dec = max(max_dec, dec)
        prev = num
    return max(max_inc, max_dec)
