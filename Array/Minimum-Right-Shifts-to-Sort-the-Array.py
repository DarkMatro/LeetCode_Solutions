def minimumRightShifts(nums: list[int]) -> int:
    """
    ID: 2855
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed array nums of length n containing distinct positive integers. Return the minimum number
    of right shifts required to sort nums and -1 if this is not possible.

    A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> minimumRightShifts([3,4,5,1,2])
    2

    Explanation:
    After the first right shift, nums = [2,3,4,5,1].
    After the second right shift, nums = [1,2,3,4,5].
    Now nums is sorted; therefore the answer is 2.

    >>> minimumRightShifts([1,3,5])
    0

    Explanation: nums is already sorted therefore, the answer is 0.

    >>> minimumRightShifts([2,1,4])
    -1

    It's impossible to sort the array using right shifts.

    >>> minimumRightShifts([21])
    0

    >>> minimumRightShifts([12,28,63,56,69,67,83,37,82,70])
    -1
    """
    min_idx = 0
    min_v = 101
    n_pivots = 0
    for i, num in enumerate(nums):
        if num < min_v:
            min_v = num
            min_idx = i
        if num < nums[i - 1]:
            n_pivots += 1
            if n_pivots > 1:
                return -1
    if min_idx == 0:
        return 0
    return len(nums) - min_idx
