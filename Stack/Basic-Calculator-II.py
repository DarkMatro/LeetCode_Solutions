def calculate(s: str) -> int:
    """
    ID: 227
    Tags:   Math, String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s which represents an expression, evaluate this expression and return its value.

    The integer division should truncate toward zero.

    You may assume that the given expression is always valid. All intermediate results will be in the range of
    [-231, 231 - 1].

    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as
    eval().

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> calculate("3+2*2")
    7

    >>> calculate(" 3/2 ")
    1

    >>> calculate(" 3+5 / 2 ")
    5
    """
    s = s.replace(' ', '')
    stack = []
    num = 0
    op = '+'
    for i, x in enumerate(s):
        if x.isdigit():
            num = num * 10 + int(x)
        if not x.isdigit() or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack[-1] *= num
            elif op == '/':
                stack[-1] = int(stack[-1] / num)
            num = 0
            op = x
    return sum(stack)
