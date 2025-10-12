def maxDepth(s: str) -> int:
    """
    ID: 1614
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested
    parentheses.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxDepth("(1+(2*3)+((8)/4))+1")
    3

    Explanation: Digit 8 is inside of 3 nested parentheses in the string.

    >>> maxDepth("(1)+((2))+(((3)))")
    3

    Explanation: Digit 3 is inside of 3 nested parentheses in the string.

    >>> maxDepth("()(())((()()))")
    3
    """
    stack = []
    ans = 0
    for i, x in enumerate(s):
        if x == '(':
            stack.append(i)
            ans = max(ans, len(stack))
        elif x == ')':
            stack.pop()
    return ans
