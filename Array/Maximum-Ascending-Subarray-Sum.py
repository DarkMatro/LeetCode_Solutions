def maxAscendingSum(nums: list[int]) -> int:
    """
    ID: 1800
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

    A subarray is defined as a contiguous sequence of numbers in an array.

    A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1.
    Note that a subarray of size 1 is ascending.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxAscendingSum([10,20,30,5,10,50])
    65

    Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

    >>> maxAscendingSum([10,20,30,40,50])
    150

    [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

    >>> maxAscendingSum([12,17,15,13,10,11,12])
    33

    [10,11,12] is the ascending subarray with the maximum sum of 33.
    """
    max_sum = 0
    s = nums[0]
    for i in range(1, len(nums)):
        cur_v = nums[i]
        if cur_v > nums[i - 1]:
            s += cur_v
        else:
            max_sum = max(max_sum, s)
            s = cur_v

    return max(max_sum, s)
