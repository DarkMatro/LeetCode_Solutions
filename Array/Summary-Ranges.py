def summaryRanges(nums: list[int]) -> list[str]:
    """
    ID: 0228
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a sorted unique integer array nums.

    A range [a,b] is the set of all integers from a to b (inclusive).

    Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element
    of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> summaryRanges([0,1,2,4,5,7])
    ['0->2', '4->5', '7']

    Explanation: The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"

    >>> summaryRanges([0,2,3,4,6,8,9])
    ['0', '2->4', '6', '8->9']

    Explanation: The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"

    >>> summaryRanges([])
    []
    """
    n = len(nums)
    if n == 0:
        return nums
    ans = []
    prev = nums[0]
    start = prev
    for i in range(1, n):
        num = nums[i]
        if num - prev != 1:
            ans.append(str(start) + '->' + str(prev) if start != prev else str(start))
            start = num
        prev = num
    else:
        ans.append(str(start) + '->' + str(prev) if start != prev else str(start))
    return ans
