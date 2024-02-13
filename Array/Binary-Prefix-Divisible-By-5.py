def prefixesDivBy5(nums: list[int]) -> list[bool]:
    """
    ID: 1018
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a binary array nums (0-indexed).

    We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to
    least-significant-bit).

    For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
    Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : list[bool]

    Examples
    --------
    >>> prefixesDivBy5([0,1,1])
    [True, False, False]

    Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
    Only the first number is divisible by 5, so answer[0] is true.

    >>> prefixesDivBy5([1,1,1])
    [False, False, False]

    >>> prefixesDivBy5([0,1,1,1,1,1])
    [True, False, False, False, True, False]
    """
    n = len(nums)
    ans = [False] * n
    num = 0
    for i in range(n):
        num = (num * 2 + nums[i]) % 5
        ans[i] = num == 0
    return ans
