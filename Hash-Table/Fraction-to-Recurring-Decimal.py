def fractionToDecimal(numerator: int, denominator: int) -> str:
    """
    ID: 166
    Tags:   Hash Table, Math, String
    Time:   O(D)
    Memory: O(1)

    Task
    ----------
    Given two integers representing the numerator and denominator of a fraction, return the fraction
    in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    If multiple answers are possible, return any of them.

    It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

    Parameters
    ----------
    numerator: int

    denominator: int

    Returns
    -------
    str

    Examples
    --------
    >>> fractionToDecimal(1, 2)
    '0.5'

    >>> fractionToDecimal(2, 1)
    '2'

    >>> fractionToDecimal(4, 333)
    '0.(012)'
    """
    if numerator % denominator == 0:
        return str(numerator // denominator)  # Exact division

    # Handle sign
    sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
    numerator, denominator = abs(numerator), abs(denominator)

    # Compute integer part
    integer_part = str(numerator // denominator)
    remainder = numerator % denominator
    result = sign + integer_part + "."

    # Dictionary to track remainders and their positions
    seen_remainders = {}
    fraction_part = ""

    while remainder:
        if remainder in seen_remainders:
            # Insert parentheses around repeating part
            index = seen_remainders[remainder]
            fraction_part = fraction_part[:index] + "(" + fraction_part[index:] + ")"
            return result + fraction_part

        seen_remainders[remainder] = len(fraction_part)
        remainder *= 10
        fraction_part += str(remainder // denominator)
        remainder %= denominator

    return result + fraction_part
