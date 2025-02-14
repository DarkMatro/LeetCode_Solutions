def sum_of_digits(n: int) -> int:
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    return sum(digits)

def minElement(nums: list[int]) -> int:
    """
    ID: 3300
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums.

    You replace each element in nums with the sum of its digits.

    Return the minimum element in nums after all replacements.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> minElement([10,12,13,14])
    1

    Explanation:
    nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

    >>> minElement([1,2,3,4])
    1

    Explanation:
    nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

    >>> minElement([999,19,199])
    10

    Explanation:
    nums becomes [27, 10, 19] after all replacements, with minimum element 10.
    """
    ans = 10001
    for num in nums:
        ans = min(ans, sum_of_digits(num))
    return ans
