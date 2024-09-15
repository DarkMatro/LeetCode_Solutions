def findDisappearedNumbers(nums: list[int]) -> list[int]:
    """
    ID: 448
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all
    the integers in the range [1, n] that do not appear in nums.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> findDisappearedNumbers([4,3,2,7,8,2,3,1])
    [5, 6]

    >>> findDisappearedNumbers([1, 1])
    [2]
    """
    return list(set(range(1, len(nums) + 1)) ^ set(nums))
