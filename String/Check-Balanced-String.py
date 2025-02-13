def isBalanced(num: str) -> bool:
    """
    ID: 3340
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string num consisting of only digits. A string of digits is called balanced if
    the sum of the digits at even indices is equal to the sum of digits at odd indices.

    Return true if num is balanced, otherwise return false.

    Parameters
    ----------
    num: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isBalanced('1234')
    False

    Explanation:
    The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
    Since 4 is not equal to 6, num is not balanced.

    >>> isBalanced('24123')
    True

    Explanation:
    The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
    Since both are equal the num is balanced.
    """
    return sum(int(num[i]) for i in range(0, len(num), 2)) == sum(
        int(num[i]) for i in range(1, len(num), 2))
