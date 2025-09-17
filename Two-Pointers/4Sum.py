def fourSum(nums: list[int], target: int) -> list[list[int]]:
    """
    ID: 18
    Tags: Array, Two Pointers, Sorting
    Time:   O(N^3)
    Memory: O(1)

    Task
    ----------
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c],
    nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.

    Parameters
    ----------
    nums: list[int]

    target: int

    Returns
    -------
    out : list[list[int]]

    Examples
    --------
    >>> fourSum([1,0,-1,0,-2,2], 0)
    [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    >>> fourSum([2,2,2,2,2], 8)
    [[2, 2, 2, 2]]
    """
    nums.sort()
    ans = []
    n = len(nums)
    x = 0
    for i in range(n - 3):
        x = nums[i]
        if i > 0 and x == nums[i - 1]:
            continue
        res = threeSum(nums[i + 1:], target - x)
        if res:
            for r in res:
                rr = r[::-1]
                rr.append(x)
                ans.append(rr[::-1])
    return ans

def threeSum(nums: list[int], target: int) -> list[list[int]]:
    res = []
    for i in range(len(nums) - 2):
        # Skip duplicate nums[i]
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                res.append([nums[i], nums[left], nums[right]])
                # Skip duplicate nums[left]
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate nums[right]
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return res
