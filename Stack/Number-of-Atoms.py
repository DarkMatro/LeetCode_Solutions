from collections import Counter

def countOfAtoms(formula: str) -> str:
    """
    ID: 726
    Tags:   Hash Table, String, Stack, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string formula representing a chemical formula, return the count of each atom.

    The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the
    name.

    One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1,
    no digits will follow.

    For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
    Two formulas are concatenated together to produce another formula.

    For example, "H2O2He3Mg4" is also a formula.
    A formula placed in parentheses, and a count (optionally added) is also a formula.

    For example, "(H2O2)" and "(H2O2)3" are formulas.
    Return the count of all elements as a string in the following form: the first name (in sorted order), followed by
    its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count
    (if that count is more than 1), and so on.

    The test cases are generated so that all the values in the output fit in a 32-bit integer.

    Parameters
    ----------
    formula: str

    Returns
    -------
    str

    Examples
    --------
    >>> countOfAtoms("H2O")
    'H2O'

    Explanation: The count of elements are {'H': 2, 'O': 1}.

    >>> countOfAtoms("Mg(OH)2")
    'H2MgO2'

    Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

    >>> countOfAtoms("K4(ON(SO3)2)2")
    'K4N2O14S4'

    Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
    """
    stack = [Counter()]
    i, n = 0, len(formula)

    while i < n:
        if formula[i] == '(':
            stack.append(Counter())
            i += 1
        elif formula[i] == ')':
            i += 1
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            mult = int(formula[start:i] or '1')
            top = stack.pop()
            for elem, cnt in top.items():
                stack[-1][elem] += cnt * mult
        else:
            start = i
            i += 1
            while i < n and formula[i].islower():
                i += 1
            elem = formula[start:i]
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            count = int(formula[start:i] or '1')
            stack[-1][elem] += count

    total = stack[-1]
    return ''.join(f"{atom}{(total[atom] if total[atom] > 1 else '')}" for atom in sorted(total))
