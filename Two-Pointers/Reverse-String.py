def reverse_string(s: list[str]) -> list[str]:
    """
    ID: 0344
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.

    Parameters
    ----------
    s : list[str]

    Returns
    -------
    s : list[str]

    Examples
    --------
    >>> reverse_string(["h","e","l","l","o"])
    ['o', 'l', 'l', 'e', 'h']

    >>> reverse_string(["H","a","n","n","a","h"])
    ['h', 'a', 'n', 'n', 'a', 'H']
    """
    n = len(s)
    for i in range(n // 2):
        s[i], s[n - i - 1] = s[n - i - 1], s[i]
    return s

