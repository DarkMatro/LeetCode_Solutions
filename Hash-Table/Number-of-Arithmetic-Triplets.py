def arithmeticTriplets(nums: list[int], diff: int) -> int:
    """
    ID: 2367
    Tags:   Array, Hash Table, Two Pointers, Enumeration
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
    A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

    i < j < k,
    nums[j] - nums[i] == diff, and
    nums[k] - nums[j] == diff.
    Return the number of unique arithmetic triplets.

    Parameters
    ----------
    nums : list[int]

    diff: int

    Returns
    -------
    int

    Examples
    --------
    >>> arithmeticTriplets([0,1,4,6,7,10], 3)
    2

    Explanation:
    (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
    (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.

    >>> arithmeticTriplets([4,5,6,7,8,9], 2)
    2

    Explanation:
    (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
    (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
    """
    seen = set()
    c = 0
    for num in nums:
        seen.add(num)
        if num - diff in seen and num - diff - diff in seen:
            c += 1
    return c
