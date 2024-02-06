def kLengthApart(nums: list[int], k: int) -> bool:
    """
    ID: 1437
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other,
    otherwise return false.

    Parameters
    ----------
    nums : list[int]

    k: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> kLengthApart[1,0,0,0,1,0,0,1], 2)
    True

    Explanation: Each of the 1s are at least 2 places away from each other.

    >>> kLengthApart[1,0,0,1,0,1], 2)
    False

    Explanation: The second 1 and third 1 are only one apart from each other.
    """
    j = k
    for num in nums:
        if num and j < k:
            return False
        elif num:
            j = 0
        else:
            j += 1
    return True
