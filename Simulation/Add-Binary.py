def add_binary(a: str, b: str) -> str:
    """
    ID: 0067
    Tags:   Math, String, Bit Manipulation, Simulation
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given two binary strings a and b, return their sum as a binary string.

    Parameters
    ----------
    a : str

    b : str

    Returns
    -------
    res : str

    Examples
    --------
    >>> add_binary("11", '1')
    '100'

    >>> add_binary("1010", '1011')
    '10101'
    """
    c = bin(int(a, 2) + int(b, 2))
    res = c.lstrip('0b')
    return '0' if res == '' else res

