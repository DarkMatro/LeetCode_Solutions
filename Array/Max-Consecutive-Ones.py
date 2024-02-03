def findMaxConsecutiveOnes(nums: list[int]) -> int:
    """
    ID: 485
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a binary array nums, return the maximum number of consecutive 1's in the array.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> findMaxConsecutiveOnes([1,1,0,1,1,1])
    3

    >>> findMaxConsecutiveOnes([1,0,1,1,0,1])
    2
    """
    size = 0
    max_size = 0
    for num in nums:
        if num == 1:
            size += 1
        else:
            max_size = max(max_size, size)
            size = 0
    return max(max_size, size)
