def maximumProduct(nums: list[int], m: int) -> int:
    """
    ID: 3584
    Tags:   Array, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums and an integer m.

    Return the maximum product of the first and last elements of any subsequence of nums of size m.

    Parameters
    ----------
    nums: list[int]

    m: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> maximumProduct([-1,-9,2,3,-2,-3,1], 1)
    81

    Explanation: The subsequence [-9] has the largest product of the first and last elements: -9 * -9 = 81. Therefore,
    the answer is 81.

    >>> maximumProduct([1,3,-5,5,6,-4], 3)
    20

    Explanation: The subsequence [-5, 6, -4] has the largest product of the first and last elements.

    >>> maximumProduct([2,-1,2,-6,5,2,-5,7], 2)
    35

    Explanation: The subsequence [5, 7] has the largest product of the first and last elements.
    """
    n = len(nums)
    max_product = float('-inf')

    max_val = float('-inf')  # largest nums[i] so far (valid i)
    min_val = float('inf')  # smallest nums[i] so far (valid i)

    for j in range(m - 1, n):  # j is last index
        i = j - (m - 1)  # first valid index that can pair with j
        val = nums[i]

        # update candidates
        max_val = max(max_val, val)
        min_val = min(min_val, val)

        # check products
        max_product = max(max_product, nums[j] * max_val, nums[j] * min_val)

    return max_product
