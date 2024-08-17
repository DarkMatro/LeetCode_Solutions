def convertToBase7(num: int) -> str:
    """
    ID: 504
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given an integer num, return a string of its base 7 representation.

    Parameters
    ----------
    num: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> convertToBase7(100)
    '202'

    >>> convertToBase7(-7)
    '-10'
    """
    # Handle the edge case where the number is zero
    if num == 0:
        return "0"

    # Determine if the number is negative and work with the absolute value
    negative = num < 0
    num = abs(num)

    # Convert to base-7
    base7 = []
    while num > 0:
        base7.append(str(num % 7))
        num //= 7

    # Reverse the digits to form the correct base-7 number
    base7 = ''.join(base7[::-1])

    # If the original number was negative, add the negative sign
    if negative:
        base7 = '-' + base7

    return base7
