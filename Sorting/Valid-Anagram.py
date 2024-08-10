from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    """
    ID: 0242
    Tags:   Hash Table, String, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
    the original letters exactly once.


    Parameters
    ----------
    s : str
    t : str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> is_anagram("anagram", "nagaram")
    True

    >>> is_anagram("rat", "car")
    False
    """
    if len(s) != len(t):
        return False
    s_d = defaultdict(int)
    for i in s:
        s_d[i] += 1

    t_d = defaultdict(int)
    for i in t:
        t_d[i] += 1

    for k, v in s_d.items():
        if k not in t_d or t_d[k] != v:
            return False

    return True
