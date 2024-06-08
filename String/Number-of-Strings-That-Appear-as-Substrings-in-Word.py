def numOfStrings(patterns: list[str], word: str) -> int:
    """
    ID: 1967
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array of strings patterns and a string word, return the number of strings in patterns
    that exist as a substring in word.

    A substring is a contiguous sequence of characters within a string.

    Parameters
    ----------
    patterns: list[str]

    word: str

    Returns
    -------
    int

    Examples
    --------
    >>> numOfStrings(["a","abc","bc","d"], "abc")
    3

    Explanation:
    - "a" appears as a substring in "abc".
    - "abc" appears as a substring in "abc".
    - "bc" appears as a substring in "abc".
    - "d" does not appear as a substring in "abc".
    3 of the strings in patterns appear as a substring in word.

    >>> numOfStrings(["a","b","c"], "aaaaabbbbb")
    2

    Explanation:
    - "a" appears as a substring in "aaaaabbbbb".
    - "b" appears as a substring in "aaaaabbbbb".
    - "c" does not appear as a substring in "aaaaabbbbb".
    2 of the strings in patterns appear as a substring in word.

    >>> numOfStrings(["a","a","a"], "ab")
    3

    Explanation: Each of the patterns appears as a substring in word "ab".
    """
    return sum([p in word for p in patterns])
