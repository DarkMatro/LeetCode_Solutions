def concatHex36(n: int) -> str:
    """
    ID: 3602
    Tags:   Math, String
    Time:   O(logN)
    Memory: O(logN)

    Task
    ----------
    You are given an integer n.

    Return the concatenation of the hexadecimal representation of n2 and the hexatrigesimal representation of n3.

    A hexadecimal number is defined as a base-16 numeral system that uses the digits 0 – 9 and the uppercase letters
    A - F to represent values from 0 to 15.

    A hexatrigesimal number is defined as a base-36 numeral system that uses the digits 0 – 9 and the uppercase letters
    A - Z to represent values from 0 to 35.

    Parameters
    ----------
    n: int

    Returns
    -------
    str

    Examples
    --------
    >>> concatHex36(13)
    'A91P1'

    Explanation:

    n2 = 13 * 13 = 169. In hexadecimal, it converts to (10 * 16) + 9 = 169, which corresponds to "A9".
    n3 = 13 * 13 * 13 = 2197. In hexatrigesimal, it converts to (1 * 362) + (25 * 36) + 1 = 2197, which corresponds to
    "1P1".
    Concatenating both results gives "A9" + "1P1" = "A91P1".

    >>> concatHex36(36)
    '5101000'

    Explanation:

    n2 = 36 * 36 = 1296. In hexadecimal, it converts to (5 * 162) + (1 * 16) + 0 = 1296, which corresponds to "510".
    n3 = 36 * 36 * 36 = 46656. In hexatrigesimal, it converts to (1 * 363) + (0 * 362) + (0 * 36) + 0 = 46656, which
    corresponds to "1000".
    Concatenating both results gives "510" + "1000" = "5101000".
    """

    def to_base(num: int, base: int, digits: str) -> str:
        """Convert a number to a given base using the provided digit set."""
        if num == 0:
            return "0"
        result = []
        while num > 0:
            result.append(digits[num % base])
            num //= base
        return "".join(reversed(result))

    hex_digits = "0123456789ABCDEF"
    hex_repr = to_base(n * n, 16, hex_digits)

    base36_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base36_repr = to_base(n * n * n, 36, base36_digits)

    return hex_repr + base36_repr
