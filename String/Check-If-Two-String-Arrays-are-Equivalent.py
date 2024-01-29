def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    """
    ID: 1662
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false
    otherwise.

    A string is represented by an array if the array elements concatenated in order forms the string.

    Parameters
    ----------
    word1: list[str]

    word2: list[str]

    Returns
    -------
    bool

    Examples
    --------
    >>> arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
    True

    Explanation:
    word1 represents string "ab" + "c" -> "abc"
    word2 represents string "a" + "bc" -> "abc"
    The strings are the same, so return true.

    >>> arrayStringsAreEqual(["a", "cb"], ["ab", "c"])
    False

    >>> arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])
    True
    """
    return ''.join(word1) == ''.join(word2)
