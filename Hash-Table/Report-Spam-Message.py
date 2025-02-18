def reportSpam(message: list[str], bannedWords: list[str]) -> bool:
    """
    ID: 3295
    Tags: Array, Hash Table, String
    Time: O(M+N)
    Memory: O(N)

    Task
    ----------
    You are given an array of strings message and an array of strings bannedWords.

    An array of words is considered spam if there are at least two words in it that exactly match
    any word in bannedWords.

    Return true if the array message is spam, and false otherwise.

    Parameters
    ----------
    message: list[str]

    bannedWords: list[str]

    Returns
    -------
    bool

    Examples
    --------
    >>> reportSpam(["hello","world","leetcode"], ["world","hello"])
    True

    Explanation:
    The words "hello" and "world" from the message array both appear in the bannedWords array.

    >>> reportSpam(["hello","programming","fun"], ["world","programming","leetcode"])
    False

    Explanation:
    Only one word from the message array ("programming") appears in the bannedWords array.
    """
    keys = set(bannedWords)
    ans = 0
    for m in message:
        if m in keys:
            ans += 1
        if ans > 1:
            return True
    return False
