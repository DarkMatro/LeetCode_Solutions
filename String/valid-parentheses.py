def is_valid(s: str) -> bool:
    """
    ID: 0020
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
    valid.

    An input string is valid if:

    1.Open brackets must be closed by the same type of brackets.
    2.Open brackets must be closed in the correct order.
    3.Every close bracket has a corresponding open bracket of the same type.

    Parameters
    ----------
    s : str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> is_valid("()")
    True

    >>> is_valid("()[]{}")
    True

    >>> is_valid("(]")
    False
    """
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack
