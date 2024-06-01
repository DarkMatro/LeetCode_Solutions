def two_sum(nums: list[int], target: int) -> list[int]:
    """
    ID: 0001
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
     target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Parameters
    ----------
    nums: list[int]
        array of integers
    target: int

    Returns
    -------
    list[int]
    indices of the two numbers such that they add up to target

    Examples
    --------
    >>> two_sum([2,7,11,15], 9)
    [0, 1]

    Because nums[0] + nums[1] == 9, we return [0, 1].

    >>> two_sum([3,2,4], 6)
    [1, 2]

    >>> two_sum([3,3], 6)
    [0, 1]
    """
    d = {}
    for i, j in enumerate(nums):
        c = target - j
        if c in d:
            return [d[c], i]
        d[j] = i
