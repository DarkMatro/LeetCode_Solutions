def numberOfPairs(nums1: list[int], nums2: list[int], k: int) -> int:
    """
    ID: 3162
    Tags:   Array, Hash Table
    Time:   O(N * M)
    Memory: O(1)

    Task
    ----------
    You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also
    given a positive integer k.

    A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1,
    0 <= j <= m - 1).

    Return the total number of good pairs.

    Parameters
    ----------
    nums1: list[int]

    nums2: list[int]

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> numberOfPairs([1,3,4], [1,3,4], 1)
    5

    Explanation:
    The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).

    >>> numberOfPairs([1,2,4,12], [2,4], 3)
    2

    Explanation:
    The 2 good pairs are (3, 0) and (3, 1).
    """
    ans = 0
    for i, x in enumerate(nums1):
        for j, y in enumerate(nums2):
            if x % (y * k) == 0:
                ans += 1
    return ans
