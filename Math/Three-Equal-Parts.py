def threeEqualParts(arr: list[int]) -> list[int]:
    """
    ID: 927
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an array arr which consists of only zeros and ones, divide the array into three
    non-empty parts such that all of these parts represent the same binary value.

    If it is possible, return any [i, j] with i + 1 < j, such that:

    arr[0], arr[1], ..., arr[i] is the first part,
    arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
    arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
    All three parts have equal binary values.
    If it is not possible, return [-1, -1].

    Note that the entire part is used when considering what binary value it represents. For example,
    [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1]
    represent the same value.

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> threeEqualParts([1,0,1,0,1])
    [0, 3]

    >>> threeEqualParts([1,1,0,1,1])
    [-1, -1]

    >>> threeEqualParts([1,1,0,0,1])
    [0, 2]
    """
    total_ones = arr.count(1)

    # If there are no 1's at all, any division will work, so we return [0, len(arr) - 1]
    if total_ones == 0:
        return [0, len(arr) - 1]

    # If total ones is not divisible by 3, return [-1, -1]
    if total_ones % 3 != 0:
        return [-1, -1]

    k = total_ones // 3
    first = second = third = -1
    count = 0

    # Find the first, second and third part starting points
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            if count == 1:
                first = i
            elif count == k + 1:
                second = i
            elif count == 2 * k + 1:
                third = i
                break

    # Check if the parts from first, second, and third to end are the same
    while third < len(arr) and arr[first] == arr[second] == arr[third]:
        first += 1
        second += 1
        third += 1

    # If we successfully matched all parts
    if third == len(arr):
        return [first - 1, second]
    else:
        return [-1, -1]
