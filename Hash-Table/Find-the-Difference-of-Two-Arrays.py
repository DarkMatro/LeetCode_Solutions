def destCity(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    """
    ID: 2215
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
    Note that the integers in the lists may be returned in any order.

    Parameters
    ----------
    nums1: list[int]

    nums2: list[int]

    Returns
    -------
    out : list[list[int]]

    Examples
    --------
    >>> destCity([1,2,3], [2,4,6])
    [[1, 3], [4, 6]]

    Explanation:
    For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3
    are not present in nums2. Therefore, answer[0] = [1,3].
    For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6
    are not present in nums2. Therefore, answer[1] = [4,6].

    >>> destCity([1,2,3,3], [1,1,2,2])
    [[3], []]

    Explanation:
    For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their
    value is only included once and answer[0] = [3].
    Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
    """
    n1 = set(nums1)
    n2 = set(nums2)
    return [list(n1 - n2), list(n2 - n1)]
