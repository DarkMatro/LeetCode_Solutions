def mergeArrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    """
    ID: 2570
    Tags:   Array, Hash Table, Two Pointers
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given two 2D integer arrays nums1 and nums2.

    nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    Each array contains unique ids and is sorted in ascending order by id.

    Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

    Only ids that appear in at least one of the two arrays should be included in the resulting array.
    Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
    If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
    Return the resulting array. The returned array must be sorted in ascending order by id.

    Parameters
    ----------
    nums1 : list[list[int]]
    nums2 : list[list[int]]

    Returns
    -------
    out : list[list[int]]

    Examples
    --------
    >>> mergeArrays([1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]])
    [[1,6],[2,3],[3,2],[4,6]]

    Explanation: The resulting array contains the following:
    - id = 1, the value of this id is 2 + 4 = 6.
    - id = 2, the value of this id is 3.
    - id = 3, the value of this id is 2.
    - id = 4, the value of this id is 5 + 1 = 6.

    >>> mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]])
    [[1,3],[2,4],[3,6],[4,3],[5,5]]

    Explanation: There are no common ids, so we just include each id with its value in the resulting list.
    """
    d1 = {k: v for k, v in nums1}
    d2 = {k: v for k, v in nums2}
    inner_keys = d1.keys() & d2.keys()
    for k in inner_keys:
        d1[k] = d1[k] + d2[k]
        del d2[k]
    d1.update(d2)
    return [[k, d1[k]] for k in sorted(d1.keys())]
