def capitalizeTitle(title: str) -> str:
    """
    ID: 2129
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string title consisting of one or more words separated by a single space, where
    each word consists of English letters. Capitalize the string by changing the capitalization of
    each word such that:

    If the length of the word is 1 or 2 letters, change all letters to lowercase.
    Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
    Return the capitalized title.

    Parameters
    ----------
    title: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> capitalizeTitle("capiTalIze tHe titLe")
    'Capitalize The Title'

    Since all the words have a length of at least 3, the first letter of each word is uppercase, and
    the remaining letters are lowercase.

    >>> capitalizeTitle("First leTTeR of EACH Word")
    'First Letter of Each Word'

    The word "of" has length 2, so it is all lowercase.
    The remaining words have a length of at least 3, so the first letter of each remaining word is
    uppercase, and the remaining letters are lowercase.

    >>> capitalizeTitle("i lOve leetcode")
    'i Love Leetcode'

    The word "i" has length 1, so it is lowercase.
    The remaining words have a length of at least 3, so the first letter of each remaining word is
    uppercase, and the remaining letters are lowercase.
    """
    words = title.split(' ')
    ans = ''
    for i, w in enumerate(words):
        if i > 0:
            ans += ' '
        if len(w) <= 2:
            ans += w.lower()
        else:
            ans += w.capitalize()
    return ans
