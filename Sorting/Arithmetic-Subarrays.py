def checkArithmeticSubarrays(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    """
    ID: 1630
    Tags:   Array, Hash Table, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    A sequence of numbers is called arithmetic if it consists of at least two elements, and the
    difference between every two consecutive elements is the same. More formally, a sequence s is
    arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

    For example, these are arithmetic sequences:

    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
    The following sequence is not arithmetic:

    1, 1, 2, 5, 7
    You are given an array of n integers, nums, and two arrays of m integers each, l and r,
    representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays
    are 0-indexed.

    Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]],
    nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false
    otherwise.

    Parameters
    ----------
    nums: list[int]

    l: list[int]

    r: list[int]

    Returns
    -------
    list[bool]

    Examples
    --------
    >>> checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5])
    [True, False, True]

    Explanation: WIn the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4],
    which is an arithmetic sequence.
    In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence
    In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an
    arithmetic sequence.

    >>> checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10])
    [False, True, False, False, True, True]
    """
    ans = []
    for left, right in zip(l, r):
        ans.append(is_arithmetic(nums[left:right + 1]))
    return ans


def is_arithmetic(arr: list[int]) -> bool:
    if len(arr) < 2:
        return False
    arr.sort()
    diff = arr[1] - arr[0]
    prev = arr[1]
    for i, x in enumerate(arr):
        if i < 2:
            continue
        if x - prev != diff:
            return False
        prev = x
    return True
