def validIPAddress(queryIP: str) -> str:
    """
    ID: 468
    Tags:   String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid
    IPv6 address or "Neither" if IP is not a correct IP of any type.

    A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot
    contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses
    while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

    A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

    1 <= xi.length <= 4
    xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and
    upper-case English letters ('A' to 'F').
    Leading zeros are allowed in xi.
    For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334"
    are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and
    "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

    Parameters
    ----------
    queryIP: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> validIPAddress('172.16.254.1')
    'IPv4'

    Explanation: This is a valid IPv4 address, return "IPv4".

    >>> validIPAddress('2001:0db8:85a3:0:0:8A2E:0370:7334')
    'IPv6'

    Explanation: This is a valid IPv6 address, return "IPv6".

    >>> validIPAddress('256.256.256.256')
    'Neither'

    Explanation: This is neither a IPv4 address nor a IPv6 address.
    """
    v6 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
    if queryIP[:5].count('.') > 0:
        splt = queryIP.split('.')
        if len(splt) != 4:
            return 'Neither'
        for x in splt:
            for i in x:
                if i.isalpha():
                    return 'Neither'
            if (len(x) > 1 and x[0] == '0') or len(x) > 3 or not x or not (0 <= int(x) <= 255):
                break
        else:
            return 'IPv4'
    elif queryIP[:5].count(':') > 0:
        splt = queryIP.split(':')
        if len(splt) != 8:
            return 'Neither'
        for x in splt:
            if not x or len(x) > 4:
                break
            for i in x.lower():
                if i not in v6:
                    return 'Neither'
        else:
            return 'IPv6'
    return 'Neither'
