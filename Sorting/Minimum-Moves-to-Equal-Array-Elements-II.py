def minMoves2(nums: list[int]) -> int:
    """
    ID: 462
    Tags:   Array, Math, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums of size n, return the minimum number of moves required to make all
    array elements equal.

    In one move, you can increment or decrement an element of the array by 1.

    Test cases are designed so that the answer will fit in a 32-bit integer.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> minMoves2([1,2,3])
    2

    Explanation: Only two moves are needed (remember each move increments or decrements one
    element): [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

    >>> minMoves2([1,10,2,9])
    16
    """
    nums.sort()
    mid_id = len(nums) // 2
    mid_v = nums[mid_id]
    return sum([abs(mid_v - x) for x in nums if x != mid_v])
