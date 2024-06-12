def generateTheString(n: int) -> str:
    """
    ID: 1374
    Tags:   String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given an integer n, return a string with n characters such that each character in such string
    occurs an odd number of times.

    The returned string must contain only lowercase English letters. If there are multiples valid
    strings, return any of them.

    Parameters
    ----------
    n: int

    Returns
    -------
    str

    Examples
    --------
    >>> generateTheString(4)
    'aaab'

    >>> generateTheString(2)
    'ab'

    >>> generateTheString(7)
    'aaaaaaa'
    """
    ans = ''
    if n % 2 == 0:
        ans = 'a' * (n - 1) + 'b'
    else:
        ans = 'a' * n
    return ans
