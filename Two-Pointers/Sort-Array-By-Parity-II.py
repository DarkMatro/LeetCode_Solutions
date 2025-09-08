def sortArrayByParityII(nums: list[int]) -> list[int]:
    """
    ID: 922
    Tags:   Array, Two Pointers, Sorting
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

    Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

    Return any answer array that satisfies this condition.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> sortArrayByParityII([4,2,5,7])
    [4, 5, 2, 7]

    Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

    >>> sortArrayByParityII([2,3])
    [2, 3]
    """
    n = len(nums)
    i, j = 0, 1

    while i < n and j < n:
        if nums[i] % 2 == 0:
            i += 2
        elif nums[j] % 2 == 1:
            j += 2
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2
    return nums
