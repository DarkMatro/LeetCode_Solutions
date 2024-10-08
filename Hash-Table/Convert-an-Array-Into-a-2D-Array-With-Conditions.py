from collections import Counter


def findMatrix(nums: list[int]) -> list[list[int]]:
    """
    ID: 2610
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums. You need to create a 2D array from nums satisfying the
    following conditions:

    The 2D array should contain only the elements of the array nums.
    Each row in the 2D array contains distinct integers.
    The number of rows in the 2D array should be minimal.
    Return the resulting array. If there are multiple answers, return any of them.

    Note that the 2D array can have a different number of elements on each row.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : list[list[int]]

    Examples
    --------
    >>> findMatrix([1,3,4,1,2,3,1])
    [[1, 3, 4, 2], [1, 3], [1]]

    Explanation: We can create a 2D array that contains the following rows:
    - 1,3,4,2
    - 1,3
    - 1
    All elements of nums were used, and each row of the 2D array contains distinct integers, so it
    is a valid answer. It can be shown that we cannot have less than 3 rows in a valid array.

    >>> findMatrix([1,2,3,4])
    [[1, 2, 3, 4]]

    Explanation: All elements of the array are distinct, so we can keep all of them in the first row
    of the 2D array.
    """
    cnt = Counter(nums)
    max_v = max(cnt.values())
    ans = [[] for i in range(max_v)]
    for k, v in cnt.items():
        for i in range(v):
            ans[i].append(k)
    return ans
