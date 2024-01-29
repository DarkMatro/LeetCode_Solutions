def searchInsert(nums: list[int], target: int) -> int:
    """
    ID: 0035
    Tags:   Array, Binary Search
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
    return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    Parameters
    ----------
    nums: list[int]

    target: int

    Returns
    -------
    int

    Examples
    --------
    >>> searchInsert([1,3,5,6], 5)
    2

    >>> searchInsert([1,3,5,6], 2)
    1

    >>> searchInsert([1,3,5,6], 7)
    4
    """
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        diff = target - nums[mid]
        if diff == 0:
            return mid
        elif diff > 0:
            lo = mid + 1
        elif diff < 0:
            hi = mid - 1
    return lo

