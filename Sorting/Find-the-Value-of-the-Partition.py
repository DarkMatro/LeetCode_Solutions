def findValueOfPartition(nums: list[int]) -> int:
    """
    ID: 2740
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    You are given a positive integer array nums.

    Partition nums into two arrays, nums1 and nums2, such that:

    Each element of the array nums belongs to either the array nums1 or the array nums2.
    Both arrays are non-empty.
    The value of the partition is minimized.
    The value of the partition is |max(nums1) - min(nums2)|.

    Here, max(nums1) denotes the maximum element of the array nums1, and min(nums2) denotes the
    minimum element of the array nums2.

    Return the integer denoting the value of such partition.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> findValueOfPartition([1,3,2,4])
    1

    Explanation: We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
    - The maximum element of the array nums1 is equal to 2.
    - The minimum element of the array nums2 is equal to 3.
    The value of the partition is |2 - 3| = 1.
    It can be proven that 1 is the minimum value out of all partitions.

    >>> findValueOfPartition([100,1,10])
    9

    Explanation: We can partition the array nums into nums1 = [10] and nums2 = [100,1].
    - The maximum element of the array nums1 is equal to 10.
    - The minimum element of the array nums2 is equal to 1.
    The value of the partition is |10 - 1| = 9.
    It can be proven that 9 is the minimum value out of all partitions.
    """
    nums.sort()
    return min([nums[i] - nums[i - 1] for i in range(1, len(nums))])
