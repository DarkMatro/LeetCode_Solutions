def countPrefixes(words: list[str], s: str) -> int:
    """
    ID: 2255
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string array words and a string s, where words[i] and s comprise only of
    lowercase English letters.

    Return the number of strings in words that are a prefix of s.

    A prefix of a string is a substring that occurs at the beginning of the string. A substring is
    a contiguous sequence of characters within a string.

    Parameters
    ----------
    words: list[str]

    s: str

    Returns
    -------
    out: int

    Examples
    --------
    >>> countPrefixes(["a","b","c","ab","bc","abc"], "abc")
    3

    Explanation: The strings in words which are a prefix of s = "abc" are:
    "a", "ab", and "abc".
    Thus, the number of strings in words which are a prefix of s is 3.

    >>> countPrefixes(["a","a"], "aa")
    2

    Explanation: Both of the strings are a prefix of s.
    Note that the same string can occur multiple times in words, and it should be counted each time.
    """
    ans = 0
    for w in words:
        if len(w) > len(s):
            continue
        for i, ch in enumerate(w):
            if s[i] != ch:
                break
        else:
            ans += 1
    return ans
