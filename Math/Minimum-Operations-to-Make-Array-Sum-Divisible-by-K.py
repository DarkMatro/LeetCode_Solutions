def minOperations(nums: list[int], k: int) -> int:
    """
    ID: 3512
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums and an integer k. You can perform the following operation any number of times:

    Select an index i and replace nums[i] with nums[i] - 1.
    Return the minimum number of operations required to make the sum of the array divisible by k.

    Parameters
    ----------
    nums: list[int]

    k: int

    Returns
    -------
    int

    Examples
    --------
    >>> minOperations([3,9,7], 5)
    4

    Explanation:
    Perform 4 operations on nums[1] = 9. Now, nums = [3, 5, 7].
    The sum is 15, which is divisible by 5.

    >>> minOperations([4,1,3], 4)
    0

    Explanation:
    The sum is 8, which is already divisible by 4. Hence, no operations are needed.

    >>> minOperations([3,2], 6)
    5

    Explanation:
    Perform 3 operations on nums[0] = 3 and 2 operations on nums[1] = 2. Now, nums = [0, 0].
    The sum is 0, which is divisible by 6.
    """
    return sum(nums) % k
