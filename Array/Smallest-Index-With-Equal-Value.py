def smallestEqual(nums: list[int]) -> int:
    """
    ID: 2057
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if
    such index does not exist.

    x mod y denotes the remainder when x is divided by y.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> smallestEqual([0,1,2])
    0

    Explanation:
    i=0: 0 mod 10 = 0 == nums[0].
    i=1: 1 mod 10 = 1 == nums[1].
    i=2: 2 mod 10 = 2 == nums[2].
    All indices have i mod 10 == nums[i], so we return the smallest index 0.

    >>> smallestEqual([4,3,2,1])
    2

    Explanation:
    i=0: 0 mod 10 = 0 != nums[0].
    i=1: 1 mod 10 = 1 != nums[1].
    i=2: 2 mod 10 = 2 == nums[2].
    i=3: 3 mod 10 = 3 != nums[3].
    2 is the only index which has i mod 10 == nums[i].

    >>> smallestEqual([1,2,3,4,5,6,7,8,9,0])
    -1

    Explanation: No index satisfies i mod 10 == nums[i].
    """
    for i, num in enumerate(nums):
        if i % 10 == num:
            return i
    return -1

