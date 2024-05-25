def isArraySpecial(nums: list[int]) -> bool:
    """
    ID: 3151
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    An array is considered special if every pair of its adjacent elements contains two numbers with
    different parity.

    You are given an array of integers nums. Return true if nums is a special array, otherwise,
    return false.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isArraySpecial([1])
    True

    Explanation: There is only one element. So the answer is true.

    >>> isArraySpecial([2,1,4])
    True

    Explanation: There is only two pairs: (2,1) and (1,4), and both of them contain numbers with
    different parity. So the answer is true.

    >>> isArraySpecial([4,3,1,6])
    False

    Explanation: nums[1] and nums[2] are both odd. So the answer is false.
    """
    ans = True
    prev = nums[0] % 2
    for i in range(1, len(nums)):
        curr = nums[i] % 2
        if curr == prev:
            ans = False
        prev = curr

    return ans


