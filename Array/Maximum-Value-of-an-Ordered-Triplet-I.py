def maximumTripletValue(nums: list[int]) -> int:
    """
    ID: 2873
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed integer array nums.

    Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have
    a negative value, return 0.

    The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> maximumTripletValue([12,6,1,2,7])
    77

    Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
    It can be shown that there are no ordered triplets of indices with a value greater than 77.

    >>> maximumTripletValue([1,10,3,4,19])
    133

    Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
    It can be shown that there are no ordered triplets of indices with a value greater than 133.

    >>> maximumTripletValue([1,2,3])
    0

    Explanation: The only ordered triplet of indices (0, 1, 2) has a negative value of
    (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.
    """
    max_v = 0
    left = nums[0]
    for i in range(1, len(nums) - 1):
        num = nums[i]
        right = max(nums[i + 1:])
        v = (left - num) * right
        left = max(left, num)
        max_v = max(max_v, v)
    return max_v

