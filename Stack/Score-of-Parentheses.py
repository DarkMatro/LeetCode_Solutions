def scoreOfParentheses(s: str) -> int:
    """
    ID: 856
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a balanced parentheses string s, return the score of the string.

    The score of a balanced parentheses string is based on the following rule:

    "()" has score 1.
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> scoreOfParentheses("()")
    1

    >>> scoreOfParentheses("(())")
    2

    >>> scoreOfParentheses("()()")
    2
    """
    stack = [0]
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)  # () -> 1, (A) -> 2*A

    return stack[-1]
