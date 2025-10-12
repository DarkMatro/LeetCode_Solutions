def removeDuplicates(s: str) -> str:
    """
    ID: 1047
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two
    adjacent and equal letters and removing them.

    We repeatedly make duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique

    Parameters
    ----------
    s: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> removeDuplicates("abbaca")
    'ca'

    Explanation: For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the
    only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the
    final string is "ca".

    >>> removeDuplicates("azxxzy")
    'ay'
    """
    stack = []
    for x in s:
        if not stack or stack[-1] != x:
            stack.append(x)
        else:
            stack.pop()
    return ''.join(stack)
