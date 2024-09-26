def getSneakyNumbers(nums: list[int]) -> list[int]:
    """
    ID: 3289
    Tags:   Array, Hash Table, Math
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    In the town of Digitville, there was a list of numbers called nums containing integers from 0
    to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous
    numbers sneaked in an additional time, making the list longer than usual.

    As the town detective, your task is to find these two sneaky numbers. Return an array of size
    two containing the two numbers (in any order), so peace can return to Digitville.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> getSneakyNumbers([0,1,1,0])
    [1, 0]

    Explanation: The numbers 0 and 1 each appear twice in the array.

    >>> getSneakyNumbers([0,3,2,1,3,2])
    [3, 2]

    Explanation: The numbers 2 and 3 each appear twice in the array.

    >>> getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2])
    [4, 5]

    Explanation: The numbers 4 and 5 each appear twice in the array.
    """
    d = set()
    ans = []
    for num in nums:
        if num in d:
            ans.append(num)
        d.add(num)
    return ans
