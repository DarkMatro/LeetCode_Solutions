from collections import defaultdict


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    ID: 0350
    Tags:   Array, Hash Table, Two Pointers, Binary Search, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
    appear as many times as it shows in both arrays and you may return the result in any order.

    Parameters
    ----------
    nums1 : list[int]

    nums2 : list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> intersect([1,2,2,1], [2,2])
    [2, 2]

    >>> intersect([4,9,5], [9,4,9,8,4])
    [9, 4]

    Explanation: [4,9] is also accepted.
    """
    hash_map, result = defaultdict(int), []
    for num in nums1:
        hash_map[num] += 1

    for num in nums2:
        if num in hash_map and hash_map[num] != 0:
            result.append(num)
            hash_map[num] -= 1

    return result
