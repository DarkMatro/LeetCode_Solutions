from collections import Counter

def checkIfPangram(sentence: str) -> bool:
    """
    ID: 1832
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A pangram is a sentence where every letter of the English alphabet appears at least once.

    Given a string sentence containing only lowercase English letters, return true if sentence is a
    pangram, or false otherwise.

    Parameters
    ----------
    sentence: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> checkIfPangram('thequickbrownfoxjumpsoverthelazydog')
    True

    Explanation: sentence contains at least one of every letter of the English alphabet.

    >>> checkIfPangram('leetcode')
    False
    """
    return len(Counter(sentence)) == 26
