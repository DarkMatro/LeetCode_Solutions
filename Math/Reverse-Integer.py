def reverse(x: int) -> int:
    """
    ID: 7
    Tags:   Math
    Time:   O(logX)
    Memory: O(1)

    Task
    ----------
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the
    value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Parameters
    ----------
    x: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> reverse(123)
    321

    >>> reverse(-123)
    -321

    >>> reverse(120)
    21
    """
    # Define the 32-bit integer range limits
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

    # Get the sign of x and work with its absolute value
    sign = -1 if x < 0 else 1
    x = abs(x)

    # Reverse the digits of x
    reversed_x = 0
    while x != 0:
        pop = x % 10  # Get the last digit
        x //= 10  # Remove the last digit from x

        # Check for overflow before actually adding the digit
        if reversed_x > (INT_MAX - pop) // 10:
            return 0

        reversed_x = reversed_x * 10 + pop

    # Apply the original sign
    reversed_x *= sign

    # Final check to ensure reversed_x is within the 32-bit signed integer range
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0

    return reversed_x