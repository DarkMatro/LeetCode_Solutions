def sortArrayByParity(nums: list[int]) -> list[int]:
    """
    ID: 905
    Tags:   Array, Two Pointers, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd
    integers.

    Return any array that satisfies this condition.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> sortArrayByParity([3,1,2,4])
    [2, 4, 3, 1]

    Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

    >>> sortArrayByParity([0])
    [0]
    """
    nums.sort(key=lambda x: 0 if x % 2 == 0 else 1)
    return nums