def sumCounts(nums: list[int]) -> int:
    """
    ID: 2913
    Tags:   Array, Hash Table
    Time:   O(N^2)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed integer array nums.

    The distinct count of a subarray of nums is defined as:

    Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that
    0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the
    distinct count of nums[i..j].
    Return the sum of the squares of distinct counts of all subarrays of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumCounts([1,2,1])
    15

    Explanation: Six possible subarrays are:
    [1]: 1 distinct value
    [2]: 1 distinct value
    [1]: 1 distinct value
    [1,2]: 2 distinct values
    [2,1]: 2 distinct values
    [1,2,1]: 2 distinct values
    The sum of the squares of the distinct counts in all subarrays is equal to
    12 + 12 + 12 + 22 + 22 + 22 = 15.

    >>> sumCounts([1,1])
    3

    Explanation: Three possible subarrays are:
    [1]: 1 distinct value
    [1]: 1 distinct value
    [1,1]: 1 distinct value
    The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
    """
    ans = 0
    for i in range(len(nums)):
        s = set()
        for j in range(i, len(nums)):
            s.add(nums[j])
            ans += len(s) ** 2
    return ans
