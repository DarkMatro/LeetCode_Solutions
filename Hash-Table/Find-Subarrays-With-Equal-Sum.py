from collections import defaultdict, Counter

def findSubarrays(nums: list[int]) -> bool:
    """
    ID: 2395
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2
    with equal sum. Note that the two subarrays must begin at different indices.

    Return true if these subarrays exist, and false otherwise.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> findSubarrays([4,2,4])
    True

    Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.

    >>> findSubarrays([1,2,3,4,5])
    False

    Explanation: No two subarrays of size 2 have the same sum.

    >>> findSubarrays([0,0,0])
    True

    Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
    Note that even though the subarrays have the same content, the two subarrays are considered
    different because they are in different positions in the original array.
    """
    d = defaultdict(int)
    for i in range(len(nums) - 1):
        d[i] = sum(nums[i:i + 2])
    cnt = Counter(d.values())
    return len([x for x in cnt.values() if x > 1]) > 0
