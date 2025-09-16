def threeSum(nums: list[int]) -> list[list[int]]:
    """
    ID: 15
    Tags: Array, Two Pointers, Sorting
    Time:   O(N^2)
    Memory: O(1)

    Task
    ----------
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and
    j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : list[list[int]]

    Examples
    --------
    >>> threeSum([-1,0,1,2,-1,-4])
    [[-1, -1, 2], [-1, 0, 1]]

    Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

    >>> threeSum([0,1,1])
    []

    Explanation: The only possible triplet does not sum up to 0.

    >>> threeSum([0,0,0])
    [[0, 0, 0]]

    Explanation: The only possible triplet sums up to 0.
    """
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        # Skip duplicate nums[i]
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                # Skip duplicate nums[left]
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate nums[right]
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return res
