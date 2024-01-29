def differenceOfSum(nums: list[int]) -> int:
    """
    ID: 2535
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a positive integer array nums.

    The element sum is the sum of all the elements in nums.
    The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
    Return the absolute difference between the element sum and digit sum of nums.

    Note that the absolute difference between two integers x and y is defined as |x - y|.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    res : int

    Examples
    --------
    >>> differenceOfSum([1,15,6,3])
    9

    Explanation:
    The element sum of nums is 1 + 15 + 6 + 3 = 25.
    The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
    The absolute difference between the element sum and digit sum is |25 - 16| = 9.

    >>> differenceOfSum([1,2,3,4])
    0

    Explanation:
    The element sum of nums is 1 + 2 + 3 + 4 = 10.
    The digit sum of nums is 1 + 2 + 3 + 4 = 10.
    The absolute difference between the element sum and digit sum is |10 - 10| = 0.
    """
    n_sum = sum(nums)
    d_sum = 0
    for i in nums:
        if 10 <= i < 100:
            d_sum += i // 10
            d_sum += i % 10
        elif 100 <= i < 1000:
            d_sum += i // 100
            d_sum += i % 100 // 10
            d_sum += i % 10
        elif 1000 <= i <= 2000:
            d_sum += i // 1000
            d_sum += i % 1000 // 100
            d_sum += i % 100 // 10
            d_sum += i % 10
        else:
            d_sum += i
    return abs(n_sum - d_sum)

