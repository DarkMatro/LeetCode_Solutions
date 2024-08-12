def minimumOperations(nums: list[int]) -> int:
    """
    ID: 3190
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums. In one operation, you can add or subtract 1 from any
    element of nums.

    Return the minimum number of operations to make all elements of nums divisible by 3.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> minimumOperations([1,2,3,4])
    3

    Explanation: All array elements can be made divisible by 3 using 3 operations:

    Subtract 1 from 1.
    Add 1 to 2.
    Subtract 1 from 4.

    >>> minimumOperations([3,6,9])
    0
    """
    ans = 0
    for x in nums:
        if x % 3 != 0:
            ans += min(x % 3, 3 - (x % 3))
    return ans
