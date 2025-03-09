def dominantIndex(nums: list[int]) -> int:
    """
    ID: 747
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums where the largest integer is unique.

    Determine whether the largest element in the array is at least twice as much as every other
    number in the array. If it is, return the index of the largest element, or return -1 otherwise.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> dominantIndex([3,6,1,0])
    1

    Explanation: 6 is the largest integer.
    For every other number in the array x, 6 is at least twice as big as x.
    The index of value 6 is 1, so we return 1.

    >>> dominantIndex([1,2,3,4])
    -1

    Explanation: 4 is less than twice the value of 3, so we return -1.
    """
    max_v, max_idx = -1, -1
    for i, n in enumerate(nums):
        if n > max_v:
            max_v = n
            max_idx = i
    nums.sort()
    return max_idx if nums[-1] // 2 >= nums[-2] else -1
