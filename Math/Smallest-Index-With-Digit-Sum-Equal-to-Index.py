def smallestIndex(nums: list[int]) -> int:
    """
    ID: 3550
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums.

    Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

    If no such index exists, return -1.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> smallestIndex([1,3,2])
    2

    Explanation: For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

    >>> smallestIndex([1,10,11])
    1

    Explanation: For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
    For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
    Since index 1 is the smallest, the output is 1.

    >>> smallestIndex([1,2,3])
    -1

    Explanation: Since no index satisfies the condition, the output is -1.
    """

    def get_digits(n: int) -> list[int]:
        digits = []
        while n != 0:
            digits.append(n % 10)
            n //= 10
        return digits

    for i, x in enumerate(nums):
        if sum(get_digits(x)) == i:
            return i
    return -1
