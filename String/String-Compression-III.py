def compressedString(word: str) -> str:
    """
    ID: 3163
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string word, compress it using the following algorithm:

    Begin with an empty string comp. While word is not empty, use the following operation:
    Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
    Append the length of the prefix followed by c to comp.
    Return the string comp.

    Parameters
    ----------
    word: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> compressedString('abcde')
    '1a1b1c1d1e'

    Explanation:
    Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the
    prefix in each operation.
    For each prefix, append "1" followed by the character to comp.

    >>> compressedString('aaaaaaaaaaaaaabb')
    '9a5a2b'

    Explanation:
    Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as
    the prefix in each operation.
    For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
    For prefix "aaaaa", append "5" followed by "a" to comp.
    For prefix "bb", append "2" followed by "b" to comp.
    """
    comp = ''
    prev = None
    n = 1
    for x in word:
        if x is None:
            prev = x
            continue
        if x == prev and n < 9:
            n += 1
        elif prev is not None:
            comp += f'{n}{prev}'
            n = 1
        prev = x
    else:
        comp += f'{n}{prev}'
    return comp
