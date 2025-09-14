from collections import defaultdict


def maxOperations(nums: list[int], k: int) -> int:
    """
    ID: 1679
    Tags:   Array, Hash Table, Two Pointers, Sorting

    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums and an integer k.

    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

    Return the maximum number of operations you can perform on the array.

    Parameters
    ----------
    nums: list[int]

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxOperations([1,2,3,4], 5)
    2

    Explanation: Starting with nums = [1,2,3,4]:
    - Remove numbers 1 and 4, then nums = [2,3]
    - Remove numbers 2 and 3, then nums = []
    There are no more pairs that sum up to 5, hence a total of 2 operations.

    >>> maxOperations([3,1,3,4,3], 6)
    1

    Explanation: Starting with nums = [3,1,3,4,3]:
    - Remove the first two 3's, then nums = [1,4,3]
    There are no more pairs that sum up to 6, hence a total of 1 operation.
    """
    ans = 0
    ch = defaultdict(int)
    for x in nums:
        if x > k:
            continue
        target = k - x
        if target in ch:
            ch[target] -= 1
            if ch[target] == 0:
                del ch[target]
            ans += 1
        else:
            ch[x] += 1
    return ans