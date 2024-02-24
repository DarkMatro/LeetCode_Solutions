def canBeIncreasing(nums: list[int]) -> bool:
    """
    ID: 1909
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one
    element, or false otherwise. If the array is already strictly increasing, return true.

    The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> canBeIncreasing([1,2,10,5,7])
    True

    Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
    [1,2,5,7] is strictly increasing, so return true.

    >>> canBeIncreasing([2,3,1,2])
    False

    Explanation:
    [3,1,2] is the result of removing the element at index 0.
    [2,1,2] is the result of removing the element at index 1.
    [2,3,2] is the result of removing the element at index 2.
    [2,3,1] is the result of removing the element at index 3.
    No resulting array is strictly increasing, so return false.

    >>> canBeIncreasing([1,1,1])
    False

    Explanation: The result of removing any element is [1,1].
    [1,1] is not strictly increasing, so return false.

    >>> canBeIncreasing([100,21,100])
    True

    >>> canBeIncreasing([541,783,433,744])
    False

    >>> canBeIncreasing([100,21,3])
    False

    >>> canBeIncreasing([105,924,32,968])
    True
    """
    removed = False
    for i in range(1, len(nums)):
        num = nums[i]
        prev = nums[i - 1]
        if num <= prev:
            if removed:
                return False
            if i > 1 and num <= nums[i - 2]:
                nums[i] = prev
            removed = True
    return True
