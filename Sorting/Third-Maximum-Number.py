def thirdMax(nums: list[int]) -> int:
    """
    ID: 414
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Given an integer array nums, return the third distinct maximum number in this array. If the
    third maximum does not exist, return the maximum number.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> thirdMax([3,2,1])
    1

    Explanation: The first distinct maximum is 3.
    The second distinct maximum is 2.
    The third distinct maximum is 1.

    >>> thirdMax([1,2])
    2

    Explanation: The first distinct maximum is 2.
    The second distinct maximum is 1.
    The third distinct maximum does not exist, so the maximum (2) is returned instead.

    >>> thirdMax([2,2,3,1])
    1

    Explanation: The first distinct maximum is 3.
    The second distinct maximum is 2 (both 2's are counted together since they have the same value).
    The third distinct maximum is 1.
    """
    sl = list(set(nums))
    return sorted(sl)[-3] if len(sl) >= 3 else sl[-1]
