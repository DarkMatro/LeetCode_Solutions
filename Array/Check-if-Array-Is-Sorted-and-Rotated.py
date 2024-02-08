def check(nums: list[int]) -> bool:
    """
    ID: 1752
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some
    number of positions (including zero). Otherwise, return false.

    There may be duplicates in the original array.

    Note: An array A rotated by x positions results in an array B of the same length such that
    A[i] == B[(i+x) % A.length], where % is the modulo operation.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> check([3,4,5,1,2])
    True

    Explanation: [1,2,3,4,5] is the original sorted array.
    You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

    >>> check([2,1,3,4])
    False

    Explanation: There is no sorted array once rotated that can make nums.

    >>> check([1,2,3])
    True

    Explanation: [1,2,3] is the original sorted array.
    You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
    """
    n_pivots = 0
    for i, num in enumerate(nums):
        if num < nums[i - 1]:
            n_pivots += 1
            if n_pivots > 1:
                return False
    return True
