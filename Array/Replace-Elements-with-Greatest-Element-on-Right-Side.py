def replaceElements(arr: list[int]) -> list[int]:
    """
    ID: 1299
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array arr, replace every element in that array with the greatest element among the elements to its right,
    and replace the last element with -1.

    After doing so, return the array.

    Parameters
    ----------
    arr : list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> replaceElements([17,18,5,4,6,1])
    [18, 6, 6, 6, 1, -1]

    Explanation:
    - index 0 --> the greatest element to the right of index 0 is index 1 (18).
    - index 1 --> the greatest element to the right of index 1 is index 4 (6).
    - index 2 --> the greatest element to the right of index 2 is index 4 (6).
    - index 3 --> the greatest element to the right of index 3 is index 4 (6).
    - index 4 --> the greatest element to the right of index 4 is index 5 (1).
    - index 5 --> there are no elements to the right of index 5, so we put -1.

    >>> replaceElements([400])
    [-1]
    """
    max_v = -1
    for i in range(len(arr) - 1, -1, -1):
        prev_v = arr[i]
        arr[i] = max_v
        max_v = max(max_v, prev_v)
    return arr
