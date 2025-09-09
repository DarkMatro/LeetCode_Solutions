def duplicateZeros(arr: list[int]) -> None:
    """
    ID: 1089
    Tags:   Array, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the
    right.

    Note that elements beyond the length of the original array are not written. Do the above modifications to the input
    array in place and do not return anything.

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    out : None

    Examples
    --------
    >>> duplicateZeros([1,0,2,3,0,4,5,0])
    [1, 0, 0, 2, 3, 0, 0, 4]

    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

    >>> duplicateZeros([1, 2, 3])
    [1, 2, 3]

    Explanation: After calling your function, the input array is modified to: [1,2,3]
    """
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    zeros = arr.count(0)  # total zeros to duplicate
    i = n - 1
    j = n + zeros - 1  # virtual index with duplicates

    # Fill backwards
    while i < j:
        if arr[i] != 0:
            if j < n:
                arr[j] = arr[i]
        else:
            # duplicate zero
            if j < n:
                arr[j] = 0
            j -= 1
            if j < n:
                arr[j] = 0
        i -= 1
        j -= 1
    return arr