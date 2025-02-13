def possibleStringCount(word: str) -> int:
    """
    ID: 3330
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Alice is attempting to type a specific string on her computer. However, she tends to be clumsy
    and may press a key for too long, resulting in a character being typed multiple times.

    Although Alice tried to focus on her typing, she is aware that she may still have done this at
    most once.

    You are given a string word, which represents the final output displayed on Alice's screen.

    Return the total number of possible original strings that Alice might have intended to type.

    Parameters
    ----------
    word: str

    Returns
    -------
    int

    Examples
    --------
    >>> possibleStringCount('abbcccc')
    5

    Explanation:
    The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

    >>> possibleStringCount('abcd')
    1

    Explanation:
    The only possible string is "abcd".

    >>> possibleStringCount('aaaa')
    4
    """
    prev = ''
    ans = 1
    for i, s in enumerate(word):
        if i == 0:
            prev = s
            continue
        if s == prev:
            ans += 1
        prev = s
    return ans
