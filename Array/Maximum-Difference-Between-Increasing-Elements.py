def maximumDifference(nums: list[int]) -> int:
    """
    ID: 2016
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j]
    (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

    Return the maximum difference. If no such i and j exists, return -1.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> maximumDifference([7,1,5,4])
    4

    The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
    Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

    >>> maximumDifference([9,4,3,2])
    -1

    There is no i and j such that i < j and nums[i] < nums[j].

    >>> maximumDifference([1,5,2,10])
    9

    The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
    """
    buy = nums[0]
    profit = -1
    for i, num in enumerate(nums):
        if i == 0:
            continue
        current_profit = num - buy
        if buy < num:
            profit = max(current_profit, profit)
        else:
            buy = num
    return profit

