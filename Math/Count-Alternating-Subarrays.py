def countAlternatingSubarrays(nums: list[int]) -> int:
    """
    ID: 3101
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a binary array nums.

    We call a subarray alternating if no two adjacent elements in the subarray have the same value.

    Return the number of alternating subarrays in nums.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> countAlternatingSubarrays([0, 1, 1, 1])
    5

    Explanation: The following subarrays are alternating: [0], [1], [1], [1], and [0,1].

    >>> countAlternatingSubarrays([1, 0, 1, 0])
    10

    Explanation: Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.
    """
    cur = -1
    n = 0
    ans = 0
    for i in nums:
        if i == cur:
            ans += (n * (n + 1)) // 2
            n = 1
        else:
            cur = i
            n += 1
    ans += (n * (n + 1)) // 2
    return ans

