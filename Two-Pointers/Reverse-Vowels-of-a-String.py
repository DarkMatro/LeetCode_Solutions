def reverseVowels(s: str) -> str:
    """
    ID: 345
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> reverseVowels("IceCreAm")
    'AceCreIm'

    Explanation:
    The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

    >>> reverseVowels("leetcode")
    'leotcede'
    """
    res = len(s) * [0]
    i = 0
    j = len(s) - 1
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while i <= j:
        if s[i].lower() in vowels and s[j].lower() in vowels:
            res[i] = s[j]
            res[j] = s[i]
            i += 1
            j -= 1
        elif s[i].lower() in vowels:
            res[j] = s[j]
            j -= 1
        else:
            res[i] = s[i]
            i += 1

    return ''.join(res)
