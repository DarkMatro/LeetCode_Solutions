from collections import Counter


def findLUSlength(strs: list[str]) -> int:
    """
    ID: 522
    Tags: Array, Hash Table, Two Pointers, String, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest
    uncommon subsequence does not exist, return -1.

    An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the
    others.

    A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

    For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get
    "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

    Parameters
    ----------
    strs: list[str]

    Returns
    -------
    out : int

    Examples
    --------
    >>> findLUSlength(["aba","cdc","eae"])
    3

    >>> findLUSlength(["aaa","aaa","aa"])
    -1
    """

    def is_subsequence(a: str, b: str) -> bool:
        """Check if `a` is subsequence of `b`."""
        i = 0
        for ch in b:
            if i < len(a) and a[i] == ch:
                i += 1
        return i == len(a)

    # Step 1: Count frequencies
    freq = Counter(strs)

    # Step 2: Sort by length (longest first)
    strs_sorted = sorted(strs, key=len, reverse=True)

    # Step 3: Check candidates
    for i, s in enumerate(strs_sorted):
        if freq[s] > 1:  # skip duplicates
            continue
        if all(not is_subsequence(s, strs_sorted[j])
               for j in range(len(strs_sorted)) if i != j):
            return len(s)

    return -1
