def arrayRankTransform(arr: list[int]) -> list[int]:
    """
    ID: 1331
    Tags:   Array, Hash Table, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Given an array of integers arr, replace each element with its rank.

    The rank represents how large the element is. The rank has the following rules:

    Rank is an integer starting from 1.
    The larger the element, the larger the rank. If two elements are equal, their rank must be the
    same.
    Rank should be as small as possible.

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    list[int]

    Examples
    --------
    >>> arrayRankTransform([40,10,20,30])
    [4, 1, 2, 3]

    Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the
    third smallest.

    >>> arrayRankTransform([100,100,100])
    [1, 1, 1]

    Explanation: Same elements share the same rank.

    >>> arrayRankTransform([37,12,28,9,100,56,80,5,12])
    [5, 3, 4, 2, 8, 6, 7, 1, 3]
    """
    d = {}
    i = 1
    for x in sorted(arr):
        if x not in d:
            d[x] = i
            i += 1
    return [d[x] for x in arr]
