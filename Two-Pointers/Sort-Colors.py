def sortColors(nums: list[int]) -> list[int]:
    """
    ID: 75
    Tags:   Array, Two Pointers, Sorting
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
    are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> sortColors([2,0,2,1,1,0])
    [0, 0, 1, 1, 2, 2]

    >>> sortColors([2,0,1])
    [0, 1, 2]
    """
    """
    Do not return anything, modify nums in-place instead.
    """
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
