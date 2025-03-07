def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    """
    ID: 1200
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Given an array of distinct integers arr, find all pairs of elements with the minimum absolute
    difference of any two elements.

    Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    list[list[int]]

    Examples
    --------
    >>> minimumAbsDifference([4,2,1,3])
    [[1, 2], [2, 3], [3, 4]]

    Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in
    ascending order.

    >>> minimumAbsDifference([1, 3, 6, 10, 15])
    [[1, 3]]

    >>> minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
    [[-14, -10], [19, 23], [23, 27]]
    """
    arr.sort()
    diff = arr[1] - arr[0]
    prev = arr[0]
    ans = []
    for i, x in enumerate(arr):
        if i == 0:
            continue
        new_diff = abs(prev - x)
        if new_diff == diff:
            ans.append([prev, x])
        elif new_diff < diff:
            diff = new_diff
            ans = [[prev, x]]
        prev = x
    return ans
