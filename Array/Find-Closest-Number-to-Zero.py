def findClosestNumber(nums: list[int]) -> int:
    """
    ID: 2239
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple
    answers, return the number with the largest value.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> findClosestNumber([-4,-2,1,4,8])
    1

    Explanation:
    The distance from -4 to 0 is |-4| = 4.
    The distance from -2 to 0 is |-2| = 2.
    The distance from 1 to 0 is |1| = 1.
    The distance from 4 to 0 is |4| = 4.
    The distance from 8 to 0 is |8| = 8.
    Thus, the closest number to 0 in the array is 1.

    >>> findClosestNumber([2,-1,1])
    1

    Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
    """
    min_v = 100_001
    for num in nums:
        v = abs(num)
        abs_min_v = abs(min_v)
        if v < abs_min_v:
            min_v = num
        elif v == abs_min_v:
            min_v = max(min_v, num)
    return min_v

