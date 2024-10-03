from collections import Counter

def findDuplicates(nums: list[int]) -> list[int]:
    """
    ID: 442
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums of length n where all the integers of nums are in the range [1, n]
    and each integer appears once or twice, return an array of all the integers that appears twice.

    You must write an algorithm that runs in O(n) time and uses only constant auxiliary space,
    excluding the space needed to store the output

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> findDuplicates([4,3,2,7,8,2,3,1])
    [3, 2]

    >>> findDuplicates([1,1,2])
    [1]

    >>> findDuplicates([1])
    []
    """
    return [k for k, v in Counter(nums).items() if v == 2]
