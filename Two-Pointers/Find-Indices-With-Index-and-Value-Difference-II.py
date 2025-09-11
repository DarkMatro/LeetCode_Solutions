def findIndices(nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
    """
    ID: 2905
    Tags:   Array, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer
    valueDifference.

    Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

    abs(i - j) >= indexDifference, and
    abs(nums[i] - nums[j]) >= valueDifference
    Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1]
    otherwise. If there are multiple choices for the two indices, return any of them.

    Note: i and j may be equal.

    Parameters
    ----------
    nums: list[int]

    indexDifference: int

    valueDifference: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> findIndices([5,1,4,1], 2, 4)
    [0, 3]

    Output:In this example, i = 0 and j = 3 can be selected.
    abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
    Hence, a valid answer is [0,3].
    [3,0] is also a valid answer.

    >>> findIndices([2,1], 0, 0)
    [0, 0]

    Output: In this example, i = 0 and j = 0 can be selected.
    abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
    Hence, a valid answer is [0,0].
    Other valid answers are [0,1], [1,0], and [1,1].

    >>> findIndices([1,2,3], 2, 4)
    [-1, -1]

    Output: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
    Hence, [-1,-1] is returned.
    """
    n = len(nums)
    min_val, min_idx = float('inf'), -1
    max_val, max_idx = float('-inf'), -1

    for j in range(n):
        # make earlier index eligible
        if j - indexDifference >= 0:
            i = j - indexDifference
            if nums[i] < min_val:
                min_val, min_idx = nums[i], i
            if nums[i] > max_val:
                max_val, max_idx = nums[i], i

        # check with min
        if min_idx != -1 and abs(nums[j] - min_val) >= valueDifference:
            return [min_idx, j]
        # check with max
        if max_idx != -1 and abs(nums[j] - max_val) >= valueDifference:
            return [max_idx, j]

    return [-1, -1]
