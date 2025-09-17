def rotate(nums: list[int], k: int) -> list[int]:
    """
    ID: 189
    Tags: Array, Math, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    Parameters
    ----------
    nums: list[int]

    k: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> rotate([1,2,3,4,5,6,7], 3)
    [5, 6, 7, 1, 2, 3, 4]

    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

    >>> rotate([-1,-100,3,99], 2)
    [3, 99, -1, -100]

    Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
    """
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    start = count = 0

    while count < n:
        current = start
        prev = nums[start]
        while True:
            nxt = (current + k) % n
            nums[nxt], prev = prev, nums[nxt]
            current = nxt
            count += 1
            if start == current:
                break
        start += 1
    return nums
