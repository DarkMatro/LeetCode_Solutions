def threeSumClosest(nums: list[int], target: int) -> int:
    """
    ID: 16
    Tags: Array, Two Pointers, Sorting
    Time:   O(N^2)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
    closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.

    Parameters
    ----------
    nums: list[int]

    target: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> threeSumClosest([-1,2,1,-4], 1)
    2

    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

    >>> threeSumClosest([0,0,0], 1)
    0

    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
    """
    nums.sort()
    n = len(nums)
    closest_sum = sum(nums[:3])

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if abs(target - closest_sum) > abs(target - curr_sum):
                closest_sum = curr_sum
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                return curr_sum
    return closest_sum
