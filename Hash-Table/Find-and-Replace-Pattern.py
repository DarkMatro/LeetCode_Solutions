def findAndReplacePattern(words: list[str], pattern: str) -> list[str]:
    """
    ID: 890
    Tags:   Array, Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a list of strings words and a string pattern, return a list of words[i] that match
    pattern. You may return the answer in any order.

    A word matches the pattern if there exists a permutation of letters p so that after replacing
    every letter x in the pattern with p(x), we get the desired word.

    Recall that a permutation of letters is a bijection from letters to letters: every letter maps
    to another letter, and no two letters map to the same letter

    Parameters
    ----------
    words: list[str]

    pattern: str

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")
    ['mee', 'aqq']

    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
    "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and
    b map to the same letter.

    >>> findAndReplacePattern(["a","b","c"], "a")
    ['a', 'b', 'c']
    """
    return [x for x in words if isIsomorphic(x, pattern)]


def isIsomorphic(s: str, t: str) -> bool:
    for i, v in enumerate(s):
        if s.index(v) != t.index(t[i]):
            return False
    return True