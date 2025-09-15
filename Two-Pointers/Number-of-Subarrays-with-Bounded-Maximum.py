def numSubarrayBoundedMax(nums: list[int], left: int, right: int) -> int:
    """
    ID: 795
    Tags:   Array, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays
    such that the value of the maximum array element in that subarray is in the range [left, right].

    The test cases are generated so that the answer will fit in a 32-bit integer.

    Parameters
    ----------
    nums: list[int]

    left: int

    right: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> numSubarrayBoundedMax([2,1,4,3], 2, 3)
    3

    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

    >>> numSubarrayBoundedMax([2,9,2,5,6], 2, 8)
    7
    """
    def f(bound):
        count = 0
        res = 0
        for num in nums:
            if num <= bound:
                count += 1
                res += count
            else:
                count = 0
        return res

    return f(right) - f(left - 1)