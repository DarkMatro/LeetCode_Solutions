def reorderSpaces(text: str) -> str:
    """
    ID: 1592
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string text of words that are placed among some number of spaces. Each word
    consists of one or more lowercase English letters and are separated by at least one space. It's
    guaranteed that text contains at least one word.

    Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent
    words and that number is maximized. If you cannot redistribute all the spaces equally, place the
    extra spaces at the end, meaning the returned string should be the same length as text.

    Return the string after rearranging the spaces.

    Parameters
    ----------
    text: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> reorderSpaces("  this   is  a sentence ")
    'this   is   a   sentence'

    Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces
    between the words: 9 / (4-1) = 3 spaces.

    >>> reorderSpaces(" practice   makes   perfect")
    'practice   makes   perfect '

    Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space.
    We place this extra space at the end of the string.
    """
    n_spaces = text.count(' ')
    words = [x for x in text.split(' ') if x]
    n_words = len(words)
    q = int(n_spaces / (n_words - 1)) if n_words > 1 else 1
    extra_spaces = n_spaces - (q * (n_words - 1))
    ans = ''
    for i, w in enumerate(words):
        ans += w
        if i < n_words - 1:
            ans += ' ' * q
    ans += ' ' * int(extra_spaces)
    return ans
