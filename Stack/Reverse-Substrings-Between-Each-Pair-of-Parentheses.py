def reverseParentheses(s: str) -> str:
    """
    ID: 1190
    Tags:   String, Stack
    Time:   O(N^2)
    Memory: O(N)

    Task
    ----------
    You are given a string s that consists of lower case English letters and brackets.

    Reverse the strings in each pair of matching parentheses, starting from the innermost one.

    Your result should not contain any brackets.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> reverseParentheses("(abcd)")
    'dcba'

    >>> reverseParentheses("(u(love)i)")
    'iloveu'

    Explanation: The substring "love" is reversed first, then the whole string is reversed.

    >>> reverseParentheses("(ed(et(oc))el)")
    'leetcode'

    Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
    """
    stack = []
    result = []
    for i, x in enumerate(s):
        if x == '(':
            stack.append(len(result))
        elif x == ')':
            start = stack.pop()
            result[start:] = result[start:][::-1]
        else:
            result.append(x)
    return ''.join(result)
