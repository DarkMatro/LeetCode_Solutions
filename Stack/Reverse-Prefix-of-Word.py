def reversePrefix(word: str, ch: str) -> str:
    """
    ID: 2000
    Tags:   Two Pointers, String, Stack
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the
    index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3
    (inclusive). The resulting string will be "dcbaefd".
    Return the resulting string.

    Parameters
    ----------
    word: str

    ch: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> reversePrefix("abcdefd", "d")
    'dcbaefd'

    Explanation: The first occurrence of "d" is at index 3.
    Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

    >>> reversePrefix("xyxzxe", "z")
    'zxyxxe'

    Explanation: The first and only occurrence of "z" is at index 3.
    Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

    >>> reversePrefix("abcd", "z")
    'abcd'

    Explanation: "z" does not exist in word.
    You should not do any reverse operation, the resulting string is "abcd".
    """
    idx = word.find(ch)
    if idx == -1:
        return word
    return word[: idx + 1][::-1] + word[idx + 1:]
