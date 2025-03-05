def findNonMinOrMax(nums: list[int]) -> int:
    """
    ID: 2733
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums containing distinct positive integers, find and return any number
    from the array that is neither the minimum nor the maximum value in the array, or -1 if there is
    no such number.

    Return the selected integer.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> findNonMinOrMax([3,2,1,4])
    2

    Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore,
    either 2 or 3 can be valid answers.

    >>> findNonMinOrMax([1,2])
    -1

    Explanation: Since there is no number in nums that is neither the maximum nor the minimum, we
    cannot select a number that satisfies the given condition. Therefore, there is no answer.

    >>> findNonMinOrMax([2,1,3])
    2

    Explanation: Since 2 is neither the maximum nor the minimum value in nums, it is the only valid
    answer.
    """
    if len(nums) <= 2:
        return -1
    nums.sort()
    return nums[1]
