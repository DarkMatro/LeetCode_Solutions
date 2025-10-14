def longestSubarray(nums: list[int]) -> int:
    """
    ID: 3708
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an array of positive integers nums.

    A Fibonacci array is a contiguous sequence whose third and subsequent terms each equal the sum of the two preceding
    terms.

    Return the length of the longest Fibonacci subarray in nums.

    Note: Subarrays of length 1 or 2 are always Fibonacci.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> longestSubarray([1,1,1,1,2,3,5,1])
    5

    Explanation: The longest Fibonacci subarray is nums[2..6] = [1, 1, 2, 3, 5].
    [1, 1, 2, 3, 5] is Fibonacci because 1 + 1 = 2, 1 + 2 = 3, and 2 + 3 = 5.

    >>> longestSubarray([5,2,7,9,16])
    5

    Explanation: The longest Fibonacci subarray is nums[0..4] = [5, 2, 7, 9, 16].
    [5, 2, 7, 9, 16] is Fibonacci because 5 + 2 = 7, 2 + 7 = 9, and 7 + 9 = 16.

    >>> longestSubarray([1000000000,1000000000,1000000000])
    2

    Explanation: The longest Fibonacci subarray is nums[1..2] = [1000000000, 1000000000].
    [1000000000, 1000000000] is Fibonacci because its length is 2.
    """
    ans = 2
    cnt = 2
    for i, x in enumerate(nums):
        if i < 2:
            continue
        s = nums[i - 1] + nums[i - 2]
        if s == x:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 2
    return ans
