def maximumProduct(nums: list[int]) -> int:
    """
    ID: 628
    Tags:   Array, Math, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums, find three numbers whose product is maximum and return the maximum
    product.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> maximumProduct([1,2,3])
    6

    >>> maximumProduct([1,2,3,4])
    24

    >>> maximumProduct([-1,-2,-3])
    -6
    """
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
