def zeroFilledSubarray(nums: list[int]) -> int:
    """
    ID: 2348
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums, return the number of subarrays filled with 0.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> zeroFilledSubarray([1,3,0,0,2,0,0,4])
    6

    Explanation: There are 4 occurrences of [0] as a subarray.
    There are 2 occurrences of [0,0] as a subarray.
    There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return
    6.

    >>> zeroFilledSubarray([0,0,0,2,0,0])
    9

    Explanation: There are 5 occurrences of [0] as a subarray.
    There are 3 occurrences of [0,0] as a subarray.
    There is 1 occurrence of [0,0,0] as a subarray.
    There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return
    9.

    >>> zeroFilledSubarray([2,10,2019])
    0

    Explanation: There is no subarray filled with 0. Therefore, we return 0.
    """
    total_count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            total_count += zero_count
        else:
            zero_count = 0

    return total_count
