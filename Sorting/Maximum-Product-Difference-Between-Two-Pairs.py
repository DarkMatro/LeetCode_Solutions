def maxProductDifference(nums: list[int]) -> int:
    """
    ID: 1913
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

    For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
    Given an integer array nums, choose four distinct indices w, x, y, and z such that the product
    difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

    Return the maximum such product difference.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> maxProductDifference([5,6,2,7,4])
    34

    Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the
    second pair (2, 4). The product difference is (6 * 7) - (2 * 4) = 34.

    >>> maxProductDifference([4,2,5,9,7,4,8])
    64

    Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the
    second pair (2, 4). The product difference is (9 * 8) - (2 * 4) = 64.
    """
    nums.sort()
    return nums[-1] * nums[-2] - nums[0] * nums[1]
