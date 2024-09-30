def wordPattern(pattern: str, s: str) -> bool:
    """
    ID: 290
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and
    a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

    Parameters
    ----------
    pattern: str

    s: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> wordPattern('abba', 'dog cat cat dog')
    True

    Explanation: The bijection can be established as:

    'a' maps to "dog".
    'b' maps to "cat".

    >>> wordPattern('abba', 'dog cat cat fish')
    False

    >>> wordPattern('aaaa', 'dog cat cat dog')
    False
    """
    words = s.split(' ')
    if len(words) != len(pattern):
        return False
    d = {}
    for x, word in zip(pattern, words):
        if x not in d:
            d[x] = word
            continue
        if d[x] != word:
            return False
    if len(set(d.values())) != len(d):
        return False
    return True
