def canBeTypedWords(text: str, brokenLetters: str) -> int:
    """
    ID: 1935
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    There is a malfunctioning keyboard where some letter keys do not work. All other keys on the
    keyboard work properly.

    Given a string text of words separated by a single space (no leading or trailing spaces) and a
    string brokenLetters of all distinct letter keys that are broken, return the number of words in
    text you can fully type using this keyboard.

    Parameters
    ----------
    text: str

    brokenLetters: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> canBeTypedWords('hello world', 'ad')
    1

    Explanation: We cannot type "world" because the 'd' key is broken.

    >>> canBeTypedWords('leet code', 'lt')
    1

    Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

    >>> canBeTypedWords('leet code', 'e')
    0

    Explanation: We cannot type either word because the 'e' key is broken.
    """
    ans = 0
    b = set(brokenLetters)
    for x in text.split(' '):
        if len(set(x) & b) == 0:
            ans += 1
    return ans
