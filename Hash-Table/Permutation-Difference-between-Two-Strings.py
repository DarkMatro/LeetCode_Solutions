def findPermutationDifference(s: str, t: str) -> int:
    """
    ID: 3146
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given two strings s and t such that every character occurs at most once in s and t is a
    permutation of s.

    The permutation difference between s and t is defined as the sum of the absolute difference
    between the index of the occurrence of each character in s and the index of the occurrence of
    the same character in t.

    Return the permutation difference between s and t.

    Parameters
    ----------
    s: str

    t: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> findPermutationDifference('abc', 'bac')
    2

    Explanation:
    For s = "abc" and t = "bac", the permutation difference of s and t is equal to the sum of:

    The absolute difference between the index of the occurrence of "a" in s and the index of the
    occurrence of "a" in t.
    The absolute difference between the index of the occurrence of "b" in s and the index of the
    occurrence of "b" in t.
    The absolute difference between the index of the occurrence of "c" in s and the index of the
    occurrence of "c" in t.
    That is, the permutation difference between s and t is equal to |0 - 1| + |1 - 0| + |2 - 2| = 2.

    >>> findPermutationDifference('abcde', 'edbac')
    12

    Explanation: The permutation difference between s and t is equal to |0 - 3| + |1 - 2| + |2 - 4|
    + |3 - 1| + |4 - 0| = 12.
    """
    s_ = {x: i for i, x in enumerate(s)}
    t_ = {x: i for i, x in enumerate(t)}
    ans = 0
    for k, v in s_.items():
        ans += abs(v - t_[k])
    return ans
