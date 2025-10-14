def evalRPN(tokens: list[str]) -> int:
    """
    ID: 150
    Tags:   Array, Math, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

    Parameters
    ----------
    tokens: list[str]

    Returns
    -------
    out : int

    Examples
    --------
    >>> evalRPN(["2","1","+","3","*"])
    9

    Explanation: ((2 + 1) * 3) = 9

    >>> evalRPN(["4","13","5","/","+"])
    6

    Explanation: (4 + (13 / 5)) = 6

    >>> evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    22

    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    """
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # '/'
                stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(token))
    return stack[0]
