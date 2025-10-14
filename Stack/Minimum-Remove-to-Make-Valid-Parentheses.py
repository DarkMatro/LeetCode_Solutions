def minRemoveToMakeValid(s: str) -> str:
    """
    ID: 1249
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
    parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> minRemoveToMakeValid("lee(t(c)o)de)")
    'lee(t(c)o)de'

    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

    >>> minRemoveToMakeValid("a)b(c)d")
    'ab(c)d'

    >>> minRemoveToMakeValid("))((")
    ''

    Explanation: An empty string is also valid.
    """
    banned_lr = remove_list(s)
    ans = ''
    for i, x in enumerate(s):
        if i not in banned_lr:
            ans += x
    banned_rl = remove_list_rev(ans[::-1])
    ans_2 = ''
    for i, x in enumerate(ans[::-1]):
        if i not in banned_rl:
            ans_2 += x
    return ans_2[::-1]

def remove_list(s: str) -> set[int]:
    stack = []
    banned = set()
    for i, x in enumerate(s):
        if x == '(':
            stack.append(i)
        elif x == ')':
            if not stack:
                banned.add(i)
            else:
                stack.pop()
    return banned

def remove_list_rev(s: str) -> set[int]:
    stack = []
    banned = set()
    for i, x in enumerate(s):
        if x == ')':
            stack.append(i)
        elif x == '(':
            if not stack:
                banned.add(i)
            else:
                stack.pop()
    return banned
