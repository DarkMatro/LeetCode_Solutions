def numberOfSpecialChars(word: str) -> int:
    """
    ID: 3121
    Tags: Hash Table, String
    Time: O(N)
    Memory: O(N)

    Task
    ----------
    You are given a string word. A letter c is called special if it appears both in lowercase and
    uppercase in word, and every lowercase occurrence of c appears before the first uppercase
    occurrence of c.

    Return the number of special letters in word.

    Parameters
    ----------
    word: str

    Returns
    -------
    int

    Examples
    --------
    >>> numberOfSpecialChars('aaAbcBC')
    3

    Explanation:
    The special characters are 'a', 'b', and 'c'.

    >>> numberOfSpecialChars('abc')
    0

    Explanation:
    There are no special characters in word.

    >>> numberOfSpecialChars('AbBCab')
    0

    Explanation:
    There are no special characters in word.
    """
    first_idx_dict = {}
    snd_idx_dict = {}
    for i, w in enumerate(word):
        if w.islower():
            first_idx_dict[w] = i
        elif w.isupper() and w not in snd_idx_dict:
            snd_idx_dict[w] = i
    ans = 0
    for k, v in first_idx_dict.items():
        if snd_idx_dict.get(k.upper(), 0) > v:
            ans += 1
    return ans
