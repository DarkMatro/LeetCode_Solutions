def isValid(word: str) -> bool:
    """
    ID: 3136
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A word is considered valid if:

    It contains a minimum of 3 characters.
    It contains only digits (0-9), and English letters (uppercase and lowercase).
    It includes at least one vowel.
    It includes at least one consonant.
    You are given a string word.

    Return true if word is valid, otherwise, return false.

    Notes:

    'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
    A consonant is an English letter that is not a vowel.

    Parameters
    ----------
    word : str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isValid("234Adas")
    True

    >>> isValid("b3")
    False

    >>> isValid("a3$e")
    False

    >>> isValid("aya")
    True
    """
    vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    has_consonant = False
    has_vowel = False
    for s in word:
        if not s.isalnum():
            return False
        if s.isalpha():
            if s not in vowel:
                has_consonant = True
            else:
                has_vowel = True
    return len(word) > 2 and has_vowel and has_consonant
