def minMoves(nums: list[int]) -> int:
    """
    ID: 453
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums of size n, return the minimum number of moves required to make all
    array elements equal.

    In one move, you can increment n - 1 elements of the array by 1.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> minMoves([1,2,3])
    3

    Explanation: Only three moves are needed (remember each move increments two elements):
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

    >>> minMoves([1,1,1])
    0
    """
    min_val = min(nums)
    moves = 0
    for num in nums:
        moves += num - min_val
    return moves
