def sumSubseqWidths(nums: list[int]) -> int:
    """
    ID: 891
    Tags:   Array, Math, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    The width of a sequence is the difference between the maximum and minimum elements in the
    sequence.

    Given an array of integers nums, return the sum of the widths of all the non-empty subsequences
    of nums. Since the answer may be very large, return it modulo 109 + 7.

    A subsequence is a sequence that can be derived from an array by deleting some or no elements
    without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of
    the array [0,3,1,6,2,2,7].

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> sumSubseqWidths([2,1,3])
    6

    Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
    The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
    The sum of these widths is 6.

    >>> sumSubseqWidths([2])
    0
    """
    mod = 10 ** 9 + 7
    nums.sort()
    ans, pow2 = 0, 1
    for x, y in zip(nums, reversed(nums)):
        ans += (x - y) * pow2
        pow2 = pow2 * 2 % mod
    return ans % mod
