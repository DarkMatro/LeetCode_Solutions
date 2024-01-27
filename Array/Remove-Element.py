def remove_element(nums: list[int], val: int) -> int:
    """
    ID: 0027
    Tags:   Array, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
    elements may be changed. Then return the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the
    following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The
    remaining elements of nums are not important as well as the size of nums.
    Return k.

    Parameters
    ----------
    nums : list[int]

    val : int

    Returns
    -------
    out : int

    Examples
    --------
    >>> remove_element([3,2,2,3], 3)
    2

    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    >>> remove_element([0,1,2,2,3,0,4,2], 2)
    5

    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    """
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1
    return k
