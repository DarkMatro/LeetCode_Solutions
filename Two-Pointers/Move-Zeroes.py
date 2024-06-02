def move_zeroes(nums: list[int]) -> None:
    """
    ID: 0283
    Tags:   Array, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
    elements.

    Note that you must do this in-place without making a copy of the array.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    None
    """
    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
