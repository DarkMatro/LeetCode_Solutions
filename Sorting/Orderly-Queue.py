def orderlyQueue(s: str, k: int) -> str:
    """
    ID: 899
    Tags:   Math, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given a string s and an integer k. You can choose one of the first k letters of s and
    append it at the end of the string.

    Return the lexicographically smallest string you could have after applying the mentioned step
    any number of moves.

    Parameters
    ----------
    s: str

    k: int

    Returns
    -------
    str

    Examples
    --------
    >>> orderlyQueue('cba', 1)
    'acb'

    Explanation: In the first move, we move the 1st character 'c' to the end, obtaining the string
    "bac".
    In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".

    >>> orderlyQueue('baaca', 3)
    'aaabc'

    Explanation: In the first move, we move the 1st character 'b' to the end, obtaining the string
    "aacab".
    In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc"
    """
    if k > 1:
        return ''.join(sorted(s))
    return min(s[i:] + s[:i] for i in range(len(s)))

