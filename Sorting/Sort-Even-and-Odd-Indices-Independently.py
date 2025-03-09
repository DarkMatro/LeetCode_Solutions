from itertools import zip_longest


def sortEvenOdd(nums: list[int]) -> list[int]:
    """
    ID: 2164
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given a 0-indexed integer array nums. Rearrange the values of nums according to the
    following rules:

    Sort the values at odd indices of nums in non-increasing order.
    For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd
    indices 1 and 3 are sorted in non-increasing order.
    Sort the values at even indices of nums in non-decreasing order.
    For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at
    even indices 0 and 2 are sorted in non-decreasing order.
    Return the array formed after rearranging the values of nums.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    list[int]

    Examples
    --------
    >>> sortEvenOdd([4,1,2,3])
    [2, 3, 4, 1]

    Explanation: First, we sort the values present at odd indices (1 and 3) in non-increasing order.
    So, nums changes from [4,1,2,3] to [4,3,2,1].
    Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
    So, nums changes from [4,1,2,3] to [2,3,4,1].
    Thus, the array formed after rearranging the values is [2,3,4,1].

    >>> sortEvenOdd([2,1])
    [2, 1]

    Explanation: Since there is exactly one odd index and one even index, no rearrangement of values
    takes place.
    The resultant array formed is [2,1], which is the same as the initial array.
    """
    ans = []
    for x, y in zip_longest(sorted(nums[::2]), sorted(nums[1::2], reverse=True)):
        if x:
            ans.append(x)
        if y:
            ans.append(y)
    return ans
