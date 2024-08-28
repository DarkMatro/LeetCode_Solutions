def isIdealPermutation(nums: list[int]) -> bool:
    """
    ID: 775
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums of length n which represents a permutation of all the
    integers in the range [0, n - 1].

    The number of global inversions is the number of the different pairs (i, j) where:

    0 <= i < j < n
    nums[i] > nums[j]
    The number of local inversions is the number of indices i where:

    0 <= i < n - 1
    nums[i] > nums[i + 1]
    Return true if the number of global inversions is equal to the number of local inversions.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isIdealPermutation([1,0,2])
    True

    Explanation: There is 1 global inversion and 1 local inversion.

    >>> isIdealPermutation([1,2,0])
    False

    Explanation: There are 2 global inversions and 1 local inversion.
    """
    for i, x in enumerate(nums):
        if abs(i - x) > 1:
            return False
    return True
