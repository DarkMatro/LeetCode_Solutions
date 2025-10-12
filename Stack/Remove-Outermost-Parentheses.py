def removeOuterParentheses(s: str) -> str:
    """
    ID: 1021
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings,
    and + represents string concatenation.

    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
    A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s =
    A + B, with A and B nonempty valid parentheses strings.

    Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are
    primitive valid parentheses strings.

    Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> removeOuterParentheses("(()())(())")
    '()()()'

    Explanation: The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

    >>> removeOuterParentheses("(()())(())(()(()))")
    '()()()()(())'

    Explanation: The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
    After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

    >>> removeOuterParentheses("()()")
    ''

    Explanation: The input string is "()()", with primitive decomposition "()" + "()".
    After removing outer parentheses of each part, this is "" + "" = "".
    """
    stack = []
    ans = ''
    for i, x in enumerate(s):
        if x == '(':
            stack.append(i)
        else:
            p = stack.pop()
            if not stack:
                ans += s[p + 1: i]
    return ans
