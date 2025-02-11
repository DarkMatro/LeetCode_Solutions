def stableMountains(height: list[int], threshold: int) -> list[int]:
    """
    ID: 3285
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    There are n mountains in a row, and each mountain has a height. You are given an integer array
    height where height[i] represents the height of mountain i, and an integer threshold.

    A mountain is called stable if the mountain just before it (if it exists) has a height strictly
    greater than threshold. Note that mountain 0 is not stable.

    Return an array containing the indices of all stable mountains in any order.

    Parameters
    ----------
    height: list[int]

    threshold: int

    Returns
    -------
    list[int]

    Examples
    --------
    >>> stableMountains([1,2,3,4,5], 2)
    [3, 4]

    Explanation:

    Mountain 3 is stable because height[2] == 3 is greater than threshold == 2.
    Mountain 4 is stable because height[3] == 4 is greater than threshold == 2.

    >>> stableMountains([10,1,10,1,10], 3)
    [1, 3]

    >>> stableMountains([10,1,10,1,10], 10)
    []
    """
    ans = []
    is_greater = False
    for i, v in enumerate(height):
        if is_greater:
            ans.append(i)
        is_greater = v > threshold
    return ans
