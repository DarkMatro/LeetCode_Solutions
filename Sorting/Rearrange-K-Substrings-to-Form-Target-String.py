from collections import Counter


def isPossibleToRearrange(s: str, t: str, k: int) -> bool:
    """
    ID: 3365
    Tags:   Hash Table, String, Sorting
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given two strings s and t, both of which are anagrams of each other, and an integer k.

    Your task is to determine whether it is possible to split the string s into k equal-sized
    substrings, rearrange the substrings, and concatenate them in any order to create a new string
    that matches the given string t.

    Return true if this is possible, otherwise, return false.

    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    using all the original letters exactly once.

    A substring is a contiguous non-empty sequence of characters within a string.

    Parameters
    ----------
    s: str

    t: str

    k: int

    Returns
    -------
    bool

    Examples
    --------
    >>> isPossibleToRearrange("abcd", "cdab", 2)
    True

    Explanation: Split s into 2 substrings of length 2: ["ab", "cd"].
    Rearranging these substrings as ["cd", "ab"], and then concatenating them results in "cdab",
    which matches t.

    >>> isPossibleToRearrange("aabbcc", "bbaacc", 3)
    True

    Explanation: Split s into 3 substrings of length 2: ["aa", "bb", "cc"].
    Rearranging these substrings as ["bb", "aa", "cc"], and then concatenating them results in
    "bbaacc", which matches t

    >>> isPossibleToRearrange("aabbcc", "bbaacc", 2)
    False

    Explanation: Split s into 2 substrings of length 3: ["aab", "bcc"].
    These substrings cannot be rearranged to form t = "bbaacc", so the output is false.
    """
    n = len(s)
    m = n // k
    return Counter([s[i: i + m] for i in range(0, n, m)]) == Counter(
        [t[i: i + m] for i in range(0, n, m)])
