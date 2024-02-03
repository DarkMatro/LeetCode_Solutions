def isMonotonic(nums: list[int]) -> bool:
    """
    ID: 896
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    An array is monotonic if it is either monotone increasing or monotone decreasing.

    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing
    if for all i <= j, nums[i] >= nums[j].

    Given an integer array nums, return true if the given array is monotonic, or false otherwise.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isMonotonic([1,2,2,3])
    True

    >>> isMonotonic([6,5,4,4])
    True

    >>> isMonotonic([1,3,2])
    False
    """
    increasing = True
    decreasing = True
    prev = nums[0]
    for i in range(1, len(nums)):
        cur_v = nums[i]
        if cur_v < prev:
            increasing = False
        elif cur_v > prev:
            decreasing = False
        if not (increasing or decreasing):
            return False
        prev = cur_v
    return increasing or decreasing
