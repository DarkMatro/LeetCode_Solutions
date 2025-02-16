def minOperations(nums: list[int], k: int) -> int:
    """
    ID: 3375
    Tags: Array, Hash Table
    Time: O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums and an integer k.

    An integer h is called valid if all values in the array that are strictly greater than h are
    identical.

    For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are
    equal to 10, but 5 is not a valid integer.

    You are allowed to perform the following operation on nums:

    Select an integer h that is valid for the current values in nums.
    For each index i where nums[i] > h, set nums[i] to h.
    Return the minimum number of operations required to make every element in nums equal to k. If
    it is impossible to make all elements equal to k, return -1.

    Parameters
    ----------
    nums: list[int]

    k: int

    Returns
    -------
    int

    Examples
    --------
    >>> minOperations([5,2,5,4,5], 2)
    2

    Explanation:
    The operations can be performed in order using valid integers 4 and then 2.

    >>> minOperations([2,1,2], 2)
    -1

    Explanation:
    It is impossible to make all the values equal to 2.

    >>> minOperations([9,7,5,3], 1)
    4

    Explanation:
    The operations can be performed using valid integers in the order 7, 5, 3, and 1.
    """
    s = set(nums)
    min_num = min(s)
    if min_num < k:
        return -1
    elif min_num > k:
        return len(s)
    else:
        return len(s) - 1
