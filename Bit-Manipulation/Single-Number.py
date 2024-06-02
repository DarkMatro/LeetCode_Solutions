def single_number(nums: list[int]) -> int:
    """
    ID: 0136
    Tags:   Array, Bit Manipulation
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.


    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> single_number([2,2,1])
    1

    >>> single_number([4,1,2,1,2])
    4

    >>> single_number([1])
    1
    """
    j = 0
    for i in nums:
        j ^= i
    return j