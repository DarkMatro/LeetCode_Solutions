def missingInteger(nums: list[int]) -> int:
    """
    ID: 2996
    Tags:   Array, Hash Table, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a 0-indexed array of integers nums.

    A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In
    particular, the prefix consisting only of nums[0] is sequential.

    Return the smallest integer x missing from nums such that x is greater than or equal to the sum
    of the longest sequential prefix.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> missingInteger([1,2,3,2,5])
    6

    Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the
    array, therefore 6 is the smallest missing integer greater than or equal to the sum of the
    longest sequential prefix.

    >>> missingInteger([3,4,5,1,12,14,13])
    15

    Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14
    belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than
    or equal to the sum of the longest sequential prefix.
    """
    # Step 1: Find the longest sequential prefix
    prefix_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
        else:
            break  # Stop at the first non-sequential element

    # Step 2: Find the smallest missing integer >= prefix_sum
    num_set = set(nums)  # Convert to set for O(1) lookup
    while prefix_sum in num_set:
        prefix_sum += 1  # Keep increasing until we find a missing number

    return prefix_sum
