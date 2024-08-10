def remove_duplicate_letters(s: str) -> str:
    """
    ID: 0316
    Tags:   String, Stack, Greedy, Monotonic Stack
    Time:   O(N)
    Memory: O(k) k is size of the alphabet

    Task
    ----------
    Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your
     result is the smallest in lexicographical order
     among all possible results.

    Parameters
    ----------
    s : str

    Returns
    -------
    out: str

    Examples
    --------
    >>> remove_duplicate_letters("bcabc")
    'abc'

    >>> remove_duplicate_letters("cbacdcbc")
    'acdb'
    """
    stack = []
    last_occ = {}
    visited = set()
    # find last idx for every symbol
    for i, letter in enumerate(s):
        last_occ[letter] = i

    for i, symbol in enumerate(s):
        if symbol not in visited:
            while stack and symbol < stack[-1] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(symbol)
            visited.add(symbol)
    return ''.join(stack)
