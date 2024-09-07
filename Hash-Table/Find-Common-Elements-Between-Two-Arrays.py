from collections import Counter

def findIntersectionValues(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    ID: 2956
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the
    following values:

    answer1 : the number of indices i such that nums1[i] exists in nums2.
    answer2 : the number of indices i such that nums2[i] exists in nums1.
    Return [answer1,answer2].

    Parameters
    ----------
    nums1: list[int]

    nums2: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> findIntersectionValues([2,3,2], [1,2])
    [2, 1]

    >>> findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6])
    [3, 4]

    Explanation:
    The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.

    The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.

    >>> findIntersectionValues([3,4,2,3], [1,5])
    [0, 0]

    Explanation:
    No numbers are common between nums1 and nums2, so answer is [0,0].
    """
    n1 = Counter(nums1)
    n2 = Counter(nums2)
    k_ = (n1 & n2).keys()
    ans1 = 0
    ans2 = 0
    for k in k_:
        ans1 += n1[k]
        ans2 += n2[k]
    return [ans1, ans2]
