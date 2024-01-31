from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    ID: 0383
    Tags:   Hash Table, String, Counting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
    magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.


    Parameters
    ----------
    ransomNote: str

    magazine: str

    Returns
    -------
    bool

    Examples
    --------
    >>> canConstruct('a', 'b')
    False

    >>> canConstruct('aa', 'ab')
    False

    >>> canConstruct('aa', 'aab')
    True
    """
    r_c = Counter(ransomNote)
    m_c = Counter(magazine)
    if r_c.keys() & m_c.keys() != r_c.keys():
        return False
    for char, n in r_c.items():
        if m_c[char] < n:
            return False
    return True