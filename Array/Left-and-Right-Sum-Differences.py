def leftRightDifference(nums: list[int]) -> list[int]:
    """
    ID: 2574
    Tags:   Array, Prefix Sum
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

    answer.length == nums.length.
    answer[i] = |leftSum[i] - rightSum[i]|.
    Where:

    leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element,
     leftSum[i] = 0.
    rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element,
     rightSum[i] = 0.
    Return the array answer.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    list[int]

    Examples
    --------
    >>> leftRightDifference([10,4,8,3])
    [15, 1, 11, 22]

    Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
    The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

    >>> leftRightDifference([1])
    [0]

    Explanation: The array leftSum is [0] and the array rightSum is [0].
    The array answer is [|0 - 0|] = [0].
    """
    n = len(nums)
    right_sum = [0] * n
    left_sum = [0] * n

    for i in range(1, n):
        left_sum[i] = left_sum[i - 1] + nums[i - 1]

    for i in range(-2, -n - 1, -1):
        right_sum[i] = right_sum[i + 1] + nums[i + 1]

    return [abs(left_sum[x] - right_sum[x]) for x in range(n)]

