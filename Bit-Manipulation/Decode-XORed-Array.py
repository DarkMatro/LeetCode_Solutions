def decode(encoded: list[int], first: int) -> list[int]:
    """
    ID: 1720
    Tags:   Array, Bit Manipulation
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    There is a hidden integer array arr that consists of n non-negative integers.

    It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
    For example, if arr = [1,0,2,1], then encoded = [1,2,3].

    You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

    Return the original array arr. It can be proved that the answer exists and is unique.

    Parameters
    ----------
    encoded: list[int]

    first: int

    Returns
    -------
    list[int]

    Examples
    --------
    >>> decode([1,2,3], 1)
    [1, 0, 2, 1]

    Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

    >>> decode([6,2,7,3], 4)
    [4, 2, 0, 7, 4]
    """
    arr = [first] * (len(encoded) + 1)
    for i in range(1, len(arr)):
        arr[i] = encoded[i - 1] ^ arr[i - 1]
    return arr


