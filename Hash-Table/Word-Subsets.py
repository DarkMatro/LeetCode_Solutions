from collections import Counter


def wordSubsets(words1: list[str], words2: list[str]) -> list[str]:
    """
    ID: 916
    Tags:   Array, Hash Table, String
    Time:   O(N+M)
    Memory: O(N)

    Task
    ----------
    You are given two string arrays words1 and words2.

    A string b is a subset of string a if every letter in b occurs in a including multiplicity.

    For example, "wrr" is a subset of "warrior" but is not a subset of "world".
    A string a from words1 is universal if for every string b in words2, b is a subset of a.

    Return an array of all the universal strings in words1. You may return the answer in any order.

    Parameters
    ----------
    words1: list[str]

    words2: list[str]

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"])
    ['facebook', 'google', 'leetcode']

    >>> wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"])
    ['apple', 'google', 'leetcode']
    """
    ans = []
    cnt = Counter()
    for w in words2:
        cnt |= Counter(w)
    for w in words1:
        cnt_w = Counter(w)
        if len(cnt - cnt_w) > 0:
            continue
        ans.append(w)
    return ans
