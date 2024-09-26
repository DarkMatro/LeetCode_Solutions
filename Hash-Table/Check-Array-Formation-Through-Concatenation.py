def canFormArray(arr: list[int], pieces: list[list[int]]) -> bool:
    """
    ID: 1640
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an array of distinct integers arr and an array of integer arrays pieces, where the
    integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces
    in any order. However, you are not allowed to reorder the integers in each array pieces[i].

    Return true if it is possible to form the array arr from pieces. Otherwise, return false.

    Parameters
    ----------
    arr: list[int]

    pieces: list[list[int]]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> canFormArray([15,88], [[88],[15]])
    True

    Explanation: Concatenate [15] then [88]

    >>> canFormArray([49,18,16], [[16,18,49]])
    False

    Explanation: Even though the numbers match, we cannot reorder pieces[0].

    >>> canFormArray([91,4,64,78], [[78],[4,64],[91]])
    True

    Explanation: Concatenate [91] then [4,64] then [78]
    """
    d = {x[0]: x for x in pieces}
    new_list = []
    for num in arr:
        if num not in d:
            continue
        new_list.extend(d[num])
    return new_list == arr
