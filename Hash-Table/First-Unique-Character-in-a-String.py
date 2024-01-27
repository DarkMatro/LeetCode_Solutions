from collections import defaultdict


def first_uniq_char(s: str) -> int:
    """
    ID: 0387
    Tags:   Hash Table, String, Queue, Counting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist,
    return -1.

    Parameters
    ----------
    s : str

    Returns
    -------
    out : int

    Examples
    --------
    >>> first_uniq_char("leetcode")
    0

    >>> first_uniq_char("loveleetcode")
    2

    >>> first_uniq_char("aabb")
    -1
    """
    res = -1
    d = defaultdict(int)
    for i, v in enumerate(s):
        d[v] += 1

    w = {}
    for k, v in d.items():
        if v == 1:
            w[k] = v
    if w:
        lt = list(w.items())[0][0]
        res = s.index(lt)
    return res
