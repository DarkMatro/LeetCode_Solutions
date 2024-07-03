def detectCapitalUse(word: str) -> bool:
    """
    ID: 520
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
    Given a string word, return true if the usage of capitals in it is right.

    Parameters
    ----------
    word: str

    Returns
    -------
    out: bool

    Examples
    --------
    >>> detectCapitalUse("USA")
    True

    >>> detectCapitalUse("FlaG")
    False
    """
    return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
