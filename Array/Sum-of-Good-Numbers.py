def sumOfGoodNumbers(nums: list[int], k: int) -> int:
    """
    ID: 3452
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array of integers nums and an integer k, an element nums[i] is considered good if it is
    strictly greater than the elements at indices i - k and i + k (if those indices exist). If
    neither of these indices exists, nums[i] is still considered good.

    Return the sum of all the good elements in the array.

    Parameters
    ----------
    nums : list[int]

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumOfGoodNumbers([1,3,2,1,5,4], 2)
    12

    Explanation: The good numbers are nums[1] = 3, nums[4] = 5, and nums[5] = 4 because they are
    strictly greater than the numbers at indices i - k and i + k.

    >>> sumOfGoodNumbers([2,1], 1)
    2

    Explanation: The only good number is nums[0] = 2 because it is strictly greater than nums[1].
    """
    n = len(nums)
    good_sum = 0
    for i, x in enumerate(nums):
        if i - k >= 0 and x <= nums[i - k]:
            continue
        if i + k < n and x <= nums[i + k]:
            continue
        good_sum += x
    return good_sum
