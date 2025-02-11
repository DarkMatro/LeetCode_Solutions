def countSubarrays(nums: list[int]) -> int:
    """
    ID: 3392
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums, return the number of subarrays of length 3 such that the sum of
    the first and third numbers equals exactly half of the second number.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> countSubarrays([1,2,1,4,1])
    1

    Explanation:

    Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third
    numbers equals half the middle number.

    >>> countSubarrays([1,1,1])
    0

    Explanation:

    [1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to
    half the middle number.
    """
    ans = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] / 2 == nums[i] + nums[i + 2]:
            ans += 1
    return ans
