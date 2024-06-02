def getConcatenation(nums: list[int]) -> list[int]:
    """
    ID: 1929
    Tags:   Array, Simulation
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and
    ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

    Specifically, ans is the concatenation of two nums arrays.

    Return the array ans.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> getConcatenation([1,2,1])
    [1, 2, 1, 1, 2, 1]

    Explanation: The array ans is formed as follows:
    - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
    - ans = [1,2,1,1,2,1]

    >>> getConcatenation([1,3,2,1])
    [1, 3, 2, 1, 1, 3, 2, 1]

    Explanation: The array ans is formed as follows:
    - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
    - ans = [1,3,2,1,1,3,2,1]
    """
    return [nums[nums[i]] for i, _ in enumerate(nums)]
