def checkPossibility(nums: list[int]) -> bool:
    """
    ID: 0665
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array nums with n integers, your task is to check if it could become non-decreasing
    by modifying at most one element.

    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
    such that (0 <= i <= n - 2).

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> checkPossibility([4,2,3])
    True

    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

    >>> checkPossibility([4,2,1])
    False

    Explanation: You cannot get a non-decreasing array by modifying at most one element.

    >>> checkPossibility([3,4,2,3])
    False
    """
    n = 0
    prev = nums[0]
    n_nums = len(nums)
    for i in range(1, n_nums):
        num = nums[i]
        if num < prev:
            if n == 1:
                return False
            n += 1
            if i >= 2 and nums[i - 2] > num:
                nums[i] = prev
        prev = nums[i]
    return True
