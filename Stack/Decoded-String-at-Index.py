def decodeAtIndex(s: str, k: int) -> str:
    """
    ID: 880
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a
    time and the following steps are taken:

    If the character read is a letter, that letter is written onto the tape.
    If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
    Given an integer k, return the kth letter (1-indexed) in the decoded string.

    Parameters
    ----------
    s: str

    k: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> decodeAtIndex("leet2code3", 10)
    'o'

    Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
    The 10th letter in the string is "o".

    >>> decodeAtIndex("ha22", 5)
    'h'

    Explanation: The decoded string is "hahahaha".
    The 5th letter is "h".

    >>> decodeAtIndex("a2345678999999999999999", 1)
    'a'

    Explanation: The decoded string is "a" repeated 8301530446056247680 times.
    The 1st letter is "a".
    """
    size = 0

    # 1️ Compute total decoded length
    for c in s:
        if c.isdigit():
            size *= int(c)
        else:
            size += 1

    # 2️ Work backwards
    for c in reversed(s):
        k %= size
        if k == 0 and c.isalpha():
            return c
        if c.isdigit():
            size //= int(c)
        else:
            size -= 1
