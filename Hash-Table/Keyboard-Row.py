def findWords(words: list[str]) -> list[str]:
    """
    ID: 500
    Tags:   Array, Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an array of strings words, return the words that can be typed using letters of the
    alphabet on only one row of American keyboard like the image below.

    In the American keyboard:

    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".

    Parameters
    ----------
    words: list[str]

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> findWords(["Hello","Alaska","Dad","Peace"])
    ['Alaska', 'Dad']

    >>> findWords(["omk"])
    []

    >>> findWords(["adsdf","sfd"])
    ['adsdf', 'sfd']
    """
    ak = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
    ans = []
    for w in words:
        x = set(w.lower())
        for s in ak:
            if len(s & x) == len(x):
                ans.append(w)
    return ans
