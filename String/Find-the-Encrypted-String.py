def getEncryptedString(s: str, k: int) -> str:
    """
    ID: 3210
    Tags:   String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given a string s and an integer k. Encrypt the string using the following algorithm:

    For each character c in s, replace c with the kth character after c in the string (in a cyclic
    manner).
    Return the encrypted string.

    Parameters
    ----------
    s: str

    k: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> getEncryptedString('dart', 3)
    'tdar'

    Explanation:

    For i = 0, the 3rd character after 'd' is 't'.
    For i = 1, the 3rd character after 'a' is 'd'.
    For i = 2, the 3rd character after 'r' is 'a'.
    For i = 3, the 3rd character after 't' is 'r'.

    >>> getEncryptedString('aaa', 1)
    'aaa'

    Explanation: As all the characters are the same, the encrypted string will also be the same.
    """
    idx = k % len(s)
    return s[idx:] + s[:idx]
