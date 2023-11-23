def plus_one(digits: list[int]) -> list[int]:
    """
    ID: 0066
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
    integer. The digits are ordered from most significant to the least significant in left-to-right order. The large
    integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    Parameters
    ----------
    digits : list[int]

    Returns
    -------
    res : list[int]

    Examples
    --------
    >>> plus_one([1, 2, 3])
    [1, 2, 4]

    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].

    >>> plus_one([4, 3, 2, 1])
    [4, 3, 2, 2]

    Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].

    >>> plus_one([9])
    [1, 0]

    Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].
    """
    res = digits
    res[-1] += 1
    if res[-1] == 10:
        for i in range(len(res) - 2, -1, -1):
            if res[i + 1] == 10:
                res[i] += 1
                res[i + 1] = 0
        if res[0] == 10:
            res[0] = 0
            res.insert(0, 1)
    return res
