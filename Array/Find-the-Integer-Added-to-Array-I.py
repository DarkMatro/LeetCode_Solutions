def addedInteger(nums1: list[int], nums2: list[int]) -> int:
    """
    ID: 3131
    Tags:   Array
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    You are given two arrays of equal length, nums1 and nums2.

    Each element in nums1 has been increased (or decreased in the case of negative) by an integer,
    represented by the variable x.

    As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain
    the same integers with the same frequencies.

    Return the integer x.

    Parameters
    ----------
    nums1 : list[int]

    nums2 : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> addedInteger([2,6,4], [9,7,5])
    3

    Explanation: The integer added to each element of nums1 is 3.

    >>> addedInteger([10], [5])
    -5

    Explanation: The integer added to each element of nums1 is -5.

    >>> addedInteger([1,1,1,1], [1,1,1,1])
    0

    Explanation: The integer added to each element of nums1 is 0.
    """
    nums1.sort()
    nums2.sort()
    return nums2[0] - nums1[0]
