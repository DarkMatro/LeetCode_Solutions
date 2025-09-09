def distinctAverages(nums: list[int]) -> int:
    """
    ID: 2465
    Tags:   Array, Hash Table, Two Pointers, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given a 0-indexed integer array nums of even length.

    As long as nums is not empty, you must repetitively:

    Find the minimum number in nums and remove it.
    Find the maximum number in nums and remove it.
    Calculate the average of the two removed numbers.
    The average of two numbers a and b is (a + b) / 2.

    For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
    Return the number of distinct averages calculated using the above process.

    Note that when there is a tie for a minimum or maximum number, any can be removed.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> distinctAverages([4,1,4,0,3,5])
    2

    Explanation: 1. Remove 0 and 5, and the average is (0 + 5) / 2 = 2.5. Now, nums = [4,1,4,3].
    2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5, and nums = [4,3].
    3. Remove 3 and 4, and the average is (3 + 4) / 2 = 3.5.
    Since there are 2 distinct numbers among 2.5, 2.5, and 3.5, we return 2.

    >>> distinctAverages([1,100])
    1

    Explanation: There is only one average to be calculated after removing 1 and 100, so we return 1.
    """
    nums.sort()
    lp, rp = 0, len(nums) - 1
    avg = set()
    while lp <= rp:
        avg.add((nums[lp] + nums[rp]) / 2)
        lp += 1
        rp -= 1
    return len(avg)
