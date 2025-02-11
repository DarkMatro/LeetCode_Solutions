def maxAdjacentDistance(nums: list[int]) -> int:
    """
    ID: 3423
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a circular array nums, find the maximum absolute difference between adjacent elements.

    Note: In a circular array, the first and last elements are adjacent.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> maxAdjacentDistance([1,2,4])
    3

    Explanation:

    Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute
    difference of |4 - 1| = 3.

    >>> maxAdjacentDistance([-5,-10,-5])
    5

    Explanation:

    The adjacent elements nums[0] and nums[1] have the maximum absolute difference of
    |-5 - (-10)| = 5.
    """
    prev = nums[0]
    ans = abs(prev - nums[-1])
    for i, v in enumerate(nums):
        ans = max(ans, abs(v - prev))
        prev = v
    return ans
