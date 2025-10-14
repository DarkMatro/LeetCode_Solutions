def smallestAbsent(nums: list[int]) -> int:
    """
    ID: 3678
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums.

    Return the smallest absent positive integer in nums such that it is strictly greater than the average of all
    elements in nums.

    The average of an array is defined as the sum of all its elements divided by the number of elements.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> smallestAbsent([3,5])
    6

    Explanation: The average of nums is (3 + 5) / 2 = 8 / 2 = 4.
    The smallest absent positive integer greater than 4 is 6.

    >>> smallestAbsent([-1,1,2])
    3

    Explanation: The average of nums is (-1 + 1 + 2) / 3 = 2 / 3 = 0.667.
    The smallest absent positive integer greater than 0.667 is 3.

    >>> smallestAbsent([4,-1])
    2

    Explanation: The average of nums is (4 + (-1)) / 2 = 3 / 2 = 1.50.
    The smallest absent positive integer greater than 1.50 is 2.
    """
    avg = sum(nums) / len(nums)
    n = set(nums)
    ans = int(avg) + 1
    if ans <= 0:
        ans = 1
    while ans in n:
        ans += 1
    return ans
