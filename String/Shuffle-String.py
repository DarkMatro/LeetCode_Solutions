def restoreString(s: str, indices: list[int]) -> str:
    """
    ID: 1528
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string s and an integer array indices of the same length. The string s will be shuffled such that
    the character at the ith position moves to indices[i] in the shuffled string.

    Return the shuffled string.

    Parameters
    ----------
    s: str

    indices: list[int]

    Returns
    -------
    out : str

    Examples
    --------
    >>> restoreString("codeleet", [4,5,6,7,0,2,1,3])
    'leetcode'

    Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

    >>> restoreString("abc", [0,1,2])
    'abc'

    Explanation: After shuffling, each character remains in its position.
    """
    arr = [''] * len(indices)
    for i, n in enumerate(indices):
        arr[n] = s[i]
    return ''.join(arr)
