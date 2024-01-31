def findNumbers(nums: list[int]) -> int:
    """
    ID: 1295
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array nums of integers, return how many of them contain an even number of digits.

    Parameters
    ----------
    nums : list[str]

    Returns
    -------
    out: int

    Examples
    --------
    >>> findNumbers([12,345,2,6,7896])
    2

    Explanation:
    12 contains 2 digits (even number of digits).
    345 contains 3 digits (odd number of digits).
    2 contains 1 digit (odd number of digits).
    6 contains 1 digit (odd number of digits).
    7896 contains 4 digits (even number of digits).
    Therefore only 12 and 7896 contain an even number of digits.

    >>> findNumbers([555,901,482,1771])
    1

    Explanation:
    Only 1771 contains an even number of digits.
    """
    ans = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            ans += 1
    return ans
