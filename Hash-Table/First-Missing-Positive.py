def firstMissingPositive(nums: list[int]) -> int:
    """
    ID: 41
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an unsorted integer array nums. Return the smallest positive integer that is not present
    in nums.

    You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> firstMissingPositive([1,2,0])
    3

    Explanation: The numbers in the range [1,2] are all in the array.

    >>> firstMissingPositive([3,4,-1,1])
    2

    Explanation: 1 is in the array but 2 is missing.

    >>> firstMissingPositive([7,8,9,11,12])
    1

    Explanation: The smallest positive integer 1 is missing.
    """
    n = len(nums)

    # Step 1: Place numbers in their correct positions
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap

    # Step 2: Find the first missing positive number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all are in place, return n + 1
    return n + 1
