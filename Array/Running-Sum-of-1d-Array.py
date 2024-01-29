def runningSum(nums: list[int]) -> list[int]:
    """
    ID: 1480
    Tags:   Array, Prefix Sum
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> runningSum([1,2,3,4])
    [1, 3, 6, 10]

    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

    >>> runningSum([1,1,1,1,1])
    [1, 2, 3, 4, 5]

    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

    >>> runningSum([3,1,2,10,1])
    [3, 4, 6, 16, 17]
    """
    s = 0
    ans = []
    for i in nums:
        s += i
        ans.append(s)
    return ans
