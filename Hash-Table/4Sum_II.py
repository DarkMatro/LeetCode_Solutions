from collections import defaultdict


def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    """
    ID: 454
    Tags:   Array, Hash Table
    Time:   O(N^2)
    Memory: O(N)

    Task
    ----------
    Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of
    tuples (i, j, k, l) such that:

    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

    Parameters
    ----------
    nums1: list[int]

    nums2: list[int]

    nums3: list[int]

    nums4: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> fourSumCount([1,2], [-2,-1], [-1,2], [0,2])
    2

    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

    >>> fourSumCount([0], [0], [0], [0])
    1
    """
    d, ans = defaultdict(int), 0
    for num1 in nums1:
        for num2 in nums2:
            d[num1 + num2] += 1
    for num3 in nums3:
        for num4 in nums4:
            ans += d[0 - (num3 + num4)]
    return ans
