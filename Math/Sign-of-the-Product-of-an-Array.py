def arraySign(nums: list[int]) -> int:
    """
    ID: 1822
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    There is a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.
    You are given an integer array nums. Let product be the product of all values in the array nums.

    Return signFunc(product).

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> arraySign([-1,-2,-3,-4,3,2,1])
    1

    Explanation: The product of all values in the array is 144, and signFunc(144) = 1

    >>> arraySign([1,5,0,2,-3])
    0

    Explanation: The product of all values in the array is 0, and signFunc(0) = 0

    >>> arraySign([-1,1,-1,1,-1])
    -1

    Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
    """
    ans = nums[0]
    for i in range(1, len(nums)):
        ans *= nums[i]
    if ans == 0:
        return 0
    return 1 if ans > 0 else -1
