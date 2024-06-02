def defangIPaddr(address: str) -> str:
    """
    ID: 1108
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a valid (IPv4) IP address, return a defanged version of that IP address.

    A defanged IP address replaces every period "." with "[.]".

    Parameters
    ----------
    address: str

    Returns
    -------
    str

    Examples
    --------
    >>> defangIPaddr("1.1.1.1")
    '1[.]1[.]1[.]1'

    >>> defangIPaddr("255.100.50.0")
    '255[.]100[.]50[.]0'
    """
    return address.replace('.', '[.]')
