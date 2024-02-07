from itertools import zip_longest


def getMinDistance(nums: list[int], target: int, start: int) -> int:
    """
    ID: 1848
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums (0-indexed) and two integers target and start, find an index i such that
    nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

    Return abs(i - start).

    It is guaranteed that target exists in nums.

    Parameters
    ----------
    nums : list[int]

    target: int

    start: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> getMinDistance([1,2,3,4,5], 5, 3)
    1

    Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

    >>> getMinDistance([1], 1, 0)
    0

    Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.

    >>> getMinDistance([1,1,1,1,1,1,1,1,1,1], 1, 0)
    0

    Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.

    >>> getMinDistance([5,3,6], 5, 2)
    2
    """
    if nums[start] == target:
        return 0
    for r, l in zip_longest(range(start + 1, len(nums)), range(start - 1, -1, -1)):
        if l is not None and nums[l] == target:
            return start - l
        elif r is not None and nums[r] == target:
            return r - start
