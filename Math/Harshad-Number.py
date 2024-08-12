def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
    """
    ID: 3099
    Tags:   Math
    Time:   O(D)
    Memory: O(1)

    Task
    ----------
    An integer divisible by the sum of its digits is said to be a Harshad number. You are given an
    integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.

    Parameters
    ----------
    x: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumOfTheDigitsOfHarshadNumber(18)
    9

    Explanation: The sum of digits of x is 9. 18 is divisible by 9. So 18 is a Harshad number and
    the answer is 9.

    >>> sumOfTheDigitsOfHarshadNumber(23)
    -1

    Explanation: The sum of digits of x is 5. 23 is not divisible by 5. So 23 is not a Harshad
    number and the answer is -1.
    """
    s_dig = 0
    n = x + 0
    while True:
        s_dig += n % 10
        n //= 10
        if n == 0:
            break
    return s_dig if x % s_dig == 0 else -1
