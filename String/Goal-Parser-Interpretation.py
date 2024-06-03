def interpret(command: str) -> str:
    """
    ID: 1678
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You own a Goal Parser that can interpret a string command. The command consists of an alphabet
    of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G",
    "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then
    concatenated in the original order.

    Given the string command, return the Goal Parser's interpretation of command.

    Parameters
    ----------
    command: str

    Returns
    -------
    str

    Examples
    --------
    >>> interpret("G()(al)")
    'Goal'

    Explanation: The Goal Parser interprets the command as follows:
    G -> G
    () -> o
    (al) -> al
    The final concatenated result is "Goal".

    >>> interpret("G()()()()(al)")
    'Gooooal'

    >>> interpret("(al)G(al)()()G")
    'alGalooG'
    """
    ans = ''
    i = 0
    while i < len(command):
        char = command[i]
        if char == '(':
            next_char = command[i + 1]
            if next_char == 'a':
                ans += 'al'
                i += 4
            elif next_char == ')':
                i += 2
                ans += 'o'
        else:
            ans += 'G'
            i += 1
    return ans
