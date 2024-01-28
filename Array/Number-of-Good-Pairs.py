def numIdenticalPairs(nums: list[int]) -> int:
    """
    ID: 1512
    Tags:   Array, Hash Table, Math, Counting
    Time:   O(N^2)
    Memory: O(1)

    Task
    ----------
    Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out: int

    Examples
    --------
    >>> numIdenticalPairs([1,2,3,1,1,3])
    4

    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

    >>> numIdenticalPairs([1,1,1,1])
    6

    Explanation: Each pair in the array are good.

    >>> numIdenticalPairs([1,2,3])
    0
    """
    k = 0
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if num == nums[j]:
                k += 1
    return k
