def is_palindrome(x: int) -> bool:
    """
    ID: 0009
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Solve it without converting the integer to a string.

    Parameters
    ----------
    x : int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> is_palindrome(121)
    True

    121 reads as 121 from left to right and from right to left.

    >>> is_palindrome(-121)
    False

    From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

    >>> is_palindrome(10)
    False

    Reads 01 from right to left. Therefore, it is not a palindrome.
    """
    if x < 0:
        return False
    y = 0
    x0 = x
    while x != 0:
        y = y * 10 + x % 10
        x //= 10
    return y == x0
