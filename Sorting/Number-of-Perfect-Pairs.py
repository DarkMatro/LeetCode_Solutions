def perfectPairs(nums: list[int]) -> int:
    """
    ID: 3649
    Tags:   Array, Math, Two Pointers, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums.

    A pair of indices (i, j) is called perfect if the following conditions are satisfied:

    i < j
    Let a = nums[i], b = nums[j]. Then:
    min(|a - b|, |a + b|) <= min(|a|, |b|)
    max(|a - b|, |a + b|) >= max(|a|, |b|)
    Return the number of distinct perfect pairs.

    Note: The absolute value |x| refers to the non-negative value of x.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> perfectPairs([0,1,2,3])
    2

    Explanation:
    There are 2 perfect pairs:

    (i, j)	(a, b)	min(|a − b|, |a + b|)	    min(|a|, |b|)	max(|a − b|, |a + b|)	    max(|a|, |b|)
    (1, 2)	(1, 2)	min(|1 − 2|, |1 + 2|) = 1	    1	        max(|1 − 2|, |1 + 2|) = 3	    2
    (2, 3)	(2, 3)	min(|2 − 3|, |2 + 3|) = 1	    2	        max(|2 − 3|, |2 + 3|) = 5	    3

    >>> perfectPairs([-3,2,-1,4])
    4

    Explanation:
    There are 4 perfect pairs:

    (i, j)	(a, b)	min(|a − b|, |a + b|)	    min(|a|, |b|)	max(|a − b|, |a + b|)	        max(|a|, |b|)
    (0, 1)	(-3, 2)	min(|-3 - 2|, |-3 + 2|) = 1	    2	        max(|-3 - 2|, |-3 + 2|) = 5	        3
    (0, 3)	(-3, 4)	min(|-3 - 4|, |-3 + 4|) = 1	    3	        max(|-3 - 4|, |-3 + 4|) = 7	        4
    (1, 2)	(2, -1)	min(|2 - (-1)|, |2 + (-1)|) = 1	1	        max(|2 - (-1)|, |2 + (-1)|) = 3	    2
    (1, 3)	(2, 4)	min(|2 - 4|, |2 + 4|) = 2	    2	        max(|2 - 4|, |2 + 4|) = 6	        4

    >>> perfectPairs([1,10,100,1000])
    0

    Explanation:
    There are no perfect pairs. Thus, the answer is 0.
    """
    nums = [abs(x) for x in nums]
    nums.sort()

    n, left = len(nums), 0
    ans = (n - 1) * n // 2

    for right, num in enumerate(nums):
        while left < right and num > 2 * nums[left]:
            left += 1
        ans -= left

    return ans
