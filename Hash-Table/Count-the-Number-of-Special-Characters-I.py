def numberOfSpecialChars(word: str) -> int:
    """
    ID: 3120
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a string word. A letter is called special if it appears both in lowercase and
    uppercase in word.

    Return the number of special letters in word.

    Parameters
    ----------
    word: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> numberOfSpecialChars('aaAbcBC')
    3

    Explanation: The special characters in word are 'a', 'b', and 'c'.

    >>> numberOfSpecialChars('abc')
    0

    Explanation: No character in word appears in uppercase.

    >>> numberOfSpecialChars('abBCab')
    1

    Explanation: The only special character in word is 'b'.
    """
    spec = set()
    for x in word:
        if x.isupper() and x.lower() in word:
            spec.add(x)
    return len(spec)
