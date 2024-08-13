def sumBase(n: int, k: int) -> int:
    """
    ID: 1837
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting
    n from base 10 to base k.

    After converting, each digit should be interpreted as a base 10 number, and the sum should be
    returned in base 10.

    Parameters
    ----------
    n: int

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumBase(34, 6)
    9

    Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.


    >>> sumBase(10, 10)
    1

    Explanation: n is already in base 10. 1 + 0 = 1.
    """
    # Convert n from base 10 to base k
    base_k_digits = 0
    while n > 0:
        base_k_digits += (n % k)
        n //= k

    # Sum the digits in base k
    return base_k_digits
