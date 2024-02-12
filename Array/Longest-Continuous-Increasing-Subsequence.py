def findLengthOfLCIS(nums: list[int]) -> int:
    """
    ID: 0674
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence
    (i.e. subarray). The subsequence must be strictly increasing.

    A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l],
    nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> findLengthOfLCIS([1,3,5,4,7])
    3

    Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
    Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by
    element 4.

    >>> findLengthOfLCIS([2,2,2,2,2])
    1

    Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
    increasing.
    """
    n_lcis = 1
    max_lcis = n_lcis
    prev = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num > prev:
            n_lcis += 1
        else:
            max_lcis = max(max_lcis, n_lcis)
            n_lcis = 1
        prev = num
    return max(max_lcis, n_lcis)
