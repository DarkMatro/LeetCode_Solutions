def trimMean(arr: list[int]) -> float:
    """
    ID: 1619
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Given an integer array arr, return the mean of the remaining integers after removing the
    smallest 5% and the largest 5% of the elements.

    Answers within 10-5 of the actual answer will be considered accepted.

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    float

    Examples
    --------
    >>> trimMean([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3])
    2.0

    Explanation: After erasing the minimum and the maximum values of this array, all elements are
    equal to 2, so the mean is 2.

    >>> trimMean([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0])
    4.0

    >>> trimMean([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4])
    4.777777777777778
    """
    arr.sort()
    n = len(arr)
    rem_idx = round(5 * n / 100)
    return sum(arr[rem_idx:-rem_idx]) / (n - 2 * rem_idx)
