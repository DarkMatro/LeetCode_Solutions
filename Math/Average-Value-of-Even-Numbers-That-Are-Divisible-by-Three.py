def averageValue(nums: list[int]) -> int:
    """
    ID: 2455
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums of positive integers, return the average value of all even integers
    that are divisible by 3.

    Note that the average of n elements is the sum of the n elements divided by n and rounded down
    to the nearest integer.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> averageValue([1,3,6,10,12,15])
    9

    Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.

    >>> averageValue([1,2,4,7,10])
    0

    Explanation: There is no single number that satisfies the requirement, so return 0.
    """
    div = [x for x in nums if x % 3 == 0 and x % 2 == 0]
    return int(sum(div) / len(div)) if div else 0
