from itertools import accumulate


def sumOfBeauties(nums: list[int]) -> int:
    """
    ID: 2012
    Tags:   Array
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i]
    equals:

    2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
    1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
    0, if none of the previous conditions holds.
    Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumOfBeauties([1,2,3])
    2

    Explanation: For each index i in the range 1 <= i <= 1:
    - The beauty of nums[1] equals 2.

    >>> sumOfBeauties([2,4,6,4])
    1

    Explanation: For each index i in the range 1 <= i <= 2:
    - The beauty of nums[1] equals 1.
    - The beauty of nums[2] equals 0.

    >>> sumOfBeauties([3,2,1])
    0

    Explanation: For each index i in the range 1 <= i <= 1:
    - The beauty of nums[1] equals 0.
    """
    prefix = list(accumulate(nums, func=max))
    suffix = list(accumulate(nums[::-1], func=min))[::-1]
    ans = 0
    for i in range(1, len(nums) - 1):
        num = nums[i]
        if prefix[i - 1] < num < suffix[i + 1]:
            ans += 2
        elif nums[i - 1] < num < nums[i + 1]:
            ans += 1
    return ans
