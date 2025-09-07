def sortedSquares(nums: list[int]) -> list[int]:
    """
    ID: 977
    Tags:   Array, Two Pointers, Sorting
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
    in non-decreasing order.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> sortedSquares([-4,-1,0,3,10])
    [0, 1, 9, 16, 100]

    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

    >>> sortedSquares([-7,-3,2,3,11])
    [4, 9, 9, 49, 121]
    """
    lp = 0
    rp = len(nums) - 1
    ans = []
    while lp <= rp:
        rx = nums[rp] ** 2
        lx = nums[lp] ** 2
        if rx > lx:
            ans.append(rx)
            rp -= 1
        else:
            ans.append(lx)
            lp += 1
    return ans[::-1]
