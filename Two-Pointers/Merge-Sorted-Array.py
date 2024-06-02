def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    ID: 0088
    Tags:   Array, Two Pointers, Sorting
    Time:   O(m + n)
    Memory: O(1)

    Task
    ----------
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
    representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
    merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    Parameters
    ----------
    nums1 : list[int]

    m : int

    nums2 : list[int]

    n : int

    Returns
    -------
    nums1 : list[int]

    Examples
    --------
    >>> merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    [1, 2, 2, 3, 5, 6]

    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

    >>> merge([1], 1, [], 0)
    [1]

    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].

    >>> merge([0], 0, [1], 1)
    [1]

    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in
     nums1.
    """
    k = len(nums1) - 1
    while n > 0:
        if m == 0 or nums2[n - 1] >= nums1[m - 1]:
            nums1[k] = nums2[n - 1]
            n -= 1
        elif m > 0:
            nums1[k] = nums1[m - 1]
            m -= 1
        k -= 1
    return nums1
