from collections import Counter


def largestInteger(nums: list[int], k: int) -> int:
    """
    ID: 3471
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums and an integer k.

    An integer x is almost missing from nums if x appears in exactly one subarray of size k within
    nums.

    Return the largest almost missing integer from nums. If no such integer exists, return -1.

    A subarray is a contiguous sequence of elements within an array.

    Parameters
    ----------
    nums: list[int]

    k: int

    Returns
    -------
    int

    Examples
    -------- 
    >>> largestInteger([3,9,2,1,7], 3)
    7

    Explanation:
    1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
    2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
    3 appears in 1 subarray of size 3: [3, 9, 2].
    7 appears in 1 subarray of size 3: [2, 1, 7].
    9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
    We return 7 since it is the largest integer that appears in exactly one subarray of size k.

    >>> largestInteger([3,9,7,2,1,7], 4)
    3

    Explanation:
    1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
    2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
    3 appears in 1 subarray of size 4: [3, 9, 7, 2].
    7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
    9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
    We return 3 since it is the largest and only integer that appears in exactly one subarray of
    size k.

    >>> largestInteger([0,0], 1)
    -1

    Explanation: There is no integer that appears in only one subarray of size 1.
    """
    if k == 1:
        c = [k for k, v in Counter(nums).items() if v == 1]
        return max(c) if c else -1
    if k == len(nums):
        return max(nums)
    c = Counter(nums)
    first = nums[0]
    last = nums[-1]
    left = first if c[first] == 1 else -1
    right = last if c[last] == 1 else -1
    return max(left, right)
