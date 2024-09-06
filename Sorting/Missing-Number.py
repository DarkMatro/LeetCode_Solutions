def missing_number(nums: list[int]) -> int:
    """
    ID: 0268
    Tags:   Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
    missing from the array.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> missing_number([3,0,1])
    2

    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the
    range since it does not appear in nums.

    >>> missing_number([0,1])
    2

    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the
    range since it does not appear in nums.

    >>> missing_number([9,6,4,2,3,5,7,0,1])
    8

    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the
    range since it does not appear in nums.
    """
    n = len(nums)
    res = [0] * (n + 1)
    for i in nums:
        res[i] += 1
    return res.index(0)
