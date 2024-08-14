def smallestRangeI(nums: list[int], k: int) -> int:
    """
    ID: 908
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums and an integer k.

    In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to
    nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most
    once for each index i.

    The score of nums is the difference between the maximum and minimum elements in nums.

    Return the minimum score of nums after applying the mentioned operation at most once for each
    index in it.

    Parameters
    ----------
    nums: list[int]

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> smallestRangeI([1], 0)
    0

    Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

    >>> smallestRangeI([0, 10], 2)
    6

    Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.

    >>> smallestRangeI([1, 3, 6], 3)
    0

    Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
    """
    min_v = min(nums)
    max_v = max(nums)
    diff, extension = max_v - min_v, 2 * k
    return 0 if diff <= extension else diff - extension
