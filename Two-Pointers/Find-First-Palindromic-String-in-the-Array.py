def firstPalindrome(words: list[str]) -> str:
    """
    ID: 2108
    Tags:   Array, Two Pointers, String
    Time:   O(N*K)
    Memory: O(1)

    Task
    ----------
    Given an array of strings words, return the first palindromic string in the array. If there is no such string,
    return an empty string "".

    A string is palindromic if it reads the same forward and backward.

    Parameters
    ----------
    words : list[str]

    Returns
    -------
    out : str

    Examples
    --------
    >>> firstPalindrome(["abc","car","ada","racecar","cool"])
    'ada'

    Explanation:
    The first string that is palindromic is "ada".
    Note that "racecar" is also palindromic, but it is not the first.

    >>> firstPalindrome(["notapalindrome","racecar"])
    'racecar'

    Explanation:
    The first and only string that is palindromic is "racecar"

    >>> firstPalindrome(["def","ghi"])
    ''

    Explanation:
    There are no palindromic strings, so the empty string is returned.
    """
    for w in words:
        if w == w[::-1]:
            return w
    return ''
