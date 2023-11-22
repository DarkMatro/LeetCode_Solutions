def remove_duplicates(nums: list[int]) -> int:
    """
    ID: 0026
    Tags:   Array, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
    element appears only once. The relative order of the elements should be kept the same. Then return the number of
    unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were
    present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    k : int

    Examples
    --------
    >>> remove_duplicates([1, 1, 2])
    2


    nums = [1,2,_] Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    >>> remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    5

    nums = [0,1,2,3,4,_,_,_,_,_]
    Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    """
    p = 0
    k = 0
    while p < len(nums):
        if nums[k] != nums[p]:
            k += 1
            nums[k] = nums[p]
        p += 1
    return k + 1
