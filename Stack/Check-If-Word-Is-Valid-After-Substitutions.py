def isValid(s: str) -> bool:
    """
    ID: 1003
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the
    following operation any number of times:

    Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where
    t == tleft + tright. Note that tleft and tright may be empty.
    Return true if s is a valid string, otherwise, return false.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isValid("aabcbc")
    True

    Explanation: "" -> "abc" -> "aabcbc"
    Thus, "aabcbc" is valid.

    >>> isValid("abcabcababcc")
    True

    Explanation: "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
    Thus, "abcabcababcc" is valid.

    >>> isValid("abccba")
    False

    Explanation: It is impossible to get "abccba" using the operation.
    """
    stack = []
    for x in s:
        if x == 'c' and len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
            stack.pop()
            stack.pop()
        else:
            stack.append(x)
    return not stack
