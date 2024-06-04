def toLowerCase(s: str) -> str:
    """
    ID: 709
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, return the string after replacing every uppercase letter with the same
    lowercase letter.

    Parameters
    ----------
    s: str

    Returns
    -------
    str

    Examples
    --------
    >>> toLowerCase("Hello")
    'hello'

    >>> toLowerCase("here")
    'here'

    >>> toLowerCase("LOVELY")
    'lovely'
    """
    ans = ''
    for c in s:
        ascii_id = ord(c)
        if 65 <= ascii_id <= 90:
            c = chr(ascii_id + 32)
        ans += c
    return ans
