def findWordsContaining(words: list[str], x: str) -> list[int]:
    """
    ID: 2942
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed array of strings words and a character x.

    Return an array of indices representing the words that contain the character x.

    Note that the returned array may be in any order.

    Parameters
    ----------
    words: list[str]

    x: str

    Returns
    -------
    list[int]

    Examples
    --------
    >>> findWordsContaining(["leet","code"], 'e')
    [0, 1]

    Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

    >>> findWordsContaining(["abc","bcd","aaaa","cbc"], 'a')
    [0, 2]

    Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

    >>> findWordsContaining(["abc","bcd","aaaa","cbc"], 'z')
    []

    Explanation: "z" does not occur in any of the words. Hence, we return an empty array.
    """
    return [i for i, word in enumerate(words) if x in word]
