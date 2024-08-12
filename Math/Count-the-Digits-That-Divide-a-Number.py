def countDigits(num: int) -> int:
    """
    ID: 1281
    Tags:   Math
    Time:   O(D)
    Memory: O(1)

    Task
    ----------
    Given an integer num, return the number of digits in num that divide num.

    An integer val divides nums if nums % val == 0.

    Parameters
    ----------
    num: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> countDigits(7)
    1

    Explanation: 7 divides itself, hence the answer is 1.

    >>> countDigits(121)
    2

    Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

    >>> countDigits(1248)
    4

    Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
    """
    ans = 0
    n = num + 0
    while True:
        dig = n % 10
        if num % dig == 0:
            ans += 1
        n //= 10
        if n == 0:
            break
    return ans
